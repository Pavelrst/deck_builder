from PIL import Image
from fpdf import FPDF
import os


class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        pass


# def save_cards_to_pdf(output_pdf_path, card_paths):
#     pdf = PDF(unit="mm", format="A4")  # Landscape orientation, A4 paper size
#     pdf.add_page()
#
#     # Assuming A4 paper size: 297mm x 210mm
#     # Define starting points for each card
#     SPACE = 8
#     positions = [
#         (SPACE, SPACE),           # top-left
#         (90+SPACE*2, SPACE),       # top-right
#         (SPACE, 120+SPACE*2),       # bottom-left
#         (90+SPACE*2, 120+SPACE*2)    # bottom-right
#     ]
#
#     for index, card_path in enumerate(card_paths):
#         x, y = positions[index]
#         pdf.image(card_path, x=x, y=y, w=90, h=120)  # width and height set to 9cm and 12cm respectively
#
#     pdf.output(output_pdf_path)

def save_cards_to_pdf(output_pdf_path, card_paths):
    pdf = PDF(unit="mm", format="A4")  # A4 paper size

    SPACE = 8
    positions = [
        (SPACE, SPACE),           # top-left
        (90+SPACE*2, SPACE),       # top-right
        (SPACE, 120+SPACE*2),       # bottom-left
        (90+SPACE*2, 120+SPACE*2)    # bottom-right
    ]

    chunks = [card_paths[i:i + 4] for i in range(0, len(card_paths), 4)]

    for chunk in chunks:
        pdf.add_page()
        for index, card_path in enumerate(chunk):
            x, y = positions[index]
            pdf.image(card_path, x=x, y=y, w=90, h=120)  # width and height set to 9cm and 12cm respectively

    pdf.output(output_pdf_path)
