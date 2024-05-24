import sys
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI.UIMainWindow import Ui_MainWindow
from UI.UIInscription import Ui_InscriptionWindow
from UI.UIConnexion import Ui_ConnexionWindow
from UI.UIRestaurateurMenu import Ui_RestaurateurMenu
from UI.UIClientMenu import Ui_ClientMenu
from UI.UIAjouterAvis import Ui_AjouterAvis
from UI.UIConsulterAvis import Ui_ConsulterAvis
from UI.UIConsulterResto import Ui_ConsulterResto
from UI.UIAjouterNote import Ui_AjouterNote
from UI.UIVersAjouterNote import Ui_VersAjouterNote
from UI.UIAjouterResto import Ui_AjouterResto
from UI.UIModifierResto import Ui_ModifierResto
from UI.UIStats import Ui_Stats
from UI.UIAjouterPlat import Ui_AjouterPlat
from UI.UIConsulterAvisModo import Ui_ConsulterAvisModo
from UI.UISupprimerAvisModo import Ui_SupprimerAvisModo
from UI.UIOther import Ui_Other
from UI.UIAvisSup3 import Ui_AvisSup3
from UI.UIPlatPlusCher import Ui_PlatPlusCher
from UI.UIClientMangeantMexicain import Ui_ClientMangeantMexicain
from UI.UIPlatAsiatique import Ui_PlatAsiatique
from UI.UIPireCodePostal import Ui_PireCodePostal
from UI.UITypeNourritureParNote import Ui_TypeNourritureParNote

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Constructeur de la classe MainWindow
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonSignIn.clicked.connect(self.open_conexion_window)
        self.ui.buttonSignUp.clicked.connect(self.open_inscription_window)
        self.nom = ""
        self.prenom = ""
        self.isModerateur = False
        self.isRestaurateur = False
        # Connexion a la bdd
        self.connection = self.create_connection()
    
    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='datatest',
                user='amara',
                password='aaa'
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
            print("La connexion a ete fermee")

    def open_conexion_window(self):
        """
        Ouverture de la fenetre de connexion
        """
        self.ui = Ui_ConnexionWindow()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonSignIn.clicked.connect(self.get_connexion_data)

    def get_connexion_data(self):
        """
        Recuperation des donnees de connexion
        """
        self.nom = self.ui.lineLName.text()
        self.prenom = self.ui.lineFName.text()
        lName = self.nom
        fName = self.prenom
        password = self.ui.linePassword.text()
        self.isRestaurateur = self.ui.checkBoxIsRestaurateur.isChecked()
        self.isModerateur = self.ui.checkBoxIsModerateur.isChecked()
        print("Nom: ", lName)
        print("Prenom: ", fName)
        print("Mot de passe : ", password)
        print("IsRestaurateur: ", self.isRestaurateur)
        print("IsModerateur: ", self.isModerateur)
        # Verifie les informations de connexion dans la bdd
        if self.connexion_query(lName, fName, password):
            # Si l'utilisateur existe dans la database, on affiche le menu principal
            self.open_menu()
        else:
            # Affiche un message d'erreur si les informations de connexion sont incorrectes
            self.ui.labelError.setText("Nom ou prénom incorrect. Veuillez réessayer.")
    
    def connexion_query(self, lName, fName, password):
        """
        Requete de connexion
        """
        try:
            with self.connection.cursor() as cursor:
                if self.isRestaurateur:
                    query = "SELECT * FROM restaurateurs WHERE lastname=%s AND firstname=%s"
                elif self.isModerateur:
                    query = "SELECT * FROM Moderateurs WHERE lastname=%s AND firstname=%s"
                else:
                    query = "SELECT * FROM Clients WHERE lastname=%s AND firstname=%s"
                cursor.execute(query, (lName, fName))
                result = cursor.fetchone()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def open_inscription_window(self):
        """
        Ouverture de la fenetre d'inscription
        """
        self.ui = Ui_InscriptionWindow()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonSignUp.clicked.connect(self.get_inscription_data)

    def get_inscription_data(self):
        """
        Recuperation des donnees d'inscription
        """
        self.nom = self.ui.lineLName.text()
        self.prenom = self.ui.lineFName.text()
        lName = self.nom
        fName = self.prenom
        password = self.ui.linePassword.text()
        adRue = self.ui.lineAdRue.text()
        adNumero = self.ui.lineAdNum.text()
        adVille = self.ui.lineAdVille.text()
        adCodePostal = self.ui.lineAdPostal.text()
        adPays = self.ui.lineAdPays.text()
        self.isModerateur = self.ui.checkBoxIsModerateur.isChecked()
        self.isRestaurateur = self.ui.checkBoxIsRestaurateur.isChecked()
        print("Nom: ", lName)
        print("Prenom: ", fName)
        print("Mot de passe : ", password)
        print("Adresse: ", adRue, adNumero, adVille, adCodePostal, adPays)
        # Verifie les informations de connexion dans la bdd
        if self.inscription_query(lName, fName, password, adRue, adNumero, adVille, adCodePostal, adPays):
            # Si l'utilisateur existe dans la database, on affiche le menu principal
            self.open_menu()
        else:
            # Affiche un message d'erreur si les informations d'inscription sont incorrectes
            self.ui.labelError.setText("Saisie incorrecte. Veuillez réessayer.")

    def inscription_query(self, lName, fName, password, adRue, adNumero, adVille, adCodePostal, adPays):
        """
        Requete d'inscription
        """
        try:
            with self.connection.cursor() as cursor:
                if self.isRestaurateur:
                    query = "INSERT INTO Restaurateurs (lastname, firstname, street, number, city, zipcode, country, restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                elif self.isModerateur:
                    query = "INSERT INTO Moderateurs (lastname, firstname, street, number, city, zipcode, country, restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                else:
                    query = "INSERT INTO Clients (lastname, firstname, street, number, city, zipcode, country, restaurant) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(query, (lName, fName, adRue, adNumero, adVille, adCodePostal, adPays, None))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def open_menu(self):
        """
        Ouverture du menu principal
        """
        if self.isRestaurateur:
            # Si "IsRestaurateur" a ete cochee, on affiche le menu du restaurateur
            self.ui = Ui_RestaurateurMenu()
            self.ui.setupUi(self)
            self.restaurateur_menu()
        else:
            # Sinon, on affiche le menu du client
            self.ui = Ui_ClientMenu()
            self.ui.setupUi(self)
            self.client_menu()

    def client_menu(self):
        """
        Fenetre du menu principal du client
        """
        self.ui.pushButtonAddOpinion.clicked.connect(self.ajouter_avis)
        self.ui.pushButtonViewOpinion.clicked.connect(self.consulter_avis)
        self.ui.pushButtonViewRestaurants.clicked.connect(self.consulter_resto)
        self.ui.pushButtonAddNote.clicked.connect(self.ajouter_note)
        self.ui.pushButtonOther.clicked.connect(self.autres_requetes)
    
    def restaurateur_menu(self):
        """
        Fenetre du menu principal du restaurateur
        """
        self.ui.pushButtonAddResto.clicked.connect(self.ajouter_restaurant)
        self.ui.pushButtonEditResto.clicked.connect(self.modifier_restaurant)
        self.ui.pushButtonAddMeals.clicked.connect(self.ajouter_plat)
        self.ui.pushButtonCheckOpinions.clicked.connect(self.consulter_avis)
        self.ui.pushButtonStat.clicked.connect(self.consulter_statistique)
        self.ui.pushButtonOther.clicked.connect(self.autres_requetes)

    def ajouter_avis(self):
        """
        Fenetre d'ajout d'avis
        """
        self.ui = Ui_AjouterAvis()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonBoxOkRetour.accepted.connect(self.get_ajouter_avis_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client)
    
    def get_ajouter_avis_data(self):
        """
        Recuperation des donnees d'ajout d'avis
        """
        nomRestaurant = self.ui.lineEditRestoName.text()
        dateVisite = self.ui.dateEdit.date().toString("yyyy-MM-dd")
        heureDebut = self.ui.timeEditHeureDebut.time().toString("hh")
        heureFin = self.ui.timeEditHeureFin.time().toString("hh")
        platsCommandes = self.ui.plainTextEditPlatCommande.toPlainText()
        prix = self.ui.lineEditPrixPaye.text()
        print("Nom du restaurant: ", nomRestaurant)
        print("Date de visite: ", dateVisite)
        print("Heure de debut: ", heureDebut)
        print("Heure de fin: ", heureFin)
        print("Plats commandes: ", platsCommandes)
        print("Prix paye: ", prix)
        # On ajoute l'avis dans la bdd
        id_avis = self.ajouter_avis_query(nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix)
        if id_avis > 0:
            print("Avis ajoute avec succes")
            self.ui.labelError.setText("Avis ajoute avec succes. Merci!")
            self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            self.vers_ajouter_note(nomRestaurant, id_avis)
        else:
            self.ui.labelError.setText("Erreur lors de l'ajout de l'avis. Veuillez reessayer.")

    def ajouter_avis_query(self, nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix):
        """
        Requete d'ajout d'avis
        """
        try:
            with self.connection.cursor() as cursor:
                query = "INSERT INTO notevalid (resto, date, heureA, heureD, menu_teste, prix_paye, client) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                client = self.prenom + " " + self.nom
                cursor.execute(query, (nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix, client))
                self.connection.commit()
                avis_id = cursor.lastrowid  # Get the id of the inserted row
                print("Avis id: ", avis_id)
                return avis_id
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def vers_ajouter_note(self, nomRestaurant, id_avis):
        """
        Fenetre d'ajout de note
        """
        self.ui = Ui_VersAjouterNote()
        self.ui.setupUi(self)
        self.ui.labelNomResto.setText(nomRestaurant)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonBoxOkRetour.accepted.connect(lambda: self.get_ajouter_note_avis(id_avis))
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client)

    def get_ajouter_note_avis(self, id_avis):
        """
        Recuperation des donnees d'ajout de note
        """
        commentaire = self.ui.plainTextEditCommentaire.toPlainText()
        note = self.ui.spinBoxNoteService.value()
        note_service_livraison = self.ui.spinBoxNoteLivraison.value()
        recommendation = self.ui.comboBoxRecommendation.currentText()
        print("Commentaire: ", commentaire)
        print("Note: ", note)
        print("Note service livraison: ", note_service_livraison)
        print("Recommendation: ", recommendation)
        # On ajoute la note dans la bdd
        if self.vers_ajouter_note_query(id_avis, commentaire, note, note_service_livraison, recommendation):
            print("Note ajoutee avec succes")
            self.ui.labelError.setText("Note ajoutee avec succes. Merci!")
            self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.ui.labelError.setText("Erreur lors de l'ajout de la note. Veuillez reessayer.")
        
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

    def consulter_avis(self):
        """
        Fenetre de consultation d'avis
        """
        if self.isModerateur:
            self.ui = Ui_ConsulterAvisModo()
            self.ui.setupUi(self)
            # On recupere les donnees de connexion entrees par l'utilisateur
            self.ui.buttonBoxOkRetour.accepted.connect(self.get_consulter_avis_data)
            # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client ou bien du restaurateur
            if self.isRestaurateur:
                self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_restaurateur)
                self.ui.pushButtonDelete.clicked.connect(self.supprimer_avis)
            else:
                self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client)
                self.ui.pushButtonDelete.clicked.connect(self.supprimer_avis)

        else:
            self.ui = Ui_ConsulterAvis()
            self.ui.setupUi(self)
            # On recupere les donnees de connexion entrees par l'utilisateur
            self.ui.buttonBoxOkRetour.accepted.connect(self.get_consulter_avis_data)
            # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client ou bien du restaurateur
            if self.isRestaurateur:
                self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_restaurateur)
            else:
                self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client) 

    def get_consulter_avis_data(self):
        """
        Recuperation des donnees de consultation d'avis
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()
        parNote = self.ui.lineEditParNote.text()
        parTypeNourriture = self.ui.lineEditParNourriture.text()
        parGammePrix = self.ui.lineEditParPrix.text()
        print("Nom du restaurant: ", nomRestaurant)
        print("Par note: ", parNote)
        print("Par type de nourriture: ", parTypeNourriture)
        print("Par gamme de prix: ", parGammePrix)
        # On utilise les donnees recuperees et cherche les avis dans la bdd
        listeResultat = self.consulter_avis_query(nomRestaurant, parNote, parTypeNourriture, parGammePrix)
        if listeResultat:
            print("Avis trouve")
            listeAvis = [f"{avis[0]} : {avis[1]}" for avis in listeResultat]
            print("Liste des avis: ", listeAvis)
            self.ui.listWidgetAvis.addItems(listeAvis)
        else:
            print("Aucun avis trouve")
    
    def consulter_avis_query(self, nomRestaurant, parNote, parTypeNourriture, parGammePrix):
        """
        Requete de consultation d'avis
        """
        try:
            with self.connection.cursor() as cursor:
                query = """
                SELECT client, commentaire FROM notevalid
                WHERE 1=1
                """
                params = []
                if nomRestaurant != "Nom du Restaurant" and nomRestaurant != "":
                    query += " AND resto=%s"
                    params.append(nomRestaurant)
                if parNote != "Par Note" or parNote != "":
                    query += " AND note=%s"
                    params.append(parNote)
                if parTypeNourriture != "Par Type de Nourriture" and parTypeNourriture != "":
                    query += " AND menu_teste=%s"
                    params.append(parTypeNourriture)
                if parGammePrix != "Par Game de Prix" and parGammePrix != "":
                    query += " AND prix_paye=%s"
                    params.append(parGammePrix)
                cursor.execute(query, params)
                result = cursor.fetchall()
                print("Resultat de la requete: ", result)
                self.ui.listWidgetAvis.clear()
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def consulter_resto(self):
        """
        Fenetre de consultation de restaurant
        """
        self.ui = Ui_ConsulterResto()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonBoxOkRetour.accepted.connect(self.get_consulter_resto_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client)

    def get_consulter_resto_data(self):
        """
        Recuperation des donnees de consultation de restaurant
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()

        # On utilise les donnees recuperees et cherche les restaurants dans la bdd
        listeResultat = self.consulter_resto_query(nomRestaurant)
        if listeResultat:
            print("Restaurant trouve")
            self.ui.labelInfoRestoAdRue.setText(listeResultat[0][5])
            self.ui.labelInfoRestoAdVille.setText(listeResultat[0][3])
            self.ui.labelInfoRestoAdPays.setText(listeResultat[0][4])
            self.ui.labelInfoRestoAdNumero.setText(str(listeResultat[0][6]))
            self.ui.labelInfoRestoAdCodePostal.setText(str(listeResultat[0][7]))
            self.ui.labelInfoEvaluation.setText(str(listeResultat[0][12]))
            self.ui.labelHeureOuverture.setText(str(listeResultat[0][8]))
            self.ui.labelHeureFermeture.setText(str(listeResultat[0][9]))
            self.ui.labelInfoGammePrix.setText(listeResultat[0][10])
            self.ui.labelInfoTypeNourriture.setText(listeResultat[0][2])
            if listeResultat[0][11] == "Yes":
                self.ui.checkBoxFaitLivraison.setChecked(True)

            self.ui.labelError.setText("Restaurant trouve. Merci!")
            self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            print("Liste des infos du restaurant: ", listeResultat)
        else:
            self.ui.labelError.setText("Aucun restaurant trouve. Veuillez reessayer.")
            self.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
    
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
                print("Resultat de la requete: ", result)
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def supprimer_avis(self):
        """
        Fenetre de suppression d'avis
        """
        selected_items = self.ui.listWidgetAvis.selectedItems()
        print("Avis selectionne: ", selected_items)
        if not selected_items:
            print("Aucun avis sélectionné.")
            return
        avisASupprimer = selected_items[0].text()
        print("Avis a supprimer: ", avisASupprimer)
        self.ui = Ui_SupprimerAvisModo()
        self.ui.setupUi(self)
        self.ui.textBrowserAvisASupprimer.setText(avisASupprimer)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.pushButtonDelete.clicked.connect(self.get_supprimer_avis_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client ou bien du restaurateur
        if self.isRestaurateur:
            self.ui.pushButtonRetour.clicked.connect(self.retour_menu_restaurateur)
        else:
            self.ui.pushButtonRetour.clicked.connect(self.retour_menu_client)

    def get_supprimer_avis_data(self):
        """
        Recuperation des donnees de suppression d'avis
        """
        avisSupprime = self.ui.textBrowserAvisASupprimer.toPlainText().split(" : ")[-1]
        justificatif = self.ui.plainTextEditJustificationSuppression.toPlainText()
        print("Avis supprime: ", avisSupprime)
        print("Justificatif: ", justificatif)
        # On supprime l'avis des avis valides et le deplace dans les avis invalides avec le justificatif
        if self.supprimer_avis_query(avisSupprime, justificatif):
            print("Avis supprime avec succes")
            self.ui.labelError.setText("Avis supprime avec succes. Merci!")
            self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.ui.labelError.setText("Erreur lors de la suppression de l'avis. Veuillez reessayer.")
            self.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
    
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
                    print("Avis non trouve")
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

    def retour_menu_client(self):
        """
        Retour au menu principal du client
        """
        self.ui = Ui_ClientMenu()
        self.ui.setupUi(self)
        self.client_menu()
    
    def retour_menu_restaurateur(self):
        """
        Retour au menu principal du restaurateur
        """
        self.ui = Ui_RestaurateurMenu()
        self.ui.setupUi(self)
        self.restaurateur_menu()

    def ajouter_note(self):
        """
        Fenetre d'ajout de note
        """
        self.ui = Ui_AjouterNote()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonBoxOkRetour.accepted.connect(self.get_ajouter_note_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client)

    def get_ajouter_note_data(self):
        """
        Recuperation des donnees d'ajout de note
        """
        nomRestaurant = self.ui.lineEditRestoName.text()
        dateVisite = self.ui.dateEditVisite.date().toString("yyyy-MM-dd")
        commentaire = self.ui.plainTextEditCommentaire.toPlainText()
        noteLivraison = self.ui.spinBoxNoteLivraison.value()
        noteService = self.ui.spinBoxNoteService.value()
        recommendation = self.ui.comboBoxRecommendation.currentText()
        print("Nom du restaurant: ", nomRestaurant)
        print("Date de visite: ", dateVisite)
        print("Commentaire: ", commentaire)
        print("Note de livraison: ", noteLivraison)
        print("Note de service: ", noteService)
        print("Recommendation: ", recommendation)
        # On ajoute la note dans la bdd
        if self.ajouter_note_query(nomRestaurant, dateVisite, commentaire, noteLivraison, noteService, recommendation):
            print("Note ajoutee avec succes")
            self.ui.labelError.setText("Note ajoutee avec succes. Merci!")
            self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            self.ui.labelError.setText("Erreur lors de l'ajout de la note. Veuillez reessayer.")

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

    def ajouter_restaurant(self):
        """
        Fenetre d'ajout de restaurant
        """
        self.ui = Ui_AjouterResto()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonBoxOkRetour.accepted.connect(self.get_ajouter_restaurant_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du restaurateur
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_restaurateur)

    def get_ajouter_restaurant_data(self):
        """
        Recuperation des donnees d'ajout de restaurant
        """
        nomRestaurant = self.ui.lineRestoName.text()
        adRue = self.ui.lineAdRue.text()
        adVille = self.ui.lineAdVille.text()
        adPays = self.ui.lineCountry.text()
        adCodePostal = self.ui.lineAdPostal.text()
        adNumero = self.ui.lineAdNum.text()
        typeNourriture = self.ui.lineTypeNourriture.text()
        gammePrix = self.ui.comboBoxGammePrix.currentText()
        # Prend uniquement le dernier mot de la gamme de prix
        gammePrix = gammePrix.split(" ")[-1]
        debutOuverture = self.ui.timeEditHeureDebut.time().toString("mm:hh")
        finOuverture = self.ui.timeEditHeureFin.time().toString("mm:hh")
        if self.ui.checkBoxFaitLivraison.isChecked():
            faitLivraison = "Yes"
        else:
            faitLivraison = "No"
        print("Nom du restaurant: ", nomRestaurant)
        print("Adresse: ", adRue, adVille, adPays, adCodePostal, adNumero)
        print("Type de nourriture: ", typeNourriture)
        print("Gamme de prix: ", gammePrix)
        print("Heure d'ouverture: ", debutOuverture)
        print("Heure de fermeture: ", finOuverture)
        print("Fait livraison: ", faitLivraison)
        # On ajoute le restaurant dans la bdd
        if self.ajouter_restaurant_query(nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, typeNourriture, gammePrix, debutOuverture, finOuverture, faitLivraison):
            print("Restaurant ajoute avec succes")
            self.ui.labelError.setText("Restaurant ajoute avec succes. Merci!")
            self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            # Ajoute le nom du restaurant au restaurateur
            self.ajouter_restaurant_restaurateur(nomRestaurant)
        else:
            self.ui.labelError.setText("Erreur lors de l'ajout du restaurant. Veuillez reessayer.")

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
    
    def ajouter_restaurant_restaurateur(self, nomRestaurant):
        """
        Requete d'ajout de restaurant au restaurateur
        """
        try:
            with self.connection.cursor() as cursor:
                query = "UPDATE restaurateurs SET restaurant=%s WHERE lastname=%s AND firstname=%s"
                cursor.execute(query, (nomRestaurant, self.nom, self.prenom))
                self.connection.commit()
                return True
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def modifier_restaurant(self):
        """
        Fenetre de consultation de restaurant
        """
        self.ui = Ui_ModifierResto()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonBoxOkRetour_2.accepted.connect(self.get_modifier_restaurant_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du restaurateur
        self.ui.buttonBoxOkRetour_2.rejected.connect(self.retour_menu_restaurateur)
    
    def get_modifier_restaurant_data(self):
        """
        Recuperation des donnees de consultation de restaurant
        """
        nomRestaurant = self.ui.lineRestoName.text()
        adRue = self.ui.lineAdRue.text()
        adVille = self.ui.lineAdVille.text()
        adPays = self.ui.lineCountry.text()
        adCodePostal = self.ui.lineAdPostal.text()
        adNumero = self.ui.lineAdNum.text()
        parTypeNourriture = self.ui.lineTypeNourriture.text()
        parGammePrix = self.ui.comboBoxGammePrix.currentText()
        # Prend uniquement le dernier mot de la gamme de prix
        parGammePrix = parGammePrix.split(" ")[-1]
        debutOuverture = self.ui.timeEditHeureDebut.time().toString("mm:hh")
        finOuverture = self.ui.timeEditHeureFin.time().toString("mm:hh")
        if self.ui.checkBoxFaitLivraison.isChecked():
            faitLivraison = "Yes"
        else:
            faitLivraison = "No"
        print("Nom du restaurant: ", nomRestaurant)
        print("Adresse: ", adRue, adVille, adPays, adCodePostal, adNumero)
        print("Par type de nourriture: ", parTypeNourriture)
        print("Par gamme de prix: ", parGammePrix)
        print("Heure d'ouverture: ", debutOuverture)
        print("Heure de fermeture: ", finOuverture)
        print("Fait livraison: ", faitLivraison)
        # On verifie que l'utilisateur est bien le proprietaire du restaurant
        if self.verifier_proprietaire_restaurant(nomRestaurant):
            # On modifie le restaurant dans la bdd
            if self.modifier_restaurant_query(nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, parTypeNourriture, parGammePrix, debutOuverture, finOuverture, faitLivraison):
                print("Restaurant modifie avec succes")
                self.ui.labelError.setText("Restaurant modifie avec succes. Merci!")
                self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            else:
                self.ui.labelError.setText("Erreur lors de la modification du restaurant. Veuillez reessayer.")
                self.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ui.labelError.setText("Vous n'etes pas le proprietaire. Veuillez reessayer.")
            self.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
    
    def verifier_proprietaire_restaurant(self, nomRestaurant):
        """
        Verifie si l'utilisateur est bien le proprietaire du restaurant
        """
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT restaurant FROM restaurateurs WHERE lastname=%s AND firstname=%s"
                cursor.execute(query, (self.nom, self.prenom))
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


    def ajouter_plat(self):
        """
        Fenetre d'ajout de plat
        """
        self.ui = Ui_AjouterPlat()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.listeAllergenes = []
        self.listeNvPlats = {}
        self.ui.pushButtonAdd.clicked.connect(self.get_ajouter_allergene_data)
        self.ui.buttonBoxOkRetour.accepted.connect(self.get_ajouter_plat_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du restaurateur
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_restaurateur)

    def get_ajouter_allergene_data(self):
        """
        Recuperation des donnees d'ajout d'allergene
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()
        if self.verifier_proprietaire_restaurant(nomRestaurant):
            allergenes = self.ui.lineCheckAllergeneNouveauPlat.text()
            self.listeAllergenes.append(allergenes)
    
    def get_ajouter_plat_data(self):
        """
        Recuperation des donnees d'ajout de plat
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()
        
        # On verifie que l'utilisateur est bien le proprietaire du restaurant
        if self.verifier_proprietaire_restaurant(nomRestaurant):
            listeMenu = self.ui.listWidgetListMenu.selectedItems()
            nomNvPlat = self.ui.lineCheckNomNouveauPlat.text()
            prixNvPlat = self.ui.doubleSpinBoxPrixNouveauPlat.value()
            listePlatsAjoutes = self.ui.listWidgetPlatAjoute.selectedItems()
        
            self.listeNvPlats[nomNvPlat] = self.listeAllergenes
            listePlatsAjoutes.append(nomNvPlat)
            self.listeAllergenes = []

            print("Nom du restaurant: ", nomRestaurant)
            print("Liste des menus: ", listeMenu)
            print("Nom du nouveau plat: ", nomNvPlat)
            print("Prix du nouveau plat: ", prixNvPlat)
            print("Liste des plats ajoutes: ", listePlatsAjoutes)
            print("Liste des nouveaux plats: ", self.listeNvPlats)
            print("Liste des allergenes: ", self.listeAllergenes)

            print("Liste des plats ajoutes mise a jour: ", listePlatsAjoutes)
        
            self.ui.listWidgetPlatAjoute.clear()
            # On ajoute la liste des nouveaux plats a la liste des plats ajoutes
            for plat in self.listeNvPlats:
                if plat not in listePlatsAjoutes:
                    listePlatsAjoutes.append(plat)
            last_plat = list(self.listeNvPlats.keys())[-1]
            # On ajoute les nouveaux plats dans la base de donnees
            if self.ajouter_plats_query(nomRestaurant, last_plat, prixNvPlat):
                # On met a jour la liste des plats dans le widget listWidgetListMenu
                self.ui.listWidgetPlatAjoute.clear()
                self.ui.listWidgetPlatAjoute.addItems(listePlatsAjoutes)
                self.ui.labelError.setText("Plats ajoutes avec succes. Merci!")
                self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            else:
                self.ui.labelError.setText("Erreur lors de l'ajout des plats. Veuillez reessayer.")
                self.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        else:
            self.ui.labelError.setText("Vous n'etes pas le proprietaire. Veuillez reessayer.")
            self.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
    
    def ajouter_plats_query(self, nomRestaurant, nvPlat, prixNvPlat):
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
                if nvPlat in self.listeNvPlats:
                    for allergen in self.listeNvPlats[nvPlat]:
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

    def consulter_statistique(self):
        """
        Fenetre de consultation de statistique
        """
        self.ui = Ui_Stats()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.ui.buttonBoxOkRetour.accepted.connect(self.get_statistique_data)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du restaurateur
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_restaurateur)

    def get_statistique_data(self):
        """
        Recuperation des donnees de consultation de statistique
        """
        nomRestaurant = self.ui.lineRestoName.text()

        # On recupere les donnees de la bdd et on les affiche
        listeStatistiques = self.consulter_statistique_query(nomRestaurant)
        if listeStatistiques:
            nombreAvis, noteMoyenne, noteMoyenneLivraison,platPopulaire = listeStatistiques[0]
            self.ui.labelNbrAvisRes.setText(str(nombreAvis))
            self.ui.labelNoteMoyenneRes.setText(str(noteMoyenne))
            self.ui.labelNoteMoyenneLivraisonRes.setText(str(noteMoyenneLivraison))
            self.ui.labelPlatPopulaireRes.setText(platPopulaire)
            print("Statistiques trouves")
            self.ui.labelError.setText("Statistiques trouves. Merci!")
            self.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
        else:
            print("Aucune statistique trouve")
            self.ui.labelError.setText("Aucune statistique trouve. Veuillez reessayer.")
            self.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")

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
                print("Résultat de la requête: ", result)
                return [result] if result else []
        except Error as e:
            print(f"Erreur lors de la requête: {e}")
            return False

    def autres_requetes(self):
        """
        Fenetre d'autres requetes
        """
        self.ui = Ui_Other()
        self.ui.setupUi(self)

        # On affiche les donnees de la bdd selon le bouton clique par l'utilisateur
        self.ui.pushButtonAvisSup3.clicked.connect(self.afficher_avis_sup3)
        self.ui.pushButtonPlatPlusCher.clicked.connect(self.afficher_plat_plus_cher)
        self.ui.pushButtonClientsMexicains.clicked.connect(self.afficher_clients_mexicains)
        self.ui.pushButtonPlatsAsiatiques.clicked.connect(self.afficher_plats_asiatiques)
        self.ui.pushButtonCodePostalPiresRestos.clicked.connect(self.afficher_pire_code_postal)
        self.ui.pushButtonTypeNourritureParNote.clicked.connect(self.afficher_type_nourriture_par_note)

        # # On recupere les donnees de connexion entrees par l'utilisateur
        # self.ui.buttonBoxOkRetour.accepted.connect(self.get_autres_requetes_data)

        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du restaurateur
        if self.isRestaurateur:
            self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_restaurateur)
        else:
            self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client)

    def afficher_avis_sup3(self):
        """
        Affiche les avis avec une note superieure a 3
        """
        self.ui = Ui_AvisSup3()
        self.ui.setupUi(self)

        # On recupere les donnees de la bdd et on les affiche
        listeAvis = self.afficher_avis_sup3_query()
        if listeAvis:
            listeAvis = [f"{avis[0]} : {avis[1]}" for avis in listeAvis]
            self.ui.listWidgetRestoObtenu.addItems(listeAvis)

        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu des requetes
        self.ui.buttonBoxOkRetour.rejected.connect(self.autres_requetes)
    
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
        
    def afficher_plat_plus_cher(self):
        """
        Affiche le plat le plus cher
        """
        self.ui = Ui_PlatPlusCher()
        self.ui.setupUi(self)

        # On recupere les donnees de la bdd et on les affiche
        platCher = self.afficher_plat_plus_cher_query()
        if platCher:
            self.ui.listWidgetRestoObtenu.addItem(platCher[0] + " avec un plat au prix de " + str(platCher[1]) + " euros")

        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu des requetes
        self.ui.buttonBoxOkRetour.rejected.connect(self.autres_requetes)
    
    def afficher_plat_plus_cher_query(self):
        """
        Requete d'affichage du plat le plus cher
        """
        try:
            with self.connection.cursor() as cursor:
                query = "SELECT name, price FROM dishes ORDER BY price DESC LIMIT 1"
                cursor.execute(query)
                result = cursor.fetchone()
                print("Resultat de la requete: ", result)
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def afficher_clients_mexicains(self):
        """
        Affiche les clients mexicains
        """
        self.ui = Ui_ClientMangeantMexicain()
        self.ui.setupUi(self)

        # On recupere les donnees de la bdd et on les affiche
        listeClients = self.afficher_clients_mexicains_query()
        if listeClients:
            listeClients = [f"{client[0]} a mange {client[1]} plats mexicains" for client in listeClients]
            self.ui.listWidgetClientsObtenus.addItems(listeClients)

        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu des requetes
        self.ui.buttonBoxOkRetour.rejected.connect(self.autres_requetes)

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
    
    def afficher_plats_asiatiques(self):
        """
        Affiche les plats asiatiques
        """
        self.ui = Ui_PlatAsiatique()
        self.ui.setupUi(self)

        # On recupere les donnees de la bdd et on les affiche
        restaurant_non_asiatique = self.afficher_plats_asiatiques_query()
        if restaurant_non_asiatique:
            self.ui.listWidgetRestoObtenu.addItem(restaurant_non_asiatique[0] + " propose " + str(restaurant_non_asiatique[1]) + " plats asiatiques")
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu des requetes
        self.ui.buttonBoxOkRetour.rejected.connect(self.autres_requetes)
    
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
                print("Resultat de la requete: ", result)
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False
    
    def afficher_pire_code_postal(self):
        """
        Affiche le code postal de la ville ou les restaurants ont les moins bonnes notes en moyenne
        """
        self.ui = Ui_PireCodePostal()
        self.ui.setupUi(self)

        # On recupere les donnees de la bdd et on les affiche
        pireCodePostal = self.afficher_pire_code_postal_query()
        if pireCodePostal:
            self.ui.listWidgetCodePostalObtenu.addItem("Le pire code postal est " + pireCodePostal[0] + " avec une note moyenne de " + str(pireCodePostal[1]))

        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu des requetes
        self.ui.buttonBoxOkRetour.rejected.connect(self.autres_requetes)
    
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
                print("Resultat de la requete: ", result)
                return result
        except Error as e:
            print(f"Erreur lors de la requete: {e}")
            return False

    def afficher_type_nourriture_par_note(self):
        """
        Affiche le type de nourriture par note le plus present
        """
        self.ui = Ui_TypeNourritureParNote()
        self.ui.setupUi(self)

        # On recupere les donnees de la bdd et on les affiche
        listeTypeNourriture = self.afficher_type_nourriture_par_note_query()
        disclaimer = "La requete actuelle ne fonctionne pas et donne une note moyenne par type de nourriture"
        self.ui.listWidgetTypeNourritureParNoteObtenu.addItem(disclaimer)
        if listeTypeNourriture:
            listeTypeNourriture = [f"{typeNourriture[0]} a une note moyenne de {typeNourriture[1]}" for typeNourriture in listeTypeNourriture]
            self.ui.listWidgetTypeNourritureParNoteObtenu.addItems(listeTypeNourriture)

        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu des requetes
        self.ui.buttonBoxOkRetour.rejected.connect(self.autres_requetes)
    
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    # fermeture de la connexion
    window.close_connection()
