import numpy as np
import matplotlib.pyplot as plt


class Sensing:
    fileName = ""
    txtTitle = ""

    numData = 0
    dL = 0
    strLength = 0
    endLength = 0

    # float data
    Length = []
    OTDR = []
    BrillouinIntensity = []
    FittedFrequency = []
    Temperature = []
    CompensatedStrain = []
    UncompensatedStrain = []

    def __init__(self, fn):
        self.fileName = fn
        self.read_botdr_data()

    def read_botdr_data(self):
        with open(self.fileName, 'r') as f:
            self.txtTitle = f.readline()
            c1 = []
            c2 = []
            c3 = []
            c4 = []
            c5 = []
            c6 = []
            c7 = []

            data = f.readlines()
            for line in data:
                line = line.strip()
                values = line.split()

                c1.append(values[0])
                c2.append(values[1])
                c3.append(values[2])
                c4.append(values[3])
                c5.append(values[4])
                c6.append(values[5])
                c7.append(values[6])

            self.numData = len(c1)
            self.dL = c1[0]
            self.strLength = c1[0]
            self.endLength = c1[-1]

            self.Length = np.array(c1, dtype='f')
            self.OTDR = np.array(c2, dtype='f')
            self.BrillouinIntensity = np.array(c3, dtype='f')
            self.FittedFrequency = np.array(c4, dtype='f')
            self.Temperature = np.array(c5, dtype='f')
            self.CompensatedStrain = np.array(c6, dtype='f')
            self.UncompensatedStrain = np.array(c7, dtype='f')

    def show_graph_simple(self):
        plt.plot(self.Length, self.OTDR)
        plt.plot(self.Length, self.BrillouinIntensity)
        plt.show()

    def show_graph_paper_style(self):
        plt.plot(self.Length, self.OTDR, 'r-*', label=r'$sin(4 \pi x)$', lw=1)
        plt.plot(self.Length, self.BrillouinIntensity, 'b--o', label=r'$ e^{-2x} sin(4\pi x) $', lw=1)
        plt.title(r'$sin(4 \pi x)$ vs. $ e^{-2x} sin(4\pi x)$')
        plt.xlabel('x')
        plt.ylabel('y')
        # plt.axis([0, 1, -1.5, 1.5])
        plt.grid(True)
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()
