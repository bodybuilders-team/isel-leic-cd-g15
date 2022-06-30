from src.phase02.ex02.crc.crc_file_check import crc_file_check
from src.phase02.ex02.crc.crc_file_compute import crc_file_compute
from src.phase02.ex02.commacode_crc.unary import unary_encode, unary_decode
from src.phase02.utils import *
import sys

CHECKSUM_LENGTH = 4


def remove_checksum(output_file):
    """
    Removes checksum from output file.

    :param output_file: output file to remove checksum from
    """
    with open(output_file, 'rb') as rf:
        checksum = rf.read(CHECKSUM_LENGTH)
        data = rf.read()
    with open(output_file, 'wb') as wf:
        wf.write(data)

    return checksum


def insert_checksum(output_file, checksum):
    """
    Inserts checksum in output file.

    :param output_file: file to insert checksum in
    :param checksum: checksum to insert
    """
    with open(output_file, 'rb') as rf:
        data = rf.read()

    with open(output_file, 'wb') as wf:
        wf.write(checksum)
        wf.write(data)


def process_file(file_path):
    print("Reading " + file_path + " file...")
    head, tail = os.path.split(file_path)
    output_file_dir = "commacode_crc_files/"
    output_file = output_file_dir + tail
    decoded_output_file_dir = "decoded_commacode_crc_files/"

    if not os.path.exists(decoded_output_file_dir):
        os.mkdir(decoded_output_file_dir)

    if not os.path.exists(output_file_dir):
        os.mkdir(output_file_dir)

    # Creating checksum of original file
    crc_file_compute(file_path, output_file)

    checksum = remove_checksum(output_file)

    # Encoding original file
    unary_encode(file_path, output_file)

    # Inserting checksum of original file in encoded file
    insert_checksum(output_file, checksum)

    test_file_paths = [output_file]

    error_probs = [0.0001, 0.001, 0.005, 0.01, 0.05]

    for error_prob in error_probs:
        head, tail = os.path.split(file_path)
        output_error_file_path = output_file_dir + str(error_prob) + "_" + tail

        add_file_errors(output_file, output_error_file_path, error_prob)
        test_file_paths.append(output_error_file_path)

    for test_file_path in test_file_paths:
        print("Testing " + test_file_path)

        # Removing checksum of original file
        checksum = remove_checksum(test_file_path)

        head, tail = os.path.split(test_file_path)
        decoded_file_path = decoded_output_file_dir + tail

        # Decoding encoded file (may fail if there are too many errors)
        error = unary_decode(test_file_path, decoded_file_path)

        if error < 0:
            print("Could not decode file")
            continue

        insert_checksum(decoded_file_path, checksum)

        # Checking if crc is valid for decoded file
        valid = crc_file_check(decoded_file_path)
        print("CRC Check passed: " + str(valid))

        remove_checksum(decoded_file_path)

        sys.stdout.flush()


# Compute the CRC of test files
if __name__ == "__main__":
    sys.stdout = open('test_commacode_crc_with_errors.log', 'w')
    iterate_files("../../../../docs/CD_TestFiles", process_file)
    sys.stdout.flush()
    sys.exit(0)
