import names

import random

def generate_pairs(pairs_num): 
    flatlanders_names = []
    generated_names = 0

    while generated_names < pairs_num:
        name = names.get_first_name()
        if name not in flatlanders_names:
            flatlanders_names.append(name)
            generated_names += 1

    front_flatlanders = flatlanders_names[:len(flatlanders_names) // 2]
    back_flatlanders = flatlanders_names[len(flatlanders_names) // 2:]

    flatlanders_pairs = []
    pairs_generated = 0

    while pairs_generated < pairs_num:
        random_pair = (random.choice(front_flatlanders), random.choice(back_flatlanders))
        if random_pair not in flatlanders_pairs:
            flatlanders_pairs.append(random_pair)
            pairs_generated += 1

    return flatlanders_pairs

def save_pairs_to_file(pairs):
    with open('flatlanders_pairs.txt', 'w') as file:
        for pair in pairs:
            file.write(pair[0] + " " + pair[1] + "\n")