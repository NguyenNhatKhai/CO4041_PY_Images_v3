#

import channel
import comparator
import constant
import decoder
import encoder
import image
import sys

image_0 = 'Image/image_0'
# image.convert_to_text(image_0)

print(f"\tEncoding")
encoder_1 = 'Encoder/encoder_1'
encoder_2 = 'Encoder/encoder_2'
encoder_3 = 'Encoder/encoder_3'
encoder_4 = 'Encoder/encoder_4'
interleave_coefficient_2 = 1
interleave_coefficient_3 = 2
interleave_coefficient_4 = 4
# encoder.rs_encode(image_0, encoder_1)
# encoder.rs_encode_hamming_encode(image_0, encoder_2, interleave_coefficient_2)
# encoder.rs_encode_hamming_encode(image_0, encoder_3, interleave_coefficient_3)
# encoder.rs_encode_hamming_encode(image_0, encoder_4, interleave_coefficient_4)

print(f"\tTransmitting")
channel_0 = 'Channel/channel_0'
channel_1 = 'Channel/channel_1'
channel_2 = 'Channel/channel_2'
channel_3 = 'Channel/channel_3'
channel_4 = 'Channel/channel_4'
channel.two_parameters_gilbert_elliot(image_0, channel_0)
channel.two_parameters_gilbert_elliot(encoder_1, channel_1)
channel.two_parameters_gilbert_elliot(encoder_2, channel_2)
channel.two_parameters_gilbert_elliot(encoder_3, channel_3)
channel.two_parameters_gilbert_elliot(encoder_4, channel_4)

print(f"\tDecoding #1")
image_1 = 'Image/image_1'
image.reformat_decoder(channel_0, image_1)
# image.convert_to_image(image_1)

print(f"\tDecoding #2")
decoder_2 = 'Decoder/decoder_2'
image_2 = 'Image/image_2'
decoder.post_rs_decode(encoder_1, channel_1, decoder_2)
image.reformat_decoder(decoder_2, image_2)
# image.convert_to_image(image_2)

print(f"\tDecoding #3")
decoder_3 = 'Decoder/decoder_3'
image_3 = 'Image/image_3'
decoder.post_hamming_post_rs_decode(encoder_2, channel_2, decoder_3, interleave_coefficient_2)
image.reformat_decoder(decoder_3, image_3)
# image.convert_to_image(image_3)

print(f"\tDecoding #4")
decoder_4 = 'Decoder/decoder_4'
image_4 = 'Image/image_4'
decoder.post_hamming_post_rs_decode(encoder_3, channel_3, decoder_4, interleave_coefficient_3)
image.reformat_decoder(decoder_4, image_4)
# image.convert_to_image(image_4)

print(f"\tDecoding #5")
decoder_5 = 'Decoder/decoder_5'
image_5 = 'Image/image_5'
decoder.post_hamming_post_rs_decode(encoder_4, channel_4, decoder_5, interleave_coefficient_4)
image.reformat_decoder(decoder_5, image_5)
# image.convert_to_image(image_5)

print(f"\tComparing")
# text_file = open('main.txt', 'w')
text_file_name = sys.argv[1]
text_file = open(text_file_name, 'w')
def image_compare(image_name_0, image_name_1):
    text_file.write(f"{comparator.segment_compare(image_name_0, image_name_1, 1) / constant.IMAGE_BITS:.32f}\n")
image_compare(image_0, image_1)
image_compare(image_0, image_2)
image_compare(image_0, image_3)
image_compare(image_0, image_4)
image_compare(image_0, image_5)
text_file.close()

# print(f"{comparator.consecutive_compare(encoder_0, channel_0)}")
# print(f"{comparator.consecutive_compare(encoder_1, channel_1)}")