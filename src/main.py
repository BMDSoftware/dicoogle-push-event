import os

from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file('index.html')

""" Notify receives a GET message 
"""
@app.route("/notify")
def notify():
    # Get query params
    name = request.args.get('name')
    
    # Return a JSON response
    return jsonify({'name': name})

""" Notify receives a POST message
"""
@app.route("/notify_post", methods=['POST'])
def notify_post():
    # 
    return jsonify({'name': name})


def main():
    app.run(port=int(os.environ.get('PORT', 9005)))

if __name__ == "__main__":
    main()
