import pprint
from parse import parse_input


# states, alphabet, transition_function, initial_state, final_states = parse_input('dfa.txt')

# print("States:", states)
# print("Alphabet:", alphabet)
# print("Transition Function:")
# pprint.pprint(transition_function)

def dfa_acceptor(dfa, input_string):

    states, alphabet, transition_function, initial_state, final_states = dfa
    current_state = initial_state
    i = 0

    while i < len(input_string):

        match_found = False

        for symbol in sorted(alphabet, key=len, reverse=True): #incerc sa abordez greedy iau cat mai mare pot
            if input_string.startswith(symbol, i): 

                if current_state in transition_function and symbol in transition_function[current_state]:


                    current_state = transition_function[current_state][symbol]
                    i += len(symbol) #si sar peste simbol 
                    match_found = True
                    break

        if not match_found:
            return False

    return current_state in final_states
 
print(dfa_acceptor(parse_input('dfa.txt'), input('Introdu un cuvant pentru a il verifica daca este acceptat sau nu: ')))
 

