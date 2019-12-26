#birthday infos using dictionary
birthdays= {
    'zahera':'july 22 1998',
    'aamna':'june 17 1998',
    'tahira':'may 7 1998',
    'aisha':'december 10 1998'
    }
while True:
    name=input("enter a name \n")
    if name =='':
        break
    elif name in birthdays:
        print(birthdays[name], "is the birthday of" , name)
    else:
        print("sorry I donot have birthday info " , name)
        print("what is his/her birthday?")
        bday=input()
        birthdays[name]=bday
        print("birthday database updated")
