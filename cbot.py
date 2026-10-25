import random

def chatbot():
    print("AI Chatbot: Hello! I am your AI Assistant.")
    print("Type 'bye' to exit.\n")

    responses = {
        "hello": ["Hello!", "Hi there!", "Hey! How can I help you?"],
        "hi": ["Hi!", "Hello!", "Hey there!"],
        "how are you": ["I am fine!", "I'm doing great!"],
        "what is your name": ["My name is AI Chatbot."],
        "who created you": ["I was created using Python."],
        "what is ai": ["AI stands for Artificial Intelligence."],
        "thank you": ["You are welcome!", "Happy to help!"],
        "bye": ["Goodbye!", "See you soon!"]
    }

    while True:
        user = input("You: ").lower().strip()

        if user == "bye":
            print("Chatbot: Goodbye! Have a nice day!")

            break

        if user in responses:
            reply = random.choice(responses[user])
            print("Chatbot:", reply,"\n")
        else:
            print("Chatbot: Sorry I can't understand.")

chatbot()                