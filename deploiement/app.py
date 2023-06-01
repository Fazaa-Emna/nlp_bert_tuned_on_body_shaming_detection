from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
from starlette.responses import HTMLResponse
from fastapi import FastAPI, Form
from prediction import BinaryBodyShaming
app = FastAPI()


@app.get('/') #data input by forms
def index():
    return {"WELCOME": "GO TO http://prod.kaisens.fr:7171/docs  route, or /post or send post request to  http://prod.kaisens.fr:7171/predict  "}

@app.get('/predict', response_class=HTMLResponse) #data input by forms
def take_inp():
    return '''<form method="post">
    <input type="text" maxlength="200" name="text" value="Text  to be tested"/>
    <input type="submit"/>
    </form>'''
