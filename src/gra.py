import pandas as pd
from tabulate import tabulate
import random
import numpy
from beautifultable import BeautifulTable


def print_table(table, top_text, left_text, bottom_text, right_text):

    color = '\u001b[35m'
    top_text = [f'{color}{item}\u001b[0m' for item in top_text]
    left_text = [f'{color}{item}\u001b[0m' for item in left_text]
    bottom_text = [f'{color}{item}\u001b[0m' for item in bottom_text]
    right_text = [f'{color}{item}\u001b[0m' for item in right_text]

    new_table = BeautifulTable()
    new_table.append_row(sum([[""], top_text, [""]],[]))
    for i in range(len(table)):
        new_table.append_row(sum([[left_text[i]], list(table[i]), [right_text[i]]],[]))
    new_table.append_row(sum([[""], bottom_text, [""]],[]))

    print(new_table)

def create_game_plate(size):

    row = [ i+1 for i in range(size)]
    table = numpy.zeros((size, size), dtype=int)
    temp = row.copy()
    random.shuffle(temp)
    table[0] = temp 

    def help(list, n):
        if n==0:
            return sum(a_ == b_ for a_, b_ in zip(list, table[n]))==0
        else:
            if sum(a_ == b_ for a_, b_ in zip(list, table[n]))==0:
                return help(list, n-1)
            else:
                return False

    for i in range(1, size):
        
        random.shuffle(temp)
        condition = True

        while condition:
            if help(temp, i):
                table[i] = temp
                condition = False
            else:
                random.shuffle(temp)


    left_text = row.copy()
    for i in range(size):
        temp = list(table[i])
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        left_text[i] = sum(n)

    right_text = row.copy()
    for i in range(size):
        temp = list(table[i])
        temp.reverse()
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        right_text[i] = sum(n)

    top_text = row.copy()
    for i in range(size):
        temp = [table[j][i] for j in range(size)]
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        top_text[i] = sum(n)

    bottom_text = row.copy()
    for i in range(size):
        temp = [table[j][i] for j in range(size)]
        temp.reverse()
        n = numpy.zeros(temp.index(size)+1, dtype=int)
        n[0] = 1
        for j in range(1,len(n)):
            if temp[j]==max(temp[:j+1]):
                n[j] = 1
        bottom_text[i] = sum(n)

    return table, top_text, left_text, bottom_text, right_text



def main():

    # rozmiar = int(input("Podaj wielkość planszy"))
    rozmiar = 4

    tablica, top_text, left_text, bottom_text, right_text = create_game_plate(rozmiar)
    print_table(tablica, top_text, left_text, bottom_text, right_text)



if __name__=="__main__":
    main()
