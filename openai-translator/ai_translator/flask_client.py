import requests
import json
from utils import LOG

url = 'http://127.0.0.1:8000/translate'

author = {'author': 'doubleTao'}
files = {'file': 'test.pdf'} # open('flask_client.py', 'rb')

res = requests.post(url=url, data=author, files=files)

LOG.debug(f"响应: {res}\n")
