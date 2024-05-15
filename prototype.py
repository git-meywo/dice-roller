# Welcome to the prototype for the dice rolling app 'Dice Roller', an app that allows easy and in depth die customization

current_die: list = []

# This part is the beginning of the dice rolling, it lets the user select which preset they want to use
def generate():
    chosen_preset = input('\nWelcome to Dice Roller! What die would you like to generate?\n1: Empty / 2: d20 / ...\n')
    if chosen_preset in die_presets:
        exec(f'{die_presets[chosen_preset]}()')
        return
    else:
        print('\nError: Answer not recognized')
        generate()
        return

die_presets: dict = {
    '1': 'generate_1',
    '2': 'generate_2'
}




# This part generates the die based on the chosen preset (view above for more information)
def generate_1():
    global current_die
    current_die = []
    print(f'\nDie generated!\nHere is your current die: {current_die}')
    return

def generate_2():
    global current_die
    current_die = [i for i in range(1, 21)]
    print(f'\nDie generated!\nHere is your current die: {current_die}')
    return




# This part lets the user select what they would like to do post generation
def post_generate():
    chosen_option = input('\nWhat would you like to do next?\n1: Edit my Die / 2: Roll my Die / 3: View Current Die\n')
    if chosen_option in post_options:
        exec(f'{post_options[chosen_option]}()')
        return
    else:
        print('\nError: Answer not recognized')
        post_generate()
        return

post_options: dict = {
    '1': 'post_option_1',
    '2': 'post_option_2',
    '3': 'post_option_3'
}




def post_option_1():
    return

def post_option_2():
    return

def post_option_3():
    return



generate()
