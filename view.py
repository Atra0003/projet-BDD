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

class View(QMainWindow):
    def __init__(self):
        """
        Constructeur de la classe MainWindow
        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


    def open_conexion_window(self):
        """
        Ouverture de la fenetre de connexion
        """
        self.ui = Ui_ConnexionWindow()
        self.ui.setupUi(self)

    def get_connexion_data(self):
        """
        Recuperation des donnees de connexion
        """
        lName = self.ui.lineLName.text()
        fName = self.ui.lineFName.text()
        password = self.ui.linePassword.text()
        isRestaurateur = self.ui.checkBoxIsRestaurateur.isChecked()
        isModerateur = self.ui.checkBoxIsModerateur.isChecked()
        return lName, fName, password, isRestaurateur, isModerateur
    
    def open_inscription_window(self):
        """
        Ouverture de la fenetre d'inscription
        """
        self.ui = Ui_InscriptionWindow()
        self.ui.setupUi(self)

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
        isModerateur = self.ui.checkBoxIsModerateur.isChecked()
        isRestaurateur = self.ui.checkBoxIsRestaurateur.isChecked()
        return lName, fName, password, isRestaurateur, isModerateur, adRue, adNumero, adVille, adCodePostal, adPays

    def open_menu(self, isRestaurateur):
        """
        Ouverture du menu principal
        """
        if isRestaurateur:
            # Si "IsRestaurateur" a ete cochee, on affiche le menu du restaurateur
            self.ui = Ui_RestaurateurMenu()
            self.ui.setupUi(self)
        else:
            # Sinon, on affiche le menu du client
            self.ui = Ui_ClientMenu()
            self.ui.setupUi(self)

    def ajouter_avis(self):
        """
        Fenetre d'ajout d'avis
        """
        self.ui = Ui_AjouterAvis()
        self.ui.setupUi(self)
    
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
        return nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix

    def vers_ajouter_note(self, nomRestaurant, id_avis):
        """
        Fenetre d'ajout de note
        """
        self.ui = Ui_VersAjouterNote()
        self.ui.setupUi(self)
        self.ui.labelNomResto.setText(nomRestaurant)

    def get_ajouter_note_avis(self):
        """
        Recuperation des donnees d'ajout de note
        """
        commentaire = self.ui.plainTextEditCommentaire.toPlainText()
        note = self.ui.spinBoxNoteService.value()
        note_service_livraison = self.ui.spinBoxNoteLivraison.value()
        recommendation = self.ui.comboBoxRecommendation.currentText()
        return commentaire, note, note_service_livraison, recommendation
        
    def consulter_avis(self, isRestaurateur, isModerateur):
        """
        Fenetre de consultation d'avis
        """
        if isModerateur:
            self.ui = Ui_ConsulterAvisModo()
            self.ui.setupUi(self)
        else:
            self.ui = Ui_ConsulterAvis()
            self.ui.setupUi(self)

    def get_consulter_avis_data(self):
        """
        Recuperation des donnees de consultation d'avis
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()
        parNote = self.ui.lineEditParNote.text()
        parTypeNourriture = self.ui.lineEditParNourriture.text()
        parGammePrix = self.ui.lineEditParPrix.text()
        return nomRestaurant, parNote, parTypeNourriture, parGammePrix
    
    def consulter_resto(self):
        """
        Fenetre de consultation de restaurant
        """
        self.ui = Ui_ConsulterResto()
        self.ui.setupUi(self)

    def get_consulter_resto_data(self):
        """
        Recuperation des donnees de consultation de restaurant
        """
        nomRestaurant = self.ui.lineCheckRestoName.text()

        return nomRestaurant
    
    def supprimer_avis(self):
        """
        Fenetre de suppression d'avis
        """
        selected_items = self.ui.listWidgetAvis.selectedItems()
        if not selected_items:
            return
        avisASupprimer = selected_items[0].text()
        self.ui = Ui_SupprimerAvisModo()
        self.ui.setupUi(self)
        self.ui.textBrowserAvisASupprimer.setText(avisASupprimer)

    def get_supprimer_avis_data(self):
        """
        Recuperation des donnees de suppression d'avis
        """
        avisSupprime = self.ui.textBrowserAvisASupprimer.toPlainText().split(" : ")[-1]
        justificatif = self.ui.plainTextEditJustificationSuppression.toPlainText()
        return avisSupprime, justificatif
    
    def ajouter_note(self):
        """
        Fenetre d'ajout de note
        """
        self.ui = Ui_AjouterNote()
        self.ui.setupUi(self)

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
        return nomRestaurant, dateVisite, commentaire, noteLivraison, noteService, recommendation

    def ajouter_restaurant(self):
        """
        Fenetre d'ajout de restaurant
        """
        self.ui = Ui_AjouterResto()
        self.ui.setupUi(self)

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
        return nomRestaurant, adRue, adVille, adPays, adCodePostal, adNumero, typeNourriture, gammePrix, debutOuverture, finOuverture, faitLivraison
    
    def modifier_restaurant(self):
        """
        Fenetre de consultation de restaurant
        """
        self.ui = Ui_ModifierResto()
        self.ui.setupUi(self)
    
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
        return nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, parTypeNourriture, parGammePrix, debutOuverture, finOuverture, faitLivraison
    
    def ajouter_plat(self):
        """
        Fenetre d'ajout de plat
        """
        self.ui = Ui_AjouterPlat()
        self.ui.setupUi(self)
        # On recupere les donnees de connexion entrees par l'utilisateur
        self.listeAllergenes = []
        self.listeNvPlats = {}

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

        return nomRestaurant, self.listeNvPlats, prixNvPlat, listePlatsAjoutes
    
    def consulter_statistique(self):
        """
        Fenetre de consultation de statistique
        """
        self.ui = Ui_Stats()
        self.ui.setupUi(self)

    def get_statistique_data(self):
        """
        Recuperation des donnees de consultation de statistique
        """
        nomRestaurant = self.ui.lineRestoName.text()

        return nomRestaurant

    def autres_requetes(self):
        """
        Fenetre d'autres requetes
        """
        self.ui = Ui_Other()
        self.ui.setupUi(self)
        
    def afficher_avis_sup3(self):
        """
        Affiche les avis avec une note superieure a 3
        """
        self.ui = Ui_AvisSup3()
        self.ui.setupUi(self) 
    
    def afficher_plat_plus_cher(self):
        """
        Affiche le plat le plus cher
        """
        self.ui = Ui_PlatPlusCher()
        self.ui.setupUi(self)
    
    def afficher_clients_mexicains(self):
        """
        Affiche les clients mexicains
        """
        self.ui = Ui_ClientMangeantMexicain()
        self.ui.setupUi(self)

    def afficher_plats_asiatiques(self):
        """
        Affiche les plats asiatiques
        """
        self.ui = Ui_PlatAsiatique()
        self.ui.setupUi(self)
    
    def afficher_pire_code_postal(self):
        """
        Affiche le code postal de la ville ou les restaurants ont les moins bonnes notes en moyenne
        """
        self.ui = Ui_PireCodePostal()
        self.ui.setupUi(self)
    
    def afficher_type_nourriture_par_note(self):
        """
        Affiche le type de nourriture par note le plus present
        """
        self.ui = Ui_TypeNourritureParNote()
        self.ui.setupUi(self)    