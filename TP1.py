import random
num = random.random()
print(num)
def mi_funcion(parametro1, parametro2):
    # Implementa la lógica de la función
    resultado = parametro1 + parametro2
    return resultado
list1 = [3]
contador = 0
print("Mi primera función es para realizar sumas.")
while contador < 10:
    # Código a ejecutar en cada iteración
    a=random.choice(list1)
    b=random.choice(list1)
    print("Esta es la suma ", contador + 1, ". Voy a sumar ", a, " + ", b, " es igual a", mi_funcion(a,b))
    contador += 1  # Incrementa el contador