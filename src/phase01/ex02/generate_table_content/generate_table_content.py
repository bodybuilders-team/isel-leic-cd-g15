from src.phase01.ex02.strings_source.strings_source import strings_source
import random


def generate_table_content(number_of_citizens, number_of_bets):
    """
    Generates two tables: one with citizens and other with bets.

    :param number_of_citizens: number of elements in the citizens table
    :param number_of_bets: number of elements in the bets table
    """

    # Get citizens information
    with open("../../../../docs/AuxFiles/Nomes.txt", "r") as namesF:
        names = namesF.read().splitlines()

    with open("../../../../docs/AuxFiles/Apelidos.txt", "r") as surnamesF:
        surnames = surnamesF.read().splitlines()

    with open("../../../../docs/AuxFiles/Concelhos.txt", "r") as residencesF:
        residences = residencesF.read().splitlines()

    with open("../../../../docs/AuxFiles/Profissões.txt", "r") as professionsF:
        professions = professionsF.read().splitlines()

    names = generate_names(names, surnames, number_of_citizens)
    residences = strings_source(residences, uniform_fmp(len(residences)), number_of_citizens).split(";")
    professions = strings_source(professions, uniform_fmp(len(professions)), number_of_citizens).split(";")

    # Generate citizens
    citizens = []
    for i in range(number_of_citizens):
        citizens.append((i, names[i], residences[i], professions[i]))

    # Write citizens table
    with open("citizens.txt", "w") as citizensF:
        for citizen in citizens:
            citizensF.write(f"{citizen[0]:08d} | {citizen[1]} | {citizen[2]} | {citizen[3]}\n")

    # Generate bets
    citizen_ids = strings_source(
        alphabet=[f"{i:08d}" for i in range(number_of_citizens)],
        fmp=uniform_fmp(number_of_citizens),
        L=number_of_bets
    ).split(";")

    bets = []
    for i in range(number_of_bets):
        random_5_nums = " ".join(sorted(random.sample([str(i) for i in range(1, 51)], 5), key=int))
        random_2_nums = " ".join(sorted(random.sample([str(i) for i in range(1, 12)], 2), key=int))
        bets.append(random_5_nums + " " + random_2_nums)

    date_days = strings_source([str(i) for i in range(28)], uniform_fmp(28), number_of_bets).split(";")
    date_months = strings_source([str(i) for i in range(1, 13)], uniform_fmp(12), number_of_bets).split(";")
    date_years = strings_source([str(i) for i in range(1950, 2022)], uniform_fmp(72), number_of_bets).split(";")

    dates = [f"{date_days[i]}-{date_months[i]}-{date_years[i]}" for i in range(number_of_bets)]

    # Write bets table
    with open("bets.txt", "w") as betsF:
        for i in range(number_of_bets):
            betsF.write(f"{citizen_ids[i]} | {bets[i]} | {dates[i]}\n")


def uniform_fmp(length):
    """
    Returns a uniform fmp (function of mass probability).
    :param length: length of the fmp
    :return: fmp
    """
    return [1 / length] * length


def generate_names(names, surnames, number_of_citizens):
    """
    Generates an array of names.

    :param names: list of first names
    :param surnames: list of last names
    :param number_of_citizens: number of names to generate

    :return: list of generated names
    """
    names = strings_source(names, uniform_fmp(len(names)), number_of_citizens * 2).split(";")
    surnames = strings_source(surnames, uniform_fmp(len(surnames)), number_of_citizens * 2).split(";")

    full_names = []

    ni = -1
    si = -1

    for i in range(number_of_citizens):
        num = random.randint(0, 2)

        if num == 0:
            full_names.append(f"{names[ni := ni + 1]} {surnames[si := si + 1]}")
        elif num == 1:
            full_names.append(f"{names[ni := ni + 1]} {names[ni := ni + 1]} {surnames[si := si + 1]}")
        elif num == 2:
            full_names.append(f"{names[ni := ni + 1]} {names[ni := ni + 1]} "
                              f"{surnames[si := si + 1]} {surnames[si := si + 1]}")

    return full_names


NUMBER_OF_CITIZENS = 2000
NUMBER_OF_BETS = 2000

# Test of generate_table_content
if __name__ == '__main__':
    generate_table_content(NUMBER_OF_CITIZENS, NUMBER_OF_BETS)
