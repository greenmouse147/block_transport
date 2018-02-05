# block_transport
# Introduction
Ce dépôt présente une implémentation de la blochain dédié à la notification d'incident.
## Composition des Transactions
### Transaction déclaration d'un incident
![alt text](/Docs/img/Incident.png "Incident")
### Transaction création d'un utilisateur
![alt text](/Docs/img/CreationUtilisateurs.png "Création Nouvel Utilisateur")
### Transaction ajout de réputation à l'utilisateur
![alt text](/Docs/img/AjoutDeReptutation.png "Ajout de reputation")

### Définition du type de transaction

| Valeur | Objectif |
| --- | --- |
| TT = 1 | Alerte |
| TT = 2 | Ajout de Réponses |
| TT = 3 | Retrait de réputation |
| TT = 4 | Création Utilisateur |
| TT = 5 | Création Entreprise |

### Définition des type de code qui permettent d'identifié le type d'événement

> Codes :<br/>
1 Accident<br/>
2 Vol<br/>
3 Agression<br/>
4 Incendie<br/>
5 Retard<br/>
<!--- --->
