from NULL_not_found import NULL_not_found

# initialize different types of NULL
Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False

# should print:
# Nothing, Cheese, Zero, Empty or Fake
# the value
# the type
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)

# should return 0
print(NULL_not_found(Fake))

# should print "Type not found"
# should return 1
print(NULL_not_found("Brian"))
