FROM python:3.8-slim

# Éviter les messages d'avertissement lors de la création de l'image
ENV DEBIAN_FRONTEND=noninteractive

# Mettre à jour et installer les dépendances
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Créer un utilisateur non-root
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Définir l'utilisateur par défaut
USER $USERNAME

# Définir le répertoire de travail
WORKDIR /workspace

# Copier les fichiers du projet (à ajuster selon votre structure)
COPY . /workspace/

# Installer les dépendances Python
RUN pip install --upgrade pip
