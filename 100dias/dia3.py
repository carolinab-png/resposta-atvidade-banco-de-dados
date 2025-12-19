print(''' 


 _____.______.______._____
 \`\                   /'/
  \ |                 | /
   >|___,____,____,___|<
  /d$$$P ,ssssssssssss. \\
 /d$$$P ,d$$$$$$$$$$$$$b \\
<=====w======w======w=====>
 \ \____> \_____/ <____/ /
  \_____________________/ pb

      
Bem Vindo ao Jogo da Ilha do Tesouro. Sua missão é chegar ao local onde está o tesouro, ultrapassando todas as armadilhas.
''')

fase1= input("Você está em uma estrada com dois caminhos a sua frente. Você escolhe ir a esquerda ou direita?").lower()
if fase1 == "esquerda":
    print("game over")
elif fase1 == "direita":
    fase2 = input("Você seguiu pelo caminho e encontrou uma ponte velha e um barco para atravessar o rio. Qual dos dois você escolhe?")
    if fase2== "ponte":
        print("game over")
    elif fase2 =="barco":
        fase3= input("você chegou ao outro lado do rio. Há dois baús, um verde e um vermelho. Qual você quer abrir")
        if fase3 == "verde":
            print("game over")
        elif fase3 == "vermelho":
            print("parabéns, você achou o tesouro!")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")
