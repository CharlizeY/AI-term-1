## Print pyramids made of *
int = int(input("Enter an integer: "))
n = 1
while n <= int:
    print("*"*n)
    n = n + 1


int = int(input("Enter an integer: "))
n = 1
while n <= int:
    print("*"*(2*n-1))
    n = n + 1



## Estimate the square root of a positive number
# Exhausive search algorithm
n = float(input(“Please enter a float number.”))
estimate = 0
criteria = 10**(-8)

While estimate < n:
    estimate_sqr = estimate**2
    if abs(estimate_sqr, n) < criteria
        print(f”The estimated square root of {n} is {estimate}.”)
        break
    
    estimate = estimate + 10**(-15)
           
gold_reference = math.sqrt(n)
if abs(estimate - gold_reference) < 0.00001:
    print("Correct answer.")
else:
    print(f"Incorrect. Program output is {estimate}, but I am expecting {gold_reference}.")

           
# Newton-Raphson (NR) algorithm - with 'break'
n = float(input(“Please enter a float number.”))
estimate = n # Could be any random positive number
estimate_new = 0
criteria = 10**(-8)

While estimate_new != estimate:
    estimate_new = 0.5 * (estimate + n/estimate)
           
    if abs(estimate_new, estimate) < criteria
            print(f”The estimated square root of {n} is {estimate_new}.”)
            break
                
    print(estimate_new)
    estimate = estimate_new
           

# NR algorithm - without 'break'
n = float(input(“Please enter a float number.”))
estimate = n # Could be any random positive number
criteria = 10**(-8)
found = FALSE

while not found:
    estimate_new = 0.5 * (estimate + n/estimate)
    print(estimate_new)
    if abs(estimate_new, estimate) < criteria
        found = TRUE
    estimate = estimate_new
    
print(f”The estimated square root of {n} is {estimate_new}.”)


# A more compact implementation of the NR algorithm
n = float(input("Please enter a positive number: "))
guess = n - 1
criteria = 10**(-8)

while abs(guess*guess - n) > criteria:
    guess = (guess + n/guess) * 0.5
    
print(f”The estimated square root of {n} is {guess}.”)



## Prime number exercise
# Test if a positive integer is a prime number
n = int(input("Please enter an integer: "))
if n == 0 or n == 1:
    print(f"{n} is not a prime number")
else:
    divisor = 2
    is_prime = True
    
    while divisor < n:
        if n % divisor == 0:
            is_prime = False
            break
        else:
        divisor = divisor + 1
        
if is_prime = False:
    print(f"{n} is not a prime number")
else:
    print(f"{n} is a prime number")
    

# List all the prime numbers smaller than N
N = int(input("Please enter an integer: "))
if N == 0 or N == 1:
    print(None)
else:
    number = 2
    
    while number <= N:
        divisor = 2
        is_prime = True
        
        while divisor < N:
            if N % divisor == 0:
                is_prime = False
                break
            else:
                divisor = divisor + 1
                
        if is_prime = True:
            print(number)
            
        number = number + 1



## Print the sum of all even/odd numbers from 1 to N, if N is even/odd
number = int(input("Enter an integer: "))
i = 1
total = number

while i < number:
    if number % 2 == 0:
        total = total + i + 1
    else:
        total = total + i
    i = i + 2

print(total)  
