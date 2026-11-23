from ddgs import DDGS
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage


def web_researcher(topic: str, max_results: int = 5) -> list[dict]:
    """Agent 1: Search the public web and collect source metadata."""
    results = []
    with DDGS() as ddgs:
        search_results = ddgs.text(
            topic,
            max_results=max_results,
            safesearch="moderate",
        )
        for item in search_results:
            url = item.get("href") or item.get("url") or ""
            title = item.get("title") or "Untitled result"
            body = item.get("body") or item.get("snippet") or ""
            if url:
                results.append({
                    "title": title,
                    "url": url,
                    "snippet": body,
                })
    return results


def _ask_model(model: str, system_prompt: str, user_prompt: str) -> str:
    """Call the local Ollama chat model through LangChain."""
    llm = ChatOllama(model=model, temperature=0)
    response = llm.invoke([
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt),
    ])
    return response.content


def findings_summarizer(topic: str, sources: list[dict], model: str) -> str:
    """Agent 2: Synthesize search snippets, preserving source references."""
    if not sources:
        return (
            "No web results were returned. Try a broader topic or check "
            "your internet connection."
        )

    source_text = "\n\n".join(
        f"[{i}] {s['title']}\nURL: {s['url']}\n"
        f"Search snippet: {s['snippet']}"
        for i, s in enumerate(sources, start=1)
    )

    return _ask_model(
        model,
        system_prompt=(
            "You are a research findings analyst. Use only the supplied "
            "search-result information. Do not invent facts, statistics, "
            "quotes, publication dates, or sources. Clearly mark uncertainty. "
            "Use inline source markers like [1] and [2]. Search snippets are "
            "limited evidence; state when more source verification is needed."
        ),
        user_prompt=(
            f"Research topic: {topic}\n\n"
            f"Search results:\n{source_text}\n\n"
            "Synthesize the main findings. Identify themes, useful evidence, "
            "disagreements, limitations, and unanswered questions. Cite "
            "claims with the supplied numbered source markers."
        ),
    )


def report_writer(topic: str, summary: str, sources: list[dict], model: str) -> str:
    """Agent 3: Turn the synthesis into a structured research report."""
    source_list = "\n".join(
        f"[{i}] {s['title']} — {s['url']}"
        for i, s in enumerate(sources, start=1)
    )

    return _ask_model(
        model,
        system_prompt=(
            "You are a careful research report writer. Produce a clear, "
            "professional report using only the supplied synthesis and source "
            "list. Do not add unsupported facts. Keep citations such as [1] "
            "next to supported claims. Distinguish evidence from analysis."
        ),
        user_prompt=f"""
Create a structured research report on: {topic}

Use these sections:
# Research Report: [topic]
## 1. Executive Summary
## 2. Research Objective
## 3. Key Findings
## 4. Analysis and Discussion
## 5. Challenges, Risks, or Limitations
## 6. Conclusion
## 7. Further Research Questions
## References

Research synthesis:
{summary}

Available sources:
{source_list}

Only include references from the supplied source list.
""",
    )


def run_research(topic: str, max_results: int = 5, model: str = "llama3.2"):
    """Run the three agents in sequence and return their outputs."""
    sources = web_researcher(topic, max_results)
    summary = findings_summarizer(topic, sources, model)
    report = report_writer(topic, summary, sources, model)

    return {
        "sources": sources,
        "summary": summary,
        "report": report,
    }
