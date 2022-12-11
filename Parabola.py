def parabola(vo,agl,x1,y1):
    X = []
    Y = []
    

    Sin = mt.sin(mt.radians(agl))
    Cos = mt.cos(mt.radians(agl))

    g = 9.8
    w = float((2 * vo * Sin) / g)

    atas = float(mt.pow(vo,2) * mt.pow(Sin,2))
    bawah = float(2*g)
    hMax = float(atas/bawah)
    R = vo * Cos * w
    g = g * -1

    posX = x1
    posY = y1

    voX = float(vo * Cos)
    voY = float(vo * Sin)
