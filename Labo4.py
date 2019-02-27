def newPlongeurs():
	global plongeurs
	for i in range(3):
		nPlongeur = input("Veuillez rentrer le nom du plongeur n° " + str(i+1) + " : ")
		plongeurs.append(nPlongeur)


def nameSauts():
	global datas
	for plongeur in plongeurs:
		data = []
		data.append(plongeur)
		for i in range(2):
			dataSaut = []
			saut = input("Veuillez rentrer le saut n° " + str(i+1) + " du plongeur " + plongeur + " : ")
			coef = input("Veuillez rentrer le coefficient de ce saut : ")
			dataSaut.append(saut)
			dataSaut.append(coef)
			data.append(dataSaut)
		datas.append(data)



def main():
	newPlongeurs()
	nameSauts()
	print(datas)
	print("En cours de construction...")


#--Variables--
plongeurs = []
datas = []

if __name__ == "__main__":
	main()