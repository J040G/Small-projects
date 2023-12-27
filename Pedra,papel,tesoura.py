import random
user_wins=0
pc_wins=0

options = ["pedra", "papel", "tesoura"]

while True:
    user_input = input("Digite pedra/papel/tesoura ou s para sair: ").lower()
    if user_input == "s":
        break
        
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("O pc escolheu", computer_pick + ".")
    
    if user_input == "pedra" and computer_pick == "tesoura":
        print("VOCÊ GANHOUUU!!")
        user_wins += 1
    
    elif user_input == "tesoura" and computer_pick == "papel":
        print("VOCÊ GANHOUUU!!")
        user_wins += 1
        
    elif user_input == "papel" and computer_pick == "pedra":
        print("VOCÊ GANHOUUU!!")
        user_wins += 1
    
    else:
        print("VOCÊ PERDEU!!")
        pc_wins += 1
print ("Você ganhou ", user_wins, " vezes.")
print ("O pc ganhou ", pc_wins, " vezes.")
print("Até mais!")