import random

# Define a list of possible user inputs and bot responses
user_inputs = ["hi", "hello", "how are you?", "what's your name?", "bye","uma"]
bot_responses = ["Hello!", "Hi there!", "I'm doing great, thanks!", "My name is Chatbot.", "Goodbye!","Hey hi"]

# Function to generate bot's response based on user input
def generate_response(user_input):
    if user_input.lower() in ["hi", "hello"]:
        return random.choice(bot_responses[:3])
    elif user_input.lower() == "how are you?":
        return bot_responses[2]
    elif user_input.lower() == "what's your name?":
        return bot_responses[3]
    elif user_input.lower() == "bye":
        return bot_responses[4]
    elif user_input.lower() == "uma":
        return bot_responses[5]
    else:
        return "I'm sorry, I didn't understand that."

# Main program loop
while True:
    user_input = input("User: ")
    bot_response = generate_response(user_input)
    print("Bot:", bot_response)



