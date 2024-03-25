import gradio as gr

from logic_textgeneration import TextGenerate

textGen = TextGenerate()

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            sourse_text = gr.Textbox(label="Sourse text")
            submit_btn = gr.Button(value="generate")
        with gr.Column():
            answer = gr.Textbox(label="Answer")

    submit_btn.click(textGen.run, inputs=sourse_text, outputs=answer)
    examples = gr.Examples(examples=["What is the computer"],
                           inputs=[sourse_text])

demo.launch()