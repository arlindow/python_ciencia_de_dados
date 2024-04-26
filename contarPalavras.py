#Este algoritmo tem como objetivo contar a frequência de cada palavra em um 
# arquivo de texto especificado.

#inicia um dicionário
word_counts = {}

# Especifique o caminho completo para o arquivo
caminho_arquivo = r"C:\DevSecOps\referencial_teorico\blocoDeNotas\Python\python_nmap.txt"

# Abra o arquivo e leia seu conteúdo
with open(caminho_arquivo, 'r') as arquivo:
    # Itere sobre cada linha do arquivo
    for linha in arquivo:
        # Divida a linha em palavras
        for palavra in linha.split():
            # Verifique se a palavra já está no dicionário de contagem de palavras
            if palavra in word_counts:
                # Se sim, incremente o contador para essa palavra
                word_counts[palavra] += 1
            else:
                # Se não, adicione a palavra ao dicionário com contador 1
                word_counts[palavra] = 1
                
# Imprima o dicionário de contagem de palavras
print(word_counts)

                

 













    


