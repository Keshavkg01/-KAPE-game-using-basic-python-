def zfig(z):
    print(".     " + str(z[0]) + "---------" + str(z[1]) + "---------" + str(z[2]))
    print(".     |         |         |")
    print(".     .  " + str(z[3]) + "------" + str(z[4]) + "------" + str(z[5]) + "  .")
    print(".     |  |      |      |  |")
    print(".     .  .  " + str(z[6]) + "---" + str(z[7]) + "---" + str(z[8]) + "  .  .")
    print(".     |  |  |       |  |  |")
    print(".     " + str(z[9]) + "-" + str(z[10]) + "-" + str(z[11]) + "     " + str(z[12]) + "-" + str(
        z[13]) + "-" + str(
        z[14]) + "")
    print(".     |  |  |       |  |  |")
    print(".     .  . " + str(z[15]) + "--" + str(z[16]) + "--" + str(z[17]) + "  .  .")
    print(".     |  |      |      |  |")
    print(".     . " + str(z[18]) + "-----" + str(z[19]) + "------" + str(z[20]) + " .")
    print(".     |         |         |")
    print(".     " + str(z[21]) + "-------" + str(z[22]) + "--------" + str(z[23]) + "")


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
z = n

print()
print("welcome to the game of kape")
print()
a = []
b = []
moves = [[10, 2], [1, 5, 3], [2, 15], [11, 5], [2, 4, 8, 6], [5, 14], [12, 8], [8, 13], [1, 22], [4, 10, 19, 12],
         [7, 11, 16],
         [9, 14, 18], [6, 13, 15, 21], [3, 14, 24], [12, 17], [16, 18, 20], [13, 17], [11, 20], [17, 19, 21, 23],
         [14, 20],
         [10, 23], [20, 22, 24], [15, 23]
         ]

stda = [[1, 2, 3], [4, 5, 6], [7, 8, 9]
    , [16, 17, 18], [19, 20, 21], [22, 23, 24]
    , [1, 10, 22], [4, 11, 19], [7, 12, 16],
        [9, 13, 18], [6, 14, 21], [3, 15, 24],
        [2, 5, 8], [10, 11, 12], [17, 20, 23], [13, 14, 15]
        ]
print("---INSTRUCTIONS---")
print("1...user1 has to first place the pawn on any corners as mentioned as numbers in above fig")
print("2...then user2 will also do the same")
print("3...each user will have 9 pawns initially")
print(stda)
print(
    "4...the user who places the pawns in any of the above small list can remove any one opponent pawn which you like")
print(
    "5...then after inserting all the pawns you have to move your  one pawn at a time from one point to neighbour point  with along the path in any directions but cant jump ")
print("6...the user can try to avoid opponent from making kape or block him with no place to move ")
print("7...if any user blocks the opponent with no other moves possible the user wins the game")
print(
    "8... the other probability of  winning is that if  number of opponents pawn drops down less than 3,then that user will lose the game  ")

print(".     " + str(n[0]) + "---------" + str(n[1]) + "---------" + str(n[2]))
print(".     |         |         |")
print(".     .  " + str(n[3]) + "------" + str(n[4]) + "------" + str(n[5]) + "  .")
print(".     |  |      |      |  |")
print(".     .  .  " + str(n[6]) + "---" + str(n[7]) + "---" + str(n[8]) + "  .  .")
print(".     |  |  |       |  |  |")
print(".     " + str(n[9]) + "-" + str(n[10]) + "-" + str(n[11]) + "     " + str(n[12]) + "-" + str(n[13]) + "-" + str(
    n[14]) + "")
print(".     |  |  |       |  |  |")
print(".     .  . " + str(n[15]) + "--" + str(n[16]) + "--" + str(n[17]) + "  .  .")
print(".     |  |      |      |  |")
print(".     . " + str(n[18]) + "-----" + str(n[19]) + "------" + str(n[20]) + " .")
print(".     |         |         |")
print(".     " + str(n[21]) + "-------" + str(n[22]) + "--------" + str(n[23]) + "")

stdb = [[1, 2, 3], [4, 5, 6], [7, 8, 9]
    , [16, 17, 18], [19, 20, 21], [22, 23, 24]
    , [1, 10, 22], [4, 11, 19], [7, 12, 16],
        [9, 13, 18], [6, 14, 21], [3, 15, 24],
        [2, 5, 8], [10, 11, 12], [17, 20, 23], [13, 14, 15]
        ]

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
for i in range(3):
    print("*pawn" + str(i + 1) + "*")
    x = int(input("user1 :  "))
    while x not in n or x in a or x in b:
        print("enter correct input")
        x = int(input("user1 :  "))
    if x in n:
        a.append(x)
    z[x - 1] = str(n[x - 1]) + "a"
    zfig(z)

    for i in stda:
        t, u, v = i
        if t in a and u in a and v in a:
            stda.remove(i)
            print("---woow its a kape for user1-" + str(i) + "--")
            p = int(input("enter the opponent pawn to remove" + str(b) + ": "))
            while p not in b:
                p = int(input("enter the opponent pawn to remove" + str(b) + ": "))
            b.remove(p)
            index = n.index(p)
            temp = z[index]
            temp = temp[:-1]
            z[index] = temp
            zfig(z)
    y = int(input("user2 :  "))
    while y not in n or y in a or y in b:
        print("enter correct input")
        y = int(input("user2 :  "))
    if y in n:
        b.append(y)
    z[y - 1] = str(n[y - 1]) + "b"
    zfig(z)

    for i in stdb:
        t, u, v = i
        if t in b and u in b and v in b:
            stdb.remove(i)
            print("---woow its a kape for user2---")
            p = int(input("enter the opponent pawn to remove" + str(a) + ": "))
            while p not in a:
                p = int(input("enter the opponent pawn to remove" + str(a) + ": "))
            index = n.index(p)
            a.remove(p)

            temp = z[index]
            temp = temp[:-1]
            z[index] = temp
            zfig(z)

    print("user1:" + str(a) + "   user2 :" + str(b))

for i in range(3, 9):
    print("*pawn" + str(i + 1) + "*")
    x = int(input("user1 :  "))
    while x not in n or x in a or x in b:
        print("enter correct input")
        x = int(input("user1 :  "))
    if x in n:
        a.append(x)
    z[x - 1] = str(n[x - 1]) + "a"
    zfig(z)
    for i in stda:
        t, u, v = i
        if t in a and u in a and v in a:
            stda.remove(i)
            print("---woow its a kape for user1-" + str(i) + "--")
            print("select from this" + str(b))
            p = int(input("enter the opponent pawn to remove: "))
            while p not in b:
                print("select from this" + str(b))
                p = int(input("enter the opponent pawn to remove: "))
            b.remove(p)
            index = n.index(p)
            temp = z[index]
            temp = temp[:-1]
            z[index] = temp
            zfig(z)

    y = int(input("user2 :  "))
    while y not in n or y in a or y in b:
        print("enter correct input")
        y = int(input("user2 :  "))
    if y in n:
        b.append(y)
    z[y - 1] = str(n[y - 1]) + "b"
    zfig(z)

    for i in stdb:
        t, u, v = i
        if t in b and u in b and v in b:
            stdb.remove(i)
            print("---woow its a kape for user2---")
            p = int(input("enter the opponent pawn to remove" + str(a) + ": "))
            while p not in a:
                p = int(input("enter the opponent pawn to remove" + str(a) + ": "))
            index = n.index(p)
            a.remove(p)

            temp = z[index]
            temp = temp[:-1]
            z[index] = temp
            zfig(z)

    print("user1:" + str(a) + "   user2 :" + str(b))


def finish(stda, stdb):
    if (len(stda) > len(stdb)):
        print("user 2 won the game")
    elif len(stda) == len(stdb):
        print("game ended in draw")
    else:
        print("user1 won the game")
    exit(0)

print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------")
while (True):
    if len(a) > 2 and len(b) > 2:
        print("Enter two values(present position and next position where pawn should be moved)")
        p, q = input("user1: ").split()
        p = int(p)
        q = int(q)
        if p in a:
            temp = moves[p-1]
            flag = str(z[q - 1])
            if q in temp or flag[-1].isdigit():
                samp = z[p - 1]
                z[p - 1] = samp[:-1]
                z[q - 1] = str(z[q - 1]) + "a"
                a.remove(p)
                a.append(q)
                for i in stda:
                    t, u, v = i
                    if t in a and u in a and v in a:
                        stda.remove(i)
                        print("---woow its a kape for user1-" + str(i) + "--")
                        print("select from this" + str(b))
                        p = int(input("enter the opponent pawn to remove: "))
                        while p not in b:
                            print("select from this" + str(b))
                            p = int(input("enter the opponent pawn to remove: "))
                        b.remove(p)
                        index = n.index(p)
                        temp = z[index]
                        temp = temp[:-1]
                        z[index] = temp

        zfig(z)
        p, q = input("user2: ").split()
        p = int(p)
        q = int(q)
        if p in b:
            temp = moves[p - 1]
            flag = str(z[q - 1])
            if q in temp or flag[-1].isdigit():
                samp = z[p-1]
                z[p - 1] = samp[:-1]
                z[q - 1] = str(z[q - 1]) + "b"
                b.remove(p)
                b.append(q)
                for i in stdb:
                    t, u, v = i
                    if t in b and u in b and v in b:
                        stdb.remove(i)
                        print("---woow its a kape for user2-" + str(i) + "--")
                        print("select from this" + str(a))
                        p = int(input("enter the opponent pawn to remove: "))
                        while p not in a:
                            print("select from this" + str(a))
                            p = int(input("enter the opponent pawn to remove: "))
                        a.remove(p)
                        index = n.index(p)
                        temp = z[index]
                        temp = temp[:-1]
                        z[index] = temp
                zfig(z)
    else:
        finish(stda, stdb);
