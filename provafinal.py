import random

def jogar():
    """Função principal para jogar o jogo de adivinhação."""
    print("Bem-vindo ao jogo 'Adivinhe o Número'!")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar qual é.")

    # Gerar um número aleatório entre 1 e 100
    número_para_adivinhar = random.randint(1, 100)
    tentativas = 0
    máximo_de_tentativas = 10  # Número máximo de tentativas

    while tentativas < máximo_de_tentativas:
        try:
            adivinhar = int(input("Digite seu palpite: "))
            if adivinhar < 1 or adivinhar > 100:
                print("Por favor, escolha um número entre 1 e 100.")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            continue

        tentativas += 1

        if adivinhar < número_para_adivinhar:
            print("O número é maior. Tente novamente.")
        elif adivinhar > número_para_adivinhar:
            print("O número é menor. Tente novamente.")
        else:
            print(f"Parabéns! Você acertou o número {número_para_adivinhar} em {tentativas} tentativas!")
            break
    else:
        print(f"Você esgotou suas tentativas. O número era {número_para_adivinhar}.")

def main():
    """Função principal para controlar o fluxo do jogo."""
    while True:
        jogar()
        play_again = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if play_again != 's':
            print("Obrigado por jogar! Até a próxima.")
            break

if __name__ == "__main__":
    main()
