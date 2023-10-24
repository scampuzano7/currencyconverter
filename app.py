from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to map operations to corresponding words
operation_words = {
    'usdaud': '$',
    'usdeuro': '€',
    'audusd': '$',
    'audeuro': '€',
    'eurousd': '$',
    'euroaud': '$',
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    operation = request.form['operation']

    if operation in operation_words:
        operation_word = operation_words[operation]

    else:
        operation_word = "Unknown Operation"

    if operation == 'usdaud':
        result = num1 * 1.57
    elif operation == 'usdeuro':
        result = num1 * 0.94
    elif operation == 'audusd':
        result = num1* 0.63
    elif operation == 'audeuro':
        result = num1 * 0.60
    elif operation == 'eurousd':
        result = num1 * 1.06
    elif operation == 'euroaud':
       result = num1 * 1.67
    else:
        result = "Invalid operation"

    formatted_result = "{:.2f}".format(result)

    custom_string = "{}".format(operation_word)

    return render_template('result.html', result=formatted_result, custom_string=custom_string)

if __name__ == '__main__':
    app.run(debug=True, port=8001)





