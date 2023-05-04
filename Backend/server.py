import os
import sys
from indicnlp import common
from flask import Flask, request
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator

# create the Flask app
app = Flask(__name__)

# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME=r"indic_nlp_library"

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES=r"indic_nlp_resources"

SCRIPT_RANGES={
                "Punjabi":'pa', 
                "Gujarati":'gu', 
                "Odia":'or', 
                "Tamil":'ta', 
                "Telugu":'te', 
                "Kannada":'kn', 
                "Malayalam":'ml', 
                "Sinhala":'si', 
                "Hindi":'hi',
                "Urdu":"hi", 
                "Marathi":'mr',   
                "Konkani":'kK',   
                "Sanskrit":'sa',   
                "Nepali":'ne',  
                "Sindhi":'sd', 
                "Bengali":'bn', 
                "Assamese":'as'
              }

# Add library to Python path
sys.path.append(r'{}\src'.format(INDIC_NLP_LIB_HOME))

# Set environment variable for resources folder
common.set_resources_path(INDIC_NLP_RESOURCES)

@app.route('/language_code',methods=['GET'])
def get_language_code():
    return SCRIPT_RANGES

@app.route('/tranliterate',methods=['POST'])
def tranliterate():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.get_json()
        script_from_language=json["from_language"]
        script_to_language=json["to_language"]
        sentence=json["sentence"]

        try:
            script_from_language=SCRIPT_RANGES[script_from_language]
            script_to_language=SCRIPT_RANGES[script_to_language]
        except:
            return "Error in the Language Code, Check the language format in /language_code",400
    
        transliterate_word=UnicodeIndicTransliterator.transliterate(sentence,script_from_language,script_to_language)
        print(transliterate_word)
        return transliterate_word
    else:
        return "Not a json content",400

@app.route("/")
def health():
    return f"Server is up!, Server information ----> {os.uname()}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8300,debug=False)