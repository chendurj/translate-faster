from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask backend!"})

if __name__ == '__main__':
    app.run(debug=True)


# # Mock translation function
# def translate_text(text, target_language):
#     # Here you can connect to your translation model later
#     return f"Translated '{text}' to {target_language}"



# # API route for translation
# @app.route('/translate', methods=['POST'])
# def translate():
#     data = request.get_json()
#     text = data.get('text')
#     target_language = data.get('target_language')
    
#     if not text or not target_language:
#         return jsonify({"error": "Text and target_language are required"}), 400

#     translated_text = translate_text(text, target_language)
#     return jsonify({"translated_text": translated_text})

# if __name__ == '__main__':
#     app.run(debug=True)
