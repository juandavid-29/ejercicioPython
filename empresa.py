numberEmpleado = 5
arrayEmpresa = [0]
for i in range(numberEmpleado):
    nombre = input('Ingrese el nombre del trabajador: ')
    salario_base = float(input('Ingrese el valor de salario base: '))
    numero_de_horas = float(input('Ingrese el numero de horas extras trabajadas: '))
    categoria1 = ('Categoria A: Producción')
    categoria2 = ('Categoria B: Oficina')
    salario_neto = 0
    horas_extras = 0
    for i in arrayEmpresa:
        if numero_de_horas >= 1:
            horas_extras = numero_de_horas*0.10*salario_base
        else:
            horas_extras = 0
    salario_neto = salario_base+horas_extras
    if salario_neto > 200000 and salario_neto <= 600000:
        print(categoria1)
    if salario_neto > 600000:
        print(categoria2)
     
    print('nombre del trabajador: ' + nombre)
    print('Valor de salario basico: ' + repr(salario_base)) 
    print('Valor de horas extras: ' + repr(horas_extras))
    print('Valor de salario neto: ' + repr(salario_neto)) 
    
suma = 0
for i in range(2):
    suma = suma + int(input("Ingrese cada salario neto y presione enter: "))

print('El valor total de la nomina es: ' + repr (suma))  




    
 





