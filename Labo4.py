def newPlongeurs():
	global plongeurs
	for i in range(3):
		nPlongeur = input("Nom sauteur " + str(i+1) + " : ")
		plongeurs.append(nPlongeur)


def nameSauts():
	global datas
	for plongeur in plongeurs:
		data = []
		data.append(plongeur)
		print("Sauteur : " + plongeur)
		for i in range(2):
			dataSaut = []
			saut = input("\tNom saut " + str(i+1) + " : ")
			coef = float(input("\tCoefficient : "))
			dataSaut.append(saut)
			dataSaut.append(coef)
			data.append(dataSaut)
		datas.append(data)


def listeSauts(nbrSaut):
	for plongeur in datas:
		print("\t" + plongeur[0] + " : " + str(plongeur[nbrSaut][0]) + "; " + str(plongeur[nbrSaut][1]))


def noteSaut():
	global datas
	for plongeur in plongeurs:
		notesSaut = []
		print("Sauteur : " + plongeur[0] + " : " + plongeur[nbrSaut][0] + "; " + plongeur[nbrSaut][1])
		for i in range(5):
			note = float(input("Points jury " + str(i) + " : "))
			notesSaut.append(note)
		datas.append(notesSaut)


def main():
	newPlongeurs()
	nameSauts()
	print(datas)
	listeSauts(1)
	noteSaut(1)
	print("En cours de construction...")


#--Variables--
plongeurs = []
datas = []

if __name__ == "__main__":
	main()