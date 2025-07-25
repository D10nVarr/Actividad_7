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
            count_pst+=1
        elif num<0:
            count_cero+=1
        else:
            count_ngt+=1
    print(f"La suma los {cant_nums} números es {nums_sum}")
    print(f"El promedio es {nums_sum/cant_nums}")
    print(f"Hay {count_pst} numeros positivos, {count_ngt} negativos y {count_cero} ceros")
    print(f"De los números {multp_tres} son múltiplos de 3")

def calcular_area_rectngl(b,a):
    return b*a
def calcular_peri_triangulo(b,a):
    return 2*b+2*a

def es_primo(num):
