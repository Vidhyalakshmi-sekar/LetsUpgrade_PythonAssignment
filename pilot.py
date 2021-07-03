# getting altitude as input
while True:
    altitude = int(input("Please enter the altitude: "))

    if altitude <= 1000:
        print('Safe to land')
        break
    elif 1000 < altitude <= 5000:
        print('Bring down to 1000')
    else:
        print('Go around and try later')
