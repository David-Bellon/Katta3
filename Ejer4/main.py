from abc import ABC, abstractmethod

class Abs(ABC):
    @abstractmethod
    def restar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass

    @abstractmethod
    def existe(self):
        pass


class Polinomio(Abs):
    def __init__(self):
        self.grados = []
        self.valores = []

    def añadir_termino(self, grado, valor):
        change = False
        for i, grad in enumerate(self.grados):
            if grad == grado:
                self.valores[i] = self.valores[i] + valor
                change = True
                break
        if not change:
            self.valores.append(valor)
            self.grados.append(grado)


    def restar(self, pol):
        out = Polinomio()
        for i, grad in enumerate(self.grados):
            for j, res_grad in enumerate(pol.grados):
                if grad not in pol.grados:
                    out.añadir_termino(grad, self.valores[i])
                    break
                if res_grad not in self.grados and res_grad not in out.grados:
                    out.añadir_termino(res_grad, -pol.valores[j])
                if grad == res_grad:
                    out.añadir_termino(grad, self.valores[i] - pol.valores[j])

                    

        print(out)
        

    def eliminar(self, grado):
        deleted = False
        for i, grad in enumerate(self.grados):
            if grad == grado:
                del self.grados[i]
                del self.valores[i]
                deleted = True
                break
        if not deleted:
            print("No existe un termino con dicho grado en el polinomio")

    def existe(self, grad):
        exist = False
        for i in self.grados:
            if i == grad:
                print("Existe el temino con grado " + str(grad) + " en el polinomio")
                exist = True
                break
        if not exist:
            print("No existe el temino con grado " + str(grad) + " en el polinomio")

    def __str__(self) -> str:
        out = ""
        for i in range(len(self.grados)):
            if self.grados[i] == 0:
                out = out + str(self.valores[i]) + " "
            elif self.grados[i] == 1:
                out = out + str(self.valores[i]) + "x "
            else:
                out = out + str(self.valores[i]) + "x^" + str(self.grados[i]) + " "
        return out

def main():
    pol1 = Polinomio()
    pol1.añadir_termino(2, -4)
    pol1.añadir_termino(3, 2)
    pol1.añadir_termino(0, 9)

    pol2 = Polinomio()
    pol2.añadir_termino(3, -1)
    pol2.añadir_termino(4, 2)
    pol2.añadir_termino(2, 3)

    pol1.eliminar(2)
    print(pol1)

    pol1.restar(pol2)