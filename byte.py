mbyte=int(input("Введите количество мегабайт: "))
gbyte=mbyte/1024
tbyte=gbyte/1024
pbyte=tbyte/1024
ebyte=pbyte/1024
zbyte=ebyte/1024
ybyte=zbyte/1024
print(str(bit)+" бит = "+str(byte)+" Байт")
print(str(bit)+" бит = "+str(kbyte)+" Килобайт")
print(str(bit)+" бит = "+str(mbyte)+" Мегабайт")
print(str(bit)+" бит = "+str(gbyte)+" Гигабайт")
print(str(bit)+" бит = "+str(tbyte)+" Терабайт")
print(str(bit)+" бит = "+str(pbyte)+" Петабайт")
print(str(bit)+" бит = "+str(ebyte)+" Эксобайт")
print(str(bit)+" бит = "+str(zbyte)+" Зетабайт")
print(str(bit)+" бит = "+str(ybyte)+" Йоттабайт")

