import pprint 

def parse_input(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

        states= lines[0].replace('\n','')
        alphabet= lines[1].replace('\n','')
        final_states= lines[2].replace('\n','')
        initial_state=lines[3].replace('\n','')

        transition_function = [el.strip('\n').split(':') for el in lines[4:]]
        transition_function = [(el[0],el[1].split(';')) for el in transition_function]
        transition_function= dict([(el[0], dict([element.split(',') for element in el[1]])) for el in transition_function])


        return ((states, alphabet, transition_function, initial_state, final_states))


states, alphabet, transition_function, initial_state, final_states = parse_input('input.txt')

def dfa_acceptor(dfa, input_string):
    states, alphabet, transition_function, initial_state, final_states = dfa
    current_state = initial_state

    for symbol in input_string:
        if symbol not in alphabet:
            print(f"Simbolul {symbol} nu face parte din alfabet.")
            return False  
        if current_state not in transition_function or symbol not in transition_function[current_state]:
            print(f"Tranzitia pentru starea {current_state} si simbolul {symbol} nu este definita.")
            return False  # functia de tranzitie nu este complet definita 
        current_state = transition_function[current_state][symbol]

    return current_state in final_states
 
print(dfa_acceptor(parse_input('input.txt'), input('Introdu un cuvant pentru a il verifica daca este acceptat sau nu: ')))

