value=100
type_value = type(value)

print(value)
print(type_value)

# Pasar de int a str
value=str(100) + " Aplausos"
type_value = type(value)

print(value)
print(type_value)

# Pasar de str a int
value=int('100')
type_value = type(value)
print(value)
print(type_value)

# Pasar de str a float
value=float('100')
type_value = type(value)
print(value)
print(type_value)

# Pasar de str a float
# En este caso se rompe recien en esta linea
# demostrando como es el lenguaje interpretado en momento de ejecucion...
# value=float('100x')
type_value = type(value)
print(value)
print(type_value)

# Convertir de float a int
number = 34.5
print( f"{number} {type(number)}")
print ( f"{int(number)} {type(int(number))}")
