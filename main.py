from PyPDF2 import PdfReader, PdfWriter
import os

def encrypter(file):
    reader = PdfReader(file)
    writer = PdfWriter()

    password = input('Qual vai ser a senha para acessar o arquivo?\n')

    for page in reader.pages:
        writer.add_page(page)

    writer.encrypt(password)

    os.remove(file)

    with open(file, "wb") as f:
        writer.write(f)


def takeFile():
    try:
        file = input('Qual o nome do arquivo (em PDF)\n')
        encrypter(file)

    except:
        check = file.split('.')
        if check[-1] != 'pdf':
            print('O arquivo deve estar em pdf\n\n---\n')
            takeFile()


    


takeFile()
