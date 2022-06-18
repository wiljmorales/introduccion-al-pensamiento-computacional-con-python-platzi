objetivo = int(input('escribe un numero entero: '))
epsilon = 0.0001
bajo = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + bajo) / 2

while abs(respuesta ** 2 - objetivo) >= epsilon:
  if respuesta ** 2 > objetivo:
    alto = respuesta
  else:
    bajo = respuesta
  print(f'r={respuesta}, a={alto}, b={bajo}')
  respuesta = (alto + bajo) / 2

print(f'La raiz cuadrada de {objetivo} es {respuesta}')
