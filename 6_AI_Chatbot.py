#Import the necessary libraries
import random

# Create a dictionary of predefined responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm just a computer program, so I don't have feelings, but thanks for asking!", "I'm doing well, thanks!"],
    "bye": ["Goodbye!", "Farewell!", "See you later!"]
}

# Function to generate a response
def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "I'm sorry, I don't understand that."

# Main loop for user interaction
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = get_response(user_input)
    print("Chatbot:", response)
