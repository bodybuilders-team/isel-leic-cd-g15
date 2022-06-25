from crc import CrcCalculator, Configuration


def crc_file_check(input_file, poly=0x04C11DB7):
    """
    Checks the CRC of the input file against the CRC in the crc file.

    :param poly: polynomial for 32-bit crc
    :param input_file: the file to check
    :param crc_file: the file containing the CRC to check against

    :return: True if the CRC matches, False otherwise
    """

    config = Configuration(
        width=32,
        polynomial=poly,
        init_value=0xFFFFFFFF,
        final_xor_value=0xFFFFFFFF,
        reverse_input=True,
        reverse_output=True,
    )

    with open(input_file, 'rb') as f:
        checksum = int.from_bytes(f.read(4), byteorder="little")
        data = f.read()

    crc_calculator = CrcCalculator(config)

    return crc_calculator.verify_checksum(data, checksum)


# Verify the CRC of test files
if __name__ == '__main__':
    print(crc_file_check("crc_files/alphabet_crc.txt"))

    import sys

    sys.exit(0)
