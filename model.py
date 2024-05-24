from datetime import datetime
import mysql.connector
from mysql.connector import Error

class Model:
    def __init__(self):
        self.connection = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='datatest',
                user='root',
                password=''
            )
            if connection.is_connected():
                print("La connexion s'est bien etablie")
                return connection
        except Error as e:
            print(f"Erreur de connexion a MySQL: {e}")
            return None
        
    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()

    def connexion_query(self, lName, fName, password, isRestaurateur, isModerateur):
        """
        Requete de connexion
        """
        try:
            with self.connection.cursor() as cursor:
                if isRestaurateur:
                    query = "SELECT * FROM restaurateurs WHERE lastname=%s AND firstname=%s"
                elif isModerateur:
                    query = "SELECT * FROM Moderateurs WHERE lastname=%s AND firstname=%s"
                else:
                    query = "SELECT * FROM Clients WHERE lastname=%s AND firstname=%s"
                cursor.execute(query, (lName, fName))
                result = cursor.fetchone()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def inscription_query(self, lName, fName, password, isRestaurateur, isModerateur, adRue, adNumero, adVille, adCodePostal, adPays):
        """
        Requete d'inscription
        """
        try:
            with self.connection.cursor() as cursor:
                if isRestaurateur:
                    query = "INSERT INTO Restaurateurs (lastname, firstname, street, number, city, zipcode, country, restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                elif isModerateur:
                    query = "INSERT INTO Moderateurs (lastname, firstname, street, number, city, zipcode, country, restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                else:
                    query = "INSERT INTO Clients (lastname, firstname, street, number, city, zipcode, country, restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (lName, fName, adRue, adNumero, adVille, adCodePostal, adPays, None))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def ajouter_avis_query(self, nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix, nomClient, prenomClient):
        """
        Requete d'ajout d'avis
        """
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO notevalid (resto, date, heureA, heureD, menu_teste, prix_paye, client) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                client = prenomClient + " " + nomClient
                cursor.execute(query, (nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix, client))
                self.connection.commit()
                avis_id = cursor.lastrowid  # Prend l'id de l'avis ajoute
                return avis_id
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def vers_ajouter_note_query(self, id_avis, commentaire, note, note_service_livraison, recommendation):
        """
        Requete d'ajout de note
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                INSERT INTO notevalid (id, commentaire, note, recommandation, note_service_livraison, date_commentaire)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    commentaire = VALUES(commentaire),
                    note = VALUES(note),
                    recommandation = VALUES(recommandation),
                    note_service_livraison = VALUES(note_service_livraison),
                    date_commentaire = VALUES(date_commentaire)
                """
                date_commentaire = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute(query, (id_avis, commentaire, note, recommendation, note_service_livraison, date_commentaire))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def consulter_avis_query(self, nomRestaurant, parNote, parTypeNourriture, parGammePrix):
        """
        Requete de consultation d'avis
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT nv.client, nv.commentaire
                FROM notevalid nv
                INNER JOIN restaurants r ON nv.resto = r.name
                WHERE 1=1
                """
                params = []
                if nomRestaurant != "Nom du Restaurant" and nomRestaurant != "":
                    query += " AND r.name=%s"
                    params.append(nomRestaurant)
                if parNote != "Par Note" and parNote != "":
                    query += " AND nv.note=%s"
                    params.append(parNote)
                if parTypeNourriture != "Par Type de Nourriture" and parTypeNourriture != "":
                    query += " AND r.type=%s"
                    params.append(parTypeNourriture)
                if parGammePrix != "Par Game de Prix" and parGammePrix != "":
                    query += " AND r.price_range=%s"
                    params.append(parGammePrix)
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def consulter_resto_query(self, nomRestaurant):
        """
        Requete de consultation de restaurant
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT * FROM restaurants
                WHERE 1=1
                """
                params = []
                if nomRestaurant != "Nom du Restaurant" or nomRestaurant != "":
                    query += " AND name=%s"
                    params.append(nomRestaurant)
                
                cursor.execute(query, params)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def supprimer_avis_query(self, avisSupprime, justificatif):
        """
        Requete de suppression d'avis
        """
        try:
            with self.connection.cursor() as cursor:
                # On recupere les infor de l'avis a supprimer
                query_select = """
                SELECT *
                FROM notevalid
                WHERE commentaire = %s
                """
                cursor.execute(query_select, (avisSupprime,))
                avis = cursor.fetchone()
                if not avis:
                    return False
                
                # On deplacer l'avis dans noteremoved
                self.deplacer_avis_invalide(avis, justificatif)
                
                # On supprimer l'avis de notevalid
                query_delete = "DELETE FROM notevalid WHERE commentaire=%s"
                cursor.execute(query_delete, (avisSupprime,))
                self.connection.commit()
                
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def deplacer_avis_invalide(self, avis, justificatif):
        """
        Deplace l'avis supprime dans les avis invalides
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                INSERT INTO noteremoved (id, commentaire, note, date, recommandation, resto, note_service_livraison, 
                date_commentaire, menu_teste, prix_paye, heureA, heureD, client, modo)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(query, (avis[0], avis[1], avis[2], avis[3], avis[4], avis[5], avis[6],
                                          avis[7], avis[8], avis[9], avis[10], avis[11], avis[12], justificatif))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def verifier_existance_restaurant_query(self, nomRestaurant):
        """
        Verifie si le restaurant existe
        """
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT * FROM restaurants WHERE name=%s"
                cursor.execute(query, (nomRestaurant,))
                result = cursor.fetchone()
                return True if result else False
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def ajouter_note_query(self, nomRestaurant, dateVisite, commentaire, noteLivraison, noteService, recommendation):
        """
        Requete d'ajout de note
        """
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO notevalid (resto, date, commentaire, note_service_livraison, note, recommandation) VALUES (%s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nomRestaurant, dateVisite, commentaire, noteLivraison, noteService, recommendation))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def ajouter_restaurant_query(self, nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, typeNourriture, gammePrix, debutOuverture, finOuverture, faitLivraison):
        """
        Requete d'ajout de restaurant
        """
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO restaurants (name, street, number, city, zipcode, country, type, price_range, opening_hours, closing_hours, delivery) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, typeNourriture, gammePrix, debutOuverture, finOuverture, faitLivraison))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
        
    def ajouter_restaurant_restaurateur(self, nomRestaurant, nomClient, prenomClient):
        """
        Requete d'ajout de restaurant au restaurateur
        """
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE restaurateurs SET restaurant=%s WHERE lastname=%s AND firstname=%s"
                cursor.execute(query, (nomRestaurant, nomClient, prenomClient))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def verifier_proprietaire_restaurant(self, nomRestaurant, nomClient, prenomClient):
        """
        Verifie si l'utilisateur est bien le proprietaire du restaurant
        """
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT restaurant FROM restaurateurs WHERE lastname=%s AND firstname=%s"
                cursor.execute(query, (nomClient, prenomClient))
                result = cursor.fetchone()
                for restaurant in result:
                    if restaurant == nomRestaurant:
                        return True
                return False
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def modifier_restaurant_query(self, nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, parTypeNourriture, parGammePrix, debutOuverture, finOuverture, faitLivraison):
        """
        Requete de modification de restaurant
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                UPDATE restaurants
                SET street=%s, number=%s, city=%s, zipcode=%s, country=%s, type=%s, price_range=%s, opening_hours=%s, closing_hours=%s, delivery=%s
                WHERE name=%s
                """
                cursor.execute(query, (adRue, adNumero, adVille, adCodePostal, adPays, parTypeNourriture, parGammePrix, debutOuverture, finOuverture, faitLivraison, nomRestaurant))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def charger_plats_restaurant_query(self, nomRestaurant):
        """
        Requete de chargement des plats du restaurant
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT d.name, d.price, a.name AS allergene
                FROM dishes d
                LEFT JOIN dish_allergens da ON d.id = da.dish_id
                LEFT JOIN allergens a ON da.allergen_id = a.id
                WHERE d.restaurant_id = (SELECT id FROM restaurants WHERE name = %s)
                """
                cursor.execute(query, (nomRestaurant,))
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def ajouter_plats_query(self, nomRestaurant, nvPlat, prixNvPlat, listeNvPlats):
        """
        Requete d'ajout de plats
        """
        try:
            with self.connection.cursor() as cursor:
                # On recupere l'identifiant du restaurant
                cursor.execute("SELECT id FROM restaurants WHERE name = %s", (nomRestaurant,))
                restaurant_id = cursor.fetchone()
                if not restaurant_id:
                    raise ValueError("Restaurant non trouve.")
                restaurant_id = restaurant_id[0]

                # On ajoute le nouveau plat
                query = "INSERT INTO dishes (restaurant_id, name, price) VALUES (%s, %s, %s)"
                cursor.execute(query, (restaurant_id, nvPlat, prixNvPlat))
                dish_id = cursor.lastrowid

                # On ajoute les allergenes
                if nvPlat in listeNvPlats:
                    for allergen in listeNvPlats[nvPlat]:
                        # On recupere ou bien insere l'identifiant de l'allergene
                        cursor.execute("SELECT id FROM allergens WHERE name = %s", (allergen,))
                        allergen_id = cursor.fetchone()
                        if not allergen_id:
                            cursor.execute("INSERT INTO allergens (name) VALUES (%s)", (allergen,))
                            allergen_id = cursor.lastrowid
                        else:
                            allergen_id = allergen_id[0]

                        # On insere dans la table dish_allergens
                        cursor.execute("INSERT INTO dish_allergens (dish_id, allergen_id) VALUES (%s, %s)",
                                    (dish_id, allergen_id))

                self.connection.commit()
                return True
        except Exception as e:
            print(f"Erreur lors de la requête: {e}")
            return False

    def consulter_statistique_query(self, nomRestaurant):
        """
        Requete de consultation de statistique
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT
                    (SELECT COUNT(*) FROM notevalid WHERE resto = %s) AS nombre_avis,
                    (SELECT AVG(note) FROM notevalid WHERE resto = %s) AS note_moyenne,
                    (SELECT AVG(note_service_livraison) FROM notevalid WHERE resto = %s) AS note_moyenne_livraison,
                    (SELECT menu_teste FROM notevalid WHERE resto = %s
                    GROUP BY menu_teste
                    ORDER BY COUNT(*) DESC
                    LIMIT 1) AS plat_populaire
                """
                cursor.execute(query, (nomRestaurant, nomRestaurant, nomRestaurant, nomRestaurant))
                result = cursor.fetchone()
                return [result] if result else []
        except Error as e:
            print(f"Erreur lors de la requête: {e}")
            return False

    def afficher_avis_sup3_query(self):
        """
        Requete d'affichage des avis avec une note superieure a 3
        """
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT name, evaluation FROM Restaurants WHERE evaluation >= 3"
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
        
    def afficher_plat_plus_cher_query(self):
        """
        Requete d'affichage du plat le plus cher
        """
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT name, price FROM dishes ORDER BY price DESC LIMIT 1"
                cursor.execute(query)
                result = cursor.fetchone()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def afficher_clients_mexicains_query(self):
        """
        Requete d'affichage des 10 clients ayant consomme le plus de plats mexicains
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT nv.client, COUNT(*) AS nombre_plats_mexicains
                FROM notevalid nv
                JOIN dishes d ON nv.resto = (SELECT name FROM restaurants WHERE id = d.restaurant_id)
                JOIN restaurants r ON d.restaurant_id = r.id
                WHERE r.type = 'mexicain'
                GROUP BY nv.client
                ORDER BY nombre_plats_mexicains DESC
                LIMIT 10
                """
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def afficher_plats_asiatiques_query(self):
        """
        Requete d'affichage du restaurant non-asiatique proposant le plus de plats asiatiques
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT r.name, COUNT(*) AS nombre_plats_asiatiques
                FROM dishes d
                JOIN restaurants r ON d.restaurant_id = r.id
                JOIN (
                    SELECT p.name AS plat_name
                    FROM dishes p
                    JOIN restaurants r ON p.restaurant_id = r.id
                    WHERE r.type = 'asiatique'
                    GROUP BY p.name
                ) AS plats_asiatiques ON d.name = plats_asiatiques.plat_name
                WHERE r.type != 'asiatique'
                GROUP BY r.name
                ORDER BY nombre_plats_asiatiques DESC
                LIMIT 1
                """
                cursor.execute(query)
                result = cursor.fetchone()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def afficher_pire_code_postal_query(self):
        """
        Requete d'affichage du pire code postal
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT r.zipcode, AVG(nv.note) AS note_moyenne
                FROM notevalid nv
                JOIN restaurants r ON nv.resto = r.name
                GROUP BY r.zipcode
                ORDER BY note_moyenne ASC
                LIMIT 1
                """
                cursor.execute(query)
                result = cursor.fetchone()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def afficher_type_nourriture_par_note_query(self):
        """
        Requete d'affichage du type de nourriture par note
        """
        try:
            with self.connection.cursor() as cursor:
                # La requete actuelle ne fonctionne pas et donne une note moyenne par type de nourriture
                query = """
                SELECT r.type, AVG(nv.note) AS note_moyenne
                FROM notevalid nv
                JOIN restaurants r ON nv.resto = r.name
                GROUP BY r.type
                """
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False