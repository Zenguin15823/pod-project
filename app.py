from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def greet():
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start():
    print('Start')
    message = 'The Pi is now aware of motion'
    return render_template('index.html', message=message)

@app.route('/stop', methods=['GET'])
def stop():
    print('Stop')
    message = 'The Pi is no longer aware of motion'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080)
