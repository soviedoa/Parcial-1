row = int(input("Ingrese la fila del dato a buscar: "))
column = int(input("Ingrese la columna del dato a buscar: "))
def  pascal(row, column):
    if row < 0 and column < 0:
        return 0
    elif row == 0 and column == 0:
        return 1
    else:
        nuevaFila = [1]
        ultimaFila = pascal(row-1,column)
        for i in range(len(ultimaFila)-1):
            nuevaFila.append(nuevaFila[i] + ultimaFila[i+1])
        nuevaFila += [1]
    return nuevaFila[column]
print("El dato a buscar es: ",pascal(row,column))