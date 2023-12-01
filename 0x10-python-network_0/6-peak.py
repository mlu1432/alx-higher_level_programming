def find_peak(list_of_integers):
    """
    Function to find a peak element in a list of integers.
    A peak is an element which is not smaller than its neighbors.
    For corner elements, we need to consider only one neighbor.
    """
    length = len(list_of_integers)
    if length == 0:
        return None
    if length == 1:
        return list_of_integers[0]
    if list_of_integers[0] >= list_of_integers[1]:
        return list_of_integers[0]
                                                                    
    for i in range(1, length - 1):
        if list_of_integers[i] >= list_of_integers[i - 1] and list_of_integers[i] >= list_of_integers[i + 1]:
            return list_of_integers[i]
                                                                                                
    if list_of_integers[length - 1] >= list_of_integers[length - 2]:
        return list_of_integers[length - 1]
