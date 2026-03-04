from parse import parse_input
 
def nfa_acceptor(nfa, input_string):
    states, alphabet, transition_function, initial_state, final_states = nfa
    
    current_states = {initial_state}
    i = 0

    while i < len(input_string):

        match_found = False
        next_states = set()  #am mai multe cai posibile, fiind NFA

        for symbol in sorted(alphabet, key=len, reverse=True):

            if input_string.startswith(symbol, i):
                
                for state in current_states:

                    if state in transition_function and symbol in transition_function[state]:
                        next_states.update(transition_function[state][symbol])

                if next_states:
                    i += len(symbol)
                    match_found = True
                    current_states = next_states 
                    break  # problema daca am cv in genul : 'a' si 'aa' mi ar lua direct 'aa'

        if not match_found:
            return False

    return any(state in final_states for state in current_states)


print(nfa_acceptor(parse_input('nfa.txt'), input('Introdu un cuvant pentru a il verifica daca este acceptat sau nu: ')))