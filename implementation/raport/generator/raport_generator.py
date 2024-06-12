import os.path
import subprocess
from PySide6 import QtGui as qtg

from .raport_generator_interface import RaportGeneratorInterface
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf as pdf

from PySide6 import QtWidgets as qtw

import sys
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import os


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

    def generate(self, figures_to_save, file_path):
        with pdf.PdfPages(file_path) as pdf_pages:
            for fig_type, fig in figures_to_save.items():
                # print("Zapisuję siatkę " + fig_type)
                pdf_pages.savefig(fig, dpi=100)
                # next_number += 1

    def generate_measurement_raport(self, file_path, image_path, left_eye, right_eye, lip, philtrum_class):
        c = canvas.Canvas(file_path, pagesize=letter)
        width, height = letter

        # Set a title for the document
        c.setFont("Helvetica-Bold", 16)
        c.drawString(72, height - 72, "Raport z pomiarów")

        # Add the image if available
        if image_path and os.path.exists(image_path):
            try:
                img = qtg.QImage(image_path)
                img_width = img.width()
                img_height = img.height()

                # Maintain aspect ratio
                max_width = width * 0.6
                max_height = height * 0.6
                aspect_ratio = img_width / img_height
                if aspect_ratio > (max_width / max_height):
                    display_width = max_width
                    display_height = max_width / aspect_ratio
                else:
                    display_height = max_height
                    display_width = max_height * aspect_ratio

                c.drawImage(image_path, 72, height - 72 - display_height - 20, width=display_width,
                            height=display_height)
            except Exception as e:
                return str(e)

        y_position = height - 72 - 20 - display_height - 40

        c.setFont("Helvetica", 12)
        # dostepne_czcionki = ['Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique', 'Helvetica', 'Helvetica-Bold',
        #             'Helvetica-BoldOblique', 'Helvetica-Oblique', 'Symbol', 'Times-Bold', 'Times-BoldItalic',
        #             'Times-Italic', 'Times-Roman', 'ZapfDingbats']

        left_eye_measurement = f"Szerokosc lewego oka: {left_eye}mm"
        right_eye_measurement = f"Szerokosc prawego oka: {right_eye}mm"
        upper_lip_measurement = f"Wysokosc gornej wargi: {lip}mm"

        c.drawString(72, y_position, left_eye_measurement)
        y_position -= 20
        c.drawString(72, y_position, right_eye_measurement)
        y_position -= 20
        c.drawString(72, y_position, upper_lip_measurement)
        y_position -= 20

        if philtrum_class != 0:
            philtrum_measurement = f"Typ rynienki podnosowej: {philtrum_class}"
            c.drawString(72, y_position, philtrum_measurement)

        c.save()
