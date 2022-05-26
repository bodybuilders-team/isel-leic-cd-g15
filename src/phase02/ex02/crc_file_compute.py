from crc import CrcCalculator, Crc8


def crc_file_compute(input_file, output_file):
    """
    Computes the CRC of a file.

    :param input_file: the input file to compute the CRC of
    :param output_file: the output file to write the CRC to
    """

    with open(input_file, "rb") as f:
        crc_calculator = CrcCalculator(Crc8.CCITT)
        data = f.read()
        checksum = crc_calculator.calculate_checksum(data)

    with open(output_file, "w") as f:
        f.write(hex(checksum))


# Compute the CRC of test files
if __name__ == "__main__":
    crc_file_compute("../../../docs/CD_TestFiles/alphabet.txt", "crc_files/alphabet_crc.txt")
