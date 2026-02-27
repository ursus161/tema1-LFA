import pprint 

def parse_input(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

        states= lines[0].replace('\n','')
        alphabet= lines[1].replace('\n','').split(',')
        final_states= lines[2].replace('\n','').split(';')
        initial_state=lines[3].replace('\n','')

        transition_function = [el.strip('\n').split(':') for el in lines[4:]]
        transition_function = [(el[0],el[1].split(';')) for el in transition_function]
        transition_function= dict([(el[0], dict([element.split(',') for element in el[1]])) for el in transition_function])


        return ((states, alphabet, transition_function, initial_state, final_states))


states, alphabet, transition_function, initial_state, final_states = parse_input('input.txt')

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
 
print(dfa_acceptor(parse_input('input.txt'), input('Introdu un cuvant pentru a il verifica daca este acceptat sau nu: ')))

