import os

from flask import Flask, send_file
from flask import request
from flask import jsonify # <- `jsonify` instead of `json`

app = Flask(__name__)

dicom_studies = []

@app.route("/")
def index():
    return send_file('index.html')

""" List studies"""
@app.route("/studies")
def studies():
    print(dicom_studies)

    # Return a JSON with studies.
    return jsonify({'studies': dicom_studies})


@app.route("/notify_post", methods=['POST'])
def notify_post():
    # Get POST JSON 
    response = request.get_json()
    print(response['StudyInstanceUID'])
    
    dicom_studies.append(response['StudyInstanceUID'])
    print(studies)
    # Return a JSON response
    return jsonify({'nStudies': len(dicom_studies)})


def main():
    app.run(port=int(os.environ.get('PORT', 9005)))

if __name__ == "__main__":
    main()
