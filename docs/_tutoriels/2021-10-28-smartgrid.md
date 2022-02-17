---
layout: page
title:  "Smartgrid"
tags: React node
authors:
- "Patrick Ouedraogo"
---

Le jeu smartgrid

<!--more-->

## Smartgrid

### Présentation du jeu




Ce projet s’inscrit dans le cadre de
l’UE Serveur Web, et consiste au développement d’un jeu en utilisant les technologies du Web


### Règles
Le jeu consiste à placer des pions à tout de rôle sur la grille.
Le premier joueur qui aligne quatre pions réalise une smartgrid et gagne la partie
### Espace d'états

La grille de jeu est de dimension 6*7, donc 42 positions que les deux joueurs d’une partie se partagent. Chaque joueur possédant en tout 21 pions placera son pion sur au maximum 7 positions permises, jusqu’à l’obtention du premier état solution.
Les positions permises pour le placement d’un pion sont limitées au nombre de colonnes de la grille ; le joueur ne pouvant placer pour chacune des colonnes que sur la première case vide, et ne pouvant placer dans une colonne si celle-ci est pleine.
Chaque case de la grille sera représentée par trois états possibles: {‘vide’, ’occupée par joueur 1’, ’occupée par joueur 2’}.

## Détails techniques

### Avec quoi il a été fait ?

Le jeu a été réalisé avec la librairie React sur le front, et Node côté serveur.


### Architecture


### Dépendances principales front/back

Backend :

- express : framework très répandu pour la construction d'applications web.
- sequelize : ORM prenant en charge le dialecte PostgreSQL.

Frontend :

- React : librairie JavaScript pour la construction d'applications web monopages.
- React-router-dom: permet de gérer le routage sur une application react monopage

### Installer le projet et lancer le projet


~~~ shell
git clone https://github.com/ipkminu/Smartgrid.git
cd Smartgrid
npm install
npm run build
node index.js
~~~
## React

### routage

~~~ shell
import React from "react";
import Home from '../views/Home';
import Nbrejoueurs from '../views/Nbrejoueurs';
import Niveaujeu from "../views/Niveaujeu";
import Grille from "../views/Grille";
import Aide from '../views/Aide';
import Cgus from '../views/Cgus';
import Espace from '../views/Espace'
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link
} from "react-router-dom";

export default function Routes() {
    return (
        <Router>
            <div>
                <div className="titre">
                    <div>
                        <Link to="/">
                            SMARTGRID
                        </Link>
                    </div>
                </div>
                {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
                <Switch>

                    <Route path="/jouer">
                        <Nbrejoueurs />
                    </Route>
                    <Route path="/nbr1">
                        <Niveaujeu />
                    </Route>
                    <Route path="/grille">
                        <Grille />
                    </Route>

                    <Route path="/aide">
                        <Aide />
                    </Route>
                    <Route path="/cgus">
                        <Cgus />
                    </Route>

                    <Route path="/espace">
                        <Espace />
                    </Route>

                    <Route path="/">
                        <Home />
                    </Route>
                </Switch>
            </div>
        </Router>
    );
}




~~~

### IA

~~~ shell

export default class IA {
    constructor(grille, couleur_machine) {
        this.grille = grille;
        this.couleur = couleur_machine;

    }

    cp_grille(grille) {
        var tab = new Array(6)
        for (let i = 0; i < 6; i++) {
            tab[i] = new Array(7)
            for (let j = 0; j < 7; j++) {
                tab[i][j] = grille[i][j];
            }
        }
        return tab;
    }

    create_fils(pere, joueur, colonne) {
        var copie = this.cp_grille(pere);
        for (let i = 0; i < 6; i++) {
            if (copie[i][colonne] === 0) {
                copie[i][colonne] = joueur;
                return copie;
            }
        }
        return null;
    }
    smart4(grille, joueur) {
        if (grille === null) return 0;
        //Verticales
        for (let j = 0; j < 7; j++) {
            for (let i = 0; i < 3; i++) {
                if (grille[i][j] === joueur && grille[i + 1][j] === joueur && grille[i + 2][j] === joueur && grille[i + 3][j] === joueur) {
                    //console.log(grille)
                    //console.log("Verticales")
                    return true;
                }
            }
        }
        //Horizontales
        for (let i = 0; i < 6; i++) {
            for (let j = 0; j < 4; j++) {
                if (grille[i][j] === joueur && grille[i][j + 1] === joueur && grille[i][j + 2] === joueur && grille[i][j + 3] === joueur) {
                    //console.log("Horiontales")
                    return true;
                }
            }
        }
        //Oblique /
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 4; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j + 1] === joueur && grille[i + 2][j + 2] === joueur && grille[i + 3][j + 3] === joueur) {
                    return true;
                }
            }
        }
        //Oblique \
        for (let i = 0; i < 3; i++) {
            for (let j = 3; j < 7; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j - 1] === joueur && grille[i + 2][j - 2] === joueur && grille[i + 3][j - 3] === joueur) {
                    return true;
                }
            }
        }
        return false;
    }
    smart3(grille, joueur) {

        //Verticales
        for (let j = 0; j < 7; j++) {
            for (let i = 0; i < 4; i++) {
                if (grille[i][j] === joueur && grille[i + 1][j] === joueur && grille[i + 2][j] === joueur) {
                    //console.log(grille)
                    //console.log("Verticales")
                    return true;
                }
            }
        }
        //Horizontales
        for (let i = 0; i < 6; i++) {
            for (let j = 0; j < 5; j++) {
                if (grille[i][j] === joueur && grille[i][j + 1] === joueur && grille[i][j + 2] === joueur) {
                    //console.log("Horiontales")
                    return true;
                }
            }
        }
        //Oblique /
        for (let i = 0; i < 4; i++) {
            for (let j = 0; j < 5; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j + 1] === joueur && grille[i + 2][j + 2] === joueur) {
                    return true;
                }
            }
        }
        //Oblique \
        for (let i = 0; i < 4; i++) {
            for (let j = 2; j < 7; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j - 1] === joueur && grille[i + 2][j - 2] === joueur) {
                    return true;
                }
            }
        }
        return false;
    }

    smart2(grille, joueur) {
        //Verticales
        for (let j = 0; j < 7; j++) {
            for (let i = 0; i < 5; i++) {
                if (grille[i][j] === joueur && grille[i + 1][j] === joueur) {
                    //console.log(grille)
                    //console.log("Verticales")
                    return true;
                }
            }
        }
        //Horizontales
        for (let i = 0; i < 6; i++) {
            for (let j = 0; j < 6; j++) {
                if (grille[i][j] === joueur && grille[i][j + 1] === joueur) {
                    //console.log("Horiontales")
                    return true;
                }
            }
        }
        //Oblique /
        for (let i = 0; i < 5; i++) {
            for (let j = 0; j < 6; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j + 1] === joueur) {
                    return true;
                }
            }
        }
        //Oblique \
        for (let i = 0; i < 5; i++) {
            for (let j = 1; j < 7; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j - 1] === joueur) {
                    return true;
                }
            }
        }
        return false;

    }

    heuristique(grille, joueur, colonne) { //Notation des colonnes 
        var fils = this.create_fils(grille, joueur, colonne);
        if (fils === null) return 0;
        var note = 0;
        if (this.smart4(fils, joueur)) note += 100000;
        
        if (this.smart4(this.create_fils(grille, 3 - joueur, colonne), 3 - joueur)) note += 10000;

        if (this.smart3(this.create_fils(grille, 3 - joueur, colonne), 3 - joueur)) note += 1000;
        if (this.smart3(fils, joueur)) note += 1000;
        if (this.smart2(fils, joueur)) note += 100;
        if (this.smart2(this.create_fils(grille, 3 - joueur, colonne), 3 - joueur)) note += 10;
        return note;
    }

    choix(grille, joueur) {
        var note = 0, col = 0;
        for (let j = 0; j < 7; j++) {
            var h = this.heuristique(grille, joueur, j);
            if (h > note) {
                note = h;
                col = j;
            }

        }
        return col;
    }


}
~~~

## Grille

~~~ shell
import Grilleinner from "../components/Grilleinner"
import ReactDOM from 'react-dom';
import React from "react"
import { Link } from "react-router-dom"

class Grille extends React.Component {
    constructor(props) {
        super(props);
        var courant = Math.floor(Math.random() * 2 + 1);
        this.state = ({
            grille: ([
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
            ]),
            grille_hist: ([
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
                [0, 0, 0, 0, 0, 0, 0,],
            ]),
            joueur: {
                pseudo: "",
                couleur: 1
            },
            jeu: {
                identifiant: null,
                niveau: 1,
                Vainqueur: null,
                courant: Math.floor(Math.random() * 2 + 1),
                messageFin: "fin"
            }


        })
    }
    Color(i) {
        if (i === 0) {
            return "white";
        }
        else if (i === 1) {
            return "red"
        }
        else if (i === 2) return "yellow";
    }
    render() {
        return (
            <div>

                <div className="sous-titre">
                    <div>
                        Jeu {/**Pion du joueur et bouton de pause à ajouter */}
                    </div>
                </div>
                <div className="controles row" >
                    <div className="sous-titre col">
                        <div data-toggle="modal" data-target="#pauseModal">
                            <svg xmlns="http://www.w3.org/2000/svg" width="55" height="55" fill="white" className="bi bi-pause-fill" viewBox="0 0 16 16">
                                <path d="M5.5 3.5A1.5 1.5 0 0 1 7 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5zm5 0A1.5 1.5 0 0 1 12 5v6a1.5 1.5 0 0 1-3 0V5a1.5 1.5 0 0 1 1.5-1.5z" />
                            </svg>
                            {/* Modal à ajouter pour la pause */}
                        </div>
                    </div>
                    <div className="sous-titre col">
                        <div>Vous êtes:</div>
                    </div>
                    <div className="sous-titre col">
                        <div>
                            <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
                                <circle fill="yellow" cx="30" cy="30" r="30" />
                            </svg>
                        </div>
                    </div>
                </div>

                <Grilleinner data={this.state} />

            </div >
        )
    }

}

export default Grille;

~~~

~~~ shell
import React from "react"
import IA from "./IA";

export default class Grilleinner extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            data: props.data,
            messageFin: "Fin du jeu"
        };

    }
    messageFin = ""
    color(i, j) {
        var num = this.props.data.grille[i][j]
        //console.log(num)
        //var num = 2;
        if (num === 0) return "white"
        else if (num === 1) return "yellow"
        else if (num === 2) return "red";

    }
    update_color(joueur) {

        for (let j = 0; j < 7; j++) {
            for (let i = 0; i < 6; i++) {

                var el = document.getElementById("col" + j).querySelector(".l" + i);
                var num = this.props.data.grille[i][j]
                var couleur = "";
                if (num === 0) couleur = "white"
                else if (num === 1) couleur = "yellow"
                else if (num === 2) couleur = "red";
                el.style.backgroundColor = couleur;
            }
        }

        this.fin_jeu(joueur);
    }
    placement_machine() {
        //console.log("Placement de la machine");
        if (this.props.data.jeu.courant === 3 - this.props.data.joueur.couleur) {
            var libres = [];
            for (let j = 0; j < 7; j++) {
                if (this.props.data.grille[5][j] === 0) {
                    libres.push(j);
                }
            }
            //console.log("libres:" + libres)
            //var choix = libres[Math.floor(Math.random() * libres.length)] //Choix de la machine

            var choix = (new IA()).choix((new IA()).cp_grille(this.props.data.grille), 2)
            console.log("choix machine:" + choix)
            for (let i = 0; i < 6; i++) {
                if (this.props.data.grille[i][choix] === 0) {
                    this.props.data.grille[i][choix] = 3 - this.props.data.joueur.couleur
                    this.update_color(3 - this.props.data.joueur.couleur);
                    this.props.data.jeu.courant = 3 - this.props.data.jeu.courant;
                    //console.log(this.props.data.grille)
                    return;
                }
            }
        }
    }
    handleClick(j) {
        //console.log("Click handled");

        //console.log("courant: " + this.props.data.jeu.courant)
        if (this.props.data.jeu.courant === this.props.data.joueur.couleur) {
            for (let i = 0; i < 6; i++) {
                if (this.props.data.grille[i][j] === 0) {
                    this.props.data.grille[i][j] = this.props.data.joueur.couleur
                    this.update_color(this.props.data.joueur.couleur);
                    this.props.data.jeu.courant = 3 - this.props.data.jeu.courant;

                    //console.log(this.props.data.grille)

                    this.placement_machine()
                    return;
                }
            }
        } this.placement_machine()


    }

    fin_jeu(joueur) {

        if (this.smart(joueur)) {

            //this.state.messageFin = "Jeu terminé. Le vainqueur est le joueur n°" + joueur;
            this.setState({
                messageFin: "Jeu terminé. Le vainqueur est le joueur n°" + joueur
            })
            console.log(this.state.messageFin)
            this.props.data.jeu.courant = 0;
            this.props.data.jeu.messageFin = "Jeu terminé. Vainqueur; joueur n°" + joueur
            document.getElementById("finjeu").click();
            return true;
        }

        for (let i = 0; i < 6; i++) {
            for (let j = 0; j < 7; j++) {
                if (this.props.data.grille[i][j] === 0) return false;
            }
        }
        this.props.data.jeu.courant = 0;
        console.log("Jeu terminé, grille pleine");
        this.props.data.jeu.messageFin = "Jeu terminé, grille pleine";
        document.getElementById("finjeu").click();
        return true;
    }
    smart(joueur) {
        const grille = this.props.data.grille;
        //Verticales
        for (let j = 0; j < 7; j++) {
            for (let i = 0; i < 3; i++) {
                if (grille[i][j] === joueur && grille[i + 1][j] === joueur && grille[i + 2][j] === joueur && grille[i + 3][j] === joueur) {
                    //console.log(grille)
                    //console.log("Verticales")
                    return true;
                }
            }
        }
        //Horizontales
        for (let i = 0; i < 6; i++) {
            for (let j = 0; j < 4; j++) {
                if (grille[i][j] === joueur && grille[i][j + 1] === joueur && grille[i][j + 2] === joueur && grille[i][j + 3] === joueur) {
                    //console.log("Horiontales")
                    return true;
                }
            }
        }
        //Oblique /
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 4; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j + 1] === joueur && grille[i + 2][j + 2] === joueur && grille[i + 3][j + 3] === joueur) {
                    return true;
                }
            }
        }
        //Oblique \
        for (let i = 0; i < 3; i++) {
            for (let j = 3; j < 7; j++) {
                if (grille[i][j] === joueur && grille[i + 1][j - 1] === joueur && grille[i + 2][j - 2] === joueur && grille[i + 3][j - 3] === joueur) {
                    return true;
                }
            }
        }

        return false;
    }


    render() {
        return (
            <div>
                <div className="grille">
                    <div id="col0" onClick={() => this.handleClick(0)}>
                        <div className={"l5 p "}></div>
                        <div className={"l4 p "}></div>
                        <div className={"l3 p "}></div>
                        <div className={"l2 p "}></div>
                        <div className={"l1 p "}></div>
                        <div className={"l0 p "}></div>
                    </div>
                    <div id="col1" onClick={() => this.handleClick(1)}>
                        <div className={"l5 p "}></div>
                        <div className={"l4 p "}></div>
                        <div className={"l3 p "}></div>
                        <div className={"l2 p "}></div>
                        <div className={"l1 p "}></div>
                        <div className={"l0 p "}></div>
                    </div>
                    <div id="col2" onClick={() => this.handleClick(2)}>
                        <div className={"l5 p"}></div>
                        <div className={"l4 p"}></div>
                        <div className={"l3 p"}></div>
                        <div className={"l2 p"}></div>
                        <div className={"l1 p"}></div>
                        <div className={"l0 p"}></div>
                    </div>
                    <div id="col3" onClick={() => this.handleClick(3)}>
                        <div className={"l5 p"}></div>
                        <div className={"l4 p"}></div>
                        <div className={"l3 p"}></div>
                        <div className={"l2 p"}></div>
                        <div className={"l1 p"}></div>
                        <div className={"l0 p"}></div>
                    </div>
                    <div id="col4" onClick={() => this.handleClick(4)}>
                        <div className={"l5 p"}></div>
                        <div className={"l4 p"}></div>
                        <div className={"l3 p"}></div>
                        <div className={"l2 p"}></div>
                        <div className={"l1 p"}></div>
                        <div className={"l0 p"}></div>
                    </div>
                    <div id="col5" onClick={() => this.handleClick(5)}>
                        <div className={"l5 p"}></div>
                        <div className={"l4 p"}></div>
                        <div className={"l3 p"}></div>
                        <div className={"l2 p"}></div>
                        <div className={"l1 p"}></div>
                        <div className={"l0 p"}></div>
                    </div>
                    <div id="col6" onClick={() => this.handleClick(6)}>
                        <div className={"l5 p"}></div>
                        <div className={"l4 p"}></div>
                        <div className={"l3 p"}></div>
                        <div className={"l2 p"}></div>
                        <div className={"l1 p"}></div>
                        <div className={"l0 p"}></div>
                    </div>
                </div>


                {/*-- Pause Modal --*/}
                <div className="modal fade" id="pauseModal" tabIndex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
                    <div className="modal-dialog modal-dialog-centered" role="document">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title" id="pauseModalLongTitle"> Pause</h5>
                                <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div className="modal-body">
                                Arrêt de jeu
                                Vous pouvez continuer à tout moment.
                            </div>
                            <div className="modal-footer">

                                <button type="button" className="btn btn-secondary" data-dismiss="modal" >Quitter</button>

                                <button type="button" className="btn btn-primary" data-dismiss="modal" aria-label="Close">Continuer</button>
                            </div>
                        </div>
                    </div>
                </div>

                {/**Fin jeu Modal  */}
                <div id="finjeu" data-toggle="modal" data-target="#finjeuModal" >

                </div>
                <div className="modal fade" id="finjeuModal" tabIndex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                    <div className="modal-dialog" role="document">
                        <div className="modal-content">
                            <div className="modal-header">
                                <h5 className="modal-title" id="exampleModalLabel">The end!!!</h5>
                                <button type="button" className="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </div>
                            <div className="modal-body">
                                {this.state.messageFin}
                            </div>
                            <div className="modal-footer">
                                <button type="button" className="btn btn-secondary" data-dismiss="modal">Quitter</button>
                                <button type="button" className="btn btn-primary" data-dismiss="modal" aria-label="Close">Nouvelle Partie</button>
                            </div>
                        </div>
                    </div>
                </div>

            </div>


        )
    }
}

~~~

