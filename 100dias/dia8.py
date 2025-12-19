import random

# --- VARIÁVEIS DE DESENHO DA FORCA ---
ESTAGIOS_FORCA = [
    # Índice 0: 0 erros
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    # Índice 1: 1 erro (Cabeça)
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    # Índice 2: 2 erros (Corpo)
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    # Índice 3: 3 erros (Braço esquerdo)
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    # Índice 4: 4 erros (Braços)
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    ---------
    """,
    # Índice 5: 5 erros (Perna esquerda)
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    ---------
    """,
    # Índice 6: 6 erros (DERROTA)
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    ---------
    """
]

def exibir_forca(chances_restantes):
    # Calcula o índice de desenho: 6 (máximo de chances) - chances_restantes
    indice_erro = 6 - chances_restantes
    print(ESTAGIOS_FORCA[indice_erro])

# --- CONFIGURAÇÕES INICIAIS ---
lista_palavras = ["iara", "onire", "carol", "python"]
palavra_sorteada = random.choice(lista_palavras)
tamanho_palavra = len(palavra_sorteada)

# Variáveis de Controle
chances_restantes = 6  
jogo_terminou = False
letras_tentadas = set() 

# LISTA: Display mutável para os acertos
display = ["_"] * tamanho_palavra 

# --- INFORMAÇÃO INICIAL ---
print("--- JOGO DA FORCA INICIADO ---")
print(f"A palavra tem {tamanho_palavra} letras.")
print("Primeira forca:")
exibir_forca(chances_restantes)
print("Palavra: " + " ".join(display))

# =======================================================
#               LOOP PRINCIPAL DO JOGO
# =======================================================

while not jogo_terminou:
    
    # 1. Solicita e valida o palpite
    letra_usuario = input("\nDigite uma letra (ou 'sair'): ").lower()

    if letra_usuario == 'sair':
        jogo_terminou = True
        break

    # 2. Verifica se a letra já foi tentada
    if letra_usuario in letras_tentadas:
        print(f"⚠️ Você já tentou a letra '{letra_usuario}'. Tente outra.")
        # Exibe o estado atual da forca e palavra antes de continuar
        exibir_forca(chances_restantes)
        print(f"Palavra atual: {' '.join(display)}")
        continue 
    
    # Adiciona a letra ao histórico de tentativas (acerto ou erro)
    letras_tentadas.add(letra_usuario)

    # 3. VERIFICAÇÃO E ATUALIZAÇÃO DA LÓGICA
    if letra_usuario in palavra_sorteada:
        print("✅ Acertou a letra! Atualizando o painel...")

        # Loop 'enumerate' para encontrar a POSIÇÃO da letra
        for posicao, letra_na_palavra in enumerate(palavra_sorteada):
            if letra_na_palavra == letra_usuario:
                display[posicao] = letra_usuario # Substitui o '_'
    
    else:
        # Lógica de Erro: Perde uma chance
        chances_restantes -= 1
        print(f"❌ Errou! '{letra_usuario}' não está na palavra.")
        

    # 4. EXIBIÇÃO DO ESTADO ATUAL
    
    # Exibe a forca atualizada APÓS o palpite (mudará apenas se for um erro)
    exibir_forca(chances_restantes) 
    
    print(f"Palavra atual: {' '.join(display)}")
    print(f"Chances restantes: {chances_restantes}")
    print(f"Letras tentadas: {', '.join(sorted(list(letras_tentadas)))}")

    # 5. CONDIÇÕES DE TÉRMINO
    
    # Condição de VITÓRIA
    if "_" not in display:
        jogo_terminou = True
        exibir_forca(chances_restantes) # Exibe a forca final, sem o boneco completo
        print(f"\n🎉 PARABÉNS! Você adivinhou a palavra: {palavra_sorteada}")
    
    # Condição de DERROTA
    elif chances_restantes <= 0:
        jogo_terminou = True
        exibir_forca(chances_restantes) # Exibe a forca com o boneco COMPLETO
        print(f"\n💀 FIM DE JOGO! Suas chances acabaram.")
        print(f"A palavra era: {palavra_sorteada}")

print("\n--- JOGO ENCERRADO ---")