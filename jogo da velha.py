def criar_tabuleiro():
    """Cria um tabuleiro vazio."""
    return [" " for _ in range(9)]

def exibir_tabuleiro(tabuleiro):
    """Exibe o tabuleiro com cores e layout aprimorado."""
    cores = {
        "X": "\033[91mX\033[0m",  # Vermelho
        "O": "\033[94mO\033[0m",  # Azul
        " ": " "
    }
    print(f" {cores[tabuleiro[0]]} | {cores[tabuleiro[1]]} | {cores[tabuleiro[2]]} ")
    print("---+---+---")
    print(f" {cores[tabuleiro[3]]} | {cores[tabuleiro[4]]} | {cores[tabuleiro[5]]} ")
    print("---+---+---")
    print(f" {cores[tabuleiro[6]]} | {cores[tabuleiro[7]]} | {cores[tabuleiro[8]]} ")

def jogador_escolhe_posicao(tabuleiro, jogador):
    """Pede ao jogador para escolher uma posição vazia."""
    while True:
        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posição de 1 a 9: ")) - 1
            if 0 <= posicao <= 8 and tabuleiro[posicao] == " ":
                return posicao
            else:
                print("Posição inválida ou já ocupada. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número de 1 a 9.")

def verificar_vitoria(tabuleiro, jogador):
    """Verifica se o jogador venceu."""
    # Linhas
    for i in range(0, 9, 3):
        if tabuleiro[i] == tabuleiro[i+1] == tabuleiro[i+2] == jogador:
            return True
    # Colunas
    for i in range(3):
        if tabuleiro[i] == tabuleiro[i+3] == tabuleiro[i+6] == jogador:
            return True
    # Diagonais
    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] == jogador:
        return True
    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] == jogador:
        return True
    return False

def verificar_empate(tabuleiro):
    """Verifica se o tabuleiro está cheio."""
    return " " not in tabuleiro

def jogar_jogo_da_velha():
    """Função principal para jogar o jogo da velha."""
    tabuleiro = criar_tabuleiro()
    jogador_atual = "X"
    jogo_ativo = True

    while jogo_ativo:
        exibir_tabuleiro(tabuleiro)
        posicao = jogador_escolhe_posicao(tabuleiro, jogador_atual)
        tabuleiro[posicao] = jogador_atual

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"\033[91mJogador {jogador_atual} venceu!\033[0m")
            jogo_ativo = False
        elif verificar_empate(tabuleiro):
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            jogo_ativo = False
        else:
            jogador_atual = "O" if jogador_atual == "X" else "X"

if __name__ == "__main__":
    print("Bem-vindo ao Jogo da Velha!")
    jogar_jogo_da_velha()
