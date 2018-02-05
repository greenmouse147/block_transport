# block_transport
# Introduction
Ce dépôt présente une implémentation de la blockchain dédié à la notification d'incident.
## Composition des Transactions
### Transaction déclaration d'un incident
![alt text](/Docs/img/Incident.png "Incident")
### Transaction création d'un utilisateur
![alt text](/Docs/img/CreationUtilisateur.png "Création Nouvel Utilisateur")
### Transaction ajout de réputation à l'utilisateur
![alt text](/Docs/img/AjoutDeReptutation.png "Ajout de reputation")

# Composition d'un Block
Un Block est composé d'un ensemble de transactions. (entre 3 et 5 à définir)

![alt text](/Docs/img/block.png "Block")

![alt text](/Docs/img/connexionBlocks.png "Block_Chain")

### Définition du type de transaction

| Valeur | Objectif |
| --- | --- |
| TT = 1 | Alerte |
| TT = 2 | Ajout de Réputation |
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
