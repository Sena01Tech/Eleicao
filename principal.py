# Autor: Luiz Felipe Santana Sena
# Componente Curricular: EXA 854 - MI - Algoritmos
# Concluido em: 13/06/2023
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.


# teste entrada somente com menor
def tratamentoStringNome():
    while True:
        try:
            recebo = input('Digite seu nome:')
            recebo = recebo.title()
            if recebo[0] == 'A' or recebo[0] == 'B' or recebo[0] == 'C' or recebo[0] == 'D' or recebo[0] == 'E' or recebo[0] == 'F' or recebo[0] == 'G' or recebo[0] == 'H' or recebo[0] == 'I' or recebo[0] == 'J' or recebo[0] == 'K' or recebo[0] == 'L' or recebo[0] == 'M' or recebo[0] == 'N' or recebo[0] == 'O' or recebo[0] == 'P' or recebo[0] == 'Q' or recebo[0] == 'R' or recebo[0] == 'S' or recebo[0] == 'T' or recebo[0] == 'U' or recebo[0] == 'V' or recebo[0] == 'W' or recebo[0] == 'X' or recebo[0] == 'Y' or recebo[0] == 'Z':
                print('Nome Valido !')
                return recebo
            else:
               print('Há algo de errado com seu nome, por favor digite novamente ') 
        except:
            print('Nome invalido !')
# teste entrada com maior e meor mas sem mensagem
def tratamentoMaiorMenor(teste_Menor, teste_Maior):
    while True:
        try:
            teste = int(input('digite:'))
            if teste >= teste_Menor and teste <= teste_Maior:
                print('Numero valido ! :)')
                return teste
            else:
                print('Numero invaido ! :(')
                print('O numero deve estar entre', teste_Menor,'e', teste_Maior)
        except ValueError:
            print('Caractere/numero invalido !')
            print('Deve ser um numero e ele deve estar entre', teste_Menor,'e', teste_Maior)

# ?
def VotoRegistro(escolhaprof):
    while True:
        voto = input('Digite qual o nome da chapa em que você deseja votar! \nSe deseja votar Nulo/Branco, digite "Nulo"')
        voto = voto.title()
        if voto == "Nulo":
            with open('VotantesP3.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[1] = int(nulos1[1])
                nulos1[1] += 1
                nulos1[1] = str(nulos1[1])
                nulos1[11] = int(nulos1[11])
                nulos1[11] += 1
                nulos1[11] = str(nulos1[11])
            with open('VotantesP3.txt','w') as file:
                for nulos2 in nulos1:
                    file.write('%s \n' %(nulos2))
            votou = 1
            if dia == 1:
                if escolhaprof == 0:
                    with open('VotosPrimeiro.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[9] = int(nulos1[9])
                        nulos1[9] += 1
                        nulos1[9] = str(nulos1[9])
                    with open('VotosPrimeiro.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
                elif escolhaprof == 1:
                    with open('VotosPrimeiro.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[11] = int(nulos1[11])
                        nulos1[11] += 1
                        nulos1[11] = str(nulos1[11])
                    with open('VotosPrimeiro.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
                elif escolhaprof == 2:
                    with open('VotosPrimeiro.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[13] = int(nulos1[13])
                        nulos1[13] += 1
                        nulos1[13] = str(nulos1[13])
                    with open('VotosPrimeiro.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
            if dia == 2:
                if escolhaprof == 0:
                    with open('VotosSegundo.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[9] = int(nulos1[9])
                        nulos1[9] += 1
                        nulos1[9] = str(nulos1[9])
                    with open('VotosSegundo.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
                elif escolhaprof == 1:
                    with open('VotosSegundo.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[11] = int(nulos1[11])
                        nulos1[11] += 1
                        nulos1[11] = str(nulos1[11])
                    with open('VotosSegundo.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
                elif escolhaprof == 2:
                    with open('VotosSegundo.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[13] = int(nulos1[13])
                        nulos1[13] += 1
                        nulos1[13] = str(nulos1[13])
                    with open('VotosSegundo.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
            if dia == 3:
                if escolhaprof == 0:
                    with open('VotosTerceiro.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[9] = int(nulos1[9])
                        nulos1[9] += 1
                        nulos1[9] = str(nulos1[9])
                    with open('VotosTerceiro.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
                elif escolhaprof == 1:
                    with open('VotosTerceiro.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[11] = int(nulos1[11])
                        nulos1[11] += 1
                        nulos1[11] = str(nulos1[11])
                    with open('VotosTerceiro.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
                elif escolhaprof == 2:
                    with open('VotosTerceiro.txt','r') as file:
                        nulos = file.readlines()
                        nulos1 = [item.rstrip('\n') for item in nulos]
                        nulos1[13] = int(nulos1[13])
                        nulos1[13] += 1
                        nulos1[13] = str(nulos1[13])
                    with open('VotosTerceiro.txt','w') as file:
                        for nulos2 in nulos1:
                            file.write('%s \n' %(nulos2))
            print('\n')
            print('Seu voto foi salvo')
            break

        with open('Concorre.txt','r') as file:
            concorrentes1 = file.readlines()
            concorrentes2 = [item.rstrip('\n') for item in concorrentes1]
            contd3 = 0
            votou = 0
            for concorre in concorrentes2:
                if concorre.startswith(voto):
                    if escolhaprof == 0:
                        concorrentes2[contd3 + 1] = int(concorrentes2[contd3 + 1])
                        concorrentes2[contd3 + 1] += 1
                        concorrentes2[contd3 + 1] = str(concorrentes2[contd3 + 1])
                    elif escolhaprof == 1:
                        concorrentes2[contd3 + 2] = int(concorrentes2[contd3 + 2])
                        concorrentes2[contd3 + 2] += 1
                        concorrentes2[contd3 + 2] = str(concorrentes2[contd3 + 2])
                    elif escolhaprof == 2:
                        concorrentes2[contd3 + 3] = int(concorrentes2[contd3 + 3])
                        concorrentes2[contd3 + 3] += 1
                        concorrentes2[contd3 + 3] = str(concorrentes2[contd3 + 3])
                    votou = 1
                contd3 += 1
        with open('Concorre.txt','w') as file:
            for concorre in concorrentes2:
                file.write('%s \n' %(concorre))
        if votou == 1:
            with open('VotantesP3.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[11] = int(nulos1[11])
                nulos1[11] += 1
                nulos1[11] = str(nulos1[11])
            with open('VotantesP3.txt','w') as file:
                for nulos2 in nulos1:
                    file.write('%s \n' %(nulos2))
            print('\n')
            print('Seu voto foi salvo')
            break
        else:
            print('Seu voto não foi salvo por algum erro, por favor, vote novamente da maneira correta!') 

# codigo principal
continuador = 0
dia = 0
while continuador == 0:
    print('\n')
    print('Para começar a votação deste dia digite 0')
    print('Para cadastrar uma nova chapa digite 1')
    print('Para remover uma chapa digite 2')
    print('Para mudar o nome do candidato digite 3')
    print('Para digitar o numero total de pessoas que vão votar digite 4')
    print('OBS: após inicio das votações, não será possivel remover chapas e/ou cadastrar nova chapa!')
    print('\n')
    escolha = tratamentoMaiorMenor(0, 4)
# verifica se a existencia de chapas para receberem votos
    if escolha == 0:
        a = int(input('A fins de confirmações. Se deseja mesmo encerrar as edições, tecle 0 novamente e aperte enter !'))
        if a == 0:
            with open('VotosTerceiro.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[2] = int(nulos1[2])
                nulos1[4] = int(nulos1[4])
                nulos1[6] = int(nulos1[6])
                if nulos1[6] == 0 and nulos1[4] == 0 and nulos1[2] == 0:
                    dia = 3
            with open('VotosSegundo.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[2] = int(nulos1[2])
                nulos1[4] = int(nulos1[4])
                nulos1[6] = int(nulos1[6])
                if nulos1[6] == 0 and nulos1[4] == 0 and nulos1[2] == 0:
                    dia = 2
            with open('VotosPrimeiro.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[2] = int(nulos1[2])
                nulos1[4] = int(nulos1[4])
                nulos1[6] = int(nulos1[6])
                if nulos1[6] == 0 and nulos1[4] == 0 and nulos1[2] == 0:
                    dia = 1
            with open('Chapas.txt', 'r') as file:
                testeexiste = file.readline()
            if testeexiste and dia == 1:
                continuador = 1
                with open('Chapas.txt', 'r') as file:
                    concorrentes = file.readlines()
                    chapas = []
                    contd1 = 0
                    for concorrente in concorrentes:
                        if contd1%4 == 0:
                            chapas.append(concorrente)
                            chapas.append('0 \n')
                            chapas.append('0 \n')
                            chapas.append('0 \n')
                        contd1 += 1
                with open('Concorre.txt', 'w') as file:
                    for chapa in chapas:
                        file.write(chapa)
            if testeexiste:
                continuador = 1
            else:
                print('Você não pode começar a eleição sem candidatos, faça um cadastramento de chapas!')
                print('\n')
                
    elif escolha == 1:
        # No arquivo, cada chapa ocupa 3 linhas, 1º para nome da chapa, 2º para nome do reitor e 3º para nome do vice reitor, sendo a 4º aquantidade de votos que a chapa possui
        print('\n')
        with open('VotantesP3.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[11] = int(nulos1[11])
        if nulos1[11] > 0:
            print('Você não pode cadastrar nova chapa após o inicio das eleições')
        else:       
            chapa = input('Digite o nome da chapa:')
            nome_reitor = input('Digite o nome do Reitor adicionado nessa chapa:')
            nome_vice = input('Digite o nome do Vice-reitor dessa chapa:')
            with open('Chapas.txt','a') as file:
                file.write('%s \n' % (chapa.title()))
                file.write('%s \n' % (nome_reitor.title()))
                file.write('%s \n' % (nome_vice.title()))
                file.write('\n')

    elif escolha == 2:
        print('\n')
        removeu = 0
        nome_removida = input('Digite o nome da chapa que vai ser removida:')
        nome_removida = nome_removida.title()
        with open('Chapas.txt','r') as file:
            lista1 = file.readlines()
            contador = 0
            for nome in lista1:
                if nome.startswith(nome_removida):
                    for i in range(4):
                        lista1.pop(contador)
                    removeu = 1
                contador += 1
        
        with open('Chapas.txt','w') as file:
            for nome_1 in lista1:
                file.write(nome_1)
        if removeu == 1:
            print('Chapa removida com sucesso!')
        else:
            print('Chapa não removida, porque não foi possivel encontra-la')

    elif escolha == 3:
        print('\n')
        with open('VotantesP3.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[11] = int(nulos1[11])
        if nulos1[11] > 0:
            print('Você não pode mudar o nome de um candidato após o inicio das eleições')
        else: 
            nome = input('Digite o nome completo do candidato que vai ser trocado:')
            nome = nome.title()
            achou = 0
            contnome = 0
            with open('Chapas.txt','r') as file:
                listaalnome = file.readlines()
                for testenome in listaalnome:
                    if testenome.startswith(nome):
                        nomenovo = input('Digite o nome da nova pessoa que vai entrar no lugar de %s:' %nome)
                        nomenovo = nomenovo.title()
                        listaalnome[contnome] = ('%s \n' %nomenovo)
                        achou = 1
                    contnome += 1
            if achou == 0:
                print('nome invalido')
            with open('Chapas.txt','w') as file:
                for testenome in listaalnome:
                    file.write(testenome)

    elif escolha == 4:
        # Número total de votantes;
        print('\n')
        with open('VotantesP3.txt','r') as file:
                nulos = file.readlines()
                nulos1 = [item.rstrip('\n') for item in nulos]
                nulos1[11] = int(nulos1[11])
        if nulos1[11] > 0:
            print('Você não pode mudar o numero de pessoas que vão votar após o inicio das eleições')
        else: 
            ntsd = int(input('Digite o valor número total de servidores docentes votantes:'))
            ntst = int(input('Digite o valor número total de servidores técnicos votantes:'))
            ntd = int(input('Digite o valor número total de discentes votantes:'))
            with open('Estipulado.txt','w') as file:
                file.write('Número total de servidores docentes votantes: \n')
                file.write('%d \n' % ntsd)
                file.write('Número total de servidores técnicos votantes: \n')
                file.write('%d \n' % ntst)
                file.write('Número total de discentes votantes: \n')
                file.write('%d \n' % ntd)
with open('Estipulado.txt','r') as file:
    estipula = file.readlines()
    estipulado = [item.rstrip('\n') for item in estipula]
    estipulado[1] = int(estipulado[1])
    estipulado[3] = int(estipulado[3])
    estipulado[5] = int(estipulado[5])
    ntsd = estipulado[1]
    ntst = estipulado[3]
    ntd = estipulado[5]

print('Dia de votação %d' % dia)

votacao = 0 
while votacao == 0:
    print('\n')
    print('menu:')
    print('Digite 0 se você for Docente')
    print('Digite 1 se você for Servidores Técnico-administrativos')
    print('Digite 2 se você for Discentes')
    print('Digite 3 para encerrar as votações de hoje')
    escolhaprof = tratamentoMaiorMenor(0, 3)
    if escolhaprof != 3:
        nome_votando = tratamentoStringNome()
    with open('VotantesP3.txt','r') as file:
            votantesP = file.readlines()
            votantes = [item.rstrip('\n') for item in votantesP]
    if escolhaprof == 3:
        votacao = int(input('A fins de confirmações. Se deseja mesmo encerrar as edições, tecle 3 novamente e aperte enter, caso contrario digite qualquer numero!'))
        if votacao == 3 and dia == 3:
            print('A votação foi encerrada por completa, a seguir, o resultado!')
            with open('Estipulado.txt','r') as file:
                estipula = file.readlines()
                estipulado = [item.rstrip('\n') for item in estipula]
                estipulado[1] = int(estipulado[1])
                estipulado[3] = int(estipulado[3])
                estipulado[5] = int(estipulado[5])
                ntsd = estipulado[1]
                ntst = estipulado[3]
                ntd = estipulado[5]
            with open('VotosPrimeiro.txt','r') as file:
                mostrar = file.readlines()
                mostrar1 = [item.rstrip('\n') for item in mostrar]
                print('\n')
                print('Número total de servidores Docentes votantes no primeiro dia : %s' %(mostrar1[2]))
                print('Número total de servidores Tecnicos votantes no primeiro dia : %s' %(mostrar1[4]))
                print('Número total Discentes votantes no primeiro dia : %s' %(mostrar1[6]))
                print('Número total de servidores Docentes que votaram branco no primeiro dia : %s' %(mostrar1[9]))
                print('Número total de servidores Tecnicos que votaram branco no primeiro dia : %s' %(mostrar1[11]))
                print('Número total Discentes votantes que votaram branco no primeiro dia : %s' %(mostrar1[13]))
            with open('VotosSegundo.txt','r') as file:
                mostrar = file.readlines()
                mostrar2 = [item.rstrip('\n') for item in mostrar]
                print('\n')
                print('Número total de servidores Docentes votantes no Segundo dia : %s' %(mostrar2[2]))
                print('Número total de servidores Tecnicos votantes no Segundo dia : %s' %(mostrar2[4]))
                print('Número total Discentes votantes no Segundo dia : %s' %(mostrar2[6]))
                print('Número total de servidores Docentes que votaram branco no Segundo dia : %s' %(mostrar2[9]))
                print('Número total de servidores Tecnicos que votaram branco no Segundo dia : %s' %(mostrar2[11]))
                print('Número total Discentes votantes que votaram branco no Segundo dia : %s' %(mostrar2[13]))
            with open('VotosTerceiro.txt','r') as file:
                mostrar = file.readlines()
                mostrar3 = [item.rstrip('\n') for item in mostrar]
                print('\n')
                print('Número total de servidores Docentes votantes no Terceiro dia : %s' %(mostrar3[2]))
                print('Número total de servidores Tecnicos votantes no Terceiro dia : %s' %(mostrar3[4]))
                print('Número total Discentes votantes no Terceiro dia : %s' %(mostrar3[6]))
                print('Número total de servidores Docentes que votaram branco no Terceiro dia : %s' %(mostrar3[9]))
                print('Número total de servidores Tecnicos que votaram branco no Terceiro dia : %s' %(mostrar3[11]))
                print('Número total Discentes votantes que votaram branco no Terceiro dia : %s' %(mostrar3[13]))
            with open('VotantesP3.txt','r') as file:
                mostrar = file.readlines()
                mostrar4 = [item.rstrip('\n') for item in mostrar]
                print('\n') 
                print('Número total de votos Nulo/Branco : %s' %(mostrar4[1]))
                print('Número total de votos : %s' %(mostrar4[11]))
                print('Número total vostos urna 1 modulo 1 : %s' %(mostrar4[3]))
                print('Número total vostos urna 2 modulo 3 : %s' %(mostrar4[5]))
                print('Número total vostos urna 3 modulo 5 : %s' %(mostrar4[7]))
                print('Número total vostos urna 4 modulo 7 : %s' %(mostrar4[9]))
            with open('Concorre.txt','r') as file:
                mostrar = file.readlines()
                mostrar5 = [item.rstrip('\n') for item in mostrar]
                ntsd_ = 0
                ntst_ = 0
                ntd_ = 0
                for i in range(len(mostrar5)):
                    if i%4 == 0:
                        print('Chapa : %s' % mostrar5[i])
                    elif i%4 == 1:
                        print('Número de votos dos Servidores Docentes na chapa %s : %s' % (mostrar5[i-1], mostrar5[i]))
                        ntsd_ += int(mostrar5[i])
                    elif i%4 == 2:
                        print('Número de votos dos Servidores Tecnicos na chapa %s : %s' % (mostrar5[i-2], mostrar5[i]))
                        ntst_ += int(mostrar5[i])
                    elif i%4 == 3:
                        print('Número de votos dos Discentes na chapa %s : %s' % (mostrar5[i-3], mostrar5[i]))
                        ntd_ += int(mostrar5[i])
                print('Porcentagem de ausencia de Servidores Doscentes votantes: %s' %(1-(ntsd_ / ntsd)))
                print('Porcentagem de ausencia de Servidores Tecnicos votantes: %s' %(1-(ntsd_ / ntsd)))
                print('Porcentagem de ausencia de Discentes votantes: %s' %(1-(ntd_ /ntd)))
                listaescore1 = []
                listaescore2 = []
                for i in range(len(mostrar5)):
                    if i%4 == 0:
                        listaescore1.append(mostrar5[i])
                        mostrar4[11] = int(mostrar4[11])
                        escore = ((int(mostrar5[i+1])/ntsd)*(1/3))+((int(mostrar5[i+2])/ntst)*(1/3))+(((int(mostrar5[i+3])/ntd)*(1/3)))*mostrar4[11]
                        listaescore2.append(escore)
                for i in range(len(listaescore1)):
                    print('Chapa %s possui um escore de : %f'%(listaescore1[i],listaescore2[i]))
                maior = max(listaescore2)
                indice = listaescore2.index(maior)
                testeempate = 0
                for i in range(indice + 1, len(listaescore2)):
                    if listaescore2[i] == maior:
                        testeempate = 1
                if testeempate == 1:
                    print('Nenhuma chapa ganhou! Foi empatado')
                elif testeempate == 0:
                    print('A chapa vencedora foi %s' %listaescore1[indice])
                    print('')
                    print('')
                break
        elif votacao != 3:
            votacao = 0

    elif nome_votando[0] == 'A' or nome_votando[0] == 'B' or nome_votando[0] == 'C' or nome_votando[0] == 'D':
        print('\n')
        print('Você está na urna do Modulo 1')
        if dia == 1:
            print('Você está no primeiro dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 2:
            print('Você está no segundo dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 3: 
            print('Você está no terceiro dia de votação')
            VotoRegistro(escolhaprof)
        with open('VotantesP3.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[3] = int(nulos1[3])
            nulos1[3] += 1
            nulos1[3] = str(nulos1[3])
        with open('VotantesP3.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif nome_votando[0] == 'E' or nome_votando[0] == 'F' or nome_votando[0] == 'G' or nome_votando[0] == 'H' or nome_votando[0] == 'I' or nome_votando[0] == 'J':
        print('\n')
        print('Você está na urna do Modulo 3')
        if dia ==1:
            print('Você está no primeiro dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 2:
            print('Você está no segundo dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 3: 
            print('Você está no terceiro dia de votação')
            VotoRegistro(escolhaprof)

        with open('VotantesP3.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[5] = int(nulos1[5])
            nulos1[5] += 1
            nulos1[5] = str(nulos1[5])
        with open('VotantesP3.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif nome_votando[0] == 'K' or nome_votando[0] == 'L' or nome_votando[0] == 'M' or nome_votando[0] == 'N' or nome_votando[0] == 'O':
        print('\n')       
        print('Você está na urna do Modulo 5')
        if dia ==1:
            print('Você está no primeiro dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 2:
            print('Você está no segundo dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 3: 
            print('Você está no terceiro dia de votação')
            VotoRegistro(escolhaprof)

        with open('VotantesP3.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[7] = int(nulos1[7])
            nulos1[7] += 1
            nulos1[7] = str(nulos1[7])
        with open('VotantesP3.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif nome_votando[0] == 'P' or nome_votando[0] == 'Q' or nome_votando[0] == 'R' or nome_votando[0] == 'S' or nome_votando[0] == 'T' or nome_votando[0] == 'U' or nome_votando[0] == 'V' or nome_votando[0] == 'W' or nome_votando[0] == 'X' or nome_votando[0] == 'Y' or nome_votando[0] == 'Z':
        print('\n')
        print('Você está na urna do Modulo 7')
        if dia ==1:
            print('Você está no primeiro dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 2:
            print('Você está no segundo dia de votação')
            VotoRegistro(escolhaprof)
        elif dia == 3: 
            print('Você está no terceiro dia de votação')
            VotoRegistro(escolhaprof)

        with open('VotantesP3.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[9] = int(nulos1[9])
            nulos1[9] += 1
            nulos1[9] = str(nulos1[9])
        with open('VotantesP3.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    if dia == 1 and escolhaprof == 0:
        with open('VotosPrimeiro.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[2] = int(nulos1[2])
            nulos1[2] += 1
            nulos1[2] = str(nulos1[2])
        with open('VotosPrimeiro.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 1 and escolhaprof == 1:
        with open('VotosPrimeiro.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[4] = int(nulos1[4])
            nulos1[4] += 1
            nulos1[4] = str(nulos1[4])
        with open('VotosPrimeiro.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 1 and escolhaprof == 2:
        with open('VotosPrimeiro.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[6] = int(nulos1[6])
            nulos1[6] += 1
            nulos1[6] = str(nulos1[6])
        with open('VotosPrimeiro.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 2 and escolhaprof == 0:
        with open('VotosSegundo.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[2] = int(nulos1[2])
            nulos1[2] += 1
            nulos1[2] = str(nulos1[2])
        with open('VotosSegundo.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 2 and escolhaprof == 1:
        with open('VotosSegundo.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[4] = int(nulos1[4])
            nulos1[4] += 1
            nulos1[4] = str(nulos1[4])
        with open('VotosSegundo.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 2 and escolhaprof == 2:
        with open('VotosSegundo.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[6] = int(nulos1[6])
            nulos1[6] += 1
            nulos1[6] = str(nulos1[6])
        with open('VotosSegundo.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 3 and escolhaprof == 0:
        with open('VotosTerceiro.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[2] = int(nulos1[2])
            nulos1[2] += 1
            nulos1[2] = str(nulos1[2])
        with open('VotosTerceiro.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 3 and escolhaprof == 1:
        with open('VotosTerceiro.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[4] = int(nulos1[4])
            nulos1[4] += 1
            nulos1[4] = str(nulos1[4])
        with open('VotosTerceiro.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
    elif dia == 3 and escolhaprof == 2:
        with open('VotosTerceiro.txt','r') as file:
            nulos = file.readlines()
            nulos1 = [item.rstrip('\n') for item in nulos]
            nulos1[6] = int(nulos1[6])
            nulos1[6] += 1
            nulos1[6] = str(nulos1[6])
        with open('VotosTerceiro.txt','w') as file:
            for nulos2 in nulos1:
                file.write('%s \n' %(nulos2))
print('Até amanhã!')
