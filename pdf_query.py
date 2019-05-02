import pdfquery

pdf = pdfquery.PDFQuery("C:/Users/David/Desktop/MyStuff/2019_STAAR_Alt2_EOC.pdf")

pdf.doc

pdf.doc.catalog # fetch attribute of underlying pdfminer document

pdf.load()

pdf.tree

pdf.tree.write("C:/Users/David/Desktop/MyStuff/test2.xml", pretty_print=True, encoding="utf-8")

