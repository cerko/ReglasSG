from io import open
import re


f = open('HH20180720.txt','r')
mensaje = f.read()
# print(mensaje)
f.close()

asientos = re.findall('Asiento [1-6]: .+ \(', mensaje)

asientos[6:] = [] # nos quedamos con solo los 6 primeras apariciones de los asientos

for i in range(len(asientos)):
    asientos[i] = asientos[i].replace("("," ").strip(" ")
    x = asientos[i]
    asientos[i] = x[11:]
    print(asientos[i])


#     La función findall()

# La función findall() devuelve una asientos con las subcadenas que cumplen el patrón en una cadena. El formato que utiliza es: findall(patrón, cadena, [flag])

# cadena = 'tengo una yama que yama se llama'
# asientos = re.findall('..ama', cadena)
# print(asientos)  # muestra: [' yama', ' yama', 'llama']