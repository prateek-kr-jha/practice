
ACTIONS = ["jump", "close your eyes", "double blink", "wink"]

def commands(binary_str):

    action_sequence = [
        ACTIONS[i] 
        for i, bit in enumerate(binary_str[1:])
        if bit == "1"
    ]

    return action_sequence[::-1] if binary_str[0] == "0" else action_sequence
    


print(commands("00011"))