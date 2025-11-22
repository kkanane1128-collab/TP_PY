print("Convertisseur de Températures")

try:
    celsius = float(input("Entrez la température en Celsius (°C) : "))
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"{celsius} °C equivaut a {fahrenheit:.2f} °F et {kelvin:.2f} K.")
except ValueError:
    print("erreur de saisie : veuillez entrer un nombre valide")
    
