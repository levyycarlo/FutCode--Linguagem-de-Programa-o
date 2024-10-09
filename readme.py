# FutCode - Linguagem de Programação Temática de Futebol
# Autor - Levy Carlo

#FutCode é uma linguagem de programação personalizada inspirada no futebol, criada para tornar o aprendizado de programação mais divertido e acessível, especialmente para fãs do esporte. A sintaxe da linguagem utiliza termos relacionados ao futebol, proporcionando uma maneira envolvente de aprender conceitos de programação. Este projeto inclui um analisador léxico (lexer) que lê um arquivo `.txt` contendo código FutCode, tokeniza e gera a saída com os tokens identificados em outro arquivo '.txt' dentro da pasta '/output'.

# Como rodar o projeto:

#1. Coloque o código FutCode em um arquivo `.txt` dentro da pasta `/input`.

#2. No terminal, execute o seguinte comando:

#python src/main.py input/nome_do_arquivo.txt

#ou 

#cd src

#python main.py ..\input\nome_do_arquivo.txt

#Exemplo de Código:
#RETIRE OS '#'

#iniciar_partida

#def_tática verificar_gol(time, gols):
#    se_der gols > 0:
#        narrar f"{time} marcou {gols} gols!"
#    senão:
#        narrar f"{time} não marcou nenhum gol."


#def_tática partida_futebol():
#    time1 = "Time A"
#    time2 = "Time B"

#    narrar "Início da partida!"

    
#    gols_time1 = recebe_passe("Quantos gols o Time A marcou?")
#    gols_time2 = recebe_passe("Quantos gols o Time B marcou?")

#    verificar_gol(time1, int(gols_time1))
#    verificar_gol(time2, int(gols_time2))

    
#    se_der int(gols_time1) > int(gols_time2):
#        narrar f"{time1} venceu!"
#    se_não_der int(gols_time2) > int(gols_time1):
#       narrar f"{time2} venceu!"
#    senão:
#        narrar "A partida terminou empatada!"


#partida_futebol()

#fim_partida






