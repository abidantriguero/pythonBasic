def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos" + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    print("Tienes $us " + str(dolares) + " dólares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Bolivianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción:  """

opcion = int(input(menu))

if opcion == 1:
    conversor("bolivianos", 6.88)
elif opcion == 2:
    conversor("argentinos", 65)
elif opcion == 3:
    conversor("mexicanos", 24)
else:
    print("Ingresa una opción correcta por favor")






# dolares = input("Cuantos dólares tienes?: ")
# dolares = float(dolares)
# valor_bolivianos = 6.88
# bolivianos = dolares * valor_bolivianos
# bolivianos = round(bolivianos, 2)
# print("Tienes Bs " + str(bolivianos) + " Bolivianos")