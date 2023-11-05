# Complete the 'counterGame' function below.

# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.


def counterGame(n):
    # Write your code here
    is_louise_turn = True

    while n > 1:
        if n & (n - 1) == 0:
            n //= 2  
        else:
            largest_power_of_two = 1
            while largest_power_of_two * 2 <= n:
                largest_power_of_two *= 2
            n -= largest_power_of_two  
        is_louise_turn = not is_louise_turn 
    return "Richard" if is_louise_turn else "Louise"
