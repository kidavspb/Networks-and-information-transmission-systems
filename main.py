import random


def p_mod(a, b):
    bl = len(b)
    while True:
        for i in range(len(a)):
            if a[i] != 0:
                a = a[i:]
                break
            if i == len(a) - 1:
                return 0
        shift = len(a) - bl
        if shift < 0:
            return a
        for i in range(len(a)):
            a[i] ^= (b + shift * [0])[i]


def coder(mx, gx):
    # gx = [1, 0, 1, 1]
    r = len(gx) - 1

    # mx = [1, 0, 1, 0]
    # mx = [0, 0, 0, 1, 1]
    k = len(mx)

    cx = p_mod(mx + r * [0], gx)
    if type(cx) == int:
        cx = [cx]
    cx = (r - len(cx)) * [0] + cx

    ax = mx + cx

    print("mx = ", mx)
    print("cx = ", cx)
    print("ax = ", ax, end="\n\n")

    return ax


def channel(ax):
    n = len(ax)
    ex = [random.randint(0, 1) for i in range(n)]
    # ex = [1, 1, 1, 1, 1, 1, 1]
    # ex = [0, 0, 0, 0, 0, 0, 0]

    bx = [ax[i] ^ ex[i] for i in range(n)]

    print("ax = ", ax)
    print("ex = ", ex)
    print("bx = ", bx, end="\n\n")

    return bx


def decoder(bx, gx):
    sx = p_mod(bx, gx)
    if sx != 0:
        E = 1
    else:
        E = 0

    print("sx = ", sx)
    return E

# ----------------------------

def alt_decoder(bx, gx):
    r = len(gx) - 1
    k = len(bx) - r

    mb = bx[:k]
    cb = bx[k:]
    alt_ax = coder(mb, gx)

    alt_cb = alt_ax[k:]
    if cb != alt_cb:
        E = 1
    else:
        E = 0

    print("cb = cx = ", cb)
    print("cb\'     = ", alt_cb)
    return E

if __name__ == "__main__":
    E1 = E2 = 0
    # while E1 == E2:
    # mx = [1, 0, 1, 0]
    mx = [random.randint(0, 1) for i in range(4)]
    gx = [1, 0, 1, 1]

    ax = coder(mx, gx)
    bx = channel(ax)
    E1 = decoder(bx, gx)
    print("E1 = ", E1, f"{' -> Произошли ошибки' if E1 == 1 else ' -> Ошибок не обнаружено'}")
    print("\n#----------------------------\n")

    E2 = alt_decoder(bx, gx)
    print("E2 = ", E2, f"{' -> Произошли ошибки' if E2 == 1 else ' -> Ошибок не обнаружено'}", end="\n\n")
