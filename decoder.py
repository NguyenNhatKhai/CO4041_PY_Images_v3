#

from constant import *

def rs_remove_parity(source_path, decoder_path):
    with open(f"{source_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    destination_content = []
    for i in range(0, len(source_content), RS_CODEWORD):
        destination_content.append(source_content[i : i + RS_MESSAGE])
    with open(f"{decoder_path}_rs_parity_removed.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def pre_rs_decode(source_path, decoder_path):
    rs_remove_parity(source_path, decoder_path)
    with open(f"{decoder_path}_rs_parity_removed.txt", 'r') as source_file:
        source_content = source_file.read()
    with open(f"{decoder_path}.txt", 'w') as destination_file:
        destination_file.write(source_content)

def rs_decoding(encoder_path, source_path, decoder_path):
    with open(f"{encoder_path}_rs_parity_added.txt", 'r') as original_file:
        original_content = original_file.read()
    with open(f"{source_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    destination_content = []
    for i in range(len(source_content) // RS_CODEWORD):
        start = i * RS_CODEWORD
        end = start + RS_CODEWORD
        different_symbols = 0
        for j in range(start, end, RS_SYMBOL):
            if original_content[j : j + RS_SYMBOL] != source_content[j : j + RS_SYMBOL]:
                different_symbols += 1
        if different_symbols > RS_CAPABILITY:
            destination_content.append(source_content[start : end])
        else:
            destination_content.append(original_content[start : end])
    with open(f"{decoder_path}_rs_decoded.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def post_rs_decode(encoder_path, source_path, decoder_path):
    rs_decoding(encoder_path, source_path, decoder_path)
    rs_remove_parity(f"{decoder_path}_rs_decoded", decoder_path)
    with open(f"{decoder_path}_rs_parity_removed.txt", 'r') as source_file:
        source_content = source_file.read()
    with open(f"{decoder_path}.txt", 'w') as destination_file:
        destination_file.write(source_content)

def deinterleave(source_path, decoder_path, interleave_coefficient):
    with open(f"{source_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    interleave_length = interleave_coefficient * HAMMING_MESSAGE
    destination_content = []
    for i in range(len(source_content) // interleave_length):
        for j in range(interleave_coefficient):
            for k in range(HAMMING_MESSAGE):
                destination_content.append(source_content[i * interleave_length + k * interleave_coefficient + j])
    with open(f"{decoder_path}_deinterleaved.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def hamming_remove_parity(source_path, decoder_path):
    with open(f"{source_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    destination_content = []
    for i in range(0, len(source_content), HAMMING_CODEWORD):
        destination_content.append(source_content[i : i + HAMMING_MESSAGE])
    with open(f"{decoder_path}_hamming_parity_removed.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def pre_hamming_pre_rs_decode(source_path, decoder_path, interleave_coefficient):
    interleave(source_path, decoder_path, interleave_coefficient)
    hamming_remove_parity(f"{decoder_path}_interleaved", decoder_path)
    deinterleave(f"{decoder_path}_hamming_parity_removed", decoder_path, interleave_coefficient)
    pre_rs_decode(f"{decoder_path}_deinterleaved", decoder_path)

def pre_hamming_post_rs_decode(encoder_path, source_path, decoder_path, interleave_coefficient):
    interleave(source_path, decoder_path, interleave_coefficient)
    hamming_remove_parity(f"{decoder_path}_interleaved", decoder_path)
    deinterleave(f"{decoder_path}_hamming_parity_removed", decoder_path, interleave_coefficient)
    post_rs_decode(encoder_path, f"{decoder_path}_deinterleaved", decoder_path)

def hamming_decoding(encoder_path, source_path, decoder_path):
    with open(f"{encoder_path}_hamming_parity_added.txt", 'r') as original_file:
        original_content = original_file.read()
    with open(f"{source_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    destination_content = []
    for i in range(len(source_content) // HAMMING_CODEWORD):
        start = i * HAMMING_CODEWORD
        end = start + HAMMING_CODEWORD
        different_bits = 0
        for j in range(start, end):
            if original_content[j] != source_content[j]:
                different_bits += 1
        if different_bits > 1:
            destination_content.append(source_content[start : end])
        else:
            destination_content.append(original_content[start : end])
    with open(f"{decoder_path}_hamming_decoded.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def interleave(source_path, decoder_path, interleave_coefficient):
    with open(f"{source_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    interleave_length = interleave_coefficient * HAMMING_CODEWORD
    destination_content = []
    for i in range(len(source_content) // interleave_length):
        for j in range(HAMMING_CODEWORD):
            for k in range(interleave_coefficient):
                destination_content.append(source_content[i * interleave_length + k * HAMMING_CODEWORD + j])
    with open(f"{decoder_path}_interleaved.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def post_hamming_pre_rs_decode(encoder_path, source_path, decoder_path, interleave_coefficient):
    interleave(source_path, decoder_path, interleave_coefficient)
    hamming_decoding(encoder_path, f"{decoder_path}_interleaved", decoder_path)
    hamming_remove_parity(f"{decoder_path}_hamming_decoded", decoder_path)
    deinterleave(f"{decoder_path}_hamming_parity_removed", decoder_path, interleave_coefficient)
    pre_rs_decode(f"{decoder_path}_deinterleaved", decoder_path)

def post_hamming_post_rs_decode(encoder_path, source_path, decoder_path, interleave_coefficient):
    interleave(source_path, decoder_path, interleave_coefficient)
    hamming_decoding(encoder_path, f"{decoder_path}_interleaved", decoder_path)
    hamming_remove_parity(f"{decoder_path}_hamming_decoded", decoder_path)
    deinterleave(f"{decoder_path}_hamming_parity_removed", decoder_path, interleave_coefficient)
    post_rs_decode(encoder_path, f"{decoder_path}_deinterleaved", decoder_path)
    