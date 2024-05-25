from mysql.connector import Error

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