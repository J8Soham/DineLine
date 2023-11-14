#people = 0
#time = 0

dining_hall_not_close = True



while dining_hall_not_close == True:
    f = open("data.txt", "r")
    Reader = f.readlines()
    people_str = ''

    for i in Reader:
        for j in i:
            if i.index() == 30 or i.index() == 31:
                people_str += i

    people = int(people_str)

    if people <= 30:
        lines = 0
    elif 30 < people <= 100:
        lines = 2
    elif (people == -1):
        check = False
        break

    f.close()

    f = open("data.txt","w")
    user = input()
    Writer = f.write(user)

    f.close()

if check == False:
    print("Dining hall closed")
else:
    print(f"There are {lines} lines.")



