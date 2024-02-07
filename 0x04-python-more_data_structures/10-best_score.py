#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    biggest_k = list(a_dictionary)[0]
    biggest_v = a_dictionary[biggest_k]
    for k, v in a_dictionary.items():
        if v > biggest_v:
            biggest_v = v
            biggest_k = k
    return biggest_k
