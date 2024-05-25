from mysql.connector import Error

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