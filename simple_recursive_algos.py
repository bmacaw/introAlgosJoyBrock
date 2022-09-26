from math import factorial


def iterate_factorial(n):  # This is twice as fast as recur_factorial
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact


print(iterate_factorial(5))


def recur_factorial(n):  # This is slower than iterate_factorial
    # and not best use for what we are trying to accomplish
    # because this function takes up more time and space by running back
    # to the function call to create those pockets for our numbers. Iteration
    # is simply multiplying each number in place and not creating anything new.
    if n == 1:  # Last in First out
        return n
    else:
        temp = recur_factorial(n - 1)
        temp = temp * n
    return temp


print(recur_factorial(5))


def recur_factorial_two(n):
    # Takes up less space, but decreases efficiency
    if n == 1: return n
    else: return n * recur_factorial_two(n-1)


print(recur_factorial_two(5))


def permute(string, pocket=""):
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i]
            back = string[i+1:]
            together = front + back
            permute(together, letter + pocket)


print(permute("ABCD", ""))

# For the above use, iteration is still a better pick, even though code is longer


def permutations(str):

    for p in range(factorial(len(str))):

        print(''.join(str))
        i = len(str) - 1
        while i > 0 and str[i - 1] > str[i]:
            i -= 1
        str[i:] = reversed(str[i:])
        if i > 0:
            q = i
            while str[i - 1] > str[q]:
                q += 1
            temp = str[i - 1]
            str[i - 1] = str[q]
            str[q] = temp


s = 'abc'
s = list(s)
permutations(s)


# Challenge 8/n or 8 Queens Problem: place 8 chess queens on an 8x8 board s
# that no two queens are able to attack each other.





