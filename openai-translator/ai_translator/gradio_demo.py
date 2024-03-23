import gradio as gr
import sys
import os
from utils import LOG,ArgumentParser,ConfigLoader
from translator import PDFTranslator
from model import OpenAIModel

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def translation(input_file):

    LOG.debug(f"源文件: {input_file.name}\n")
 
    # 解析命令行
    argument_parser = ArgumentParser()
    args = argument_parser.parse_arguments()
    
    model_name = args.openai_model 
    api_key = args.openai_api_key
    model = OpenAIModel(model=model_name, api_key=api_key)
    translator = PDFTranslator(model)

    output_file_path = translator.translate_pdf(
        input_file.name, file_format='markdown')
    
    LOG.debug(f"结果文件: {output_file_path}\n")
    return output_file_path

gr.Interface(
        fn=translation,
        title="OpenAI-Translator Author:doubleTao",
        inputs=[
            gr.components.File(label="Upload your file"),
        ],
        outputs=[
            gr.components.File(label="Download translation result")
        ],
        allow_flagging="never"
    ).launch(share=True, server_name="0.0.0.0")

