#Carlos Eduardo Rodrigues Mello
#O programa que você desenvolverá irá receber como entrada um arquivo de texto (.txt)contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadasem um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadassegundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número deoperações que estão descritas no arquivo, este número de operações será um inteiro; as linhasseguintes seguirão sempre o mesmo padrão de três linhas: a primeira linha apresenta o código daoperação (U para união, I para interseção, D para diferença e C produto cartesiano), a segunda eterceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplodas linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver: 4;U;3, 5, 67, 7;1, 2, 3, 4;I;1, 2, 3, 4, 5;4, 5;D;1, A, C, 34;A, C, D, 23;C;3, 4, 5, 5, A, B, R;1, B, C, D, 1;Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e umproduto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑, 𝟓, 𝟔𝟕, 𝟕} e {𝟏, 𝟐, 𝟑, 𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dadosdos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá contera informação e a formatação mostrada a seguir:União: conjunto 1 {3, 5, 67, 7}, conjunto 2 {1, 2, 3, 4}. Resultado: {3, 5, 67, 7, 1, 2, 4}Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquerum dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivode textos de entrada formatada segundo o exemplo de saída acima. Observe as letras maiúsculas eminúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.No caso do texto de exemplo, teremos 4 linhas, e apenas 4 linhas de saída, formatadas epontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entradacontendo um número diferente de operações, operações com dados diferentes, e operações em ordem diferentes. Os arquivos de entrada criados para os seus testes devem estar disponíveis tanto noambiente repl.it quanto no ambiente Github.Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,no mínimo um arquivo de testes criado pelo próprio professor.
#Mude o arquivo aqui em arquivotxt
arquivotxt = open("texto.txt", 'r')
numerodeoperações = int(arquivotxt.readline(1))
contador = 0

def União(con1, con2):
    c1 = con1
    c2 = con2
    for i in c1:
        if i not in conjunto1:
            conjunto1.append(i)
    for j in c2:
        if j not in conjunto2:
            conjunto2.append(j)
    print("conjunto 1 {",', '.join(map(str, conjunto1)),"}, ",end='',sep="")
    print("conjunto 2 {",', '.join(map(str, conjunto2)),"}.",end=' ',sep="")
    resultado = conjunto1
    for i in conjunto2:
        if i not in conjunto1:
            resultado.append(i)
    print('Resultado: {', ', '.join(map(str, resultado)), '}', sep="")
  
def Interseção(con1, con2):
    c1 = con1
    c2 = con2
    for i in c1:
        if i not in conjunto1:
            conjunto1.append(i)
    for j in c2:
        if j not in conjunto2:
            conjunto2.append(j)
    print("conjunto 1 {",', '.join(map(str, conjunto1)),"}, ",end='',sep="")
    print("conjunto 2 {",', '.join(map(str, conjunto2)),"}.",end=' ',sep="")
    for i in conjunto1:
        for j in conjunto2:
            if i == j:
                resultado.append(i)
    print('Resultado: {', ', '.join(map(str, resultado)), '}', sep="")

def Diferença(con1, con2):
    c1 = con1
    c2 = con2
    for i in c1:
        if i not in conjunto1:
            conjunto1.append(i)
    for j in c2:
        if j not in conjunto2:
            conjunto2.append(j)
    print("conjunto 1 {",', '.join(map(str, conjunto1)),"}, ",end='',sep="")
    print("conjunto 2 {",', '.join(map(str, conjunto2)),"}.",end=' ',sep="")
    for i in conjunto1:
        if i not in conjunto2:
            resultado.append(i)
    print('Resultado: {', ', '.join(map(str, resultado)), '}', sep="")
  
def Cartesiano(con1, con2):
    c1 = con1
    c2 = con2
    for i in c1:
        if i not in conjunto1:
            conjunto1.append(i)
    for j in c2:
        if j not in conjunto2:
            conjunto2.append(j)
    print("conjunto 1 {",', '.join(map(str, conjunto1)),"}, ",end='',sep="")
    print("conjunto 2 {",', '.join(map(str, conjunto2)),"}.",end=' ',sep="")
    print("Resultado: {", end='')
    for i in conjunto1:
        for j in conjunto2:
            print('(', i, ', ', sep="", end='')
            if i == conjunto1[-1] and j == conjunto2[-1]:
                print(j, ')', sep="", end='')
            else:
                print(j, '), ', sep="", end='')
    print('}')
  
for line in arquivotxt:
    c1 = []
    c2 = []
    conjunto1 = []
    conjunto2 = []
    resultado = []
    if contador < numerodeoperações:
        if line.startswith("U"):
            print('União: ', end='')
            con1 = arquivotxt.readline().replace(',', '').split()
            con2 = arquivotxt.readline().replace(',', '').split()
            União(con1, con2)
            contador += 1
        elif line.startswith("I"):
            print('Interseção: ', end='')
            con1 = arquivotxt.readline().replace(',', '').split()
            con2 = arquivotxt.readline().replace(',', '').split()
            Interseção(con1, con2)
            contador += 1
        elif line.startswith("D"):
            print('Diferença: ', end='')
            con1 = arquivotxt.readline().replace(',', '').split()
            con2 = arquivotxt.readline().replace(',', '').split()
            Diferença(con1, con2)
            contador += 1
        elif line.startswith("C"):
            print('Produto Cartesiano: ', end='')
            con1 = arquivotxt.readline().replace(',', '').split()
            con2 = arquivotxt.readline().replace(',', '').split()
            Cartesiano(con1, con2)
            contador += 1
else:
    0
arquivotxt.close()
