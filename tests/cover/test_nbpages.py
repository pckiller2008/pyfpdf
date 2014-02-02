# -*- coding: utf-8 -*-

"Simple test to check alias_nb_pages replacement under unicode fonts"

#PyFPDF-cover-test:format=PDF
#PyFPDF-cover-test:fn=nb_pages.pdf
#PyFPDF-cover-test:hash=4f22df85e31007cb275fabdc9fa78f97

import common
from fpdf import FPDF

import os

def dotest(outputname, nostamp):
    pdf = FPDF()
    if nostamp:
        pdf._putinfo = lambda: common.test_putinfo(pdf)

    # set default alias: {nb} that will be replaced with total page count
    pdf.alias_nb_pages()

    # Add a Unicode font (uses UTF-8)
    pdf.add_font('DejaVu', '', \
        os.path.join(common.basepath, "fonts", 'DejaVuSansCondensed.ttf'), \
        uni=True)
    pdf.set_font('DejaVu', '', 14)

    for i in range(5):
        pdf.add_page()
        pdf.set_font('Arial','B',16)
        pdf.cell(40,10,'Hello World! Page %d from {nb}' % (i + 1))
        pdf.set_font('DejaVu','',14)
        pdf.cell(40,30,'Hello World! unicode {nb}')


    pdf.output(outputname, 'F')

if __name__ == "__main__":
    common.testmain(__file__, dotest)
