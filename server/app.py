# server/app.py
from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:str_to_print>')
def print_string(str_to_print):
    print(str_to_print)
    return str_to_print

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ""
    for i in range(parameter):
        result += str(i) + "\n"
    return result

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return str(result)

if __name__ == '__main__':
    app.run(port=5555)
