from crc import CrcCalculator, Configuration


def crc_file_compute(input_file, output_file, poly=0x04C11DB7):
    """
    Computes the CRC of a file.

    :param poly: polynomial for 32-bit crc
    :param input_file: the input file to compute the CRC of
    :param output_file: the output file to write the CRC to
    """

    config = Configuration(
        width=32,
        polynomial=poly,
        init_value=0xFFFFFFFF,
        final_xor_value=0xFFFFFFFF,
        reverse_input=True,
        reverse_output=True,
    )

    with open(input_file, "rb") as f:
        crc_calculator = CrcCalculator(config)
        data = f.read()
        checksum = crc_calculator.calculate_checksum(data)

    with open(output_file, "wb") as f:
        f.write(checksum.to_bytes(length=4, byteorder="little"))
        f.write(data)


# Compute the CRC of test files
if __name__ == "__main__":
    crc_file_compute("../../../docs/CD_TestFiles/alphabet.txt", "crc_files/alphabet_crc.txt")

    import sys

    sys.exit(0)
