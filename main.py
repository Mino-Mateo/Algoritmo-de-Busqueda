def imprimir_Arreglo(arreglo):
  tamanio = len(arreglo)
  for i in range(tamanio):
    print(f'[{arreglo[i]}]', end = "")

def algoritmo_Busqueda_Lineal(arreglo, sueldo):
  resultado = False
  tamanio = len(arreglo)
  for i in range(tamanio):
    if(arreglo[i] == sueldo):
      resultado = True
      return resultado
  return resultado

listaSueldos = [20.8, 150.5, 170.5, 180.5, 190.30, 75.6, 200]
imprimir_Arreglo(listaSueldos)
sueldo = float(input("\nIngrese el sueldo a encontrar: "))
respuesta = algoritmo_Busqueda_Lineal(listaSueldos, sueldo)
if respuesta:
  print("El sueldo fue encontrado en nuestro sistema")
else:
  print("El sueldo no fue encontrado en nuestro sistema")