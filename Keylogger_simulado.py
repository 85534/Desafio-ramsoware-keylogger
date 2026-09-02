from pathlib import Path

ARQUIVO_LOG = Path("keylogger_simulado.txt")


def iniciar():
    print("=== KEYLOGGER SIMULADO ===")
    print("Laboratório educacional.")
    print()
    print("Digite textos voluntariamente para o teste.")
    print("Digite SAIR para finalizar.")
    print()

    with ARQUIVO_LOG.open("a", encoding="utf-8") as arquivo:

        while True:
            entrada = input("> ")

            if entrada.upper() == "SAIR":
                break

            arquivo.write(entrada + "\n")

    print()
    print(f"Registro de teste salvo em: {ARQUIVO_LOG}")


if __name__ == "__main__":
    iniciar()
