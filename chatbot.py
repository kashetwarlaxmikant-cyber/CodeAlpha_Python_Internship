```python
# CodeAlpha Task 4: Basic Chatbot

def chatbot():
    print("=" * 40)
    print("       WELCOME TO PYTHON CHATBOT")
    print("=" * 40)

    print("Chatbot: Hello! Welcome to my chatbot.")
    print("Chatbot: You can type 'bye' to exit.")
    print("Chatbot: Let's start chatting!\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks! How are you?")

        elif user_input == "i am fine":
            print("Chatbot: That's great to hear!")

        elif user_input == "what is your name":
            print("Chatbot: I am Python Chatbot.")

        elif user_input == "what can you do":
            print("Chatbot: I can answer simple predefined questions.")

        elif user_input == "thank you" or user_input == "thanks":
            print("Chatbot: You're welcome!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break

        elif user_input == "":
            print("Chatbot: Please type something.")

        else:
            print("Chatbot: Sorry, I don't understand that.")

    print("\nChatbot session ended.")


# Run the chatbot
if __name__ == "__main__":
    chatbot()
```
