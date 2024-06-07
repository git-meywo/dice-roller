-- Welcome to the prototype for the dice rolling app 'Dice Roller', an app that allows easy and in depth die customization

local current_die = {}

local die_presets = {
    ['1'] = 'Generate_1',
    ['2'] = 'Generate_2',
    ['3'] = 'Generate_3'
}

-- This part is the beginning of the dice rolling, it lets the user select which preset they want to use
function Generate()
    print('\nWelcome to Dice Roller! What dice would you like to generate?\n1: Empty / 2: d20 / 3: d6\n')
    local chosen_preset = io.read()

    if die_presets[chosen_preset] ~= nil then
        local command = die_presets[chosen_preset] .. '()'
                load(command)()
        return
    else
        print('\nError: Answer not recognized')
        Generate()
        return
    end
end
