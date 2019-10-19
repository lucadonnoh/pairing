import matplotlib.pyplot as plt
import math

def squarepairing():
    x = 0
    y = 0
    list_x = []
    list_y = []
    list_x.append(x);
    list_y.append(y);
    for i in range(100):
        if x == 0:
            x = y + 1
            y = 0
        else:
            if x > y:
                x = x
                y = y + 1
            else:
                if x <= y:
                    x = x - 1
                    y = y
        list_x.append(x)
        list_y.append(y)
    for i_x, i_y in zip(list_x,list_y):
        if i_x >= i_y:
            label = max(i_x, i_y)*max(i_x, i_y)+i_y
        else:
            label = max(i_x, i_y)*max(i_x, i_y)+i_y+i_y-i_x
        plt.text(i_x, i_y, '{}'.format((int)(label)), color='#e86f68')

    plt.plot(list_x,list_y, '--o', color='#444444')
    plt.axis([-0.5, 6.5, -0.5, 6.5])
    plt.savefig('squarepairing.png', dpi=600)
    plt.show()


    


def topair(n):
    print(n)
    a = n*8
    b = a + 1
    c = math.sqrt(b)
    d = c - 1
    e = d / 2
    w = math.floor(e)
    f = w + 1
    g = w*f
    t = g / 2
    y = n - t
    x = w - y
    print(str(x) + "," + str(y))
    return [x,y]


x = []
y = []
plt.style.use('dark_background')
fig = plt.figure()
ax = fig.add_subplot(111)
plt.setp(ax.get_xticklabels(), color="#c2b28f")
plt.setp(ax.get_yticklabels(), color="#c2b28f")

def plotta():
    for i in range(npoints):
        punto = topair(i)
        x.append(punto[0])
        y.append(punto[1])

    for i_x, i_y in zip(x,y):
        plt.text(i_x, i_y, '{}'.format((int)((i_x+i_y)*(i_x+i_y+1)/2+i_y)), color='#e86f68')

    #plt.plot(x,y, 'ro')
    plt.plot(x,y, '--o', color='#444444')
    plt.axis([-0.5, 6.5, -0.5, 6.5])
    #plt.axis('off')
    
    plt.savefig('trianglepairing.png', dpi=600)
    plt.show()


npoints = 100

#plotta()
squarepairing()

