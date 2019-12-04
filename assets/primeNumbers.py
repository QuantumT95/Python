def isPrime(num):
  # prime numbers are greater than 1
  if num >= 1:
    # check for factors
    for i in range(2,num):
        if (num % i) == 0:
            return False
            break
    else:
        return True

def FindPrimes(P):
  counter = 0
  i = 1
  for i in range(i, P):
    if isPrime(i) == True:
      print(i, "is a prime number")
      counter += 1
    i += 1
  print("Number of prime numbers between 1 and", P, "is:", counter)

def FindPrimes2(Q):
  counter = 0
  i = 1
  while counter < Q + 1:
    if isPrime(i) == True:
      counter += 1
    i += 1
  print(Q, "th prime number is ", i)


# take input from the user
num = int(input("Enter a number: "))

FindPrimes2(num)

def isPrimeShort(number):
  if number == 2:
    return 1
  if number % 2 == 0:
    return 0