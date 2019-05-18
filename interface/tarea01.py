import numpy as np # liberia para el manejo de los arreglos
import matplotlib.pyplot as plt # libreria de manejo de los graficos
from mpl_toolkits.mplot3d import Axes3D # libreria para proyectar graficos en 3D
import tkinter as tk # libreria para menejar las interface grafica


def create_plot():
    """
    La presente es una función de ejemplo de cómo projectar en un gráfico 3D una curva paramétrica
    tomada desde https://matplotlib.org/gallery/mplot3d/lines3d.html
    :return:
    """
    plt.rcParams['legend.fontsize'] = 12

    fig = plt.figure()
    ax = Axes3D(fig)

    # Prepare arrays x, y, z
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z ** 2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)

    ax.plot(x, y, z, label='Curva Paramétrica de Ejemplo')
    ax.legend()

    plt.show()


if __name__ == '__main__':
    create_plot()
