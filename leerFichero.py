from io import open
f = open('HH20180720.txt','r')
mensaje = f.read()
print(mensaje)
f.close()