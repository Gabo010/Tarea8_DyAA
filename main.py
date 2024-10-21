def producto_maximo(arreglo, inicio, fin):
    if inicio == fin:
        return arreglo[inicio], [arreglo[inicio]]

    mitad = (inicio + fin) // 2
    producto_izquierda, subarreglo_izquierda = producto_maximo(arreglo, inicio, mitad)
    producto_derecha, subarreglo_derecha = producto_maximo(arreglo, mitad + 1, fin)
    producto_cruzado, subarreglo_cruzado = producto_maximo_cruzado(arreglo, inicio, mitad, fin)

    if producto_izquierda >= producto_derecha and producto_izquierda >= producto_cruzado:
        return producto_izquierda, subarreglo_izquierda
    elif producto_derecha >= producto_izquierda and producto_derecha >= producto_cruzado:
        return producto_derecha, subarreglo_derecha
    else:
        return producto_cruzado, subarreglo_cruzado


def producto_maximo_cruzado(arreglo, inicio, mitad, fin):
    producto_izquierda = float('-inf')
    producto_derecha = float('-inf')
    producto_actual = float('-inf')
    pares_izquierda = []
    pares_derecha = []

    # Calcular el producto máximo del lado izquierdo
    for i in range(inicio, mitad + 1):
        for j in range(i + 1, mitad + 1):
            producto = arreglo[i] * arreglo[j]
            if producto > producto_izquierda:
                producto_izquierda = producto
                pares_izquierda = [arreglo[i], arreglo[j]]

    # Calcular el producto máximo del lado derecho
    for i in range(mitad + 1, fin + 1):
        for j in range(i + 1, fin + 1):
            producto = arreglo[i] * arreglo[j]
            if producto > producto_derecha:
                producto_derecha = producto
                pares_derecha = [arreglo[i], arreglo[j]]

    # Comparar cruzado entre un número del lado izquierdo y otro del lado derecho
    for i in range(inicio, mitad + 1):
        for j in range(mitad + 1, fin + 1):
            producto = arreglo[i] * arreglo[j]
            if producto > producto_actual:
                producto_actual = producto
                pares_cruzados = [arreglo[i], arreglo[j]]

    # Determinar cuál de los tres productos es el mayor
    if producto_izquierda >= producto_derecha and producto_izquierda >= producto_actual:
        return producto_izquierda, pares_izquierda
    elif producto_derecha >= producto_izquierda and producto_derecha >= producto_actual:
        return producto_derecha, pares_derecha
    else:
        return producto_actual, pares_cruzados


if __name__ == "__main__":
    arreglo = [9, 15, 30, 56, 90, 12, 10]
    resultado, numeros_multiplicados = producto_maximo(arreglo, 0, len(arreglo) - 1)
    print(f"El producto máximo en el arreglo es: {resultado}")
    print(f"Los números que se multiplicaron para obtener este valor son: {numeros_multiplicados}")
