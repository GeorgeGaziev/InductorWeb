from flask import request, jsonify, render_template
from app import app
from app.forms import InputForm
from app import Inductor

@app.route('/')
@app.route('/index')
def index():
    form = InputForm()
    return render_template('index.html', title='Обработка ФИО', form=form)

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        inputText = str(request.form.get('inputText', 0))
        outputText = Inductor.ProcessSingle(inputText)
        data = {'outputText': outputText}
        data = jsonify(data)
        return data
    #return render_template('index.html')
