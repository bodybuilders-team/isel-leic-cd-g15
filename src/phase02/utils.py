import os


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
