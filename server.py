import os
import sys
import json
from flask import Flask, request,jsonify
from flask_cors import CORS, cross_origin
from aksharamukha import transliterate
from aksharamukha import GeneralMap

# create the Flask app
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

SCRIPT_LANGUAGES = ["autodetect",*GeneralMap.IndicScripts]

@app.route('/language_code',methods=['GET'])
@cross_origin()
def get_language_code():
    return SCRIPT_LANGUAGES

@app.route('/tranliterate',methods=['POST'])
@cross_origin()
def tranliterate():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json_data = request.get_json()
        from_language=json_data["from_language"]
        to_language=json_data["to_language"]
        sentence=json_data["sentence"]

        if from_language not in SCRIPT_LANGUAGES:
            return "Incorrect from_language",400
        if to_language not in SCRIPT_LANGUAGES:
            return "Incorrect to_language",400

        try:
            transliterate_word=transliterate.process(from_language,to_language,sentence)
        except Exception as e:
            return e,400
        
        return json.dumps({"input_words":from_language,"translitered_words":transliterate_word},ensure_ascii=False)
    else:
        return "Not a json content",400

@app.route("/")
def health():
    return f"Server is up!, Server information ----> {os.uname()}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8400,debug=False)