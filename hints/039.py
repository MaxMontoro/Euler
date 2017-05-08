"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""    

import cProfile
    
def is_right_triangle(a, b, c):
    return a**2 + b**2 == c**2


def get_right_triangles_with_perimeter(p):
    for a in range(1, p//3):
        for b in range(1, p-a+1):
            c = p - b - a
            if is_right_triangle(a, b, c):
                yield
                    
                    
def get_number_of_solutions(perimeter):
    sols = 0
    for x in get_right_triangles_with_perimeter(perimeter):
        sols += 1
    return sols


def max_number_of_solutions_below(n):
    solutions = {}
    for perimeter in range(n):
        solutions[perimeter] = get_number_of_solutions(perimeter)
    return max(solutions.keys(), key = lambda x: solutions[x])
    

cProfile.run('max_number_of_solutions_below(300)') 