# M1 x M2 ;
# M3 x M4 ;
# M1 x M3 ;
# M2 x M4 ;
# M2 x M3 ;
# M1 x M4 ;
# Média das 6 DEs
from math import sqrt

avaliacoes = {
    'Anna':
        {
            'M1': 2,
            'M2': 4,
            'M3': 0,
            'M4': 3,
        },

    'Geo':
        {
            'M1': 4.3,
            'M2': 1,
            'M3': 4,
            'M4': 3.7,
        },

    'Pedro':
        {
            'M1': 3.8,
            'M2': 2.3,
            'M3': 4.1,
            'M4': 4.5
        },
    'Igor':
        {
            'M1': 5,
            'M2': 3.0,
            'M3': 4,
            'M4': 2,
        },
    'Andre':
        {
            'M1': 3.5,
            'M2': 3,
            'M3': 4,
            'M4': 3.0
        },

    'Thullyo':
        {
            'M1': 3.0,
            'M2': 4.0,
            'M3': 0,
            'M4': 5.0,
        },

    'Edi':
        {
            'M1': 5,
            'M2': 4,
            'M3': 2.0,
            'M4': 2
        },
    'Lucas':
        {
            'M1': 4,
            'M2': 3.5,
            'M3': 2.2,
            'M4': 3.3
        },
    'Emanoel':
        {
            'M1': 3,
            'M2': 2,
            'M3': 4,
            'M4': 4.5
        }
}
def printLines():
    print("=*" * 20)

printLines()
print("Função euclidiana")
printLines()
def eucl(user1, user2):
    si = {}
    for item in avaliacoes[user1]:
        #verifica de o filme está presente nos dois usuários
        if item in avaliacoes[user2]:
            si[item] = 1

    if len(si) == 0: return 0
    sumTotal = sum([pow(avaliacoes[user1][item] - avaliacoes[user2][item], 2)
               for item in avaliacoes[user1] if item in avaliacoes[user2]
               ])

    return 1 / (1 + sqrt(sumTotal))

def calSim(user):
    list = []

    for u in avaliacoes:
        if u != user:
            data = {}
            data['name'] = u
            data['sim'] = eucl(user, u)
            list.append(data)

    def compare(obj):
        return (-obj['sim'], obj['name'])

    orderList = sorted(list, key=compare)
    print(f"User {user} ranking:")
    for i, u in enumerate(orderList):
        print(f"    {i + 1}° {u['name']} - similarity: {(u['sim'] * 100):.2f}%")
    printLines()

for u in avaliacoes:
    calSim(u)