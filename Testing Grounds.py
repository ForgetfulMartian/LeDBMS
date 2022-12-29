"""import os
Databases = {'bababoi': [['Name', 'A', 'B', 'C', 'D', 'E', 'F'], ['Roll No.', 1, 2, 3, 4, 5, 6], ['Bus No.', 1, 2, 3, 4, 5, 6]], 'Hehe': [['Name', 'G', 'H', 'I', 'J', 'K', 'F'], ['Roll No.', 7, 8, 9, 10, 11, 12], ['Marks', 12, 34, 56, 78, 90, 10]], 'gg': [['Name', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'F'], ['Roll No.', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], ['Bus No.', 1, 2, 3, 4, 5, 6, '', '', '', '', '', ''], ['Marks', '', '', '', '', '', '', 12, 34, 56, 78, 90, 10]]}
os.chdir("Databases")
for i in Databases:
    f = open(i+'.csv', 'w')

    for j in Databases[i]:

        a = ''
        b = 0
        for k in j:

            if b == 0:

                a = a + str(k)

            else:

                a = a+','+str(k)
            b += 1
        f.write(a+"\n")



        else:

            if len(eval(User_Input)) > len(list(Databases.keys())[0]):
                a = input("Length of Column is bigger than Key Column, To trim enter T or anything else to continue "
                          "without adding column")

                if a.lower() == 't':
                    Databases[cd].append(eval(User_Input)[:len(list(Databases.keys())[0])])
                else:
                    continue
            elif len(eval(User_Input)) < len(list(Databases.keys())[0]):
                b = eval(User_Input)
                for i in range(len(list(Databases.keys())[0])-len(eval(User_Input))):
                    b.append('')
                Databases[cd].append(b)
"""

elif User_Input.lower().startswith("row add"):

    User_Input = User_Input[8:]

    if len(list(Databases[cd])) == 0:
        for i in User_Input:
            a = [i]
            Databases[cd].append(a)


else:

    if len(eval(User_Input)) > len(Databases[cd][0]):
        a = input("Length of Column is bigger than Key Column, To trim enter T or anything else to continue "
                  "without adding column:")

        if a.lower() == 't':
            Databases[cd].append(eval(User_Input)[:len(list(Databases[cd][0]))])

        else:
            continue

    elif len(eval(User_Input)) < len(list(Databases[cd][0])):
        b = eval(User_Input)
        for i in range(len(list(Databases[cd][0])) - len(eval(User_Input))):
            b.append('')
        Databases[cd].append(b)

    else:
        Databases[cd].append(eval(User_Input))