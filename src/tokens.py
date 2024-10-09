import re


PALAVRAS_CHAVE = { 
    #condicionais
    "se_der": "IF",
    "senão": "ELSE",
    "se_não_der": "ELIF",
    #Controle de Fluxos
    
    #Tratamento de Exceções
    "tenta_aí": "TRY",
    "capturar":"except",
    "finalmente":"finally",
    "lançar":"raise",
    

    #Gerenciamento de Contexto
    "com":"with",
    "como":"as",
    
    #Manipular funções
    "retornar":"return",
    "pausar":"yield",

    #Controle de Loop
    "quebra":"break",
    "seguir":"continue",
    "nada":"pass",

    #Loops de repetição
    "para":"for",
    "enquanto":"while",

    #Declarar função / classe
    "def_tática":"Def",
    "jogada":"lambda",
    "time":"class",

    #Declaração de variáveis e tipos
    "na_midia":"global",
    "gol_true":"True", #booleano
    "gol_false":"False", #booleano
    "sem_pontos":"None",
    "de_fora":"nonlocal",

    #Operador lógico
    "e":"and",
    "ou":"or",
    "não":"not",

    #Operadores de Verificação de Estrutura de Dados
    "tem":"in",
    "é":"is",

    #Módulos e importações
    "contrata":"import",
    "de":"from",

    #Início e fim do código
    "iniciar_partida":"start_codigo",
    "fim_partida":"end_codigo",

    #Outras palavras chaves
    "time_de_reserva": "PUBLIC",
    "time_titular": "PRIVATE",
    "escalação": "LIST",
    "narrar": "PRINT",
    "recebe_passe": "INPUT",
}


TOKENS = [
    (r'#.*', None),  # Comentários
    (r'\b(' + '|'.join(PALAVRAS_CHAVE.keys()) + r')\b', 'PALAVRA_CHAVE'),  # Palavras-chave
    (r'"([^"\\]*(\\.[^"\\]*)*)"', 'STRING'),  # Strings com aspas duplas
    (r"'([^'\\]*(\\.[^'\\]*)*)'", 'STRING'),  # Strings com aspas simples
    (r'\d+\.\d+', 'NUMERO_REAL'),  # Números reais
    (r'\d+', 'NUMERO_INTEIRO'),  # Números inteiros
    (r'==', 'IGUAL'),  # Igualdade
    (r'!=', 'DIFERENTE'),  # Diferença
    (r'>=', 'MAIOR_IGUAL'),  # Maior ou igual
    (r'<=', 'MENOR_IGUAL'),  # Menor ou igual
    (r'>', 'MAIOR'),  # Maior
    (r'<', 'MENOR'),  # Menor
    (r'=', 'OPERADOR_ATRIBUICAO'),  # Atribuição
    (r'~', 'OPERADOR_TIL'),  # Operador til
    (r'[a-zA-Z0-9_ãáâàäçêéíóôõúü]+', 'IDENTIFICADOR'),  # Identificadores
    (r'\[', 'COLCHETE_ESQ'),  # Colchete esquerdo
    (r'\]', 'COLCHETE_DIR'),  # Colchete direito
    (r';', 'PONT_VIRGULA'),  # Ponto e vírgula
    (r',', 'VIRGULA'),  # Vírgula
    (r'\+', 'OPERADOR_SOMA'),  # Adição
    (r'-', 'OPERADOR_SUBTRACAO'),  # Subtração
    (r'\*', 'OPERADOR_MULTIPLICACAO'),  # Multiplicação
    (r'\/', 'OPERADOR_DIVISAO'),  # Divisão
    (r'%', 'OPERADOR_PORCENTAGEM'),  # Porcentagem
    (r'\(', 'PAR_ESQUERDO'),  # Parêntese esquerdo
    (r'\)', 'PAR_DIREITO'),  # Parêntese direito
    (r':', 'DOIS_PONTOS'),  # Dois pontos
    (r'\.', 'PONTO'),  # Ponto
    (r'\s+', None),  # Espaços em branco
]

class Token:
    def __init__(self, tipo, valor, linha):
        self.tipo = tipo       
        self.valor = valor      
        self.linha = linha      

    def __repr__(self):
        
        if self.valor is not None:
            return f"{self.tipo}: {self.valor} (linha: {self.linha})"
        return self.tipo
