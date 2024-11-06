#/usr/bin/python3

def exponential(base: int | float, expo: int | float) -> int | float:
    """
    Calculates the exponential of a base raised to a given exponent.

    Parameters:
    base (int or float): The base number. If negative, it will be converted to its absolute value.
    expo (int or float): The exponent to which the base is raised.

    Returns:
    int or float: The result of the exponential operation. If the base is negative and the exponent is odd, 
                  the result will be negative. Otherwise, it will be positive.
    """
    
    # Handling when base value is 0
    if base == 0:
        return 0
    
    # Handling when exponential is 0
    if expo == 0:
        return 1
    
    # Handling negative base case
    if base < 0:
        base = abs(base)
        if expo % 2 != 0:
            return -exponential(base, expo)
        
    # Handling negative exponential
    if expo < 0:
        return 1 / exponential(base, -expo)
    
    ## Recursive case handling
    # Step 1: breaking the recursive problem into two parts, two halves of exponents.
    if expo % 2 == 0:
        half_power = exponential(base, expo // 2)
        return half_power * half_power
    
    # Step 2: for odd case exponentials, reducing their values on each iteration until the result is gotten.
    else:
        return base * exponential(base, expo - 1)


# Test cases
if __name__ == "__main__":
    print(exponential(-5, -3))
    print(exponential(5, 3))
    print(exponential(0, 3))
