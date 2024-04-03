from numba import njit


@njit(parallel=True)
def calculateDifference(askBinance, bidBinance, askBybit, bidBybit):
    """
    Calculates the difference between
    :param askBinance:
    :param bidBinance:
    :param askBybit:
    :param bidBybit:
    :return:
    """
    spreadBinance = askBinance - bidBinance
    spreadBybit = askBybit - bidBybit