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
		temp = []
		temp.append(plongeur[0])
		temp.append(plongeur[3])
		data.append(temp)
	print(triBulle(data))
	print("\nClassement final")
	#for plongeur in datas:

def main():
	#newPlongeurs()
	#nameSauts()
	#listeSauts(1)
	#noteSaut(1)
	#calculPoints(1)
	#listeSauts(2)
	#noteSaut(2)
	cumul()
	affichage()
	print(datas)


#--Variables--
plongeurs = []
datas = [['Durant Pol', ['Plongeon en avant tendu', 1.6, [8.0, 10.0, 3.0, 8.0, 8.0], 24.0], ['Plongeon retourné groupé', 2.0, [5.0, 6.0, 2.0, 10.0, 8.0]]], ['Lariviere Marcel', ['Salto et demi avant avec une vrille', 2.4, [9.0, 9.0, 8.9, 9.0, 9.0], 27.0], ['Salto et demi arrière groupé', 2.0, [9.0, 8.2, 8.2, 9.0, 10.0]]], ['Lebouteu Jules', ['Salto et demi arrière groupé', 2.0, [4.0, 3.0, 7.0, 5.0, 3.0], 12.0], ['Salto et demi arrière groupé', 2.0, [10.0, 9.8, 8.9, 9.0, 7.9]]]]

if __name__ == "__main__":
	main()