# Registro
# Recibas de forma dinamica: nombre, año de nacimiento, correo y contraseña

"""
    Nombre: Fernando
    Email: fernando@correo.com
    Tendrás 55 años en el 2025
    Tu contraseña es: ****
"""

name = input("Cuál es tu nombre? : ")
year_of_birth = input("En qué año naciste? : ")
email = input("Cuál es tu correo electrónico? : ")
password = input("Cuál es tu contraseña? : ")

future_age = 2050 - int(year_of_birth)
password_length = len(password)

card = f"""
    Nombre: {name}
    Email: {email}
    Tendrás {future_age} años en el 2050 
    Tu contraseña es: {'*' * password_length}
"""

print(card)