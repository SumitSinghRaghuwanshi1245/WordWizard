def sum_of_digits(n):
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n

num = int(input("Enter number: "))
print("Digital Root (single digit sum):", sum_of_digits(num))
