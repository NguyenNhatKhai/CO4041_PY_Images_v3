#

from constant import *

def segment_compare(file_path_0, file_path_1, segment_length):
    with open(f"{file_path_0}.txt", 'r') as file_0, open(f"{file_path_1}.txt", 'r') as file_1:
        content_0 = file_0.read()
        content_1 = file_1.read()
    if len(content_0) != len(content_1):
        raise Exception("ERROR 1327")
    different_segments = 0
    for i in range(0, len(content_0), segment_length):
        if content_0[i : i + segment_length] != content_1[i : i + segment_length]:
            different_segments += 1
    return different_segments

def consecutive_compare(file_path_0, file_path_1):
    with open(f"{file_path_0}.txt", 'r') as file_0, open(f"{file_path_1}.txt", 'r') as file_1:
        content_0 = file_0.read()
        content_1 = file_1.read()
    if len(content_0) != len(content_1):
        raise Exception("ERROR 1901")
    different_consecutives = [0] * (2 * RS_SYMBOL)
    for i in range(len(content_0)):
        different_bits = 0
        while content_0[i] != content_1[i]:
            different_bits += 1
            i += 1
        if different_bits >= 2 * RS_SYMBOL:
            different_consecutives[0] += 1
        elif different_bits > 0:
            different_consecutives[different_bits] += 1
    return different_consecutives

        
        