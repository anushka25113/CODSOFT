import re

def rule_based_chatbot(user_input):
    user_input = user_input.lower()

    # Simple pattern matching for common user queries
    if re.search(r'\b(hi|hello|hey)\b', user_input):
        return "Hello! How can I assist you today?"

    elif re.search(r'\b(how are you|how are you doing)\b', user_input):
        return "I'm just a computer program, but I'm here to help!"

    elif re.search(r'\b(goodbye|bye|see you)\b', user_input):
        return "Goodbye! If you have more questions, feel free to ask."

    elif re.search(r'\b(thank you|thanks)\b', user_input):
        return "You're welcome! Anything else you'd like to know?"

    # Additional predefined rules
    elif re.search(r'\b(weather|forecast)\b', user_input):
        return "I'm sorry, I don't have real-time weather information. You can check a weather website for that."

    elif re.search(r'\b(joke|funny)\b', user_input):
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif re.search(r'\b(age|old)\b', user_input):
        return "I don't have an age. I'm just a program running on a computer."

    else:
        return "I'm sorry, I don't understand that. Can you please ask something else?"

# Main loop for the chatbot
while True:
    user_query = input("You: ")

    if user_query.lower() in ['exit', 'quit']:
        print("Chatbot: Goodbye!")
        break

    bot_response = rule_based_chatbot(user_query)
    print("Chatbot:", bot_response)
    