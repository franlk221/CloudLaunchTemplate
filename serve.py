from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def main():
    if request.method == 'GET':
        return socket.gethostname()
    if request.method == 'POST':
        subprocess.Popen(['python3', 'stress_cpu.py'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
