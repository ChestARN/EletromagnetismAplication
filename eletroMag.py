from math import *


def produtoPonto(coord1, coord2, state):
    if state in range(3):
        return coord1 * coord2
    if state == 3:
        return


def produtoVect(v, vv, vvv):
    ax = v[0]
    ay = v[1]
    az = v[2]
    bx = vv[0]
    by = vv[1]
    bz = vv[2]
    if vvv == 0:
        return ay * bz - az * by
    if vvv == 1:
        return az * bx - ax * bz
    if vvv == 2:
        return ax * by - ay * bx


def converteCoord():
    res = float()
    vectD = []
    vectC = []
    vectE = []

    p1 = list(map(int, (input("Digite as coordenadas do ponto 1: ").split(" "))))
    p2 = list(map(int, (input("Digite as coordenadas do ponto 2: ").split(" "))))

    print(f"Coordanadas do ponto 1: {p1}")
    print(f"Coordenadas do ponto2: {p2}")

    for i in range(3):
        res = res + pow(p2[i] - p1[i], 2)
        vectD.append(p2[i] - p1[i])
    res = sqrt(res)

    print(f"Distância entre os pontos: {res:.2f}")
    print(f"Coordenadas do vetor: {vectD[0]}ax {vectD[1]}ay {vectD[2]}az")

    print("Para o ponto 1:")

    vectC.append(sqrt(pow(p1[0], 2) + pow(p1[1], 2)))
    vectC.append(atan(p1[1]/p1[0])*180/3.14)
    vectC.append(p1[2])

    print(f"O mesmo ponto em coordenadas cilindricas: {vectC[0]:.0f}ρ {vectC[1]:.4f}𝜙 {vectC[2]:.0f}z")

    vectE.append(sqrt(pow(p1[0], 2) + pow(p1[1], 2) + pow(p1[2], 2)))
    vectE.append(atan(sqrt(pow(p1[0], 2) + pow(p1[1], 2))/p1[2])*180/3.14)
    vectE.append(atan(p1[1]/p1[0])*180/3.14)

    print(f"Mesmo ponto em coordenadas esféricas: {vectE[0]:.0f}𝑟 {vectE[1]:.4f}𝜃 {vectE[2]:.4f}𝜙")

    print("Para o ponto 2:")

    vectC.append(sqrt(pow(p2[0], 2) + pow(p2[1], 2)))
    vectC.append(atan(p2[0]/p2[1])*180/3.14)
    vectC.append(p2[2])

    print(f"O mesmo ponto em coordenadas cilindricas: {vectC[3]:.0f}ρ {vectC[4]:.4f}𝜙 {vectC[5]:.0f}z")

    vectE.append(sqrt(pow(p2[0], 2) + pow(p2[1], 2) + pow(p2[2], 2)))
    vectE.append(atan(sqrt(pow(p2[0], 2) + pow(p2[1], 2))/p2[2]))
    vectE.append(atan(p2[0]/p2[1])*180/3.14)

    print(f"Mesmo ponto em coordenadas esféricas: {vectE[3]:.0f}𝑟 {vectE[4]:.4f}𝜃 {vectE[5]:.4f}𝜙")


def vetores():
    v1 = list(map(int, (input("Digite as coordenadas do vetor 1: ").split(" "))))
    v2 = list(map(int, (input("Digite as coordenadas do vetor 2: ").split(" "))))
    v3 = list(map(int, (input("Digite as coordenadas do vetor 3: ").split(" "))))
    vaux1 = [0, 0, 0]
    vaux2 = [0, 0, 0]
    lvct = []
    unitvect1 = []
    unitvect2 = []
    aux = 0
    aux2 = 0
    aux3 = 0
    product = 0

    for i in range(3):
        aux = produtoPonto(v1[i], v2[i], i) + aux
        aux2 = pow(v2[i], 2) + aux2
        aux3 = pow(v1[i], 2) + aux3

    for i in range(3):
        lvct.append((aux * v2[i]) / aux2)

    print(f"As componentes do vetor 1 ao longo do vetor 2  são: {lvct[0]:.4f}ax {lvct[1]:.4f}ay {lvct[2]:.4f}az")

    for i in range(3):
        unitvect1.append(v2[i] / aux3)

    for i in range(3):
        unitvect2.append(v2[i] / aux2)

    print(f"O vetor unitário do vetor 1 é : {unitvect1[0]:.4f}ax {unitvect1[1]:.4f}ay {unitvect1[2]:.4f}az")
    print(f"O vetor unitário do vetor 2 é : {unitvect2[0]:.4f}ax {unitvect2[1]:.4f}ay {unitvect2[2]:.4f}az")

    aux = 0
    aux2 = 0
    aux3 = 0
    for i in range(3):
        aux = pow(v1[i], 2) + aux
        aux2 = pow(v2[i], 2) + aux2
        aux3 = float(produtoPonto(v1[i], v2[i], i) + aux3)

    angVect = acos(aux3 / (sqrt(aux) * sqrt(aux2)))*180/3.14

    print(f"O ângulo entre os vetores 1 e 2 é: {angVect:.1f}")

    aux = 0
    aux2 = 0
    for i in range(3):
        vaux1[i] = produtoVect(v2, v3, i)
        vaux2[i] = produtoVect(v1, v2, i)

    for i in range(3):
        aux = produtoPonto(v1[i], vaux1[i],i) + aux
        aux2 = produtoPonto(v3[i], vaux2[i], i) + aux2

    print(f"O valor de A . BXC / AXB . C, sendo A o vetor 1, B o vetor 2 e CC o vetor 3 é: {(aux/aux2):.2f}")


def main():
    converteCoord()
    vetores()


main()
