x = int(input("Number: "))
if x < 0:
    x = 0
    print("Negative, set it to "+ str(x))
elif x < 5:
    print('Less than 5')
elif x == 5:
    x = 20
    print('Equals 5 and set to ' + str(x))
else:
    print("Greater than 5")