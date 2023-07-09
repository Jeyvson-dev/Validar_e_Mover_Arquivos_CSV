import shutil
import os
import re
from datetime import datetime
from UtilClass import UtilClass

util_class = UtilClass()

# Obter a data e hora atuais
data_hora_atual = str(datetime.now())
data_hora_atual = data_hora_atual.replace(" ", "")
current_time_string = re.sub(r'[^\w\s]', '', data_hora_atual)

newName = ''
currentDir = os.getcwd()+'/'
fillesDir = 'FILLES/'
sucessDir = 'SUCESS/'
failDir = 'FAIL/'
validateFille = []

#Varrer os arquivos dentro da pasta "FILLES"
for ListFilles in util_class.list_filles(currentDir+fillesDir):
    #Valida se o arquivo é CSV
    if(util_class.get_extension_filles(ListFilles) == '.csv'):
        try:
            #Varre todo o arquivo 'CSV' e valida se a quantidade de colunas é igual a 6 (seis)
            for colunn in util_class.get_csv_lines(currentDir+fillesDir + ListFilles):
                if(len(colunn) != 6):
                    validateFille.append('ERROR')
                else:
                    validateFille.append('SUCESS')
            #Caso o arquivo não atenda a quantidade de colunas correta move para a pasta ("FAIL")
            if 'ERROR' in validateFille:
                newName = current_time_string + '_' + ListFilles
                os.rename(currentDir + fillesDir + ListFilles, currentDir + fillesDir + newName)
                shutil.move(currentDir + fillesDir + newName, failDir)
                print(f'Fomato do arquivo inválido o arquivo {ListFilles} foi movido para a pasta de {failDir}')
            else:
            # Caso passe por todas às validaçoes é movido para a pasta 'SUCESS'
                newName = current_time_string + '_' + ListFilles
                os.rename(currentDir + fillesDir + ListFilles, currentDir + fillesDir + newName)
                shutil.move(currentDir + fillesDir + newName, failDir)
                print(f'Segue O formato correto o arquivo {ListFilles} foi movido para a pasta de {sucessDir}')
        except:
            print('Erro ao valdiar e Mover o arquivo')
    else:
        #Caso o arquivo não seja CSV move diretamente para a pasta "FAIL"
        newName = current_time_string + '_' + ListFilles
        os.rename(currentDir + fillesDir + ListFilles, currentDir + fillesDir + newName)
        shutil.move(currentDir + fillesDir + newName, failDir)
        print(f'Extensão do arquivo inválida o arquivo {newName} foi movido para a pasta de {failDir}')