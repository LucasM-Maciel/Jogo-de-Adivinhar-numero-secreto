import random
pontuacao= 0
elogio = " "
tentativas_sobrando= 5
tentativas_usadas = 1
def verificarpluralusadas(tentativa):
    if tentativa <= 1:
        return "tentativa"
    else:
        return "tentativas"
    
def verificarpluralsobrando(tentativa):
    if tentativa-1 <= 1:
        return "tentativa"
    else:
        return "tentativas"
def pergunta_numero_inteiro(dificuldade):
     while True:
        try:
            numero = int(input(f"Tente acertar um número de 1 a {10*dificuldade}"))
            return numero
        except ValueError:
            print("Não é número")
            continue
    
def verificar_inteiro_dificuldade():
    while True:
        try:
            dificuldade=int(input("Olá seja bem vindo! Esse é o jogo do número misterioso escolha a dificuldade de 1 a 3\n número 4 para finalizar o jogo e ver sua pontuação"))
            return dificuldade
        except ValueError:
            print("Não é número")
            continue

while True:
    dificuldade= verificar_inteiro_dificuldade()
    if dificuldade== 4:
        break
    elif dificuldade==1:
        numerosecreto = numerosecreto = random.randint(1, 10*dificuldade)
        tentativas_sobrando= 5
        tentativas_usadas = 1
        while tentativas_sobrando>0:
            palavra_tentativa_sobrando = verificarpluralsobrando(tentativas_sobrando)
            palavra_tentativa_usadas = verificarpluralusadas(tentativas_usadas)
            desafio_nivel1 = pergunta_numero_inteiro(dificuldade)
            if desafio_nivel1 > 10 or desafio_nivel1<1:
                print("Número inválido, tente um número de 1 a 10")
                continue
            elif desafio_nivel1>numerosecreto:
                tentativas_sobrando -=1
                print(f"O número {desafio_nivel1} é maior que o número secreto!\n você  tem {tentativas_sobrando} {palavra_tentativa_sobrando}")
                tentativas_usadas += 1
            elif desafio_nivel1<numerosecreto:
                tentativas_sobrando -=1
                print(f"O número {desafio_nivel1} é menor que o número secreto!\n você  tem {tentativas_sobrando} {palavra_tentativa_sobrando}")
                tentativas_usadas += 1
            else:
                print(f"Parabéns o número {numerosecreto} é o número secreto e você acertou em {tentativas_usadas} {palavra_tentativa_usadas}")
                pontuacao+=10
                break
                
        if tentativas_sobrando==0:
            print("\nvocê perdeu, tente novamente")  
    
    elif dificuldade==2:
        numerosecreto = random.randint(1, 10*dificuldade)
        tentativas_sobrando= 5
        tentativas_usadas = 1
        while tentativas_sobrando>0:
            palavra_tentativa_sobrando = verificarpluralsobrando(tentativas_sobrando)
            palavra_tentativa_usadas = verificarpluralusadas(tentativas_usadas)
            desafio_nivel2 = pergunta_numero_inteiro(dificuldade)
            if desafio_nivel2 > 20 or desafio_nivel2<1:
                print("Número inválido, tente um número de 1 a 20")
                continue
            elif desafio_nivel2>numerosecreto:
                tentativas_sobrando -=1
                print(f"O número {desafio_nivel2} é maior que o número secreto!\n você  tem {tentativas_sobrando} {palavra_tentativa_sobrando}")
                tentativas_usadas += 1
            elif desafio_nivel2<numerosecreto:
                tentativas_sobrando -=1
                print(f"O número {desafio_nivel2} é menor que o número secreto!\n você  tem {tentativas_sobrando} {palavra_tentativa_sobrando}")
                tentativas_usadas += 1
            else:
                print(f"Parabéns o número {numerosecreto} é o número secreto e você acertou em {tentativas_usadas} {palavra_tentativa_usadas}")
                pontuacao +=20
                break
        if tentativas_sobrando==0:
            print("\nvocê perdeu, tente novamente")  
    elif dificuldade==3:
        numerosecreto = random.randint(1, 10*dificuldade)
        tentativas_sobrando= 5
        tentativas_usadas = 1
        while tentativas_sobrando>0:
            palavra_tentativa_sobrando = verificarpluralsobrando(tentativas_sobrando)
            palavra_tentativa_usadas = verificarpluralusadas(tentativas_usadas)
            desafio_nivel3 = pergunta_numero_inteiro(dificuldade)
            if desafio_nivel3 > 30 or desafio_nivel3<1:
                print("Número inválido, tente um número de 1 a 30")
                continue
            elif desafio_nivel3>numerosecreto:
                tentativas_sobrando -=1
                print(f"O número {desafio_nivel3} é maior que o número secreto!\n você  tem {tentativas_sobrando} {palavra_tentativa_sobrando}")
                tentativas_usadas += 1
            elif desafio_nivel3<numerosecreto:
                tentativas_sobrando -=1
                print(f"O número {desafio_nivel3} é menor que o número secreto!\n você  tem {tentativas_sobrando} {palavra_tentativa_sobrando}")
                tentativas_usadas += 1
            else:
                print(f"Parabéns o número {numerosecreto} é o número secreto e você acertou em {tentativas_usadas} {palavra_tentativa_usadas}")
                pontuacao +=30
                break
        if tentativas_sobrando==0:
            print("\nvocê perdeu, tente novamente")          
    else: 
        print("número inválido digite um número de 1 a 3  conforme a dificuldade desejada\n número 4 para parar e ver a pontuação")
        
if pontuacao <= 10:
    elogio = "você é um adivinhador horrível"
elif pontuacao >10 and pontuacao<= 50:
    elogio = "você está no caminho pra ser um adivinhador excelente!"
else:
    elogio = "Adivinhador Supremo!"
    
print(f"\nparabéns você fez {pontuacao} pontos!\n {elogio}")
