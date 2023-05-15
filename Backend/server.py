import os
import sys
from flask import Flask, request
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
    return GeneralMap.IndicScripts

@app.route('/tranliterate',methods=['POST'])
@cross_origin()
def tranliterate():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        from_language=json["from_language"]
        to_language=json["to_language"]
        sentence=json["sentence"]

        try:
            transliterate_word=transliterate.process(from_language,to_language,sentence)
        except Exception as e:
            print(e)
            return "Error in the Language Code, Check the language format in /language_code",400
    
        print(transliterate_word)
        return transliterate_word
    else:
        return "Not a json content",400

@app.route("/")
def health():
    return f"Server is up!, Server information ----> {os.uname()}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8400,debug=False)