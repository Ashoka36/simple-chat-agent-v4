
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    # Simple echo / logic for now. 
    # You can expand this to talk to an LLM or use custom logic.
    if "hello" in user_message.lower():
        response = "Hi there! I'm your simple chat agent hosted on Render. How can I help you today?"
    elif "who are you" in user_message.lower():
        response = "I am a simple Flask-based chat agent created by Twin."
    else:
        response = f"You said: {user_message}. This is a simple response from your agent."
    
    return jsonify({"response": response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
