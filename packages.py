import os
import numpy
import random
import uuid
import pickle
import math
import warnings
import itertools
from beautifultable import BeautifulTable
from itertools import permutations
from collections import ChainMap
from string import ascii_letters, digits
from colorama import Fore, Style


def unique(list):
    unique_list = []
    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
