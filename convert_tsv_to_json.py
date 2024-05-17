import csv
import json

def convert(input_tsv_file):
    # Définir les chemins des fichiers d'entrée et de sortie
    #input_tsv_file = 'valid_comments.tsv'
    output_json_file = input_tsv_file.replace('.tsv', '.json')

    # Liste pour stocker les lignes converties en dictionnaires
    data = []

    # Liste des clés à utiliser
    if input_tsv_file == 'valid_comments.tsv':
        keys = ['commentaire', 'note', 'date', 'recommandation', 'resto', 'Note_service/livraison', 
                'date commentaire', 'menu_teste', 'prix_paye', 'heureA', 'heureD', 'client']
    else:
        keys = ['commentaire', 'note', 'date', 'recommandation', 'resto', 'Note_service/livraison', 
                'date commentaire', 'menu_teste', 'prix_paye', 'heureA', 'heureD', 'client', 'modo']

    # Lire le fichier TSV et convertir les lignes en dictionnaires
    with open(input_tsv_file, 'r', encoding='utf-8') as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        next(tsv_reader)  # Ignorer la première ligne si elle contient des en-têtes
        for row in tsv_reader:
            if len(row) == len(keys):  # Vérifiez que le nombre de colonnes correspond au nombre de clés
                row_dict = {keys[i]: row[i] for i in range(len(keys))}
                data.append(row_dict)
            else:
                print(f"Skipping row with incorrect number of columns: {row}")

    # Convertir les dictionnaires en JSON
    json_data = json.dumps(data, indent=4)

    # Écrire le JSON dans un fichier
    with open(output_json_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print("Conversion terminée. Le fichier JSON a été créé :", output_json_file)


def main_convert():
    convert('valid_comments.tsv')
    convert('removed_comments.tsv')