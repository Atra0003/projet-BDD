import json
import mysql.connector
from mysql.connector import Error
from Notes import buildNote
import xml.etree.ElementTree as ET
from restaurants import buildRestaurant
from convert_tsv_to_json import main_convert


def connect_to_mysql():
    """Connexion à MySQL."""
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='amara',
            password='aaa',  # Remplace par ton mot de passe MySQL
            database='datatest'
        )
        print("La connexion s'est bien établie")
        return conn
    except Error as e:
        print(f"Erreur lors de la connexion à MySQL: {e}")
        return None

def create_database_and_table(tableName, conn):
    """Crée la table si elle n'existe pas."""
    try:
        cursor = conn.cursor()
        cursor.execute("USE datatest")  # Utilisation de la base de données existante
        if(tableName == "Restaurateurs"):
            sql = f'''
            CREATE TABLE IF NOT EXISTS {tableName} (
                id INT AUTO_INCREMENT PRIMARY KEY,
                firstname VARCHAR(255),
                lastname VARCHAR(255),
                street VARCHAR(255),
                number INT,
                zipcode VARCHAR(10),
                city VARCHAR(255),
                country VARCHAR(255),
                restaurant VARCHAR(255),
                CONSTRAINT chk_Country_{tableName} CHECK (country IN ("France", "Belgium"))
            )
        '''

        else:
            sql = f'''
                CREATE TABLE IF NOT EXISTS {tableName} (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    firstname VARCHAR(255),
                    lastname VARCHAR(255),
                    street VARCHAR(255),
                    number INT,
                    zipcode VARCHAR(10),
                    city VARCHAR(255),
                    country VARCHAR(255),
                    restaurant VARCHAR(255),
                    CONSTRAINT chk_Country_{tableName} CHECK (country IN ("France", "Belgium"))
                )
            '''

        cursor.execute(sql)
        print(f"Table {tableName} créée ou déjà existante.")
    except Error as e:
        print(f"Erreur lors de la création de la table {tableName}: {e}")
    finally:
        cursor.close()

def insert_data_to_table(informations, tableName, conn):
    """Insère des données dans la table."""
    try:
        cursor = conn.cursor()
        for customer in informations:
            if(tableName == "Restaurateurs"):
                firstname = customer.get('firstname', '')
                lastname = customer.get('lastname', '')
                address = customer.get('address', {})
                street = address.get('street', '')
                number = address.get('number', 0)
                zipcode = address.get('zipcode', '')
                city = address.get('city', '')
                country = address.get('country', '')
                restaurant = customer.get("restaurant")
                sql = f'''
                    INSERT INTO {tableName} (firstname, lastname, street, number, zipcode, city, country, restaurant)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(sql, (firstname, lastname, street, number, zipcode, city, country, restaurant))
            else:
                firstname = customer.get('firstname', '')
                lastname = customer.get('lastname', '')
                address = customer.get('address', {})
                street = address.get('street', '')
                number = address.get('number', 0)
                zipcode = address.get('zipcode', '')
                city = address.get('city', '')
                country = address.get('country', '')
                sql = f'''
                    INSERT INTO {tableName} (firstname, lastname, street, number, zipcode, city, country)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
                cursor.execute(sql, (firstname, lastname, street, number, zipcode, city, country))

        conn.commit()
        print("L'insertion des données s'est bien passée.")
    except Error as e:
        print(f"Erreur lors de l'insertion des données : {e}")
    finally:
        cursor.close()

if __name__ == '__main__':
    files_path = ['customers.json', 'moderators.json', 'restaurateur.json']
    tableNames = ['Clients', 'Moderateurs', 'Restaurateurs']
    conn = connect_to_mysql()
    if conn is not None and conn.is_connected():
        for i in range(len(files_path)):
            with open(files_path[i], 'r', encoding='utf-8') as file:
                customers = json.load(file)
            create_database_and_table(tableNames[i], conn)
            insert_data_to_table(customers, tableNames[i], conn)
        
        buildRestaurant(conn)
        main_convert()
        buildNote("valid_comments.json", conn)
        buildNote("removed_comments.json", conn)
        
        conn.close()
