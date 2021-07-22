def nearest_square(n):
    """Returns the nearest perfect-square that is less than or equal to 
    a number 'n' given."""
    if n < 1:
        return 0
    square_root = n**.5
    return int((square_root//1)**2)

    