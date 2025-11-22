print("Mini-calculatrice")

try:
    nombre1 = float(input("entrez le premier nombre :"))
    nombre2 = float(input("entrez le deuxieme nombre :"))
    operation = input("entrez l'operation (+, -, *, /) :")
    resultat = 0
    operation_valide = True
    if operation == "+":
        resultat = nombre1 + nombre2
    elif operation == "-":
         resultat = nombre1 - nombre2
    elif operation == "*":
         resultat = nombre1 * nombre2 
    elif operation == "/":
        if nombre2 != 0:
             resultat = nombre1 / nombre2
        else:
            print("erreur : division par zero")
            
    if operation_valide:       
         print("le resultat de", nombre1, operation, nombre2, "est :", resultat)
    else:       
         operation_valide = False        
         print("erreur : operation inconnue")
    
except ValueError:
    print("Erreur de saisie : Veuillez entrer des chiffres valides.")
         
  
    
                
         

        
    
    
    