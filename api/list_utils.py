"""
A few helpers for working with lists
"""

def find_by(l, key):
    """
    Find an element in a list by a specified condition
    """

    res = [item for item in l if key(item)]
    if res != []:
        return res[0]
    
    return None

def group_into_pairs(l):
    """
    Group neighbour elements into pairs

    Examples:

    group_into_pairs([1,2,3,4]) == [(1,2), (3,4)]
    group_into_pairs([1,2,3]) == [(1,2), (3)]
    """

    if l is None or l == []:
        return []

    res = []
    list_len = len(l)
    for i in range(0, list_len, 2):
        if i == list_len - 1:
            res.append((l[i],))
        else:
            res.append((l[i], l[i + 1]))
    
    return res

def diff(l1, l2):
    """
    Find the difference between two lists
    """
    return [x for x in l1 if x not in l2]