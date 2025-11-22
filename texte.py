print("Analyseur de Texte")
saisie = input("Entrez un mot ou une phrase : ")

if len(saisie.strip()) == 0:
    print("vous n'avez rien saisi.")
else:
    longueur = len(saisie) 
    maj = saisie.upper()
    minu = saisie.lower()
    inverse = saisie[::-1]
    print(f"\nAnalyse de '{saisie}' :")
    print(f"- Longueur : {longueur} caractères")
    print(f"- Majuscules : {maj}")
    print(f"- Minuscules : {minu}")
    print(f"- Inversion  : {inverse}")
    if saisie.lower() == inverse.lower():
        print("\nC'est un PALINDROME ! <<<")
    else:
        print("\nCe n'est pas un palindrome.")

