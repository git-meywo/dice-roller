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




# WIP - The modify part is unusable at the moment, please refrain from using it
def ask_modify():
    chosen_option = input('\nWould you like to modify your die?\n1: Yes / 2: No / 3: See Current Die\n')
    if chosen_option in modify_options:
        exec(f'{modify_options[chosen_option]}()')
        return
    else:
        print('\nError: Answer not recognized')
        ask_modify()
        return

modify_options: dict = {
    '1': 'modify_option_1',
    '2': 'modify_option_2',
    '3': 'modify_option_3'
}




generate()
