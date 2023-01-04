import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as mplot3d
import numpy as np
import mpl_toolkits.mplot3d.axes3d as axes3d

def main():
    LINK_LEN = 100

    fig = plt.figure()
    ax = plt.axes(projection="3d")

    z = [0, 1, 2, 3, 4, 5, 6, 7]
    x = [0, 2, 3, 5, 7, 10, 14, 10]
    y = [0, 4, 5, 2, 3, 5, 7, 10]

    for i in range(len(z)):
        ax.plot(x[i:i+2], y[i:i+2], z[i:i+2], label="link"+str(i))
    ax.legend()

    plt.show()

if __name__ == "__main__":
    main()