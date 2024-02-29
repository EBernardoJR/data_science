from math import sqrt

avaliacoes = {
    'Ana':
        {'Freddy x Jason': 2.5,
         'O Ultimato Bourne': 3.5,
         'Star Trek': 3.0,
         'Exterminador do Futuro': 3.5,
         'Norbit': 2.5,
         'Star Wars': 3.0},

    'Marcos':
        {'Freddy x Jason': 3.0,
         'O Ultimato Bourne': 3.5,
         'Star Trek': 1.5,
         'Exterminador do Futuro': 5.0,
         'Star Wars': 3.0,
         'Norbit': 3.5},

    'Pedro':
        {'Freddy x Jason': 2.5,
         'O Ultimato Bourne': 3.0,
         'Exterminador do Futuro': 3.5,
         'Star Wars': 4.0},

    'Claudia':
        {'O Ultimato Bourne': 3.5,
         'Star Trek': 3.0,
         'Star Wars': 4.5,
         'Exterminador do Futuro': 4.0,
         'Norbit': 2.5},

    'Adriano':
        {'Freddy x Jason': 3.0,
         'O Ultimato Bourne': 4.0,
         'Star Trek': 2.0,
         'Exterminador do Futuro': 3.0,
         'Star Wars': 3.0,
         'Norbit': 2.0},

    'Janaina':
        {'Freddy x Jason': 3.0,
         'O Ultimato Bourne': 4.0,
         'Star Wars': 3.0,
         'Exterminador do Futuro': 5.0,
         'Norbit': 3.5},

    'Leonardo':
        {'O Ultimato Bourne': 4.5,
         'Norbit': 1.0,
         'Exterminador do Futuro': 4.0}
}

avaliacoes2 = {'Freddy x Jason':
                   {'Ana': 2.5,
                    'Marcos:': 3.0,
                    'Pedro': 2.5,
                    'Adriano': 3.0,
                    'Janaina': 3.0},

               'O Ultimato Bourne':
                   {'Ana': 3.5,
                    'Marcos': 3.5,
                    'Pedro': 3.0,
                    'Claudia': 3.5,
                    'Adriano': 4.0,
                    'Janaina': 4.0,
                    'Leonardo': 4.5},

               'Star Trek':
                   {'Ana': 3.0,
                    'Marcos:': 1.5,
                    'Claudia': 3.0,
                    'Adriano': 2.0},

               'Exterminador do Futuro':
                   {'Ana': 3.5,
                    'Marcos:': 5.0,
                    'Pedro': 3.5,
                    'Claudia': 4.0,
                    'Adriano': 3.0,
                    'Janaina': 5.0,
                    'Leonardo': 4.0},

               'Norbit':
                   {'Ana': 2.5,
                    'Marcos:': 3.0,
                    'Claudia': 2.5,
                    'Adriano': 2.0,
                    'Janaina': 3.5,
                    'Leonardo': 1.0},

               'Star Wars':
                   {'Ana': 3.0,
                    'Marcos:': 3.5,
                    'Pedro': 4.0,
                    'Claudia': 4.5,
                    'Adriano': 3.0,
                    'Janaina': 3.0}
               }


def printLines():
    print("=*" * 20)


print('distância euclidiana da Ana e do Marcos')
distanceAM = 1 / (1 + sqrt(pow(avaliacoes['Ana']['Star Trek'] - avaliacoes['Marcos']['Star Trek'], 2) + pow(
    avaliacoes['Ana']['Exterminador do Futuro'] - avaliacoes['Marcos']['Exterminador do Futuro'], 2)))
print(distanceAM)

printLines()
print("Função euclidiana")
printLines()


def eucl(user1, user2, base):
    si = {}
    for item in base[user1]:
        # verifica de o filme está presente nos dois usuários
        if item in base[user2]:
            si[item] = 1

    if len(si) == 0: return 0
    sumTotal = sum([pow(base[user1][item] - base[user2][item], 2)
                    for item in base[user1] if item in base[user2]
                    ])

    return 1 / (1 + sqrt(sumTotal))


def calSim(user, base):
    list = []

    for u in base:
        if u != user:
            data = {}
            data['name'] = u
            data['sim'] = eucl(user, u, base)
            list.append(data)

    def compare(obj):
        return (-obj['sim'], obj['name'])

    orderList = sorted(list, key=compare)
    print(f"User {user} ranking:")
    for i, u in enumerate(orderList[0:30]):
        print(f"{i + 1}° {u['name']} - similarity: {u['sim']}")


def calRecomendacao(usuario, base):
    print("")
    print(f"Recomendações para o usuário {usuario}")
    totais = {}
    somaSim = {}
    for outro in base:
        if outro == usuario: continue
        sim = eucl(usuario, outro, base)
        # Pulando usuários que n tem similaridades
        if sim <= 0: continue

        for filme in base[outro]:
            if filme not in base[usuario]:
                totais.setdefault(filme, 0)
                # Buscando a nota que o outro usuário deu pro filme
                totais[filme] += base[outro][filme] * sim  # Total
                somaSim.setdefault(filme, 0)
                somaSim[filme] += sim  # Soma sim

    rankings = [(total / somaSim[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]



def carregaMovieLens(path = 'C:/Users/emano/Documents/Projetos/data science/recommendation_system/ml-100k'):
    filmes = {}
    for line in open(path + '/u.item'):
        #obtendo somente os dois primeiros itens da linha
        (id, title) = line.split('|')[0:2]
        filmes[id] = title
    base = {}
    #Arquivo que contém as avaliações dos usuários
    for line in open(path + '/u.data'):
        (user, idfilme, nota, tempo) = line.split('\t')
        base.setdefault(user, {})
        #Setando a nota do usuário por meio do id do filme
        base[user][filmes[idfilme]] = float(nota)
    return base


baseMovies = carregaMovieLens()
user = '76'
calSim(user, baseMovies)
print(calRecomendacao(user, baseMovies))