from mysql.connector import Error

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