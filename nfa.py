from parse import parse_input
from dfa import dfa_acceptor
 

# m am gandit sa fac conversie de fiecare data de la orice automat finit nedeterminist la unul determinist
# ulterior de la un automat finit nedeterminist cu lambda miscari la unul fara lambda miscari


# desi nu s a mentionat la curs, mie mi se pare
def nfa_to_dfa(states, alphabet, transition_function, init_state, final_states):
    start = frozenset({init_state}) # o fac frozenset pentru a o avea hashable

    dfa_states = [start]
    dfa_transition = {}
    queue = [start]

    while queue: 
        current = queue.pop(0)
        dfa_transition[current] = {}
        for symbol in alphabet:  #ma uit unde merge simbolul symbol si adun tot in acel frozenset
            next_states = frozenset(
                s for state in current
                for s in transition_function.get(state, {}).get(symbol, [])
            )
            dfa_transition[current][symbol] = next_states
            if next_states not in dfa_states:
                dfa_states.append(next_states)
                queue.append(next_states)

    dfa_final = [s for s in dfa_states if s & set(final_states)]

  
    return dfa_states, alphabet, dfa_transition, start, dfa_final




if __name__ == '__main__':
    states, alphabet, tf, init, finals, words = parse_input('nfa_input.txt')
    dfa_states, dfa_alphabet, dfa_tf, dfa_init, dfa_finals = nfa_to_dfa(states, alphabet, tf, init, finals)
    print(dfa_acceptor((dfa_states, dfa_alphabet, dfa_tf, dfa_init, dfa_finals, words)))