# Presentation of the project

## Abstract

Millions of users are registered on cryptocurrency exchange platforms without possessing any substantial knowledge concerning the subject. During the last decade, cryptocurrencies have gained momentum. This sudden surge in popularity can be seen through a split between conservatives and progressives. The latter specifically regards the emergence of cryptocurrencies as an opportunity that shouldn't be missed. Following this trend, various applications have emerged providing in-depth technical analysis of different cryptocurrencies and offer strong decision support. However, as the digitalization keeps on going forward, a bigger part of all feelings/emotions are communicated via social networks, therefore the social media impact on cryptocurrencies prices can be often underestimated. Our project aims to develop a user-friendly web application that provides a valuable tool to facilitate investment decisions adapted to this new asset class. Thus, we are offering a major innovation that provides real-time sentiment analysis of all relevant tweets that are related to each cryptocurrency.

## Authors

* Ruben Kempter : ruben.kempter@unil.ch
* Dimitri André : dimitri.andre@unil.ch
* Guillaume Pavé : guillaume.pave@unil.ch

## Install project and libraries

1) clone project on your computer

```bash
git clone https://github.com/GuillaumePv/ProjetCrypto_app.git
```
2) launch the shell script to run our code

```bash
.\launcher.sh
```

3) Go to http://127.0.0.1:8050/ in your browser

# Project structure

```
├── README.md          <- The top-level README for developers using this project.
│
├── include/             <- Librairies created
│
├── static /            <- static files (images)                     
│
│
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│   
│   
├── main.py   <- Main python file that manage all our different codes
│
├── models/   <- ML models used in the dasboard are stocked in this folder
│
│
├── scripts/   <- folder that contains python file that create data pipeline for ou rML prediction
│
├── infos.log         <- log file of our software.
│
├── scrapper.log         <- log file for our web scraper.
│
```

## TO-DO

- [x] Stop tweet dataflow
- [x] find indicators
- [x] cleaning data
- [x] make libraries for the layout
- [x] write report
- [x] make video
- [x] improve launcher.sh to install necesary librairies
