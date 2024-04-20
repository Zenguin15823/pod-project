from flask import Flask
from pod import views

app = Flask(__name__)
app.register_blueprint(views.bp)