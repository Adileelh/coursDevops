# Utilise l'image Python 3.7 Alpine
FROM python:3.7-alpine

# Définit le répertoire de travail
WORKDIR /tpdocker

# Copie le contenu local dans le répertoire de travail du conteneur
COPY . .

RUN pip install -r requirements.txt

# Exécute le script Python
CMD ["python", "main.py"]
