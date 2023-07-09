import os
import csv

class UtilClass:
    def get_extension_filles(self, filles_way):
        _, extension = os.path.splitext(filles_way)
        return extension

    def list_filles(self, diretory):
        filles = os.listdir(diretory)
        return filles

    def get_csv_lines(self, fille_name):
        lines = []

        # Abrir o arquivo CSV em modo leitura
        with open(fille_name, "r", newline="") as csv_fille:
            csv_reader = csv.reader(csv_fille)

            # Ler todas as linhas do arquivo CSV
            for line in csv_reader:
                # Adicionar a linha à lista de linhas
                lines.append(line)

        return lines