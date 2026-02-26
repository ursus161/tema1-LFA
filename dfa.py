

def parse_input(filename):
    with open(filename,'r') as f:
        lines = f.readlines()

        states= lines[0].replace('\n','')
        alphabet= lines[1].replace('\n','')
        final_states= lines[2].replace('\n','')
        initial_state=lines[3].replace('\n','')

        transition_function = [el.strip('\n').split(':') for el in lines[4:]]
        transition_function = [(el[0],el[1].split(';')) for el in transition_function]
        transition_function= [(el[0], [element.split(',') for element in el[1]]) for el in transition_function]


        print('states:',states)
        print('alphabet:',alphabet)
        print('final_states:',final_states)
        print('initial_state:',initial_state)
        print('transition_function:',transition_function)


parse_input("input.txt")
