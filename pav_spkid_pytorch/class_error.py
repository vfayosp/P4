n_errores = 0
total=0
with open('lpcc_class_hsize250_lr000125.log') as f:
    for linea in f:
        total=total+1
        fichero_class = linea.split()
        fichero = fichero_class[0].split('/')
        classificacion = fichero_class[1]
        if fichero[1] != classificacion:
            n_errores = n_errores+1
p_error = (n_errores/total)*100

f = open("p_error_class.txt","a")
f.write("p_error lp = {0:.5f}\n".format(p_error))
f.close

print("El número de errores es de", n_errores)
print("La probabilidad de error en clasificación es del {0:.5f}%".format(p_error))