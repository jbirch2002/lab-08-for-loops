print("Let’s party...")

countdown_start = int(input("How long 'til the party? "))

if countdown_start <= 0 or countdown_start > 100:
    print("PARTY NOW!!!")

else:
    for i in range(countdown_start, 0, -1):
        print(i)
    print("PARTY TIME!!!")
