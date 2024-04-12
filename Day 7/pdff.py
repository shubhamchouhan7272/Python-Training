from fpdf import FPDF

ref = FPDF()
ref.add_page()
ref.set_font("Arial", size=20)
ref.cell(200,100,"Welcome to PDF", align="L")

ref.output("pythonfile.pdf")