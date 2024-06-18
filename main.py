from flask import Flask, request, jsonify, render_template
from src.chatbot import ChatBot
from src.conversation_flow import provide_response

app = Flask(__name__, template_folder='web/templates', static_folder='web/static')
chatbot = ChatBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = provide_response(chatbot, user_input)
    return jsonify({'response': response})


if __name__ == "__main__":
    app.run(debug=True)
