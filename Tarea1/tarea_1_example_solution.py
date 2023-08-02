# Primera funcion
def separa_letras(cadena):
    minusc = ""  # variable para letras minusculas
    mayusc = ""  # variable para letras mayusculas
    codigo_error = 0  # variable para codigo error/exito

    # verifica si cadena no es str
    if not isinstance(cadena, str):
        codigo_error += -100
        minusc = None
        mayusc = None
        # print(codigo_error, mayusc, minusc)
        return codigo_error, None, None
    # .strip() verifica si cadena es un str vacio
    elif not cadena.strip():
        codigo_error += -300
        minusc = None
        mayusc = None
        # print(codigo_error, mayusc, minusc)
        return codigo_error, None, None
    # verifica que cadena solo sea alfabeticos(a-z)
    elif not cadena.isalpha():
        codigo_error += -200
        minusc = None
        mayusc = None
        # print(codigo_error, mayusc, minusc)
        return codigo_error, None, None

    for char in cadena:  # si no existen ninguno de los errores, separa el str
        if char.isupper():  # para los caracteres en mayuscula del string
            mayusc += char   # añade las mayusculas a la variable mayusc
        elif char.islower():  # para los caracteres en minuscula del string
            minusc += char  # añade las minusculas a la variable minusc
    # print(codigo_error, mayusc, minusc)
    return codigo_error, mayusc, minusc

# Segunda funcion
# Primeramente se verifica si las variables de entrada
# corresponden a numeros enteros o son strings.


def potencia_manual(base, potencia):
    if isinstance(base, str) or isinstance(potencia, str) is True:
        estado = -400  # Se asignan codigos de error para las salidas de
        result = None  # estado y result si se cumpliera que son strings.
    else:  # Despues de verificar que son numeros, se asgina el estado 0
        estado = 0  # representando que no hay errores.
        if potencia == 0:  # En caso que el exponenete de la potencia sea 0
            result = 1    # Se asigna como resultado 1
            return estado, result
        else:  # Inicia como tal la logica de la potencia usando solo sumas
            result = base  # Se asigna como resultado la base
            for _ in range(1, potencia):  # Primer ciclo que aplica el segundo
                # ciclo segín el numero del (exponente - 1)
                suma = 0  # Suma temporal iniciando en 0
                for _ in range(result):  # Ciclo que se repiete según la base
                    suma += base  # A suma se  asgina/suma el valor de la base
                    result = suma  # Esa suma se asgina como el resultado final
    return estado, result
