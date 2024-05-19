import os.path

from .raport_generator_interface import RaportGeneratorInterface
import numpy as np
import matplotlib.pyplot as plt


class RaportGenerator(RaportGeneratorInterface):

    def __init__(self):
        self.path = "resources"
        self.child_data = "child_data.csv"
        self.child_file = open(os.path.join(self.path, self.child_data))
        self.gender = self.child_file.readline()[7]
        self.child_array = np.genfromtxt(
            os.path.join(self.path, self.child_data),
            delimiter=',',
            dtype=None,
            skip_header=2
        )
        self.child_age_weight_array_X = []
        self.child_age_weight_array_Y = []

        for sublist in self.child_array:
            if ~np.isnan(sublist[1]):
                # this will contain age values
                self.child_age_weight_array_X.append(sublist[0])
                # and this will contain weight values
                self.child_age_weight_array_Y.append(sublist[1])

        if self.gender == "f":
            self.age_weight_data = "who_charts/girl_age_weight.csv"
        else:
            self.age_weight_data = "who_charts/boy_age_weight.csv"

        self.age_weight_array = np.loadtxt(os.path.join(self.path, self.age_weight_data), delimiter=',', skiprows=1)

    def generate(self):
        # plots
        plt.figure()

        # f(age) = weight
        plt.subplot(1, 1, 1)
        plt.plot( \
            # weird syntax - the fragment below takes
            # all rows in first column (age) and reads all records for certain age,
            # creating a red dashed (r--) line on chart, and blue one for record from child_data.csv
            self.age_weight_array[:, 0], self.age_weight_array[:, 1], 'r--', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 2], 'r--', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 3], 'r--', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 4], 'r--', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 5], 'k-', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 6], 'r--', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 7], 'r--', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 8], 'r--', \
            self.age_weight_array[:, 0], self.age_weight_array[:, 9], 'r--', \
            self.child_age_weight_array_X, self.child_age_weight_array_Y, 'b-*')

        plt.grid(True)
        plt.xlabel('age [months]')
        plt.ylabel('weight [kg]')
        plt.xlim([0, 24])
        plt.xticks(np.arange(0, 25, 3))

        plt.text(self.age_weight_array[13, 0], self.age_weight_array[13, 1], '2%', fontsize=7)
        plt.text(self.age_weight_array[14, 0], self.age_weight_array[14, 2], '5%', fontsize=7)
        plt.text(self.age_weight_array[15, 0], self.age_weight_array[15, 3], '10%', fontsize=7)
        plt.text(self.age_weight_array[16, 0], self.age_weight_array[16, 4], '25%', fontsize=7)
        plt.text(self.age_weight_array[17, 0], self.age_weight_array[17, 5], '50%', fontsize=7)
        plt.text(self.age_weight_array[18, 0], self.age_weight_array[18, 6], '75%', fontsize=7)
        plt.text(self.age_weight_array[19, 0], self.age_weight_array[19, 7], '90%', fontsize=7)
        plt.text(self.age_weight_array[20, 0], self.age_weight_array[20, 8], '95%', fontsize=7)
        plt.text(self.age_weight_array[21, 0], self.age_weight_array[21, 9], '98%', fontsize=7)

        # adjusting margins
        plt.subplots_adjust(wspace=0.4, hspace=0.4)

        # saving graphs
        fig1 = plt.gcf()

        fig1.set_size_inches(16, 9)
        fig1.savefig(os.path.join(self.path, 'growth.pdf'), dpi=100)
        fig1.savefig(os.path.join(self.path, 'growth.png'), dpi=100)

        print("Chart generated and saved")
