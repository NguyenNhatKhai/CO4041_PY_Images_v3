#

from constant import *

def reformat_image(image_path, encoder_path):
    with open(f"{image_path}.txt", 'r') as source_file:
        source_content = source_file.read()
    destination_content = source_content + '0' * ((RS_MESSAGE - (len(source_content) % RS_MESSAGE)) % RS_MESSAGE)
    with open(f"{encoder_path}_image_reformated.txt", 'w') as destination_file:
        destination_file.write(destination_content)

def rs_add_parity(encoder_path):
    with open(f"{encoder_path}_image_reformated.txt", 'r') as source_file:
        source_content = source_file.read()
    destination_content = []
    for i in range(0, len(source_content), RS_MESSAGE):
        destination_content.append(source_content[i : i + RS_MESSAGE] + '0' * RS_PARITY)
    with open(f"{encoder_path}_rs_parity_added.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def rs_encode(image_path, encoder_path):
    reformat_image(image_path, encoder_path)
    rs_add_parity(encoder_path)
    with open(f"{encoder_path}_rs_parity_added.txt", 'r') as source_file:
        source_content = source_file.read()
    with open(f"{encoder_path}.txt", 'w') as destination_file:
        destination_file.write(source_content)

def interleave(encoder_path, interleave_coefficient):
    with open(f"{encoder_path}_rs_parity_added.txt", 'r') as source_file:
        source_content = source_file.read()
    interleave_length = interleave_coefficient * HAMMING_MESSAGE
    source_content += '0' * ((interleave_length - len(source_content) % interleave_length) % interleave_length)
    destination_content = []
    for i in range(len(source_content) // interleave_length):
        for j in range(HAMMING_MESSAGE):
            for k in range(interleave_coefficient):
                destination_content.append(source_content[i * interleave_length + k * HAMMING_MESSAGE + j])
    with open(f"{encoder_path}_interleaved.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))
        
def hamming_add_parity(encoder_path):
    with open(f"{encoder_path}_interleaved.txt", 'r') as source_file:
        source_content = source_file.read()
    destination_content = []
    for i in range(0, len(source_content), HAMMING_MESSAGE):
        destination_content.append(source_content[i : i + HAMMING_MESSAGE] + '0' * HAMMING_PARITY)
    with open(f"{encoder_path}_hamming_parity_added.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def deinterleave(encoder_path, interleave_coefficient):
    with open(f"{encoder_path}_hamming_parity_added.txt", 'r') as source_file:
        source_content = source_file.read()
    interleave_length = interleave_coefficient * HAMMING_CODEWORD
    destination_content = []
    for i in range(len(source_content) // interleave_length):
        for j in range(interleave_coefficient):
            for k in range(HAMMING_CODEWORD):
                destination_content.append(source_content[i * interleave_length + k * interleave_coefficient + j])
    with open(f"{encoder_path}_deinterleaved.txt", 'w') as destination_file:
        destination_file.write(''.join(destination_content))

def rs_encode_hamming_encode(image_path, encoder_path, interleave_coefficient):
    reformat_image(image_path, encoder_path)
    rs_add_parity(encoder_path)
    interleave(encoder_path, interleave_coefficient)
    hamming_add_parity(encoder_path)
    deinterleave(encoder_path, interleave_coefficient)
    with open(f"{encoder_path}_deinterleaved.txt", 'r') as source_file:
        source_content = source_file.read()
    with open(f"{encoder_path}.txt", 'w') as destination_file:
        destination_file.write(source_content)

            