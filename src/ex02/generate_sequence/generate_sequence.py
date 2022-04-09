from src.ex02.strings_source.strings_source import strings_source

sequence_alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
sequence_fmp = [1 / 36] * 36

SEQUENCE_LENGTH = 24
SEQUENCE_REPEAT_LENGTH = 4


def generate_sequence():
    """
    Generates an alphanumeric sequence similar to software activation/registration keys

    :return: generated sequence
    """

    sequence = strings_source(sequence_alphabet, sequence_fmp, SEQUENCE_LENGTH).replace(";", "")
    sequence = " ".join(sequence[i:i + SEQUENCE_REPEAT_LENGTH] for i in range(0, len(sequence), SEQUENCE_REPEAT_LENGTH))

    print("Sequence: ", sequence)
    return sequence


FILES = 5
SEQUENCES_PER_FILE = 1000

# Write sequences in files
if __name__ == '__main__':
    for i in range(FILES):
        with open(f"sequences{i}.txt", "w") as f:
            for j in range(SEQUENCES_PER_FILE):
                f.write(generate_sequence() + "\n")
