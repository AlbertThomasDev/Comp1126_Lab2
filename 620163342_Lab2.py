def computedSquare(n):
  a = 1
  while a <= n-1:
    b = 1
    while b <= n-1:
      if a*a + b*b == n:
        return "True"
      b = b + 1
    a = a + 1
  return "False"



def isPrime(n):
  i = 2
  for i in range(i,n):
    if n%i == 0:
       return "False"
  return "True"




def trickWithPrime(a,b):
  while a <= 3:
    a = int(input("first parameter should not be less than or equal to 3: "))

  for a in range(a,b+1):
    c = 0
    for i in range(2,a):
      if a%i == 0:
        c = c + 1
    if c == 0:
      print(a)
      rem = ((a*a)+29)%8
      print("C^_^3"*rem)
    #print(c)



def prime_time(m,n):
  while m > n:
    print("First parameter should be less than ", n)
    m = int(input("Enter a new number: "))

  for i in range(1,n+1):
    prime = isPrime(i)
    if prime == "True":
      prime2 = isPrime(i-m)
      if prime2 == "True":
        print(i,end = ",")

  
