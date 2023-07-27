from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__)

responses = {
  "hi": ["Hello!", "Hi there!", "Hey!"],
  "how are you":
  ["I'm doing well, thank you!", "I'm fine, how about you?", "All good!"],
  "bye": ["Goodbye!", "See you later!", "Bye-bye!"],
  "what's your name": [
    "I'm a chatbot!", "I don't have a name, but you can call me Bot.",
    "I'm an AI language model!"
  ],
  "tell me a joke": [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why don't some couples go to the gym? Because some relationships don't work out!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
  ],
  "thank you": ["You're welcome!", "No problem!", "Anytime!"],
  "how old are you": [
    "I don't have an age, I'm a program running on a computer!",
    "Age is just a number for a chatbot like me!"
  ],
  "what is your favorite color": [
    "I don't have preferences, as I'm an AI language model!",
    "I appreciate all colors equally!"
  ],
  "who created you": [
    "I was created by a team of developers at OpenAI!",
    "My creators are talented software engineers!"
  ],
  "where are you from": [
    "I exist in the virtual world of computers!",
    "You can find me in the servers of the internet!"
  ],
  "what can you do": [
    "I can chat with you, answer questions, and provide information!",
    "I'm designed for natural language understanding and conversation!"
  ],
  "who is your favorite actor": [
    "As an AI, I don't have personal preferences!",
    "I don't watch movies, but I can talk about actors!"
  ],
  "what is the meaning of life": [
    "The meaning of life is a profound philosophical question!",
    "Many philosophers have pondered this question for centuries!"
  ],
  "how can I learn programming": [
    "Learning programming requires practice and dedication!",
    "There are many online resources and tutorials available to start learning!"
  ],
  "what is the capital of france": [
    "The capital of France is Paris!",
    "Paris is known for its rich history and culture!"
  ],
  "tell me a fun fact": [
    "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
    "Bananas are berries, while strawberries are not actual berries but rather aggregate fruits!"
  ],
  "what is the weather today": [
    "I'm sorry, but I'm just a chatbot and cannot provide real-time information!",
    "Please check a weather website or app for the latest updates!"
  ],
  "do you like music": [
    "As an AI, I don't have preferences, but I can appreciate music!",
    "Music is a wonderful form of art and expression!"
  ],
  "who is your favorite author": [
    "As a chatbot, I don't have personal preferences!",
    "I can discuss various authors and their works if you'd like!"
  ],
  "what are your hobbies": [
    "I don't have hobbies, but I enjoy helping users like you!",
    "My main focus is on providing useful information and engaging in conversation!"
  ],
  "what is the meaning of ai": [
    "AI stands for Artificial Intelligence!",
    "AI is a field of computer science focused on creating intelligent machines that can perform tasks that typically require human intelligence!"
  ]
}


def get_response(user_input):
  user_input = user_input.lower()
  for key in responses:
    if key in user_input:
      return random.choice(responses[key])
  return "I'm sorry, I don't understand that. Can you try again?"


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
  user_message = request.form['user_message']
  response = get_response(user_message)
  return jsonify({'bot_message': response})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
