import os

from flask import Flask, send_file
from flask import request
from flask import jsonify # <- `jsonify` instead of `json`

app = Flask(__name__)

studies = []

@app.route("/")
def index():
    return send_file('index.html')

""" Notify receives a GET message 
"""
@app.route("/notify")

@app.route("/notify_post", methods=['POST'])
def notify_post():
    # Get POST JSON 
    response = request.get_json()
    studies.append(response['StudyInstanceUID'])
    # Return a JSON response
    return jsonify({'nStudies': len(studies)})


def main():
    app.run(port=int(os.environ.get('PORT', 9005)))

if __name__ == "__main__":
    main()
