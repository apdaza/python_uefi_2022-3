from random import shuffle

valores = ['A', 'J', 'Q', 'K'] + [str(x) for x in range(2, 11)]
pintas = ['Diamantes', 'Corazones', 'Picas', 'Treboles']

baraja = [(v, p) for v in valores for p in pintas]

puntos = {'A': 11,
          'J': 10,
          'Q': 10,
          'K': 10,
          '10': 10,
          '9': 9,
          '8': 8,
          '7': 7,
          '6': 6,
          '5': 5,
          '4': 4,
          '3': 3,
          '2': 2
        }

shuffle(baraja)

jugador1 = baraja.pop()
jugador2 = baraja.pop()

#jugador1 = ('A', 'Diamantes')
print(jugador1, jugador2)

p1, p2 = puntos[jugador1[0]], puntos[jugador2[0]]

if p1 > p2:
    print("gana jugador1")
elif p1 < p2:
    print("gana jugador2")
else:
    print("empate")
