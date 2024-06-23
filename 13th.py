n_terms = int(input("How many terms? "))

# first two terms
n_1, n_2 = 0, 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
   print("Please enter a positive integer")
elif n_terms == 1:
   print("Fibonacci sequence up to",n_terms,":")
   print(n_1)
else:
   print("Fibonacci sequence:")
   while count < n_terms:
       print(n_1)
       n_th = n_1 + n_2
       # update values
       n_1 = n_2
       n_2 = n_th
       count += 1
