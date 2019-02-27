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
			print(datas[j])
			print(datas[j][i])
			datas[j][i].append(notesSaut)
		i += 1


def main():
	#newPlongeurs()
	#nameSauts()
	datas = [['P', ['p1', 1.0], ['p2', 2.0]], ['M', ['m1', 1.0], ['m2', 2.0]], ['J', ['j1', 1.0], ['j2', 2.0]]]
	listeSauts(1)
	noteSaut(1)
	print("En cours de construction...")


#--Variables--
plongeurs = []
datas = []

if __name__ == "__main__":
	main()