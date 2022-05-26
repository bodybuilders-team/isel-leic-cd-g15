from crc import CrcCalculator, Crc8


def crc_file_check(input_file, crc_file):
    """
    Checks the CRC of the input file against the CRC in the crc file.

    :param input_file: the file to check
    :param crc_file: the file containing the CRC to check against

    :return: True if the CRC matches, False otherwise
    """

    with open(input_file, 'rb') as f:
        data = f.read()

    with open(crc_file, 'r') as f:
        checksum = f.read()

    crc_calculator = CrcCalculator(Crc8.CCITT)
    return crc_calculator.verify_checksum(data, int(checksum, 16))


# Verify the CRC of test files
if __name__ == '__main__':
    print(crc_file_check("../../../docs/CD_TestFiles/alphabet.txt", "crc_files/alphabet_crc.txt"))
