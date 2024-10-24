from flask import Flask, render_template, jsonify

app = Flask(__name__)

# API route that returns "server is up and running"
@app.route('/api/status', methods=['GET'])
def api_status():
    return jsonify({"message": "server is up and running"}), 200

# Web route that renders a template greeting the user
@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

