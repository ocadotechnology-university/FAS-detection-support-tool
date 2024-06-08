import os.path

from .raport_generator_interface import RaportGeneratorInterface
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf

from PySide6 import QtWidgets as qtw

import sys


class RaportGenerator(RaportGeneratorInterface):

    def __init__(self):
        self.path = "resources"
        self.age_head_c_data = None
        self.age_weight_data = None
        self.age_height_data = None
        self.age_head_c_array = None
        self.age_weight_array = None
        self.age_height_array = None
        self.gender = "f"
        self._load_reference_data()

    def _load_reference_data(self):
        if self.gender == "f":
            self.age_head_c_data = "who_charts/girl_age_headc.csv"
            self.age_weight_data = "who_charts/girl_age_weight.csv"
            self.age_height_data = "who_charts/girl_age_height.csv"
        else:
            self.age_head_c_data = "who_charts/boy_age_headc.csv"
            self.age_weight_data = "who_charts/boy_age_weight.csv"
            self.age_height_data = "who_charts/boy_age_height.csv"
        self.age_head_c_array = np.loadtxt(os.path.join(self.path, self.age_head_c_data), delimiter=',', skiprows=1)
        self.age_weight_array = np.loadtxt(os.path.join(self.path, self.age_weight_data), delimiter=',', skiprows=1)
        self.age_height_array = np.loadtxt(os.path.join(self.path, self.age_height_data), delimiter=',', skiprows=1)

    def generate_chart(self, reference_data, x_label, y_label, filename, value, age):
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
        )

        ax.grid(True)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_xlim([0, 24])
        ax.set_xticks(np.arange(0, 25, 3))

        percentiles = ['2%', '5%', '10%', '25%', '50%', '75%', '90%', '95%', '98%']
        for i, percentile in enumerate(percentiles):
            ax.text(reference_data[13 + i, 0], reference_data[13 + i, i + 1], percentile, fontsize=7)

        ax.scatter(age, value, color='blue')

        # fig.tight_layout()
        # fig.savefig(os.path.join(self.path, filename + '.pdf'), dpi=100)
        # fig.savefig(os.path.join(self.path, filename + '.png'), dpi=100)
        return fig

    def generate_age_head_c_chart(self, age, value):
        return self.generate_chart(
            self.age_head_c_array,
            'age [months]',
            'circuit [cm]',
            'growth_head_circuit',
            value,
            age
        )

    def generate_age_weight_chart(self, age, value):
        return self.generate_chart(
            self.age_weight_array,
            'age [months]',
            'weight [kg]',
            'growth_weight',
            value,
            age
        )

    def generate_age_height_chart(self, age, value):
        return self.generate_chart(
            self.age_height_array,
            'age [months]',
            'height [cm]',
            'growth_height',
            value,
            age
        )

    def generate(self, figures_to_save):
        app = qtw.QApplication.instance()
        if app is None:
            app = qtw.QApplication(sys.argv)

        options = qtw.QFileDialog.Options()
        folder_path = qtw.QFileDialog.getExistingDirectory(None, "Wybierz katalog", options=options)

        highest = 0
        print(f"os.path.join(self.path, 'saved_charts')={os.path.join(self.path, 'saved_charts')}")
        print(f"folder_path={folder_path}")
        for filename in os.listdir(os.path.join(self.path, 'saved_charts')):
            print(f"filename={filename}")
            if filename.startswith('child_growth_') and filename.endswith('.pdf'):
                try:
                    number = int(filename[len('child_growth_'):-4])
                    if number > highest:
                        highest = number
                except ValueError:
                    pass

            next_number = highest + 1

        # if folder_path:
        #     for fig_type, fig in figures_to_save.items():
        #         print("Zapisuję siatkę " + fig_type)
        #         fig.savefig(os.path.join(folder_path, f'growth_{fig_type}_{next_number}.pdf'), dpi=100)
        #         fig.savefig(os.path.join(folder_path, f'growth_{fig_type}_{next_number}.png'), dpi=100)
        #         next_number += 1
        if folder_path:
            pdf_file_path = os.path.join(folder_path, f'child_growth_{next_number}.pdf')

            with pdf.PdfPages(pdf_file_path) as pdf_pages:
                for fig_type, fig in figures_to_save.items():
                    print("Zapisuję siatkę " + fig_type)
                    pdf_pages.savefig(fig, dpi=100)
                    next_number += 1

            msg_box = qtw.QMessageBox()
            msg_box.setIcon(qtw.QMessageBox.Icon.Information)
            msg_box.setText("Siatki zostały zapisane w wybranym katalogu")
            msg_box.setWindowTitle("Sukces!")
            msg_box.setStandardButtons(qtw.QMessageBox.StandardButton.Ok)
            msg_box.exec()
        else:
            print("Nie wybrano katalogu!")
