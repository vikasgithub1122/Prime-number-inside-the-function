def Prime(max_num):
    """
    Check whether the given number is prime or not
    """
    for num in range (2, max_num):
        if max_num % num == 0:
            return False
    return True

def twin_Prime(max_num):
    """
    Generates the list of twin primes
    """
    for first_num in range(2, max_num):
        second_num = first_num + 2
        if (Prime(first_num) and Prime(second_num)):
            print(" {0} and {1}".format(first_num, second_num))

print("Twin Prime: ")
twin_Prime(20)

