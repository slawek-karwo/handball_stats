import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


x_mecze_a = []
y_Arek_a = []
y_Szymon_a = []
y_Patryk_a = []

plt.style.use('fivethirtyeight')
data = pd.read_excel('Top scorrers road.xlsx')
x_mecze = list(data['Mecz'])
y_Arek = list(data['Arek sum'])
y_Szymon = data['Szymon sum']
y_Patryk = data['Patryk sum']


def animate(i):
    print(i)

    x_mecze_a.append(x_mecze[i])
    y_Arek_a.append(y_Arek[i])
    y_Szymon_a.append(y_Szymon[i])
    y_Patryk_a.append(y_Patryk[i])

    plt.cla()
    plt.plot(x_mecze_a, y_Arek_a, color='orange', label=f'Arkadiusz Moryto {y_Arek[i]}')
    plt.plot(x_mecze_a, y_Szymon_a, color='blue', label=f'Szymon Sićko {y_Szymon[i]}')
    plt.plot(x_mecze_a, y_Patryk_a, color='red', label=f'Patryk Mauer {y_Patryk[i]}')
    plt.xlabel('Games', size=10)
    plt.ylabel('Goals', size=10)
    plt.tight_layout()
    plt.legend(loc='upper left', prop={'size': 8})


# ani = FuncAnimation(plt.gcf(), animate, interval=1000, frames=50)
ani = FuncAnimation(plt.gcf(), animate, interval=1000, frames=25, repeat=False)
ani.save('animation.gif', writer='imagemagick')



