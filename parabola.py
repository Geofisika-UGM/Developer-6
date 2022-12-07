# Mengimport Modul
import matplotlib.pyplot as plt
import math as mt

# Mendefinisikan waktu
def frange(start, stop=None, step=None):
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    print("start = ", start, "stop = ", stop, "step = ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

# Rumus Gerak Parabola
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



    X.append(posX)
    Y.append(posY)

    # Mendefinisikan rentang waktu grafik
    for t in frange(0,w+0.1,0.1):
    
        posX = voX * t
        X.append(posX)
        posY = vo * t * Sin + (0.5 * g * mt.pow(t,2))
        Y.append(posY)
     
        if posY < 0:
            print('Waktu Analitik ketika menyentuh tanah : ',t)
            print('Jarak Maksimal dari Analitik ',posX)
            print('\n')
            break
      
    
    print('Waktu Total : ',w)
    plt.xlabel('Jarak') # Memberi label pada sumbu x
    plt.ylabel('Ketinggian') # Memberi label pada sumbu y
    plt.plot(X,Y) 
    plt.xlim(0,R+1)
    plt.ylim(0,hMax+0.1)
    print ('Jarak Maksimum : ',R)
    print ('Tinggi Maksimum : ',hMax)
    plt.show() # Menampilkan grafik
