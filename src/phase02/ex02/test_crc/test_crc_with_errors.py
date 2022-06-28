import random

from src.phase02.ex02.crc_file_check import crc_file_check
from src.phase02.ex02.crc_file_compute import crc_file_compute
from src.phase02.utils import *
import sys


def add_file_errors(input_file_path, output_file_path, error_prob):
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


def process_file(file_path):
    print("Reading " + file_path + " file...")
    head, tail = os.path.split(file_path)
    output_file_dir = "crc_files/"
    output_file = output_file_dir + tail

    if not os.path.exists(output_file_dir):
        os.mkdir(output_file_dir)

    crc_file_compute(file_path, output_file)

    test_file_paths = [output_file]

    error_probs = [0.0001, 0.001, 0.005, 0.01, 0.05]

    for error_prob in error_probs:
        head, tail = os.path.split(file_path)
        output_error_file_path = "crc_files/" + str(error_prob) + "_" + tail

        add_file_errors(output_file, output_error_file_path, error_prob)
        test_file_paths.append(output_error_file_path)

    for test_file_path in test_file_paths:
        print("Testing " + test_file_path)
        valid = crc_file_check(test_file_path)
        print("CRC Check passed: " + str(valid))
        sys.stdout.flush()


# Compute the CRC of test files
if __name__ == "__main__":
    sys.stdout = open('test_crc_with_errors.log', 'w')
    iterate_files("../../../docs/CD_TestFiles", process_file)

    sys.exit(0)
