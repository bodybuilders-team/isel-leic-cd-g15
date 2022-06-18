import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import entropy


def entropy_from_list(labels):
    """
    Calculates entropy from a list.
    :param labels: list
    :return: entropy
    """

    value, counts = np.unique(labels, return_counts=True)
    return round(entropy(counts, base=2), ndigits=4)


def show_histogram(labels, x_label, title, labels_entropy):
    """
    Shows a histogram of labels.
    :param labels: histogram labels
    :param x_label: histogram x label
    :param title: histogram title
    :param labels_entropy: labels entropy
    """

    plt.hist(labels, bins=len(labels))
    plt.xlabel(x_label)
    plt.ylabel("Occurrences")
    plt.suptitle(title, fontsize=18)
    plt.title("Entropy: " + str(labels_entropy))
    plt.gcf().subplots_adjust(bottom=0.15)
    plt.show()
