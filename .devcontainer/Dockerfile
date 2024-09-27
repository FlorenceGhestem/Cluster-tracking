FROM ubuntu:20.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Install basic dependencies
RUN apt-get update && apt-get install -y \
    software-properties-common \
    curl \
    wget \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    libxml2-dev \
    libcurl4-openssl-dev \
    libsqlite3-dev \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python 3.8
RUN add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    apt-get install -y python3.8 python3.8-venv python3.8-dev python3-pip && \
    update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1 && \
    update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

# Install R 4.4
RUN wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc && \
    add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/" && \
    apt-get update && \
    apt-get install -y r-base r-base-dev

# Install Python dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# Install R dependencies
COPY renv.lock /tmp/renv.lock
RUN R -e "install.packages('renv', repos = 'https://cloud.r-project.org/')" && \
    R -e "renv::restore(lockfile = '/tmp/renv.lock')"

# Install Shiny
RUN R -e "install.packages('shiny', repos='https://cloud.r-project.org/')"

# Set working directory
WORKDIR /workspace

# Set environment variables
ENV PYTHONPATH="/workspace/src/python:${PYTHONPATH}"
ENV R_LIBS_USER="/workspace/renv/library"

CMD ["/bin/bash"]
