# -*- coding: iso-8859-1 -*-
with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.readlines()
print("Tipo de dado da vari�vel",type(conteudo))
print("Conte�do do arquivo:",conteudo)