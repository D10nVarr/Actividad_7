def operar_nums(cant_nums):
    nums_sum=0
    count_pst=0
    count_ngt=0
    count_cero=0
    multp_tres=0

    for i in range(cant_nums):
        num=float(input("Ingrese su numero: "))
        nums_sum+=num
        if num%3==0:
            multp_tres+=1
        if num==0:
            count_cero+=1
        elif num>0:
            count_pst+=1
        else:
            count_ngt+=1
    print(f"\nLa suma los {cant_nums} números es {nums_sum}")
    print(f"El promedio es {nums_sum/cant_nums}")
    print(f"Hay {count_pst} numeros positivos, {count_ngt} negativos y {count_cero} ceros")
    print(f"De los números {multp_tres} son múltiplos de 3")

def calcular_area_rectngl(b,a):
    return b*a
def calcular_peri_triangulo(b,a):
    return 2*b+2*a

def es_primo(num):
    primo=True
    if num<=1:
        primo=False
    else:
        for i in range(2,num):
            if num%i==0:
                primo=False
                break
    return primo

def promediar_notas(cant_nums):
    num_suma = 0
    mayor_nota=0
    riesgo_nota=0

    for i in range(cant_nums):
        num=float(input(f"Ingrese la calificación: "))
        if num>=0:
            num_suma+=num
            if num>=85:
                mayor_nota+=1
            elif num<60:
                riesgo_nota+=1
        else:
            print("La calificación ingresada no es válida")

    print(f"\nEl promedio de las notas es de {num_suma/ cant_nums}")
    print(f"Hay {mayor_nota} notas mayores a 85")
    print(f"Hay {riesgo_nota} notas que estan en zona de riesgo")

def agrupar_numeros(cant_nums):
    num = float(input("Ingrese un numero: "))
    max_num = num
    min_num = num
    frec_num=num
    cont_frec_nums=1

    for i in range(cant_nums - 1):
        num = float(input("Ingrese un numero: "))
        if frec_num==num:
            cont_frec_nums+=1

        else:
            frec_num=num
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    print(f"\nEl número mayor es {max_num}, el menor es {min_num} y se repiten {cont_frec_nums}")

def calcular_nums(a,b):
    return f"\nDe {a} y {b} la suma es {a+b}, su resta es {a-b} su producto es {a*b} y su división es {a/b}"

while True:
    print("\n---MENÚ DE OPERACIONES---")

    print("1. Sumar, promediar, contar positivos/negativos y contar los múltiplos de 3")
    print("2. Cálcular el área de un rectángulo")
    print("3. Verificar si un número primo o no")
    print("4. Calcular el promedio de n calificacio y cuantos superon los 85 o son menores a 60")
    print("5. Mayor, menor y cuántos ser repiten de de n números")
    print("6. Calculadora básica")
    print("7. Salir del programa")

    opcion=input("Seleccione una de las 7 opciones: ")

    match opcion:
        case "1":
            nums = int(input("Ingrese la cantidad de numeros: "))
            operar_nums(nums)

        case "2":
            base=float(input("Ingrese la base del ractángulo: "))
            altura=float(input("Ingrese la altura del rectángulo: "))

            print(f"\nEl área del rectángulo es de {calcular_area_rectngl(base,altura)} y su perímetro es de {calcular_peri_triangulo(base,altura)}")

        case "3":
            num=int(input("Ingrese el número que desee modificar: "))
            if es_primo(num):
                print("\nEl número ingresado es primo")
            else:
                print("\nEl número ingresado no es primo")

        case "4":
            notas=int(input("Ingrese la cantidad de notas que desee operar: "))
            promediar_notas(notas)

        case "5":
            numeros=int(input("Ingrese la cantidad de numeros que desee: "))
            agrupar_numeros(numeros)
        case "6":
            num_1=float(input("Ingrese el primer número: "))
            num_2=float(input("Ingrese el segundo número: "))

            print(calcular_nums(num_1,num_2))

        case "7":
            print("Saliendo del programa ...")
            break

        case _:
            print("Opción no válida")



