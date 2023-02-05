n = (int)(input('Please think of a number between 0 and 100!\n'))
e = 1
g = 0
low = 0
high = 100
ans = (high + low )//2.0
while True:
    print ('Is your secret number '+str(int(ans))+'?')
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if response == 'h':
        high = ans
    elif response == 'l':
        low = ans
    elif response == 'c':
        print ('Game over. Your secret number was '+str(int(ans)))
        break
    ans = (high + low)//2.0

