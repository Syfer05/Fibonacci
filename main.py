# Python program 
# Fibonacci Sequence

val1 = ''
def item():
    try:
        val1 = int(input("Enter the number of items you want between [2:20]: "))
    except ValueError:
        print("That's not an int!")   
        item()
        
    if val1 not in range(2, 21):
        item()
    else:
        sequence(val1)

    

def sequence(val2):
    alpha = [0,1]
    for i in range (1, val2):
        alpha.append(alpha[-2] + alpha[-1])
    print(alpha)


item()
