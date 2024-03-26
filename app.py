from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static', static_folder='static')

# Dictionary for currency symbols based on selection
operation_words = {
    'usdaud': '$',
    'usdeuro': '€',
    'audusd': '$',
    'audeuro': '€',
    'eurousd': '$',
    'euroaud': '$',
    'nokusd': '$',
    'nokaud': '$',
    'nokeuro': '€',
    'audnok': 'kr',
    'usdnok': 'kr',
    'euronok': 'kr',
    'jpyusd': '$',
    'jpyaud': '$',
    'jpyeuro': '€',
    'jpynok': 'kr',
    'usdjpy': '¥',
    'audjpy': '¥',
    'eurojpy': '¥',
    'nokjpy': '¥',
    'cnyusd': '$',
    'cnyaud': '$',
    'cnyeuro': '€',
    'cnynok': 'kr',
    'cnyjpy': '¥',
    'usdcny': '¥',
    'audcny': '¥',
    'eurocny': '¥',
    'nokcny': '¥',
    'jpycny': '¥',   
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
    elif operation == 'usdnok':
        result = num1 * 0.94
    elif operation == 'nokusd':
        result = num1 * 0.11
    elif operation == 'nokaud':
        result = num1 * 0.16
    elif operation == 'nokeuro':
        result = num1 * 0.10
    elif operation == 'audnok':
        result = num1 * 6.28
    elif operation == 'euronok':
        result = num1 * 9.78
    elif operation == 'usdjpy':
        result = num1 * 113.89
    elif operation == 'audjpy':
        result = num1 * 86.88
    elif operation == 'eurojpy':
        result = num1 * 120.01
    elif operation == 'nokjpy':
        result = num1 * 12.20
    elif operation == 'jpyusd':
        result = num1 * 0.0088
    elif operation == 'jpyaud':
        result = num1 * 0.0115
    elif operation == 'jpyeuro':
        result = num1 * 0.0083
    elif operation == 'jpynok':
        result = num1 * 0.082
    elif operation == 'cnyusd':
        result = num1 * 0.14
    elif operation == 'cnyaud':
        result = num1 * 0.19
    elif operation == 'cnyeuro':
        result = num1 * 0.14
    elif operation == 'cnynok':
        result = num1 * 1.55
    elif operation == 'cnyjpy':
        result = num1 * 15.07
    elif operation == 'usdcny':
        result = num1 * 6.90
    elif operation == 'audcny':
        result = num1 * 5.25
    elif operation == 'eurocny':
        result = num1 * 7.11
    elif operation == 'nokcny':
        result = num1 * 0.64
    elif operation == 'jpycny':
        result = num1 * 0.067
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

    #Solution is formatted to show two decimal places
    formatted_result = "{:.2f}".format(result)
    
    #Prints the designated currency symbol
    custom_string = "{}".format(operation_word)

    return render_template('result.html', result=formatted_result, custom_string=custom_string)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)





