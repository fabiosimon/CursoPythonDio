import textwrap
from os import system, name 

def menu():
    menu = """
    ================ MENU ================
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """
    
    
    return input(textwrap.dedent(menu))

###################################################
def deposito(Saldo):
    while True:
        valor = input("Valor: ")
    
       
        valor=valor.replace(",",".")
        try:
            val = float(valor)
        except ValueError:
            print("Erro: passe um valor numerico positivo")
            continue

        if val < 0:
            print("Erro: valor deve ser positivo")
            continue
        
        val=int(val * 100) / 100
        
        if val == 0:
            break
        
        Saldo += val
        Movimentos.append(f"Deposito : {val}  -  Saldo : {Saldo} ")
        
        print(f"Deposito de {val} realizado com sucesso!")
        input("Enter para continuar")
        system("clear")
        
        break
    return Saldo    
    

###################################################
def saque(saldo,saques):
    
    if saques == 3:
        print("Já realizou 3 saques hoje.")
        input("Enter para continuar")
        system("clear")
        return saldo,saques
    
    while True:
        valor = input("Valor: ")
    
       
        valor=valor.replace(",",".")
        try:
            val = float(valor)
        except ValueError:
            print("Erro: passe um valor numerico ")
            continue
 


        val=abs(val)
        
        val=int(val * 100) / 100
        
        if val == 0:
            break
        
        if val > saldo:
            print(f"Saldo insuficiente: {saldo}")
            input("Enter para continuar")
            system("clear")
            break
        
        saldo -= val
        saques=saques + 1
        Movimentos.append(f"Saque    : {val}  -  Saldo : {saldo} ")
                            
        print(f"Saldo de {val} realizado com sucesso!")
        input("Enter para continuar")
        system("clear")
        
        break
    return saldo , saques
    
    return

####################################################
def extrato():
    
    system("clear")
    
    print("=============== Movimentação de Hoje  ===============")
    
    for linha in Movimentos:
        x=linha
        print(x)
    
    print("\n\n\n\n")
    input("Enter para continuar")
    system("clear")
    

################ INICIO #############################

Saldo=0.0
SaquesDia=0
Movimentos = []

Movimentos.append(f"Inicio : {Saldo}")


while True:
    
    opcao = menu()
    
    if opcao.lower()=='q':
        break
    
    if opcao.lower() == 'd':
        Saldo=deposito(Saldo)
    
    if opcao.lower() == 'e':
        extrato()
    
    if opcao.lower() == 's':
        Saldo, SaquesDia=saque(Saldo, SaquesDia)
    
     
    
    
