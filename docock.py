def tail_fac(n, acc=0):
    if n == 0:
        return acc
    return tail_fac(n-1, acc + n)

n = int(input("Enter a number: "))
guess = int(input(f"Enter the your guess at the tail factorial of {n}: "))
print(f"Tail factorial of {n} is {tail_fac(n)}, your guess: {guess}")

if guess == tail_fac(n):
    print("Your guess was correct")
else:
    print("Your guess was wrong")