x = int (input('Enter your number \n'))
epsilon = 0.001
g = 0
low = 1.0
high = x
root = (high + low)/2.0
while abs (root ** 2 - x )>= epsilon:
    print ('low = '+str(low)+' high = '+str(high)+' root = '+str(root))
    g += 1
    if root **2 < x :
        low = root
    else :
        high = root
    root = (high + low)/2.0
print('Number of Guesses = '+str(g))
print(str(root)+" is close to the square root of "+str(x))