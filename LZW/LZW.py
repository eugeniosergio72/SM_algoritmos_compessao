class LZW:
    def __init__(self):
        self.tabela = dict()
        self.lista = []

    def compressao(self, string):
        for i in range(256):
            self.tabela[chr(i)] = i
        actual = ''
        proximo_codigo = 257

        for i in string:
            actual += i
            if actual not in self.tabela:
                self.tabela[actual] = proximo_codigo
                proximo_codigo += 1
                actual = actual[:-1]
                self.lista.append(self.tabela[actual])
                actual = i
        self.lista.append(self.tabela[actual])

        return self.lista

    def decompressao(self):
        tabela = dict()
        for i in range(256):
            tabela[i] = chr(i)

        palavra = ''
        proximo_codigo = 257
        ans = ''
        for i in self.lista:
            ans += tabela[i]
            if palavra != '':
                tabela[proximo_codigo] = palavra + tabela[i][0]
                proximo_codigo += 1
            palavra = tabela[i]
        return ans


if __name__ == '__main__':
    lzw = LZW()


    """ Testando """
    f = open("compressao.txt", "r")
    dados = f.read()

    compresao = lzw.compressao(dados)

    print("Saida codificada: ", compresao)

    descompresao = lzw.decompressao()

    print(lzw.decompressao())

    with open('descompressao.txt', 'w') as arquivo:
        for v in descompresao:
            arquivo.write(str(v))
