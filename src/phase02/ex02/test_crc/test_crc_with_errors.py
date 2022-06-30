from src.phase02.ex02.crc.crc_file_check import crc_file_check
from src.phase02.ex02.crc.crc_file_compute import crc_file_compute
from src.phase02.utils import *
import sys


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
    iterate_files("../../../../docs/CD_TestFiles", process_file)
    sys.stdout.flush()

    sys.exit(0)
