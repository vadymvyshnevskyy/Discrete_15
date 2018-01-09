'''
Discrete math and programming project
№15 "Create a transitive closure of a matrix using Warshall's algorithm"

Created by: Lebyak Markiyan, Vyshnevskiy Vadym, Shtokhman Yuriy
08/01/2018
'''
import random

def generate_matrix():
    '''
    (None) -> (list)
    This function generates matrix (2-4)x(2-4) and returns a list of integers.
    '''
    l = random.randint(2, 4)
    arr = [[random.randint(0, 1) for j in range(l)] for i in range(l)]
    print("Random Matrix:")
    print_matrix(arr)
    print("\n")
    return arr

def print_matrix(lst):
    '''
    (list) -> (string)
    This function prints out a matrix.
    '''
    for i in lst:
        for j in i:
            print(j, end = " ")
        print("")

def find_trans(lst):
    '''
    (list) ->
    This function finds transitive closure of a matrix and prints it out.
    '''
    length = len(lst)
    for i in range(length):
        for j in lst:
            if j[i] == 1:
                for z in range(length):
                    j[z] = j[z] or lst[i][z]
            else:
                continue
        print("Transitive matrix. Step %d :" % (i+1))
        print_matrix(lst)
        print("\n")
find_trans(generate_matrix())
