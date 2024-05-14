


def buildValidAvit(path, conn, etat):
    cursor = conn.cursor()
    table = "noteValide" if etat == "1" else "noteInvalide"
    avis_modo_col = ", avis_Modo VARCHAR(255)" if etat == "2" else ""
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table} (
            commentaire TEXT,
            note FLOAT,
            dv VARCHAR(255),
            recommandation VARCHAR(20),
            restaurant VARCHAR(255),
            Note_service_livraison VARCHAR(255),
            date_commentaire VARCHAR(255),
            menu_teste TEXT,
            prix_paye FLOAT,
            Heure_de_début_de_repas VARCHAR(20),
            Heure_de_fin_de_repas VARCHAR(20),
            nom_client VARCHAR(255)
            {avis_modo_col}
        )
    """)

    with open(path, 'r') as file:
        next(file)
        for line in file:
            fields = line.strip().split('\t')
            data = tuple(fields[:12]) if etat == "1" else tuple(fields)
            cols = "commentaire, note, dv, recommandation, restaurant, Note_service_livraison, date_commentaire, menu_teste, prix_paye, Heure_de_début_de_repas, Heure_de_fin_de_repas, nom_client"
            if etat == "2":
                cols += ", avis_Modo"
            placeholders = ', '.join(['%s'] * len(data))
            cursor.execute(f"INSERT INTO {table} ({cols}) VALUES ({placeholders})", data)

    conn.commit()
    cursor.close()