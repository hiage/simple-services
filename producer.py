from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/')
def root():
    return ''

@app.route('/produce')
def produce():
    return 'Message from Producer Service'

if __name__ == '__main__':
    metrics.start_http_server(port=50011)
    app.run(host='0.0.0.0', port=5001, debug=True)
