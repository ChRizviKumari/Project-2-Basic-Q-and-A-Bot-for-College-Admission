def provide_response(chatbot, user_input):
    contextual_response = chatbot.get_contextual_response(user_input)
    if contextual_response:
        return contextual_response
    
    response = chatbot.get_response(user_input)
    chatbot.remember_context(user_input, response)
    return response
