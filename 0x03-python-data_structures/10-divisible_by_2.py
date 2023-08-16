def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list and returns a list of True/False values."""
    results = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            results.append(True)
        else:
            results.append(False)

    return (results)
