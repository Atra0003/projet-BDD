class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.ui.buttonSignIn.clicked.connect(self.handle_connexion)
        self.view.ui.buttonSignUp.clicked.connect(self.handle_inscription)
        self.lName = ""
        self.fName = ""
        self.isRestaurateur = False
        self.isModerateur = False


    def handle_connexion(self):
        self.view.open_conexion_window()
        # On recupere les donnees de connexion entrees par l'utilisateur
        def connexion_data_after_click():
            self.lName, self.fName, password, self.isRestaurateur, self.isModerateur = self.view.get_connexion_data()
            # Verifie les informations de connexion dans la bdd
            if self.model.connexion_query(self.lName, self.fName, password, self.isRestaurateur, self.isModerateur):
                # Si l'utilisateur existe dans la database, on affiche le menu principal
                self.handle_menu()
            else:
                # Affiche un message d'erreur si les informations de connexion sont incorrectes
                self.view.ui.labelError.setText("Nom ou prénom incorrect. Veuillez réessayer.")
        self.view.ui.buttonSignIn.clicked.connect(connexion_data_after_click)

    def handle_inscription(self):
        self.view.open_inscription_window()
        # On recupere les donnees d'inscription entrees par l'utilisateur
        def inscription_data_after_click():
            self.lName, self.fName, password, self.isRestaurateur, self.isModerateur, adRue, adNumero, adVille, adCodePostal, adPays = self.view.get_inscription_data()
            # Verifie les informations de connexion dans la bdd
            if self.model.inscription_query(self.lName, self.fName, password, self.isRestaurateur, self.isModerateur, adRue, adNumero, adVille, adCodePostal, adPays):
                # Si l'utilisateur existe dans la database, on affiche le menu principal
                self.handle_menu()
            else:
                # Affiche un message d'erreur si les informations d'inscription sont incorrectes
                self.view.ui.labelError.setText("Saisie incorrecte. Veuillez réessayer.")
        self.view.ui.buttonSignUp.clicked.connect(inscription_data_after_click)

    def handle_menu(self):
        self.view.open_menu(self.isRestaurateur)
        if self.isRestaurateur:
            # Fenetre du menu principal du restaurateur
            self.view.ui.pushButtonAddResto.clicked.connect(self.handle_ajouter_restaurant)
            self.view.ui.pushButtonEditResto.clicked.connect(self.handle_modifier_restaurant)
            self.view.ui.pushButtonAddMeals.clicked.connect(self.handle_ajouter_plat)
            self.view.ui.pushButtonCheckOpinions.clicked.connect(self.handle_consulter_avis)
            self.view.ui.pushButtonStat.clicked.connect(self.handle_consulter_statistique)
            self.view.ui.pushButtonOther.clicked.connect(self.handle_autres_requetes)
        else:
            # Fenetre du menu principal du client
            self.view.ui.pushButtonAddOpinion.clicked.connect(self.handle_ajouter_avis)
            self.view.ui.pushButtonViewOpinion.clicked.connect(self.handle_consulter_avis)
            self.view.ui.pushButtonViewRestaurants.clicked.connect(self.handle_consulter_resto)
            self.view.ui.pushButtonAddNote.clicked.connect(self.handle_ajouter_note)
            self.view.ui.pushButtonOther.clicked.connect(self.handle_autres_requetes)

    def handle_ajouter_avis(self):
        self.view.ajouter_avis()

        def add_avis_after_click():
            nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix = self.view.get_ajouter_avis_data()
            # On verifie que le restaurant existe
            if self.model.verifier_existance_restaurant_query(nomRestaurant):
                # On ajoute l'avis dans la bdd
                id_avis = self.model.ajouter_avis_query(nomRestaurant, dateVisite, heureDebut, heureFin, platsCommandes, prix, self.lName, self.fName)
                if id_avis > 0:
                    self.view.ui.labelError.setText("Avis ajoute avec succes. Merci!")
                    self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
                    self.handle_vers_ajouter_note(nomRestaurant, id_avis)
                else:
                    self.view.ui.labelError.setText("Erreur lors de l'ajout de l'avis. Veuillez reessayer.")
                    self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
            else:
                self.view.ui.labelError.setText("Restaurant introuvable. Veuillez reessayer.")
                self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.view.ui.buttonBoxOkRetour.accepted.connect(add_avis_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)

    def handle_vers_ajouter_note(self, nomRestaurant, id_avis):
        self.view.vers_ajouter_note(nomRestaurant, id_avis)
        def ajouter_note_after_click():
            commentaire, note, note_service_livraison, recommendation = self.view.get_ajouter_note_avis()
            if self.model.vers_ajouter_note_query(id_avis, commentaire, note, note_service_livraison, recommendation):
                self.view.ui.labelError.setText("Note ajoutee avec succes. Merci!")
                self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            else:
                self.view.ui.labelError.setText("Erreur lors de l'ajout de la note. Veuillez reessayer.")
        self.view.ui.buttonBoxOkRetour.accepted.connect(ajouter_note_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)

    def handle_consulter_avis(self):
        self.view.consulter_avis(self.isRestaurateur, self.isModerateur)

        def consulter_avis_after_click():
            nomRestaurant, parNote, parTypeNourriture, parGammePrix = self.view.get_consulter_avis_data()
            # On utilise les donnees recuperees et cherche les avis dans la bdd
            listeResultat = self.model.consulter_avis_query( nomRestaurant, parNote, parTypeNourriture, parGammePrix)
            self.view.ui.listWidgetAvis.clear()
            if listeResultat:
                listeAvis = [f"{avis[0]} : {avis[1]}" for avis in listeResultat]
                self.view.ui.listWidgetAvis.addItems(listeAvis)
        self.view.ui.buttonBoxOkRetour.accepted.connect(consulter_avis_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)
        if self.isModerateur:
            self.view.ui.pushButtonDelete.clicked.connect(self.handle_supprimer_avis)

    def handle_consulter_resto(self):
        self.view.consulter_resto()
        
        def consulter_resto_after_click():
            nomRestaurant = self.view.get_consulter_resto_data()
            # On utilise les donnees recuperees et cherche les restaurants dans la bdd
            listeResultat = self.model.consulter_resto_query(nomRestaurant)
            if listeResultat:
                self.view.ui.labelInfoRestoAdRue.setText(listeResultat[0][5])
                self.view.ui.labelInfoRestoAdVille.setText(listeResultat[0][3])
                self.view.ui.labelInfoRestoAdPays.setText(listeResultat[0][4])
                self.view.ui.labelInfoRestoAdNumero.setText(str(listeResultat[0][6]))
                self.view.ui.labelInfoRestoAdCodePostal.setText(str(listeResultat[0][7]))
                self.view.ui.labelInfoEvaluation.setText(str(listeResultat[0][12]))
                self.view.ui.labelHeureOuverture.setText(str(listeResultat[0][8]))
                self.view.ui.labelHeureFermeture.setText(str(listeResultat[0][9]))
                self.view.ui.labelInfoGammePrix.setText(listeResultat[0][10])
                self.view.ui.labelInfoTypeNourriture.setText(listeResultat[0][2])
                if listeResultat[0][11] == "Yes":
                    self.view.ui.checkBoxFaitLivraison.setChecked(True)

                self.view.ui.labelError.setText("Restaurant trouve. Merci!")
                self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            else:
                self.view.ui.labelError.setText("Aucun restaurant trouve. Veuillez reessayer.")
                self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.view.ui.buttonBoxOkRetour.accepted.connect(consulter_resto_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)

    def handle_supprimer_avis(self):
        self.view.supprimer_avis()
        def supprimer_avis_after_click():
            avisSupprime, justificatif = self.view.get_supprimer_avis_data()
            # On supprime l'avis des avis valides et le deplace dans les avis invalides avec le justificatif
            if self.model.supprimer_avis_query(avisSupprime, justificatif):
                self.view.ui.labelError.setText("Avis supprime avec succes. Merci!")
                self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
            else:
                self.view.ui.labelError.setText("Erreur lors de la suppression de l'avis. Veuillez reessayer.")
                self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        # On connecte le bouton de suppression d'avis a la fonction de suppression
        self.view.ui.pushButtonDelete.clicked.connect(supprimer_avis_after_click)
        self.view.ui.pushButtonRetour.clicked.connect(self.handle_menu)

    def handle_ajouter_note(self):
        self.view.ajouter_note()
        
        def ajouter_note_after_click():
            nomRestaurant, dateVisite, commentaire, noteLivraison, noteService, recommendation = self.view.get_ajouter_note_data()
            # On verifie que le restaurant existe
            if self.model.verifier_existance_restaurant_query(nomRestaurant):
                # On ajoute la note dans la bdd
                if self.model.ajouter_note_query(nomRestaurant, dateVisite, commentaire, noteLivraison, noteService, recommendation):
                    self.view.ui.labelError.setText("Note ajoutee avec succes. Merci!")
                    self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
                else:
                    self.view.ui.labelError.setText("Erreur lors de l'ajout de la note. Veuillez reessayer.")
                    self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
            else:
                self.view.ui.labelError.setText("Restaurant introuvable. Veuillez reessayer.")
                self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.view.ui.buttonBoxOkRetour.accepted.connect(ajouter_note_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)

    def handle_ajouter_restaurant(self):
        self.view.ajouter_restaurant()

        def ajouter_restaurant_after_click():
            nomRestaurant, adRue, adVille, adPays, adCodePostal, adNumero, typeNourriture, gammePrix, debutOuverture, finOuverture, faitLivraison = self.view.get_ajouter_restaurant_data()
            # On verifie que le restaurant n'existe pas deja
            if self.model.verifier_existance_restaurant_query(nomRestaurant):
                self.view.ui.labelError.setText("Restaurant deja existant. Veuillez reessayer.")
                self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
            else:
                # On ajoute le restaurant dans la bdd
                if self.model.ajouter_restaurant_query(nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, typeNourriture, gammePrix, debutOuverture, finOuverture, faitLivraison):
                    self.view.ui.labelError.setText("Restaurant ajoute avec succes. Merci!")
                    self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
                    # Ajoute le nom du restaurant au restaurateur
                    self.model.ajouter_restaurant_restaurateur(nomRestaurant, self.lName, self.fName)
                else:
                    self.view.ui.labelError.setText("Erreur lors de l'ajout du restaurant. Veuillez reessayer.")
                    self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.view.ui.buttonBoxOkRetour.accepted.connect(ajouter_restaurant_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)

    def handle_modifier_restaurant(self):
        self.view.modifier_restaurant()

        def modifier_restaurant_after_click():
            nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, parTypeNourriture, parGammePrix, debutOuverture, finOuverture, faitLivraison = self.view.get_modifier_restaurant_data()
            # On verifie que l'utilisateur est bien le proprietaire du restaurant
            if self.model.verifier_proprietaire_restaurant(nomRestaurant, self.lName, self.fName):
                # On modifie le restaurant dans la bdd
                if self.model.modifier_restaurant_query(nomRestaurant, adRue, adNumero, adVille, adCodePostal, adPays, parTypeNourriture, parGammePrix, debutOuverture, finOuverture, faitLivraison):
                    self.view.ui.labelError.setText("Restaurant modifie avec succes. Merci!")
                    self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
                else:
                    self.view.ui.labelError.setText("Erreur lors de la modification du restaurant. Veuillez reessayer.")
                    self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
            else:
                self.view.ui.labelError.setText("Vous n'etes pas le proprietaire. Veuillez reessayer.")
                self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.view.ui.buttonBoxOkRetour_2.accepted.connect(modifier_restaurant_after_click)
        self.view.ui.buttonBoxOkRetour_2.rejected.connect(self.handle_menu)

    def handle_ajouter_plat(self):
        self.view.ajouter_plat()
        isProprietaire = self.model.verifier_proprietaire_restaurant(self.view.ui.lineCheckRestoName.text(), self.lName, self.fName)

        if isProprietaire:
            # Charge les plats du restaurant
            listePlats = self.model.charger_plats_restaurant_query(self.view.ui.lineCheckRestoName.text())
            self.view.ui.listWidgetListMenu.clear()
            for plat in listePlats:
                allergenes = ", ".join(plat[2:]) if plat[2] != None else "aucun"  # Prend l'allergene du plat s'il y en a, sinon affiche "aucun"
                self.view.ui.listWidgetListMenu.addItem(plat[0] + " : " + str(plat[1]) + " euros, allergenes : " + allergenes)

        def ajouter_allergenes_after_click():
            if isProprietaire:
                self.view.get_ajouter_allergene_data()
        def ajouter_plat_after_click():
            nomRestaurant, listeNvPlats, prixNvPlat, listePlatsAjoutes = self.view.get_ajouter_plat_data()
            # Netttoie la liste des plats ajoutes
            self.view.ui.listWidgetPlatAjoute.clear()
            if isProprietaire:
                # On ajoute la liste des nouveaux plats a la liste des plats ajoutes
                for plat in listeNvPlats:
                    if plat not in listePlatsAjoutes:
                        listePlatsAjoutes.append(plat)
                last_plat = list(listeNvPlats.keys())[-1]
                # On ajoute les nouveaux plats dans la base de donnees
                if self.model.ajouter_plats_query(nomRestaurant, last_plat, prixNvPlat, listeNvPlats):
                    # On met a jour la liste des plats dans le widget listWidgetListMenu
                    self.view.ui.listWidgetPlatAjoute.clear()
                    self.view.ui.listWidgetPlatAjoute.addItems(listePlatsAjoutes)
                    self.view.ui.labelError.setText("Plats ajoutes avec succes. Merci!")
                    self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
                    # On met a jour la liste des plats dans le widget listWidgetListMenu
                    listePlats = self.model.charger_plats_restaurant_query(self.view.ui.lineCheckRestoName.text())
                    self.view.ui.listWidgetListMenu.clear()
                    for plat in listePlats:
                        allergenes = ", ".join(plat[2:]) if plat[2] != None else "aucun"  # Prend l'allergene du plat s'il y en a, sinon affiche "aucun"
                        self.view.ui.listWidgetListMenu.addItem(plat[0] + " : " + str(plat[1]) + " euros, allergenes : " + allergenes)
                else:
                    self.view.ui.labelError.setText("Erreur lors de l'ajout des plats. Veuillez reessayer.")
                    self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")

        self.view.ui.pushButtonAdd.clicked.connect(ajouter_allergenes_after_click)
        self.view.ui.buttonBoxOkRetour.accepted.connect(ajouter_plat_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)

    def handle_consulter_statistique(self):
        self.view.consulter_statistique()

        def consulter_statistique_after_click():
            nomRestaurant = self.view.get_statistique_data()

            # On verifie que le restaurant existe
            if self.model.verifier_existance_restaurant_query(nomRestaurant):
                # On recupere les statistiques du restaurant
                listeStatistiques = self.model.consulter_statistique_query(nomRestaurant)
                if listeStatistiques:
                    nombreAvis, noteMoyenne, noteMoyenneLivraison,platPopulaire = listeStatistiques[0]
                    self.view.ui.labelNbrAvisRes.setText(str(nombreAvis))
                    self.view.ui.labelNoteMoyenneRes.setText(str(noteMoyenne))
                    self.view.ui.labelNoteMoyenneLivraisonRes.setText(str(noteMoyenneLivraison))
                    self.view.ui.labelPlatPopulaireRes.setText(platPopulaire)
                    self.view.ui.labelError.setText("Statistiques trouves. Merci!")
                    self.view.ui.labelError.setStyleSheet("color: rgb(0, 255, 0);")
                else:
                    self.view.ui.labelError.setText("Aucune statistique trouve. Veuillez reessayer.")
                    self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
            else:
                self.view.ui.labelError.setText("Restaurant introuvable. Veuillez reessayer.")
                self.view.ui.labelError.setStyleSheet("color: rgb(255, 0, 0);")
        self.view.ui.buttonBoxOkRetour.accepted.connect(consulter_statistique_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_menu)
        

    def handle_autres_requetes(self):
        self.view.autres_requetes()
        # On affiche les donnees de la bdd selon le bouton clique par l'utilisateur
        self.view.ui.pushButtonAvisSup3.clicked.connect(self.handle_afficher_avis_sup3)
        self.view.ui.pushButtonPlatPlusCher.clicked.connect(self.handle_afficher_plat_plus_cher)
        self.view.ui.pushButtonClientsMexicains.clicked.connect(self.handle_afficher_clients_mexicains)
        self.view.ui.pushButtonPlatsAsiatiques.clicked.connect(self.handle_afficher_plats_asiatiques)
        self.view.ui.pushButtonCodePostalPiresRestos.clicked.connect(self.handle_afficher_pire_code_postal)
        self.view.ui.pushButtonTypeNourritureParNote.clicked.connect(self.handle_afficher_type_nourriture_par_note)

    def handle_afficher_avis_sup3(self):
        self.view.afficher_avis_sup3()

        def afficher_avis_sup3_after_click():
            # On recupere les donnees de la bdd et on les affiche
            listeAvis = self.model.afficher_avis_sup3_query()
            if listeAvis:
                listeAvis = [f"{avis[0]} : {avis[1]}" for avis in listeAvis]
                self.view.ui.listWidgetRestoObtenu.addItems(listeAvis)
        self.view.ui.buttonBoxOkRetour.accepted.connect(afficher_avis_sup3_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_autres_requetes)

    def handle_afficher_plat_plus_cher(self):
        self.view.afficher_plat_plus_cher()

        def afficher_plat_plus_cher_after_click():
            # On recupere les donnees de la bdd et on les affiche
            platCher = self.model.afficher_plat_plus_cher_query()
            if platCher:
                self.view.ui.listWidgetRestoObtenu.addItem(platCher[0] + " avec un plat au prix de " + str(platCher[1]) + " euros")
        self.view.ui.buttonBoxOkRetour.accepted.connect(afficher_plat_plus_cher_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_autres_requetes)

    def handle_afficher_clients_mexicains(self):
        self.view.afficher_clients_mexicains()
        
        def afficher_clients_mexicains_after_click():
            listeClients = self.model.afficher_clients_mexicains_query()
            if listeClients:
                listeClients = [f"{client[0]} a mange {client[1]} plats mexicains" for client in listeClients]
                self.view.ui.listWidgetClientsObtenus.addItems(listeClients)
        self.view.ui.buttonBoxOkRetour.accepted.connect(afficher_clients_mexicains_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_autres_requetes)

    def handle_afficher_plats_asiatiques(self):
        self.view.afficher_plats_asiatiques()
        
        def afficher_plats_asiatiques_after_click():
            restaurant_non_asiatique = self.model.afficher_plats_asiatiques_query()
            if restaurant_non_asiatique:
                self.view.ui.listWidgetRestoObtenu.addItem(restaurant_non_asiatique[0] + " propose " + str(restaurant_non_asiatique[1]) + " plats asiatiques")
        self.view.ui.buttonBoxOkRetour.accepted.connect(afficher_plats_asiatiques_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_autres_requetes)

    def handle_afficher_pire_code_postal(self):
        self.view.afficher_pire_code_postal()
        
        def afficher_pire_code_postal_after_click():
            pireCodePostal = self.model.afficher_pire_code_postal_query()
            if pireCodePostal:
                self.view.ui.listWidgetCodePostalObtenu.addItem("Le pire code postal est " + pireCodePostal[0] + " avec une note moyenne de " + str(pireCodePostal[1]))
        self.view.ui.buttonBoxOkRetour.accepted.connect(afficher_pire_code_postal_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_autres_requetes)

    def handle_afficher_type_nourriture_par_note(self):
        self.view.afficher_type_nourriture_par_note()
        
        def afficher_type_nourriture_par_note_after_click():
            listeTypeNourriture = self.model.afficher_type_nourriture_par_note_query()
            if listeTypeNourriture:
                listeTypeNourriture = [f"{typeNourriture[0]} a une note moyenne de {typeNourriture[1]}" for typeNourriture in listeTypeNourriture]
                self.view.ui.listWidgetTypeNourritureParNoteObtenu.addItems(listeTypeNourriture)
        self.view.ui.buttonBoxOkRetour.accepted.connect(afficher_type_nourriture_par_note_after_click)
        self.view.ui.buttonBoxOkRetour.rejected.connect(self.handle_autres_requetes)
