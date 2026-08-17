import time

print("======================================================")
print("")
print("                     Path of Shadows                  ")
print("")
print("======================================================")

nome = input("Qual o seu nome?  ")
print()
print()
print(f"Bem-Vindo, {nome}.")
print()
print("Sua jornada pelo caminho das sombras começa agora...")   

time.sleep(2)
escolha_classe = 0
while escolha_classe != 1 and escolha_classe != 2 and escolha_classe != 3:
    print("")
    print("[1] Guerreiro")
    print("[2] Mago")
    print("[3] Arqueiro")
    print("")

    escolha_classe = int(input("Escolha sua classe: "))
    print("")

    if escolha_classe == 1:
        classe = 'Guerreiro'
        vida = 120
        ataque = 15
        defesa = 12
    

    elif escolha_classe == 2:
        classe = 'Mago'
        vida = 100
        ataque = 20
        defesa = 8
    

    elif escolha_classe == 3:
        classe = 'Arqueiro'
        vida = 80
        ataque = 25
        defesa = 5

    else: 
        print("Escolha uma classe válida")

vida_atual = vida

    
    
print("Boa escolha! Abaixo suas informações:")
print("")
print(f"Classe: {classe}")
print(f"Vida: {vida_atual}/{vida}")
print(f"Ataque: {ataque}")
print(f"Defesa: {defesa}")

time.sleep(2)
print()
print("Você segue pela floresta...")
print("O vento fica mais forte. As árvores começam a esconder a luz do sol")
print("E de repente, você escuta um barulho atrás de você.")
print("UM GOBLIN!!")
print()
time.sleep(1)
inimigo = 'Goblin'
vida_inimigo = 60
vida_atual_inimigo = vida_inimigo
ataque_inimigo = 10
defesa_inimigo = 5
print()

print("======================================================")
print("")
print("----------------------- Goblin -----------------------")
print("")
print("======================================================")
print()
print(f"Classe: {inimigo}")
print(f"Vida: {vida_atual_inimigo}/{vida_inimigo}")
print(f"Ataque: {ataque_inimigo}")
print(f"Defesa: {defesa_inimigo}")
print()
time.sleep(3)

print("======================================================")
print("----------------------- Combate ----------------------")
print("======================================================")
morreu = False
fugiu = False
while vida_atual_inimigo > 0:
    print()
    print("[1] Atacar!")
    print("[2] Fugir!")
    print()
    escolha_ataque = 0
   
    
    while escolha_ataque != 1 and escolha_ataque != 2:
        escolha_ataque = int(input(""))

        if escolha_ataque == 1:
            time.sleep(1)
            dano = ataque - defesa_inimigo
            if dano < 1:
                dano = 1
            vida_atual_inimigo -= dano
            
            
            print(f"Você atacou o {inimigo}!")
            print(f"Dano causado: {dano}")
            print()
            print(f"Goblin: {vida_atual_inimigo}/{vida_inimigo} HP                        {classe}: {vida_atual}/{vida} HP ")
            time.sleep(2)
            
            dano_inimigo = ataque_inimigo - defesa
            if dano_inimigo < 1:
                dano_inimigo = 1
                        
            if vida_atual_inimigo > 0:
                vida_atual -= dano_inimigo
                print("")
                print("O inimigo atacou você!")
                print(f"Dano causado: {dano_inimigo}")
                print("")
                print(f"Goblin: {vida_atual_inimigo}/{vida_inimigo} HP                        {classe}: {vida_atual}/{vida} HP ")
                print("")
                
                if vida_atual <= 0:
                    print()
                    print("Você morreu!")
                    print("GAME OVER")
                    morreu = True
                    break
                
                
        elif escolha_ataque == 2:
            fugiu = True
            break
        
    
    if fugiu:
        break
    if morreu:
        break
    
if vida_atual_inimigo <= 0:
    print()
    print(f"O {inimigo} morreu!")
    print("")
    print("Você venceu a batalha!")
    print()
    
elif morreu:
    print()
    print("GAME OVER!")
    
else:
    print()
    print("Você fugiu...")
  

            

            
    
    
    