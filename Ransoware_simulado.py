from pathlib import Path
from cryptography.fernet import Fernet

PASTA_TESTES = Path("testes")
ARQUIVO = PASTA_TESTES / "arquivo_teste.txt"
ARQUIVO_CRIPTOGRAFADO = PASTA_TESTES / "arquivo_teste.txt.encrypted"
ARQUIVO_RESGATE = PASTA_TESTES / "LEIA_ME.txt"
CHAVE = PASTA_TESTES / "chave.key"


def preparar_ambiente():
    PASTA_TESTES.mkdir(exist_ok=True)

    if not ARQUIVO.exists():
        ARQUIVO.write_text(
            "Arquivo criado exclusivamente para o laboratório.\n",
            encoding="utf-8"
        )

    if not CHAVE.exists():
        chave = Fernet.generate_key()
        CHAVE.write_bytes(chave)


def carregar_chave():
    return CHAVE.read_bytes()


def criptografar():
    if not ARQUIVO.exists():
        print("Arquivo de teste não encontrado.")
        return

    chave = carregar_chave()
    fernet = Fernet(chave)

    dados = ARQUIVO.read_bytes()
    dados_criptografados = fernet.encrypt(dados)

    ARQUIVO_CRIPTOGRAFADO.write_bytes(dados_criptografados)

    print("Arquivo criptografado com sucesso.")
    print(f"Resultado: {ARQUIVO_CRIPTOGRAFADO}")


def descriptografar():
    if not ARQUIVO_CRIPTOGRAFADO.exists():
        print("Arquivo criptografado não encontrado.")
        return

    chave = carregar_chave()
    fernet = Fernet(chave)

    dados = ARQUIVO_CRIPTOGRAFADO.read_bytes()
    dados_descriptografados = fernet.decrypt(dados)

    ARQUIVO.write_bytes(dados_descriptografados)

    print("Arquivo descriptografado com sucesso.")
    print(f"Resultado: {ARQUIVO}")


def mensagem_resgate():
    mensagem = """SIMULAÇÃO EDUCACIONAL

Este arquivo faz parte de um laboratório controlado
sobre o funcionamento de ransomware.

Nenhum arquivo fora da pasta de testes foi alterado.
"""

    ARQUIVO_RESGATE.write_text(
        mensagem,
        encoding="utf-8"
    )

    print(f"Mensagem criada: {ARQUIVO_RESGATE}")


def menu():
    preparar_ambiente()

    while True:
        print("\n=== RANSOMWARE SIMULADO ===")
        print("1 - Criptografar arquivo de teste")
        print("2 - Descriptografar arquivo de teste")
        print("3 - Criar mensagem de resgate")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criptografar()

        elif opcao == "2":
            descriptografar()

        elif opcao == "3":
            mensagem_resgate()

        elif opcao == "4":
            print("Encerrando.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
