import sys
import os
from flask import Flask, render_template
import webbrowser
from threading import Timer
# यह सुनिश्चित करता है कि PyInstaller के अंदर भी templates फोल्डर सही मिले
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
def open_browser():
	webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    Timer(1.2, open_browser).start()
    app.run(port=5000, debug=False)