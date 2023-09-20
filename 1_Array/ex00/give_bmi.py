import sys as Sys


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""
	A function that calculates BMIs from given heights and weights

	Arguments:
		height (list[int | float]): List of heights in meters
		weight (list[int | float]): List of weights in kilograms

	Returns:
		a list of BMIs calculated from the input
	"""

	# hide traceback message for assertion errors
	Sys.tracebacklimit = 0

	# make sure the arguments are lists
	assert type(height) is list, "height must be a list"
	assert type(weight) is list, "weight must be a list"

	# make sure the two lists are the same size
	assert len(height) == len(weight), "height and weight must have the same size"

	# make sure the lists only contain ints or floats
	assert all(type(n) is int or type(n) is float for n in height), "height must only contain ints or floats"
	assert all(type(n) is int or type(n) is float for n in weight), "weight must only contain ints or floats"

	# make sure the values are within the expected range
	assert all(n > 0 and n <= 3 for n in height), "heights must be in meters and not zero"
	assert all(n > 0 and n <= 1000 for n in weight), "weights must be in kilograms and not zero"

	# the calculated BMIs
	return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""
	A function that transforms given list of BMIs to
	booleans indicating whether each is above the limit

	Arguments:
		bmi (list[int | float]): list of BMIs to transform
		limit (int): BMIs have to be above this limit

	Returns:
		a list of booleans where True means above the limit
	"""

	# hide traceback message for assertion errors
	Sys.tracebacklimit = 0

	# make sure the arguments are a list and an int
	assert type(bmi) is list, "bmi must be a list"
	assert type(limit) is int, "limit must be an int"

	# make sure the list only contains ints or floats
	assert all(type(n) is int or type(n) is float for n in bmi), "bmi must only contain ints or floats"

	# transform the list
	return [n > limit for n in bmi]
