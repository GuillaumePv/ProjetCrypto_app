## Presentation of project

## Install project and librairies

1) cloner le projet sur son ordinateur

```bash
git clone https://github.com/GuillaumePv/ProjetCrypto_app.git
```
2) installer les librairies nécessaires pour le projet

```bash
pip3 install -r requirements.txt
```

# Project structure

```
├── README.md          <- The top-level README for developers using this project.
│
├── include             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── src                <- Source code for use in this project.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├── infos.log         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── scrapper.log         <- Data dictionaries, manuals, and all other explanatory materials.
│
```

## TO-DO
- [ ] augmenter la vitesse de loading
- [x] ajouter des stats dexcriptives au projet
- [ ] ML Model 
- [x] arreter flux de tweet
- [x] trouver les indicateurs
- [x] cleaning data
- [ ] tester les différents algos sur bitcoin
- [ ] tester sur les autres cryptos
- [x] faire une libraries pour le layout
- [ ] faire fonctionner twint sur heroku
- [ ] Ecrire le rapport
- [ ] tourner la vidéo de présentation
- [x] tester avec un subprocess + launch tab => style jupyter notebook
- [x] améliorer le launcher en installant toutes les libraires

## Bug

* maj twint pour utiliser dans Heroku