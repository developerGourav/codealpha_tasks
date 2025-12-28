import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
# The first item is the regex pattern the user types
# The second item is a list of possible responses the bot can give
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you today?", "Greetings!"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by Gourav.", "You can call me ChatBot!", "I don't have a name, but I'm here to help."]
    ],
    [
        r"how are you ?",
        ["I'm doing good, thank you!", "I'm just a computer program, so I don't have feelings, but I'm functioning perfectly!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem at all.", "Don't worry about it."]
    ],
    [
        r"i am (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Great!", "That's awesome."]
    ],
    [
        r"(.*) help (.*)",
        ["I can help you with basic queries. Try asking my name or saying hello!", "Sure, what do you need help with?"]
    ],
    [
        r"(.*) created you?",
        ["I was created using Python and the NLTK library.", "A developer like you created me!"]
    ],
    [
        r"quit|exit|bye",
        ["Goodbye! Have a nice day.", "See you soon!", "Bye! Take care."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't quite understand that.", "Could you rephrase that?", "I'm still learning!"]
    ]
]

def start_chat():
    print("---------------------------------------------")
    print("Chatbot: Hello! I am online. Type 'quit' to exit.")
    print("---------------------------------------------")
    
    # Create the chatbot instance
    chatbot = Chat(pairs, reflections)
    
    # Start the conversation
    chatbot.converse()

if __name__ == "__main__":
    start_chat()