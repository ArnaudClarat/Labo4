# coding=utf-8
def triBulle(tab):
    t = tab.copy()
    test = True
    while test:
        test = False
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = temp
                test = True
    return t


def triBulle2(tab):
    t = tab.copy()
    test = True
    while test:
        test = False
        for i in range(len(t) - 1):
            if t[i][1] < t[i + 1][1]:
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = temp
                test = True
    return t


def triBulle3(tab):
    j = 0
    t = tab.copy()
    test = True
    while test:
        test = False
        j += 1
        for i in range(len(t) - 1):
            if t[i][1][3] > t[i + 1][1][3]:
                temp = t[i]
                t[i] = t[i + 1]
                t[i + 1] = temp
                test = True
    return t


def newPlongeurs():
    global plongeurs
    for i in range(3):
        nPlongeur = input("Nom sauteur " + str(i + 1) + " : ")
        plongeurs.append(nPlongeur)


def nameSauts():
    global datas
    print("")
    for plongeur in plongeurs:
        data = [plongeur]
        print("\nSauteur : " + plongeur)
        for i in range(2):
            dataSaut = []
            saut = input("\tNom saut " + str(i + 1) + " : ")
            coef = float(input("\tCoefficient : "))
            dataSaut.append(saut)
            dataSaut.append(coef)
            data.append(dataSaut)
        datas.append(data)


def listeSauts(nbrSaut):
    print("\nListe passage saut " + str(nbrSaut))
    for plongeur in datas:
        print("\t" + plongeur[0] + " : " + str(plongeur[nbrSaut][0]) + "; " + str(plongeur[nbrSaut][1]))


def noteSaut(nbrSaut):
    global datas
    print("\nSaut " + str(nbrSaut))
    for plongeur in datas:
        notesSaut = []
        print("\nSauteur : " + plongeur[0] + " : " + str(plongeur[nbrSaut][0]) + "; " + str(plongeur[nbrSaut][1]))
        for i in range(5):
            note = float(input("Points jury " + str(i + 1) + " : "))
            notesSaut.append(note)
        plongeur[nbrSaut].append(notesSaut)


def calculPoints(nbrSaut):
    global datas
    for plongeur in datas:
        subTot = 0
        points = triBulle(plongeur[nbrSaut][2])[1:-1]
        for point in points:
            subTot += point
        total = subTot * plongeur[nbrSaut][1]
        plongeur[nbrSaut].append(total)


def cumul():
    global datas
    calculPoints(2)
    for plongeur in datas:
        point1 = plongeur[1][3]
        point2 = plongeur[2][3]
        plongeur.append(point1 + point2)


def affichage():
    data = []
    for plongeur in datas:
        temp = [plongeur[0], plongeur[3]]
        data.append(temp)
    data = triBulle2(data)
    print("\nClassement final")
    for plongeur in data:
        print("\t" + plongeur[0] + " : " + str(round(plongeur[1])))


def main():
    global datas
    newPlongeurs()
    nameSauts()
    listeSauts(1)
    noteSaut(1)
    calculPoints(1)
    datas = triBulle3(datas)
    listeSauts(2)
    noteSaut(2)
    cumul()
    affichage()


# --Variables--
plongeurs = []
datas = []

if __name__ == "__main__":
    main()
