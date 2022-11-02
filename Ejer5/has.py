import hashlib
N = 8
def code():
    mensaje = str(input("Mensaje: ")).encode()
    m = hashlib.sha256()
    a = [mensaje[i:i+N] for i in range(0, len(mensaje), N)]
    for i in a:
        m.update(i)
    print(m.hexdigest())

def decode():
    mensaje = str(input("Mensaje: ")).encode()
    m = hashlib.sha256()
    a = [mensaje[i:i+N] for i in range(0, len(mensaje), N)]
    for i in a:
        m.update(i)
    print(m.hexdigest())


def main(): 
    code()
    decode()