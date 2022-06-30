import os
import random


def add_file_errors(input_file_path, output_file_path, error_prob):
    """
    Flips bits of file @ input_file_path based on error_prob and writes
    the output to file @ output_file_path
    """
    with open(input_file_path, 'rb') as f:
        file_bits = read_file_bits(f)

    with open(output_file_path, 'wb') as f:
        os.path.getsize(input_file_path)
        file_bit_size = len(file_bits)  # almost max integer size, for the 150 kb file...
        num_bit_errors = int(file_bit_size * error_prob)

        bit_error_idxs = random.sample(range(0, file_bit_size - 1), num_bit_errors)
        for bit_error_idx in bit_error_idxs:
            file_bits[bit_error_idx] = 1 if file_bits[bit_error_idx] == 0 else 0

        output_bytes = bits_to_bytes(file_bits)
        f.write(bytes(output_bytes))


def iterate_files(directory, callback):
    """
    Iterates through all files in a directory and calls a callback function for each file.

    :param directory: the directory to iterate through
    :param callback: the callback function to call for each file
    """

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)

        # Checking if it is a file
        if os.path.isfile(f):
            callback(f)


def byte_to_bits(b):
    """
    Converts a byte to a list of bits.

    :param b: the byte to convert
    :return: the list of bits
    """

    bits = []
    for i in range(8):
        bits.append((b >> i) & 1)

    return bits


def bits_to_byte(bits):
    """
    Converts a list of bits to a byte.

    :param bits: the list of bits
    :return: the byte
    """

    byte = 0
    for i in reversed(range(0, 8)):
        bit = bits[i]
        byte = (byte << 1) | bit

    return byte


def chunks(data, n):
    """
    Yield successive n-sized chunks from data.

    :param data: the data to chunk
    :param n: the size of each chunk
    """

    for i in range(0, len(data), n):
        yield data[i:i + n]


def read_file_bits(f):
    """
    Reads file as array of bits

    :param f: file
    :return: array of bits
    """

    file_bits = []
    while 1:
        # Do stuff with byte.
        byte_s = f.read(1)
        if not byte_s:
            break
        byte = byte_s[0]
        file_bits.extend(byte_to_bits(byte))

    return file_bits


def bits_to_bytes(decoded_bits):
    """
    Converts array of bits to array of bytes

    :param decoded_bits: bits
    :return: bytes
    """

    return [bits_to_byte(bits) for bits in chunks(decoded_bits, 8)]
