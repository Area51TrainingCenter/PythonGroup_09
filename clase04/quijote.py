import PyPDF2

pdf = PyPDF2.PdfFileReader('quijote.pdf')
primera_pagina = list(pdf.pages)[0]
print(primera_pagina.extractText())

for pagina in pdf.pages:
    texto = pagina.extractText()
    # print(texto)

