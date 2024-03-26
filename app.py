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
#USD to other currencies
    if operation == 'usdaud':
        result = num1 * 1.53
    elif operation == 'usdeuro':
        result = num1 * 0.92
    elif operation == 'usdnok':
        result = num1 * 10.70
    elif operation == 'usdjpy':
        result = num1 * 151.32
    elif operation == 'usdcny':
        result = num1 * 7.22
#AUD to other currencies
    elif operation == 'audjpy':
        result = num1 * 99.12
    elif operation == 'audnok':
        result = num1 * 7.01
    elif operation == 'audusd':
        result = num1* 0.65
    elif operation == 'audeuro':
        result = num1 * 0.60
    elif operation == 'audcny':
        result = num1 * 4.73
#EURO to other currencies
    elif operation == 'eurojpy':
        result = num1 * 164.07
    elif operation == 'eurousd':
        result = num1 * 1.08
    elif operation == 'euroaud':
       result = num1 * 1.66
    elif operation == 'euronok':
        result = num1 * 11.60
    elif operation == 'eurocny':
        result = num1 * 7.72
#NOK to other currencies
    elif operation == 'nokjpy':
        result = num1 * 14.14
    elif operation == 'nokusd':
        result = num1 * 0.093
    elif operation == 'nokaud':
        result = num1 * 0.14
    elif operation == 'nokeuro':
        result = num1 * 0.0086
    elif operation == 'nokcny':
        result = num1 * 0.67
#JPY to other currencies
    elif operation == 'jpyusd':
        result = num1 * 0.0066
    elif operation == 'jpyaud':
        result = num1 * 0.010
    elif operation == 'jpyeuro':
        result = num1 * 0.0061
    elif operation == 'jpynok':
        result = num1 * 0.071
    elif operation == 'jpycny':
        result = num1 * 0.048
#CNY to other currencies
    elif operation == 'cnyusd':
        result = num1 * 0.14
    elif operation == 'cnyaud':
        result = num1 * 0.21
    elif operation == 'cnyeuro':
        result = num1 * 0.13
    elif operation == 'cnynok':
        result = num1 * 1.48
    elif operation == 'cnyjpy':
        result = num1 * 20.97
#Invalid operation
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





