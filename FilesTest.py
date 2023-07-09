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

new_name = ''
current_dir = os.getcwd()+'/'
filles_dir = 'FILLES/'
sucess_dir = 'SUCESS/'
fail_dir = 'FAIL/'
validate_fille = []

#Varrer os arquivos dentro da pasta "FILLES"
for ListFilles in util_class.list_filles(current_dir+filles_dir):
    #Valida se o arquivo é CSV
    if(util_class.get_extension_filles(ListFilles) == '.csv'):
        try:
            #Varre todo o arquivo 'CSV' e valida se a quantidade de colunas é igual a 6 (seis)
            for colunn in util_class.get_csv_lines(current_dir+filles_dir + ListFilles):
                if(len(colunn) != 6):
                    validate_fille.append('ERROR')
                else:
                    validate_fille.append('SUCESS')
            #Caso o arquivo não atenda a quantidade de colunas correta move para a pasta ("FAIL")
            if 'ERROR' in validate_fille:
                new_name = current_time_string + '_' + ListFilles
                os.rename(current_dir + filles_dir + ListFilles, current_dir + filles_dir + new_name)
                shutil.move(current_dir + filles_dir + new_name, fail_dir)
                print(f'Fomato do arquivo inválido o arquivo {ListFilles} foi movido para a pasta de {fail_dir}')
            else:
            # Caso passe por todas às validaçoes é movido para a pasta 'SUCESS'
                new_name = current_time_string + '_' + ListFilles
                os.rename(current_dir + filles_dir + ListFilles, current_dir + filles_dir + new_name)
                shutil.move(current_dir + filles_dir + new_name, sucess_dir)
                print(f'Segue O formato correto o arquivo {ListFilles} foi movido para a pasta de {sucess_dir}')
        except:
            print('Erro ao valdiar e Mover o arquivo')
    else:
        #Caso o arquivo não seja CSV move diretamente para a pasta "FAIL"
        new_name = current_time_string + '_' + ListFilles
        os.rename(current_dir + filles_dir + ListFilles, current_dir + filles_dir + new_name)
        shutil.move(current_dir + filles_dir + new_name, fail_dir)
        print(f'Extensão do arquivo inválida o arquivo {new_name} foi movido para a pasta de {fail_dir}')