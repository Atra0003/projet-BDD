from mysql.connector import Error

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