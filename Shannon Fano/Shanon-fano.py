def calcular_probabilidades(arquivo):
    with open(arquivo, 'r') as arquiv:
        texto = arquiv.read()
    frequencias = {}
    total_caracteres = len(texto)

    for caractere in texto:
        if caractere in frequencias:
            frequencias[caractere] += 1
        else:
            frequencias[caractere] = 1

    probabilidades = {simbolo: frequencia / total_caracteres for simbolo, frequencia in frequencias.items()}
    return probabilidades

def comprimir(texto, tabela):
    codigo_comprimido = ""
    for caractere in texto:
        codigo_comprimido += tabela[caractere]
    return codigo_comprimido

def descomprimir(codigo_comprimido, tabela):
    palavra = ""
    codigo_temporario = ""
    for bit in codigo_comprimido:
        codigo_temporario += bit
        for simbolo, codigo in tabela.items():
            if codigo_temporario == codigo:
                palavra += simbolo
                codigo_temporario = ""
                break
    return palavra

def criar_tabela(probabilidades):
    simbolos_ordenados = sorted(probabilidades.keys(), key=lambda simbolo: probabilidades[simbolo], reverse=True)
    tabela = {}

    def construir_tabela(simbolos):
        if len(simbolos) == 1:
            return

        meio = len(simbolos) // 2
        for simbolo in simbolos[:meio]:
            tabela[simbolo] = tabela.get(simbolo, '') + '0'
        for simbolo in simbolos[meio:]:
            tabela[simbolo] = tabela.get(simbolo, '') + '1'

        construir_tabela(simbolos[:meio])
        construir_tabela(simbolos[meio:])

    construir_tabela(simbolos_ordenados)
    return tabela

def comprimir_(arquivo, tabela, codigo):
    with open(arquivo, 'r') as arquivo:
        texto = arquivo.read()

    codigo_comprimido = comprimir(texto, tabela)

    with open(codigo, 'w') as codigo:
        codigo.write(codigo_comprimido)
    
    return codigo_comprimido

    

def descomprimir_(codigo, tabela, arquivo_descomprimido):
    with open(codigo, 'r') as arquivo_c:
        codigo_comprimido = arquivo_c.read()

    palavra = descomprimir(codigo_comprimido, tabela)

    with open(arquivo_descomprimido, 'w') as arquivo_d:
        arquivo_d.write(palavra)

    return palavra

arquivo_original = 'compressao.txt'
probabilidades = calcular_probabilidades(arquivo_original)
tabela = criar_tabela(probabilidades)

#tabela
#print(tabela)

codigo = 'depos_compressao.txt'
codificando = comprimir_(arquivo_original, tabela, codigo)

arquivo_descomprimido = 'antes_compressao.txt'
decodificando = descomprimir_(codigo, tabela, arquivo_descomprimido)

print("Saida codificada", codificando)
print("Saida decodificada", decodificando,)