#Codelab_Variables_Python

nombre = "Carlos"
#Variable Primitiva int. En Python permiten almacenar un valor numérico no decimal ya sea positivo o negativo de cualquier valor.
edad = 26
#Estatura en metros
#Variable Primitiva float En Python permiten almacenar un máximo de 2^64 números diferentes.
estatura = 1.70
ejercicio = False

print("Datos del Estudiante")
print("Nombre", nombre)
print("Edad", edad)
print("Estatura", estatura)
print("Hace ejercicio", ejercicio)

#Aplica la fórmula de la suma de los primeros n números pares, tomando como n la variable de tipo entero y almacenar el resultado en una variable
print("Ingrse le numero inicial")
i = int(input())
print("Ingrse el numero final")
f = int(input())
suma = 0
print("***Numeros Pares***")
while i <= f:
    if i % 2 == 0:
        print(i)
        suma = suma + i
    i += 1    
print("La suma de los números es: ", suma)