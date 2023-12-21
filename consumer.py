import requests
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os

producer = os.getenv('PRODUCER_API')
app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def root():
    return ''

@app.route('/consume')
def consume():
    url = 'http://' + producer + '/produce'
    response = requests.get(url)
    return f'Message from Consumer Service: {response.text}'

if __name__ == '__main__':
    metrics.start_http_server(port=50022)
    app.run(host='0.0.0.0', port=5002, debug=True)
