from flask import Flask, jsonify,request,send_file
from flask_cors import CORS, cross_origin
import io
import sys
import os
import pdfplumber

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import ArgumentParser, LOG
from model import OpenAIModel
from translator import PDFTranslator

argument_parser = ArgumentParser()
args = argument_parser.parse_arguments()
model_name = args.openai_model 
api_key = args.openai_api_key 
model = OpenAIModel(model=model_name, api_key=api_key)

# pdf_file_path = args.book
# file_format = args.file_format

translator = PDFTranslator(model)

'''''
    启动Flask服务端
'''''
app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate():
    LOG.debug(f"请求: {request}\n")
    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    LOG.debug(f"FILE: {request.files['file']}\n")
    translator.translate_pdf(file, "PDF", "中文", './jupyter')

    translated_pdf = io.BytesIO()
    origin_file_name = file.filename.split('.')[0]
    translated_file_name = origin_file_name + '_translated.pdf'
    with pdfplumber.open('./jupyter/' + translated_file_name) as pdf:
        for page in pdf.pages:
            translated_pdf.write(page.extract_text().encode('utf-8'))

    translated_pdf.seek(0)

    return send_file(translated_pdf, as_attachment=True, download_name='translated.pdf')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)