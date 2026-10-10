# python-prod-basics

[![CI](https://github.com/roastytoasty777/python-prod-basics/actions/workflows/ci.yml/badge.svg)](https://github.com/roastytoasty777/python-prod-basics/actions/workflows/ci.yml)

Exercices de Python de production : pytest, Pydantic, CI GitHub Actions.

Le projet contient un outil en ligne de commande qui lit un fichier CSV de candidats, valide chaque ligne avec Pydantic, puis écrit les lignes valides et les lignes refusées dans deux fichiers séparés.

## Installation

```bash
git clone https://github.com/roastytoasty777/python-prod-basics
cd python-prod-basics
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Utilisation

```bash
python main.py data/candidates.csv
```

Le programme crée deux fichiers à la racine du projet :

- `valid.csv` : les candidats valides
- `errors.csv` : les lignes refusées

Exemple d'entrée (`data/candidates.csv`) :

```csv
name,email,experience
Test,test@example.com,0
John,john@example.com,5
Alice,alice@example.com,-1
Sam,invalid-email,3
```

Résultat : `valid.csv` contient Test et John, `errors.csv` contient Alice (expérience négative) et Sam (email invalide).

## Tests

```bash
python -m pytest -v
```

Les tests tournent aussi automatiquement sur GitHub Actions à chaque push.

## Structure

```
src/
  candidate.py          modèle Pydantic Candidate
  candidate_loader.py   tri des candidats valides et refusés
  csv_io.py             lecture et écriture des fichiers CSV
tests/                  tests pytest
data/                   exemple de fichier d'entrée
main.py                 point d'entrée en ligne de commande
```