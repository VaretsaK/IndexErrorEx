import sequence


def return_index_value(given_seq: sequence):
    try:
        input_index = int(input("Enter an index to return: "))
    except ValueError:
        return "Enter only digits."

    try:
        value_by_index = given_seq[input_index]
    except IndexError:
        return "There is no such index in a given array."
    else:
        return value_by_index
