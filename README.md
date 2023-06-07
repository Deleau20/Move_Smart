# Move_Smart

Projet pour le secteur des transports.

Ce projet vise à mener une réflexion sur le domaine du transport et donner une solution numérique à un problème majeur selon notre spécialité.

Les solutions proposé dans ce projet sont entre autres:

- Mettre en place une application web qui permettra aux automobilistes de signaler rapidement un cas de vol ou un incidents quelconque qui concerne leur engin, il permet de mettre en contact rapidement ces automobilistes avec les autoritées compétente .

- Aussi ce projet aura une section voyage qui permet à un voyager de faire une étude de prix en fonction de son trajet et lui proposera le meilleur des prix ( on prendra également en compte la disponibilité )

Identifiants :

Administrateur =

    email : fred@gmail.com
    mdp : 0987

lien de l'application web : 


L'utilisation d'une application web pour signaler les accidents routiers revêt une importance cruciale dans notre société moderne. Cette technologie permet de simplifier et d'accélérer le processus de signalement des incidents sur les routes, ce qui peut contribuer à sauver des vies et à améliorer la sécurité routière de manière significative.

En utilisant une application web dédiée au signalement des accidents, les utilisateurs peuvent facilement signaler un incident dès qu'ils le constatent. Cela permet une transmission rapide de l'information aux autorités compétentes, aux services d'urgence et aux autres conducteurs, afin de prendre les mesures nécessaires pour minimiser les risques et fournir une assistance appropriée sur le lieu de l'accident.

Grâce à l'application web, les détails de l'accident tels que l'emplacement exact, les dégâts matériels, les blessures et d'autres informations pertinentes peuvent être communiqués de manière précise et rapide. Cela facilite le déploiement efficace des ressources et des services d'urgence appropriés, ce qui peut permettre d'économiser un temps précieux lors de situations critiques.

De plus, l'application web peut également aider à collecter des données précieuses sur les accidents routiers. En analysant ces données, les autorités compétentes peuvent identifier les zones à risque élevé, évaluer l'efficacité des mesures de sécurité en place et prendre des décisions éclairées pour améliorer l'infrastructure routière et prévenir les accidents futurs.

L'utilisation de l'application web de signalement des accidents routiers favorise également la sensibilisation du public à la sécurité routière. En encourageant les utilisateurs à signaler les incidents, nous renforçons une culture de responsabilité collective et d'engagement envers la sécurité de tous. Cela peut inciter les conducteurs à adopter des comportements plus prudents et à respecter les règles de la route, contribuant ainsi à réduire le nombre d'accidents et de victimes.

En conclusion, l'importance de l'utilisation d'une application web pour signaler les accidents routiers réside dans sa capacité à accélérer la transmission d'informations vitales, à faciliter le déploiement des services d'urgence, à collecter des données précieuses et à sensibiliser le public à la sécurité routière. En utilisant cette technologie, nous avons le pouvoir de créer un environnement routier plus sûr pour tous les usagers de la route, en œuvrant ensemble pour prévenir les accidents et préserver des vies précieuses.

.container{
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 50vh;
}

.content1{
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
}



.content1 p{
  color: white;
  font-size: 4rem; 
}



.contentbtn {
  /* border: #0b2239 solid 2px; */
  display: flex;
  justify-content: center;
  align-items: center;

}

.btn {
  --color: #4ad295;
  --color2: #0b2239;
  padding: 0.8em 1.75em;
  background-color: transparent;
  border-radius: 6px;
  border: 2px solid var(--color);
  transition: 0.5s;
  position: relative;
  overflow: hidden;
  cursor: pointer;
  z-index: 1;
  font-weight: 500;
  font-size: 17px;
  text-transform: uppercase;
  color: var(--color);
}

.btn::after,
.btn::before {
  content: "";
  display: block;
  height: 100%;
  width: 100%;
  transform: skew(90deg) translate(-50%, -50%);
  position: absolute;
  inset: 50%;
  left: 25%;
  z-index: -1;
  transition: 0.5s ease-out;
  background-color: var(--color);
}

.btn::before {
  top: -50%;
  left: -25%;
  transform: skew(90deg) rotate(180deg) translate(-50%, -50%);
}

.btn:hover::before {
  transform: skew(45deg) rotate(180deg) translate(-50%, -50%);
}

.btn:hover::after {
  transform: skew(45deg) translate(-50%, -50%);
}

.btn:hover {
  color: var(--color2);
}

.btn:active {
  filter: brightness(0.7);
  transform: scale(0.98);
}

@media only screen and (max-width: 1000px) {
  header {
    padding: 0 20px;
  }
  header .header-right .hamburger {
    display: block;
  }
  header .header-left nav {
    margin: 0;
    position: absolute;
    top: -100%;
    left: 0;
    width: 100%;
    height: fit-content;
    background-color: #0b2239;
    padding: 30px;
    transition: 0.3s;
    text-align: center;
    z-index: -1;
  }
  header .header-left nav.active {
    top: 70px;
  }
  header .header-left nav ul {
    display: block;
  }
}

@media only screen and (max-width: 500px) {
  nav .login-signup {
    display: block;
    margin-top: 20px;
  }
  header .header-right .login-signup {
    display: none;
  }
}

@media screen and (max-width: 768px) {
  .container {
    flex-direction: column;
    min-height: 20vh;
  }
  .content1 {
    width: 100%;
  }
  .content1 p {
    font-size: 3rem;
  }
  .btn {
    font-size: 14px;
  }
}

@media screen and (max-width: 480px) {
  .btn {
    font-size: 14px;
  }

  .content1 p {
    font-size: 2rem;
  }

}