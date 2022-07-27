tupla = ('floyd', 'led', 'dylan', 'morisson', 'stramp',
         'neil', 'crosby', 'still', 'nash', 'scorpions')
print(tupla[0:5])
print(tupla[-4:])
print(sorted(tupla)) # a função sorted() é usada para colocar um tupla inteira em ordem alfabetica. o python tranforma a tupla em uma lista, pois tuplas sao imutaveis, assim temos a tupla intacta
print(f'a banda Supertramp está na {tupla.index("stramp")+1}ª posiçao')
