import gradio as gr
from research_pipeline import run_research

def research(topic, max_results, model):
    if not topic or not topic.strip():
        return "Please enter a research topic.", "", ""

    try:
        result = run_research(
            topic=topic.strip(),
            max_results=int(max_results),
            model=model,
        )
        sources_md = "\n\n".join(
            f"{i}. **{item['title']}**  \n"
            f"   {item['url']}  \n"
            f"   {item['snippet']}"
            for i, item in enumerate(result["sources"], start=1)
        )
        return result["summary"], result["report"], sources_md
    except Exception as exc:
        return f"Research failed: {exc}", "", ""

with gr.Blocks(title="AI Research Assistant", theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        """
        # AI Research Assistant
        Research a topic with a three-agent workflow:
        **Web Researcher → Findings Summarizer → Report Writer**

        The app uses DuckDuckGo search and a local Ollama model.
        """
    )

    with gr.Row():
        topic = gr.Textbox(
            label="Research topic",
            placeholder="e.g. Applications of RAG in healthcare",
            lines=2,
            scale=4,
        )
        with gr.Column(scale=1):
            max_results = gr.Slider(
                minimum=3, maximum=10, value=5, step=1,
                label="Search results per topic"
            )
            model = gr.Dropdown(
                choices=["llama3.2"],
                value="llama3.2",
                label="Local Ollama model",
                allow_custom_value=True,
            )

    run_btn = gr.Button("Research topic", variant="primary")

    with gr.Tabs():
        with gr.Tab("Executive summary"):
            summary_out = gr.Markdown()
        with gr.Tab("Structured research report"):
            report_out = gr.Markdown()
        with gr.Tab("Sources"):
            sources_out = gr.Markdown()

    run_btn.click(
        fn=research,
        inputs=[topic, max_results, model],
        outputs=[summary_out, report_out, sources_out],
    )
    topic.submit(
        fn=research,
        inputs=[topic, max_results, model],
        outputs=[summary_out, report_out, sources_out],
    )

if __name__ == "__main__":
    demo.launch()
