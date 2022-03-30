ips={}
resp="S"
while resp =="S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digete <S> para continuar: ").upper()

print("Exibindo as máquinas que compõem uma mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)