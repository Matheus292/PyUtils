from PyPDF2 import PdfMerger
import pikepdf

def mergear_arquivos(lista_arquivo, nome_arquivo):

    if valida_info_arquivo(lista_arquivo, nome_arquivo):

        merger = PdfMerger()

        for arquivo in lista_arquivo:
            merger.append(arquivo)

        merger.write(nome_arquivo,)
        merger.close()
   
def remover_senha_pdf(arquivo, senha, nome_arquivo):
    try:
        pdf = pikepdf.open(arquivo, password=senha,)
        pdf.save(nome_arquivo)
    except:
        print('Erro ao tentar retirar senha do pdf!')

def valida_info_arquivo(lista_arquivo, nome_arquivo):

    if lista_arquivo is None or len(lista_arquivo) == 0:
        print('Por favor informe a lista de arquivos pra mesclar')
        return False
    
    if nome_arquivo is None or nome_arquivo == '':
        print('Por favor informe o nome do arquivo')
        return False
    
    return True
