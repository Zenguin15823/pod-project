# The Pod Project

This project represents a collaboration with Dave Clark to supplement an interactive art project. Mr. Clark has created a show piece of ambient pods and wishes to introduce an opportunity for viewers to interact with the art. The approach we have taken is to employ a Raspberry Pi to display lighting effects based on motion detection.

https://github.com/Zenguin15823/pod-project/assets/90000508/6cdfb410-0e3a-4c3e-955b-b0ff654102a6

## Install

Since we want the program to load when the Pi starts up, adding a `systemd` configuration seems like the best choice.

```
[Unit]
Description=Pod-Project
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/pod-project/app.py
Restart=always
User=pi

[Install]
WantedBy=multi-user.target
```

https://www.makeuseof.com/what-is-systemd-launch-programs-raspberry-pi/

## Troubleshooting

### Favorite Icon

Inititally, we received a 404 on `favicon.ico`. The Flask team suggests handling the [favico](https://flask.palletsprojects.com/en/3.0.x/patterns/favicon/) as a static asset. E.g.

```html
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" />
```
