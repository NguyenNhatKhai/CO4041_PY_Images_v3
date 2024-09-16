#

from constant import *
from random import random

def two_parameters_gilbert_elliot(encoder_path, channel_path):
    with open(f"{encoder_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    state = 'good'
    destination_content = []
    for char in source_content:
        if state == 'good':
            destination_content.append(char)
            if random() < GE2_GOOD_TO_BAD:
                state = 'bad'
        elif state == 'bad':
            destination_content.append('0' if char == '1' else '1')
            if random() < GE2_BAD_TO_GOOD:
                state = 'good'
    with open (f"{channel_path}.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))
