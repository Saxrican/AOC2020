def lineParse(passwordStr):
    #15-16 p: ppppppppppplppppp
    splitStep1 = passwordStr.split("-")
    #"15","16 p: ppppppppppplppppp"
    splitStep2 = splitStep1[1].split(" ")
    #"15","16","p:","ppppppppppplppppp"
    lowerNo = int(splitStep1[0])
    upperNo = int(splitStep2[0])
    letter = splitStep2[1].strip(":")
    password = splitStep2[2]
    return [lowerNo,upperNo,letter,password]

def function1(var1):
    correctPasswords = []
    for i in var1:
        passwordCheck = lineParse(i)
        charCount = passwordCheck[3].count(passwordCheck[2])
        if charCount >= passwordCheck[0]:
            if charCount <= passwordCheck[1]:
                correctPasswords.append(passwordCheck[3])
    return correctPasswords

def function2(var2):
    correctPasswords2 = []
    for i in var2:
        passwordCheck = lineParse(i)
        char1 = passwordCheck[3][passwordCheck[0]-1]
        char2 = passwordCheck[3][passwordCheck[1]-1]
        if char1 == passwordCheck[2]:
            if char2 != passwordCheck[2]:
                correctPasswords2.append(passwordCheck[3])
        elif char2 == passwordCheck[2]:
                correctPasswords2.append(passwordCheck[3])
    return correctPasswords2

