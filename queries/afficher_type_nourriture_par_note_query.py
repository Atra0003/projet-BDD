from mysql.connector import Error

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