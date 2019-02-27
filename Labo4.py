def triBulle (tab) :
	t = tab.copy()
	test=True
	while test :
		test = False
		for i in range(len(t)-1) :
			if t[i] > t[i+1] :
				temp = t[i]
				t[i] = t[i+1]
				t[i+1] = temp
				test = True
	return t


def newPlongeurs():
	global plongeurs
	for i in range(3):
		nPlongeur = input("Nom sauteur " + str(i+1) + " : ")
		plongeurs.append(nPlongeur)


def nameSauts():
	global datas
	print("")
	for plongeur in plongeurs:
		data = []
		data.append(plongeur)
		print("\nSauteur : " + plongeur)
		for i in range(2):
			dataSaut = []
			saut = input("\tNom saut " + str(i+1) + " : ")
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
	j = 0
	print("\nSaut " + str(nbrSaut))
	for plongeur in datas:
		notesSaut = []
		print("\nSauteur : " + plongeur[0] + " : " + str(plongeur[nbrSaut][0]) + "; " + str(plongeur[nbrSaut][1]))
		for i in range(5):
			note = float(input("Points jury " + str(i + 1) + " : "))
			notesSaut.append(note)
		datas[j][nbrSaut].append(notesSaut)
		j += 1


def calculPoints(nbrSaut):
	global datas
	j = 0
	for plongeur in datas:
		subTot = 0
		points = triBulle(plongeur[nbrSaut][2])[1:-1]
		for point in points:
			subTot += point
			total = subTot * plongeur[nbrSaut][1]
		datas[j][nbrSaut].append(total)
		j += 1
	print(datas)




def main():
	#newPlongeurs()
	#nameSauts()
	#listeSauts(1)
	#noteSaut(1)
	#calculPoints(1)


#--Variables--
plongeurs = []
datas = [['P', ['p1', 1.0, [8.0, 10.0, 3.0, 8.0, 8.0], 24.0], ['p2', 2.0]], ['M', ['m1', 1.0, [9.0, 9.0, 8.9, 9.0, 9.0], 27.0], ['m2', 2.0]], ['J', ['j1', 1.0, [4.0, 3.0, 7.0, 5.0, 3.0], 12.0], ['j2', 2.0]]]

if __name__ == "__main__":
	main()