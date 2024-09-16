# Threat Intelligence Automation

## Description
Ce projet développe un outil ou un script d'automatisation pour la collecte de données d'intelligence sur les menaces à partir de diverses sources ouvertes (OSINT) et l'utilisation de ces données pour mettre à jour les règles de sécurité dans un pare-feu ou un IDS/IPS.

## Fonctionnalités
- Agrégation de sources OSINT pour identifier les menaces.
- Mise à jour automatique des règles dans un pare-feu ou IDS.
- Alertes en temps réel basées sur les données de menaces collectées.

## Tech Stack
- Python
- OSINT (Open Source Intelligence)
- Splunk
- Suricata

## Installation
1. Clonez le dépôt
   ```
   git clone https://github.com/percevalFox/threat-intelligence-automation.git
   ```

2. Accédez au répertoire du projet

   ```
   cd threat-intelligence-automation
   ```
3. Installez les dépendances
   ```
   pip install -r requirements.txt
   ```

## Configuration
Modifiez le fichier config/config.yaml pour configurer les paramètres de l'outil.

## Utilisation
Lancez les scripts depuis le répertoire src.

## Tests
Les tests unitaires sont situés dans le répertoire tests.
