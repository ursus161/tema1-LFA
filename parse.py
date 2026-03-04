def parse_input(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

        machine = input('Parsam un DFA SAU NFA?\n').strip().upper()

        states= lines[0].replace('\n','')
        alphabet= lines[1].replace('\n','').split(',')
        final_states= lines[2].replace('\n','').split(';')
        initial_state=lines[3].replace('\n','')

        transition_function = [el.strip('\n').split(':') for el in lines[4:]]
        transition_function = [(el[0],el[1].split(';')) for el in transition_function]
        transition_function= dict([(el[0], dict([element.split(',') for element in el[1]])) for el in transition_function])
        
        if machine == 'NFA':
            for state in transition_function:
                for word in list(transition_function[state]):

                    transition_function[state][word] = transition_function[state][word].split('/')
          
        

        return ((states, alphabet, transition_function, initial_state, final_states))