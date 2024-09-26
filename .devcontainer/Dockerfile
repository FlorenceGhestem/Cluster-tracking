FROM python:3.8-slim
RUN apt-get update && apt-get install -y --no-install-recommends r-base r-base-dev && rm -rf /var/lib/apt/lists/*


WORKDIR /cluster-tracking

COPY .. .

RUN pip install --no-cache-dir -r requirements.txt

RUN R -e "install.packages('renv', repos = 'https://cloud.r-project.org/')"

CMD ["/bin/bash"]
