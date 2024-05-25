import json
import mysql.connector
from datetime import datetime

def buildNote(json_file, conn):
    # Déterminer le nom de la table à partir du nom du fichier
    if 'valid' in json_file:
        table_name = "NoteValid"
    else:
        table_name = "NoteRemoved"

    # Lire le fichier JSON
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    cursor = conn.cursor()

    # Création de la table
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INT AUTO_INCREMENT PRIMARY KEY,
            commentaire LONGTEXT,
            note FLOAT CHECK (note >= 0 AND note <= 5),
            date DATETIME,
            recommandation VARCHAR(255),
            CHECK (recommandation IN ('recommandé', 'à éviter d''urgence', 'déconseillé')),
            resto VARCHAR(255),
            note_service_livraison FLOAT CHECK (note_service_livraison >= 0 AND note_service_livraison <= 5),
            date_commentaire DATE,
            menu_teste TEXT,
            nb_plat INT,
            prix_paye DECIMAL(10, 2),
            heureA INT,
            heureD INT,
            client VARCHAR(255),
            {'' if table_name == 'NoteValid' else 'modo VARCHAR(255),'}
            CHECK (heureA < heureD)
        )
    """)

    # Insertion des données
    for entry in data:
        commentaire = entry.get('commentaire', '')
        note = float(entry.get('note', 0.0))
        date_str = entry.get('date', '')
        recommandation = entry.get('recommandation', '')
        resto = entry.get('resto', '')
        note_service_livraison = float(entry.get('Note_service/livraison', '')[-1])  # Convertir en float et ne stocker que le dernier caractère
        date_commentaire = entry.get('date commentaire', '')
        menu_teste = entry.get('menu_teste', '')
        nb_plat = len(menu_teste.split(';'))
        prix_paye = float(entry.get('prix_paye', 0.0))
        heureA = int(entry.get('heureA', 0))  # Convertir en entier
        heureD = int(entry.get('heureD', 0))  # Convertir en entier
        client = entry.get('client', '')
        modo = entry.get('modo', '') if table_name == "NoteRemoved" else None

        # Convertir la date au format 'YYYY-MM-DD HH:MM:SS'
        formatted_date = datetime.strptime(date_str, '%m/%d/%Y %H:%M').strftime('%Y-%m-%d %H:%M:%S')

        if table_name == "NoteValid":
            sql = f"""
                INSERT INTO {table_name} (commentaire, note, date, recommandation, resto, note_service_livraison, 
                                          date_commentaire, menu_teste, nb_plat, prix_paye, heureA, heureD, client)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (commentaire, note, formatted_date, recommandation, resto, note_service_livraison,
                                 date_commentaire, menu_teste, nb_plat, prix_paye, heureA, heureD, client))
        else:
            sql = f"""
                INSERT INTO {table_name} (commentaire, note, date, recommandation, resto, note_service_livraison, 
                                          date_commentaire, menu_teste, nb_plat, prix_paye, heureA, heureD, client, modo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (commentaire, note, formatted_date, recommandation, resto, note_service_livraison,
                                 date_commentaire, menu_teste, nb_plat, prix_paye, heureA, heureD, client, modo))

    conn.commit()
    cursor.close()

if __name__ == '__main__':
    # Configuration de la base de données
    conn = mysql.connector.connect(
        host='localhost',
        user='amara',
        password='aaa',  # Remplace par ton mot de passe MySQL
        database='datatest'
    )

    buildNote('donnees_projet/valid_comments.json', conn)
    buildNote('donnees_projet/removed_comments.json', conn)

    conn.close()
