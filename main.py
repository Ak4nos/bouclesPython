nombres_saisis = input("Sélectionner une liste de nombre entiers séparés par une virgule : ")
liste_des_nombres = nombres_saisis.split(',')
print(liste_des_nombres)
somme_des_nombres = 0
resultat = 0
pairs = 0
for nombre in liste_des_nombres:
  nombre = int(nombre)
  somme_des_nombres += nombre
  moyenne = somme_des_nombres / len(liste_des_nombres)
  if nombre > moyenne:
    resultat += 1
  print("Somme des nombres : ", somme_des_nombres)
  print("Moyenne des nombres : ", moyenne)
  print("Nombre de nombres supérieurs à la moyenne : ", resultat)
  
  
while (nombre%2) == 0:
    pairs += 1
    break
print("Nombre de nombres pairs : ", pairs)
