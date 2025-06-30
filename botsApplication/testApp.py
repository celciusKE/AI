from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot_endpoint():
    user_message = request.json.get('message')
    bot_response = ""

    if user_message:
        user_message_lower = user_message.lower()
        if "hello" in user_message_lower:
            bot_response = "Hi there! How can I help you today?"
        elif "how are you" in user_message_lower:
            bot_response = "I'm a bot, so I don't have feelings, but I'm ready to assist you!"
        elif "bye" in user_message_lower:
            bot_response = "Goodbye! Have a great day!"
        else:
            bot_response = "I'm not sure I understand. Can you rephrase that?"
    else:
        bot_response = "Please send a message."

    return jsonify({"message": bot_response})

if __name__ == '__main__':
    # Run on a specific port, e.g., 5000
    app.run(port=5000)