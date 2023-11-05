import re
import long_responses as long

def messgae_probability(user_messgge, recognised_words, single_response=False, required_words=[]) :
    messeage_certainly = 0
    has_required_words = True

    # Count how many words are present in each predefined 
    for word in user_messgge:
        if word in recognised_words:
            messeage_certainly += 1
    
    # Calculate the percent of recognised words in a user message 
    percentage = float(messeage_certainly) / float(len(recognised_words))

    for words in required_words:
        if words not in user_messgge:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0
    

def check_all_messages(message):
    highest_prob_list = {}
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = messgae_probability(message, list_of_words, single_response, required_words)

    # Responses
    response('Hello!', ['hello','hi','sup','hey', 'heyo'], single_response=True)
    response('I\'m doing fine, and you?', ['how' , 'are', 'you', 'doing'], required_words=['how'])
    response('Thank you!', ['i', 'love', 'code', 'palace'], required_words=['code', 'palace'])

    # Long responses
    response(long.R_EATING, ['what', 'you', 'eat'], required_words=['you', 'eat'])
    response(long.R_ADVISE, ['give', 'advice'], required_words=['advice'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get response 
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


# Test your response system 
while True:
    print('Bot: '+ get_response(input('You: ')))