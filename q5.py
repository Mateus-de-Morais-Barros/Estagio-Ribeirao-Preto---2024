'''
Escreva um programa que inverta os caracteres de um string. 


IMPORTANTE: 

	a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 

	b) Evite usar funções prontas, como, por exemplo, reverse; 
'''

string = "o rato roeu a roupa do rei de roma"

gnirts = ''
cur = string.__len__() - 1
for i in string:
    gnirts += string[cur]
    cur -= 1
    

print(gnirts)