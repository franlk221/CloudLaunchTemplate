from flask import Flask, request
app = Flask(__name__)

seed = 0
dct = {}

@app.route('/', methods=['GET','POST'])
def main():
    global seed
    if request.method == 'GET':
        dct['seed'] = seed
        return str(dct['seed'])
    if request.method == 'POST':
        newSeed = request.get_json()
        seed = new_seed['num']
        dct['seed'] = new_seed['num']
        return str(dct['seed'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
