from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate():

    amharic_sentence = request.json.get('amharic_sentence')

    # Call your translation function here and get the English translation
    english_translation = translate_amharic_to_english(amharic_sentence)

    return jsonify({'english_translation': english_translation})

def translate_amharic_to_english(amharic_sentence):
    # Implement your translation logic here
    english_translation = f"Translated: {amharic_sentence}"

    return english_translation

if __name__ == '__main__':
    app.run(debug=False)
