from mysql.connector import Error

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