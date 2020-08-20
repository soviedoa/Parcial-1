n = int(input("Ingrese los dos últimos dígitos de su número de documento "))
def Id(n):
    if n < 2:
        return 1
    else:
        return str(n)+" "+str(Id(n-1))
print(Id(n))