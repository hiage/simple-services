from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def greeting():
    name = request.args.get('name', 'World')
    return jsonify({'message': 'Hello, {}!'.format(name)})

if __name__ == '__main__':
    app.run()