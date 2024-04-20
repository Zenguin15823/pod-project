#!/usr/bin/env python
from os import environ
from pod import app

app.run(host='0.0.0.0', debug=True, port=8080)