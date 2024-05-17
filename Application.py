import sys
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
from UI.UIAjouterResto import Ui_AjouterResto
from UI.UIModifierResto import Ui_ModifierResto
from UI.UIStats import Ui_Stats
from UI.UIAjouterPlat import Ui_AjouterPlat
from UI.UIConsulterAvisModo import Ui_ConsulterAvisModo
from UI.UISupprimerAvisModo import Ui_SupprimerAvisModo

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
        self.isModerateur = False
        self.isRestaurateur = False
        # Connexion a la bdd
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
        lName = self.ui.lineLName.text()
        fName = self.ui.lineFName.text()
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
        lName = self.ui.lineLName.text()
        fName = self.ui.lineFName.text()
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
    
    def restaurateur_menu(self):
        """
        Fenetre du menu principal du restaurateur
        """
        self.ui.pushButtonAddResto.clicked.connect(self.ajouter_restaurant)
        self.ui.pushButtonEditResto.clicked.connect(self.modifier_restaurant)
        self.ui.pushButtonAddMeals.clicked.connect(self.ajouter_plat)
        self.ui.pushButtonCheckOpinions.clicked.connect(self.consulter_avis)
        self.ui.pushButtonStat.clicked.connect(self.consulter_statistique)

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
        dateVisite = self.ui.dateEdit.date().toString("dd/MM/yyyy")
        heureDebut = self.ui.timeEditHeureDebut.time().toString("hh:mm")
        heureFin = self.ui.timeEditHeureFin.time().toString("hh:mm")
        platsCommandes = self.ui.plainTextEditPlatCommande.toPlainText()
        prix = self.ui.lineEditPrixPaye.text()
        print("Nom du restaurant: ", nomRestaurant)
        print("Date de visite: ", dateVisite)
        print("Heure de debut: ", heureDebut)
        print("Heure de fin: ", heureFin)
        print("Plats commandes: ", platsCommandes)
        print("Prix paye: ", prix)
        # On utilise les donnees recuperees

    def consulter_avis(self):
        """
        Fenetre de consultation d'avis
        """
        if self.isModerateur:
            self.ui = Ui_ConsulterAvisModo()
            self.ui.setupUi(self)
            # On recupere les donnees de connexion entrees par l'utilisateur
            self.ui.buttonBoxOkRetour.accepted.connect(self.get_modo_consulter_avis_data)
            # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client ou bien du restaurateur
            if self.isRestaurateur:
                self.ui.pushButtonRetour.clicked.connect(self.retour_menu_restaurateur)
                self.ui.pushButtonDelete.clicked.connect(self.supprimer_avis)
            else:
                self.ui.pushButtonRetour.clicked.connect(self.retour_menu_client)
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
    
    def get_modo_consulter_avis_data(self):
        """
        Recuperation des donnees de consultation d'avis
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()
        parNote = self.ui.lineEditParNote.text()
        parTypeNourriture = self.ui.lineEditParNourriture.text()
        parGammePrix = self.ui.lineEditParPrix.text()
        listeAvis = self.ui.listWidgetAvis.selectedItems()
        print("Nom du restaurant: ", nomRestaurant)
        print("Par note: ", parNote)
        print("Par type de nourriture: ", parTypeNourriture)
        print("Par gamme de prix: ", parGammePrix)
        print("Liste des avis: ", listeAvis)
        # On utilise les donnees recuperees

    def get_consulter_avis_data(self):
        """
        Recuperation des donnees de consultation d'avis
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()
        parNote = self.ui.lineEditParNote.text()
        parTypeNourriture = self.ui.lineEditParNourriture.text()
        parGammePrix = self.ui.lineEditParPrix.text()
        listeAvis = self.ui.listWidgetAvis.selectedItems()
        print("Nom du restaurant: ", nomRestaurant)
        print("Par note: ", parNote)
        print("Par type de nourriture: ", parTypeNourriture)
        print("Par gamme de prix: ", parGammePrix)
        print("Liste des avis: ", listeAvis)
        # On utilise les donnees recuperees

    def consulter_resto(self):
        """
        Fenetre de consultation de restaurant
        """
        self.ui = Ui_ConsulterResto()
        self.ui.setupUi(self)
        # Si l'utilisateur clique sur le bouton "Cancel", on retourne au menu principal du client
        self.ui.buttonBoxOkRetour.rejected.connect(self.retour_menu_client)
    
    def supprimer_avis(self):
        """
        Fenetre de suppression d'avis
        """
        self.ui = Ui_SupprimerAvisModo()
        self.ui.setupUi(self)
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
        avisSupprime = self.ui.textBrowserAvisASupprimer.toPlainText()
        justificatif = self.ui.plainTextEditJustificationSuppression.toPlainText()
        print("Avis supprime: ", avisSupprime)
        print("Justificatif: ", justificatif)
        # On utilise les donnees recuperees

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
        dateVisite = self.ui.dateEditVisite.date().toString("dd/MM/yyyy")
        commentaire = self.ui.plainTextEditCommentaire.toPlainText()
        note = self.ui.spinBoxNote.value()
        recommendation = self.ui.comboBoxRecommendation.currentText()
        print("Nom du restaurant: ", nomRestaurant)
        print("Date de visite: ", dateVisite)
        print("Commentaire: ", commentaire)
        print("Note: ", note)
        print("Recommendation: ", recommendation)
        # On utilise les donnees recuperees

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
        debutOuverture = self.ui.timeEditHeureDebut.time().toString("hh:mm")
        finOuverture = self.ui.timeEditHeureFin.time().toString("hh:mm")
        faitLivraison = self.ui.checkBoxFaitLivraison.isChecked()
        print("Nom du restaurant: ", nomRestaurant)
        print("Adresse: ", adRue, adVille, adPays, adCodePostal, adNumero)
        print("Type de nourriture: ", typeNourriture)
        print("Gamme de prix: ", gammePrix)
        print("Heure d'ouverture: ", debutOuverture)
        print("Heure de fermeture: ", finOuverture)
        print("Fait livraison: ", faitLivraison)
        # On utilise les donnees recuperees
    
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
        debutOuverture = self.ui.timeEditHeureDebut.time().toString("hh:mm")
        finOuverture = self.ui.timeEditHeureFin.time().toString("hh:mm")
        faitLivraison = self.ui.checkBoxFaitLivraison.isChecked()
        print("Nom du restaurant: ", nomRestaurant)
        print("Adresse: ", adRue, adVille, adPays, adCodePostal, adNumero)
        print("Par type de nourriture: ", parTypeNourriture)
        print("Par gamme de prix: ", parGammePrix)
        print("Heure d'ouverture: ", debutOuverture)
        print("Heure de fermeture: ", finOuverture)
        print("Fait livraison: ", faitLivraison)
        
        # On utilise les donnees recuperees

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
        allergenes = self.ui.lineCheckAllergeneNouveauPlat.text()
        self.listeAllergenes.append(allergenes)
    
    def get_ajouter_plat_data(self):
        """
        Recuperation des donnees d'ajout de plat
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()
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
        # On utilise les donnees recuperees
        
        # On ajoute la liste des nouveaux plats a la liste des plats ajoutes
        for plat in self.listeNvPlats:
            if plat not in listePlatsAjoutes:
                listePlatsAjoutes.append(plat)

        print("Liste des plats ajoutes mise a jour: ", listePlatsAjoutes)
        
        # On met a jour la liste des plats dans le widget listWidgetListMenu
        self.ui.listWidgetPlatAjoute.clear()
        self.ui.listWidgetPlatAjoute.addItems(listePlatsAjoutes)

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
        nombreAvis = self.ui.labelNbrAvisRes.text()
        noteMoyenne = self.ui.labelNoteMoyenneRes.text()
        platPopulaire = self.ui.labelPlatPopulaireRes.text()
        # On recupere les donnees de la bdd et on les affiche

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    # fermeture de la connexion
    window.close_connection()