matriz = [[1, 2, 4], [1, 6, 9], [2, 0, 7]]
def sarrus_it(matriz):
    det = 0
    for i in range(len(matriz)):
        aux = matriz[:]
        aux.pop(0)
        aux[0] = matriz[1][:]
        aux[0].pop(i)
        aux[1] = matriz[2][:]
        aux[1].pop(i)
        sub_det = (aux[0][0] * aux[1][1]) - (aux[0][1] * aux[1][0])
        if i % 2 == 0:
            signo = 1
        else:
            signo = -1
        det = det + signo*matriz[0][i]*sub_det
    return det

print(sarrus_it(matriz))