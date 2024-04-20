from flask import Blueprint, render_template, request
from .ops import activate, off, test
from threading import Thread

bp = Blueprint('views', __name__)
# Decorate the routes with the @bp.route decorator

@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@bp.route('/start', methods=['GET'])
def start():
    message = 'The Pi is now aware of motion'
    t = Thread(target=activate)
    t.start()
    return render_template('index.html', message=message)

@bp.route('/stop', methods=['GET'])
def stop():
    message = 'The Pi is no longer aware of motion'
    off()
    return render_template('index.html', message=message)

@bp.route('/test', methods=['GET'])
def test():
    print('Test')
    message = 'Test the LED display'
    # test()
    return render_template('index.html', message=message)
