import sys
import os
from lexer import Lexer

def imprimir_cabecalho():
    return "| %-15s | %-25s | %-5s |" % ("Lexema", "Token", "Linha")

def imprimir_token(token):
    return "| %-15s | %-20s | %-5d |" % (token.valor.ljust(15), token.tipo.ljust(20), token.linha)

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py <nome_do_arquivo>")
        return

    nome_arquivo = sys.argv[1]
    nome_arquivo = os.path.abspath(nome_arquivo)

   
    nome_saida = os.path.join("..", "output", "resultado.txt")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            texto = arquivo.read()
            lexer = Lexer(texto)
            tokens = lexer.obter_tokens()

            
            print(imprimir_cabecalho())
            
            with open(nome_saida, 'w', encoding='utf-8') as arquivo_saida:
                
                arquivo_saida.write(imprimir_cabecalho() + '\n')
                for token in tokens:
                    
                    linha_token = imprimir_token(token)
                    print(linha_token)
                    arquivo_saida.write(linha_token + '\n')

            print(f"Tokens gravados em: {nome_saida}")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
