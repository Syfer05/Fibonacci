# Python program 
# Fibonacci Sequence
  
val = int(input("Enter the number of items you want: "))
alpha = [0,1]
for i in range (1, val):
    alpha.append(alpha[-2] + alpha[-1])
print(alpha)