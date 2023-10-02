from ft_calculator import calculator

# the @staticmethod decorator allows methods
# to be called without a class object

# initialize the arrays
a = [5, 10, 2]
b = [2, 4, 3]

# should print 56 (5*2 + 10*4 + 2*3)
calculator.dotproduct(a, b)

# should print [7, 14, 5]
calculator.add_vec(a, b)

# should print [3, 6, -1]
calculator.sous_vec(a, b)
