import os.path

from .raport_generator_interface import RaportGeneratorInterface
import numpy as np
import matplotlib.pyplot as plt


class RaportGenerator(RaportGeneratorInterface):

    def __init__(self):
        self.path = "resources"
        self.child_data = "child_data.csv"
        self._read_child_file()

        if self.gender == "f":
            self.age_weight_data = "who_charts/girl_age_weight.csv"
            self.age_height_data = "who_charts/girl_age_height.csv"
            self.age_eye_width_data = "who_charts/girl_age_eye_width.csv"
            self.age_upper_lip_height_data = "who_charts/girl_age_upper_lip_height.csv"
        else:
            self.age_weight_data = "who_charts/boy_age_weight.csv"
            self.age_height_data = "who_charts/boy_age_height.csv"
            self.age_eye_width_data = "who_charts/boy_age_eye_width.csv"
            self.age_upper_lip_height_data = "who_charts/boy_age_upper_lip_height.csv"

        self._load_reference_data()

    def _read_child_file(self):
        if hasattr(self, 'child_file'):
            self.child_file.close()

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
        self.child_age_height_array_X = []
        self.child_age_height_array_Y = []
        self.child_age_eye_width_array_X = []
        self.child_age_eye_width_array_Y = []
        self.child_age_upper_lip_height_array_X = []
        self.child_age_upper_lip_height_array_Y = []

        for sublist in self.child_array:
            if ~np.isnan(sublist[1]):
                # this will contain age values
                self.child_age_weight_array_X.append(sublist[0])
                self.child_age_height_array_X.append(sublist[0])
                self.child_age_eye_width_array_X.append(sublist[0])
                self.child_age_upper_lip_height_array_X.append(sublist[0])
                # this will contain weight values
                self.child_age_weight_array_Y.append(sublist[1])
                # TODO this should contain height values
                self.child_age_height_array_Y.append(sublist[1])
                # TODO this should contain eye width values
                self.child_age_eye_width_array_Y.append(sublist[1])
                # TODO this should contain upper lip height values
                self.child_age_upper_lip_height_array_Y.append(sublist[1])

    def _load_reference_data(self):
        self.age_weight_array = np.loadtxt(os.path.join(self.path, self.age_weight_data), delimiter=',', skiprows=1)
        self.age_height_array = np.loadtxt(os.path.join(self.path, self.age_height_data), delimiter=',', skiprows=1)
        self.age_eye_width_array = np.loadtxt(os.path.join(self.path, self.age_eye_width_data), delimiter=',',
                                              skiprows=1)
        self.age_upper_lip_height_array = np.loadtxt(os.path.join(self.path, self.age_upper_lip_height_data),
                                                     delimiter=',', skiprows=1)

    def generate_chart(self, reference_data, child_x, child_y, x_label, y_label, filename):
        fig, ax = plt.subplots(figsize=(16, 9))

        ax.plot(
            reference_data[:, 0], reference_data[:, 1], 'r--',
            reference_data[:, 0], reference_data[:, 2], 'r--',
            reference_data[:, 0], reference_data[:, 3], 'r--',
            reference_data[:, 0], reference_data[:, 4], 'r--',
            reference_data[:, 0], reference_data[:, 5], 'k-',
            reference_data[:, 0], reference_data[:, 6], 'r--',
            reference_data[:, 0], reference_data[:, 7], 'r--',
            reference_data[:, 0], reference_data[:, 8], 'r--',
            reference_data[:, 0], reference_data[:, 9], 'r--',
            child_x, child_y, 'b-*'
        )

        ax.grid(True)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_xlim([0, 24])
        ax.set_xticks(np.arange(0, 25, 3))

        percentiles = ['2%', '5%', '10%', '25%', '50%', '75%', '90%', '95%', '98%']
        for i, percentile in enumerate(percentiles):
            ax.text(reference_data[13 + i, 0], reference_data[13 + i, i + 1], percentile, fontsize=7)

        # fig.tight_layout()
        # fig.savefig(os.path.join(self.path, filename + '.pdf'), dpi=100)
        # fig.savefig(os.path.join(self.path, filename + '.png'), dpi=100)
        return fig

    def generate_age_weight_chart(self):
        return self.generate_chart(
            self.age_weight_array,
            self.child_age_weight_array_X,
            self.child_age_weight_array_Y,
            'age [months]',
            'weight [kg]',
            'growth_weight'
        )

    def generate_age_height_chart(self):
        return self.generate_chart(
            self.age_height_array,
            self.child_age_height_array_X,
            self.child_age_height_array_Y,
            'age [months]',
            'height [cm]',
            'growth_height'
        )

    def generate_age_eye_width_chart(self):
        return self.generate_chart(
            self.age_eye_width_array,
            self.child_age_eye_width_array_X,
            self.child_age_eye_width_array_Y,
            'age [months]',
            'eye width [mm]',
            'growth_eye_width'
        )

    def generate_age_upper_lip_height_chart(self):
        return self.generate_chart(
            self.age_upper_lip_height_array,
            self.child_age_upper_lip_height_array_X,
            self.child_age_upper_lip_height_array_Y,
            'age [months]',
            'upper lip height [mm]',
            'growth_upper_lip_height'
        )

    def generate(self, figures_to_save):
        highest = 0
        for filename in os.listdir(self.path):
            if filename.startswith('growth_') and filename.endswith('.pdf'):
                try:
                    number = int(filename[7:-4])
                    if number > highest:
                        highest = number
                except ValueError:
                    pass

        next_number = highest + 1

        for fig_type, fig in figures_to_save.items():
            print("Saving " + fig_type + " chart")
            fig.savefig(os.path.join(self.path + "\\saved_charts", f'growth_{fig_type}_{next_number}.pdf'), dpi=100)
            fig.savefig(os.path.join(self.path + "\\saved_charts", f'growth_{fig_type}_{next_number}.png'), dpi=100)
            next_number += 1

    def set_child_data_file(self, file_path):
        self.child_data = file_path
        self._read_child_file()
        print(self.child_file)
