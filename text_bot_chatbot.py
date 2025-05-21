import nltk
import random

# Download required data
nltk.download('punkt')

# Sample responses
greetings = ["hello", "hi", "hey", "hola", "namaste"]
greet_responses = ["Hello there!", "Hi! How can I help you?", "Hey buddy!", "Hi, superstar!"]

farewells = ["bye", "goodbye", "see you", "exit", "quit"]
farewell_responses = ["Goodbye!", "See you later!", "Bye, have a great day!", "Take care!"]

def respond(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)

    if any(word in greetings for word in tokens):
        return random.choice(greet_responses)
    elif any(word in farewells for word in tokens):
        return random.choice(farewell_responses)
    else:
        return "I'm still learning. Can you ask something else?"

# Chat loop
print("ChatBot: Hello! I'm your chatbot. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("ChatBot: Goodbye!")
        break
    response = respond(user_input)
    print("ChatBot:", response)
