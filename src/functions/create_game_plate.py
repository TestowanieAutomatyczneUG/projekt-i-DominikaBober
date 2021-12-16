import sys
sys.path.append('./')
from packages import *

def create_game_plate(table):

    size = len(table)
    row = table[0]

    left_text = row.copy()
    right_text = row.copy()
    top_text = row.copy()
    bottom_text = row.copy()

    for i in range(size):

        # left_text
        temp = list(table[i])
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        left_text[i] = sum(n)

        # right_text
        temp = list(table[i])
        temp.reverse()
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        right_text[i] = sum(n)

        # top_text
        temp = [table[j][i] for j in range(size)]
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        top_text[i] = sum(n)

        # bottom_text
        temp = [table[j][i] for j in range(size)]
        temp.reverse()
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        bottom_text[i] = sum(n)

    return top_text, left_text, bottom_text, right_text
