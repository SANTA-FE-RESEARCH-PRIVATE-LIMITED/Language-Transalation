# Language Transliteration - Backend
## Getting started
## About the installation
- Create a virtual environment for installing the pip packages
- Install the required packages using `pip install -r requirements.txt`

## Starting the server
- The server runs on flask development server, Start the server using `python3 server.py`

## Server endpoints
- To get the languages that can be translitered by the application
    ```
    ENDPOINT: /language_code
    METHOD: GET
    RESPONSE: 
    {
        "accepted_languages":<list> # List of languages
    }
    STATUS_CODE: 200
    ```
- To transliterate a word
    ```
    ENDPOINT: /transliterate
    METHOD: POST
    HEADER : 
    {
        'Content-Type':'application/json'
    }
    REQUEST_PAYLOAD: 
    {
        'from_language':<str> # Language that were feteched from the /language_code endpoint
        'to_language':<str> # Language that were feteched from the /language_code endpoint
        'sentence':<str> # Sentence to be transliterate!
    }
    RESPONSE:
    {
        "input_words":<str>
        "transliterated_word:<str>
    }
    STATUS_CODE: 200
    ```
- Incase of error
    ```
    STATUS_CODE:400
    RESPONSE: 
    {
        "error":<message containing the reason>
        "msg_code":400 
    }
    ```