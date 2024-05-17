import xml.etree.ElementTree as ET
from mysql.connector import Error

def create_database_and_tables(conn):
    """Crée les bases de données et les tables nécessaires."""
    try:
        cursor = conn.cursor(buffered=True)
        cursor.execute("CREATE DATABASE IF NOT EXISTS datatest")
        cursor.execute("USE datatest")
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Restaurants (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                type VARCHAR(100),
                city VARCHAR(255),
                country VARCHAR(255),
                street VARCHAR(255),
                number INT,
                zipcode VARCHAR(50),
                opening_hours TIME,
                closing_hours TIME,
                price_range VARCHAR(50),
                evaluation DECIMAL(3,1),
                CONSTRAINT chk_price_range CHECK (price_range IN ('bas', 'haut', 'moyen'))

            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dishes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                restaurant_id INT,
                name VARCHAR(255),
                price DECIMAL(5,2),
                FOREIGN KEY (restaurant_id) REFERENCES Restaurants(id)
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Allergens (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100)
            );
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Dish_Allergens (
                dish_id INT,
                allergen_id INT,
                PRIMARY KEY (dish_id, allergen_id),
                FOREIGN KEY (dish_id) REFERENCES Dishes(id),
                FOREIGN KEY (allergen_id) REFERENCES Allergens(id)
            );
        ''')
        print("Tables created successfully.")
    except Error as e:
        print(f"Erreur lors de la création des tables: {e}")
    finally:
        cursor.close()

def parse_xml_and_insert_data(xml_file_path, conn):
    """Parse le fichier XML et insère les données dans la base de données."""
    cursor = conn.cursor(buffered=True)
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    for resto in root.findall('restaurant'):
        name = resto.find('name').text if resto.find('name') is not None else ''
        type_cuisine = resto.find('type').text if resto.find('type') is not None else ''
        price_range = resto.find('price_range').text if resto.find('price_range') is not None else ''
        evaluation = float(resto.find('evaluation').text) if resto.find('evaluation') is not None else 0.0
        address = resto.find('address')
        city = address.find('city').text if address is not None and address.find('city') is not None else ''
        country = address.find('country').text if address is not None and address.find('country') is not None else ''
        street = address.find('street').text if address is not None and address.find('street') is not None else ''
        number = int(address.find('number').text) if address is not None and address.find('number') is not None else 0
        zipcode = address.find('zipcode').text if address is not None and address.find('zipcode') is not None else ''
        opening_hours = resto.find('opening_hours/opening').text if resto.find('opening_hours/opening') is not None else '00:00:00'
        closing_hours = resto.find('opening_hours/closing').text if resto.find('opening_hours/closing') is not None else '00:00:00'
        
        cursor.execute("INSERT INTO Restaurants (name, type, city, country, street, number, zipcode, opening_hours, closing_hours, price_range, evaluation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (name, type_cuisine, city, country, street, number, zipcode, opening_hours, closing_hours, price_range, evaluation))
        restaurant_id = cursor.lastrowid

        for dish in resto.find('menu').findall('dish'):
            dish_name = dish.find('name').text if dish.find('name') is not None else ''
            price = float(dish.find('price').text.strip('€')) if dish.find('price') is not None else 0.0
            cursor.execute("INSERT INTO Dishes (restaurant_id, name, price) VALUES (%s, %s, %s)", (restaurant_id, dish_name, price))
            dish_id = cursor.lastrowid

            allergens = dish.find('allergens')
            if allergens is not None and allergens.text != 'None':
                for allergen in allergens.findall('allergen'):
                    allergen_name = allergen.text
                    cursor.execute("INSERT IGNORE INTO Allergens (name) VALUES (%s)", (allergen_name,))
                    cursor.execute("SELECT id FROM Allergens WHERE name = %s", (allergen_name,))
                    allergen_id = cursor.fetchone()[0]
                    cursor.execute("INSERT INTO Dish_Allergens (dish_id, allergen_id) VALUES (%s, %s)", (dish_id, allergen_id))

    conn.commit()
    print("Data inserted successfully.")
    cursor.close()

def buildRestaurant(conn):
    print("pass")
    create_database_and_tables(conn)
    xml_file_path = 'restos.xml'  # Assure-toi que le chemin est correct
    parse_xml_and_insert_data(xml_file_path, conn)
