from nearest import nearest_square


def nearest_square_0():
	assert(nearest_square(0) == 0)

def nearest_square_1():
	assert(nearest_square(1) == 1)

def nearest_square_n10():
	assert(nearest_square(-10) == 0)

def nearest_square_16():
	assert(nearest_square(16) == 16)

def nearest_square_17():
	assert(nearest_square(17) == 16)