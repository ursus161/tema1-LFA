import pprint

def parse_input(filename):

    transition_function = {}

    with open(filename, 'r') as f:

        lines = f.readlines()
        states = lines[1].strip().split()
        noEdges = int(lines[2].strip())
        alphabet = []

        for el in lines[3:3+noEdges]: #3+noEdges exclusiv 

            el = el.strip().split()
            leaving_state , arriving_state, symbol = el

            if symbol not in alphabet:
                alphabet.append(symbol)

            if leaving_state not in transition_function:
                transition_function[leaving_state] = {symbol : arriving_state}
            else:
                transition_function[leaving_state].update({symbol : arriving_state})
        
             
        initState = lines[3+noEdges].strip()
        noFinalStates = int(lines[3+noEdges+1].strip())
        finalStates = []

        for el in lines[5+noEdges:5+noEdges+noFinalStates]:
                finalStates.append(el.strip())
            
        noWordsToCheck = int(lines[5+noEdges+noFinalStates])
        wordsToCheck = []

        for el in lines[6+noEdges+noFinalStates:]:
            wordsToCheck.append(el.strip())

        return(states, alphabet, transition_function, initState, finalStates, wordsToCheck)
    
