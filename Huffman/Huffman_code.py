# Nodo da arvore de Huffman
class Nodo:
    def __init__(self, prob, simbolo, esquerda=None, direita=None):
        # probabilidade do simbolo
        self.prob = prob
        # simbolo
        self.simbolo = simbolo
        # nodo a esquerda
        self.esquerda = esquerda
        # nodo a direita
        self.direita = direita
        # direccao da arvore (0/1)
        self.codigo = ''

""" Funcao para a imprimir os simbolos dos codigos da arvore de Huffman"""
codigos = dict()

def calculo_codigos(nodo, val=''):
    # codigo de huffman para nodo actual 
    novo_valor = val + str(nodo.codigo)

    if (nodo.esquerda):
        calculo_codigos(nodo.esquerda, novo_valor)
    if (nodo.direita):
        calculo_codigos(nodo.direita, novo_valor)

    if (not nodo.esquerda and not nodo.direita):
        codigos[nodo.simbolo] = novo_valor

    return codigos

""" Funcao para calcular a probabilidade dos simbolos dados na entrada"""

def calculo_probabilidade(dados):
    simbolos = dict()
    for elemento in dados:
        if simbolos.get(elemento) == None:
            simbolos[elemento] = 1
        else:
            simbolos[elemento] += 1
    return simbolos

""" Funcao para obter a saida codificada"""

def saida_codificada(dados, codificando):
    codificando_saida = []
    for c in dados:
        codificando_saida.append(codificando[c])

    string = ''.join([str(item) for item in codificando_saida])
    return string

""" Funcao para calcular o espaco dos dados antes e depos da compressao"""

def total_obtido(dados, codificando):
    antes_compressao = len(dados) * 8  # quantidade total de bits para armazenamento antes da compressao
    depos_compressao = 0
    simbolos = codificando.keys()
    for simbolo in simbolos:
        count = dados.count(simbolo)
        depos_compressao += count * len(codificando[simbolo])  # calculando quantidade dde bits necessaria para cada simbolo
    #Mostrando espaco usado antes da compressao
    #print("Espaco usado antes da compressao (bits):", antes_compressao)
    #Mostrando espaco usado depois da compressao
    #print("Espaco usado depois da compressao (bits):", depos_compressao)

def Codificacao_Huffman(dados):
    simbolo_com_probabliidade = calculo_probabilidade(dados)
    simbolos = simbolo_com_probabliidade.keys()
    probabilidades = simbolo_com_probabliidade.values()
    #Mostrando os simbolos
    #print("simbolos: ", simbolos)
    #Mostrando as probabilidades
    #print("probabilidades: ", probabilidades)

    nodos = []

    # Convertendo os simbolos e a probabilidade no nodo da arvore de Huffman 
    for simbolo in simbolos:
        nodos.append(Nodo(simbolo_com_probabliidade.get(simbolo), simbolo))

    while len(nodos) > 1:
        # Organizando todos os nodos em ordem crescente e sua probabilidade
        #nodos = sorted(nodos, key=lambda x: x.prob)
        # for nodo in nodos:
        #      print(nodo.simbolo, nodo.prob)

        # escolhendo os 2 menores nodos
        direita = nodos[0]
        esquerda = nodos[1]

        esquerda.codigo = 0
        direita.codigo = 1

        # combine the 2 smallest nodos to create new nodo
        novo_nodo = Nodo(esquerda.prob + direita.prob, esquerda.simbolo + direita.simbolo, esquerda, direita)

        nodos.remove(esquerda)
        nodos.remove(direita)
        nodos.append(novo_nodo)

    Codificacao_Huffman = calculo_codigos(nodos[0])
    #Mostrando os simbolos com seus codigos
    #print("simbolos com codigos", Codificacao_Huffman)
    total_obtido(dados, Codificacao_Huffman)
    saida_codifica_retorno = saida_codificada(dados, Codificacao_Huffman)
    return saida_codifica_retorno, nodos[0]

def Decodificacao_Huffman(dados_codificados, arvore_huffman):
    root_arvore = arvore_huffman
    saida_decodificada = []
    for x in dados_codificados:
        if x == '1':
            arvore_huffman = arvore_huffman.direita
        elif x == '0':
            arvore_huffman = arvore_huffman.esquerda
        try:
            if arvore_huffman.esquerda.simbolo == None and arvore_huffman.direita.simbolo == None:
                pass
        except AttributeError:
            saida_decodificada.append(arvore_huffman.simbolo)
            arvore_huffman = root_arvore

    string = ''.join([str(item) for item in saida_decodificada])
    return string

""" Testando """
f = open("compressao.txt", "r")
dados = f.read()
codificando, arvore = Codificacao_Huffman(dados)
print("Saida codificada", codificando)
print("Saida decodificada", Decodificacao_Huffman(codificando, arvore))

descomprimido = Decodificacao_Huffman(codificando, arvore)

with open('descompressao.txt', 'w') as arquivo:
    for v in descomprimido:
        arquivo.write(str(v))
