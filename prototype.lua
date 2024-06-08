-- Welcome to the prototype for the dice rolling app 'Dice Roller', an app that allows easy and in depth die customization

local current_die = {}

-- This function converts the table into a string
local function convert_table(tbl)
    local converted_table = {}
    for key, value in pairs(tbl) do
        table.insert(converted_table, value)
    end
    return '[' .. table.concat(converted_table, ", ") .. ']'
end

-- PLACEHOLDER - POST_GENERATE
local function post_generate()
    print('THIS IS A PLACEHOLDER')
end

-- This part generates the die based on the chosen preset
local function generate_1()
    current_die = {}
    print('\nDie generated!\nHere is your current die: ' .. convert_table(current_die))
    post_generate()
    return
end

local function generate_2()
    current_die = {}
    for i = 1, 20 do
        current_die[i] = i
    end
    print('\nDie generated!\nHere is your current die: ' .. convert_table(current_die))
    post_generate()
    return
end

local function generate_3()
    current_die = {}
    for i = 1, 6 do
        current_die[i] = i
    end
    print('\nDie generated!\nHere is your current die: ' .. convert_table(current_die))
    post_generate()
    return
end

-- This variable is the list of available options in the generate() function
local die_presets = {
    ['1'] = generate_1,
    ['2'] = generate_2,
    ['3'] = generate_3
}

-- This part is the beginning of the dice rolling, it lets the user select which preset they want to use
local function generate()
    print('\nWelcome to Dice Roller! What dice would you like to generate?\n1: Empty / 2: d20 / 3: d6\n')
    local chosen_preset = io.read()

    if die_presets[chosen_preset] ~= nil then
        die_presets[chosen_preset]()
        return
    else
        print('\nError: Answer not recognized')
        generate()
        return
    end
end

generate()