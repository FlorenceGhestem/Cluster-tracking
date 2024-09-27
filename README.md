# Cluster-Tracking Approach for Longitudinal Patient Data Analysis

## Purpose of the Repository

This repository contains the implementation of two novel cluster-tracking approaches for analyzing longitudinal patient data extracted from medico-administrative databases, this is intially a fork from (JudithLamb/Cluster-tracking)[https://github.com/JudithLamb/Cluster-tracking]. The primary goals of this research are:

1. To identify clusters of patients at different ages using two clustering strategies:
   a. Markov Cluster algorithm (MCL) applied to patient networks built from raw data
   b. K-means applied directly to raw data
2. To track these clusters over time, defining cluster-trajectories
3. To visualize the results using an R Shiny application

The approaches were initially applied to antithrombotic drug reimbursements data from the Échantillon Généraliste des Bénéficiaires (EGB, a French cohort) between 2008 and 2018 for patients aged 60 to 70 years. Due to privacy concerns, this repository uses a simulated dataset of 5,594 patients with their drug reimbursements, derived from the original raw data.

This work aims to provide researchers and healthcare professionals with tools to better understand patient trajectories and drug usage patterns over time.

This repository aims to provide an environment to run the code with the right dependencies, to get familiar with the code.

## Repository Structure

```
.
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── LICENSE
├── README.md
├── data
│   ├── README.md
│   ├── input
│   └── output
├── renv.lock
├── requirements.txt
└── src
    ├── R
    │   ├── app.R
    │   └── functions.R
    └── python
        └── cluster_tracking.py
```

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Remote - Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code

## Getting Started

There are two ways to set up the development environment: using the pre-built image from GitHub Container Registry or building the image locally.

### Option 1: Using the Pre-built Image (Recommended)

1. Ensure you have Docker installed and running on your machine.

2. Pull the pre-built image from GitHub Container Registry:
   ```
   docker pull ghcr.io/YOUR_GITHUB_USERNAME/your-repo-name:latest
   ```
   Replace `YOUR_GITHUB_USERNAME` and `your-repo-name` with the appropriate values.

3. If the repository is private, you'll need to authenticate with GitHub Container Registry first:
   ```
   echo $GITHUB_PAT | docker login ghcr.io -u YOUR_GITHUB_USERNAME --password-stdin
   ```
   Replace `$GITHUB_PAT` with your GitHub Personal Access Token.

4. Clone this repository:
   ```
   git clone https://github.com/FlorenceGhestem/Cluster-tracking.git
   cd Cluster-tracking
   ```

5. Open the repository in Visual Studio Code:
   ```
   code .
   ```

6. When prompted by VS Code, click "Reopen in Container" or use the command palette (F1) and select "Remote-Containers: Reopen in Container".

7. VS Code will use the pre-built image to create your development container.

### Option 2: Building the Image Locally

If you prefer to build the image locally or need to make modifications:

1. Clone this repository:
   ```
   git clone https://github.com/FlorenceGhestem/Cluster-tracking.git
   cd Cluster-tracking
   ```

2. Open the repository in Visual Studio Code:
   ```
   code .
   ```

3. When prompted by VS Code, click "Reopen in Container" or use the command palette (Crtl+Shift+P) and select "Remote-Containers: Reopen in Container".

4. VS Code will build the Docker image based on the Dockerfile in the `.devcontainer` directory. This may take a few minutes the first time.

## Using the Development Environment

### Running Python Scripts

1. Open a terminal in VS Code (Terminal -> New Terminal).
2. Navigate to the Python source directory:
   ```
   cd src/python
   ```
3. Run the Python script:
   ```
   python cluster_tracking.py
   ```

### Running the R Shiny App

1. Open a terminal in VS Code.

2. Start R by typing:
   ```
   R
   ```
3. In the R console, run:
   ```R
    shiny::runApp("src/R/app.R", host = "0.0.0.0", port = 3838)
   ```
4. Access the Shiny app in your browser at `http://localhost:3838`.

The R Shiny app allows you to visualize the tracking of clusters and the cluster-trajectories from the simulated data. It provides:
- An alluvial plot showing the tracking of clusters, where blocks represent clusters and stream fields represent common patients.
- A flowchart visualizing cluster-trajectories, with blocks representing clusters and arrow thickness indicating the number of common patients.
- Cluster characteristics, including the two most used drugs, sex ratio, and total number of patients.
- Options to choose between the two clustering strategies and display clusters above a selected size limit.

## Modifying the Environment

If you need to modify the development environment:

1. Edit the `Dockerfile` in the `.devcontainer` directory.
2. Rebuild the container:
   - Open the command palette in VS Code (Ctrl+Shift+P)
   - Select "Remote-Containers: Rebuild Container"

## Updating Dependencies

### Python Dependencies

1. Update `requirements.txt` with new packages.
2. Rebuild the container as described above.

### R Dependencies

1. In the R console within the container, use `renv::install()` to install new packages.
2. Update the `renv.lock` file:
   ```R
   renv::snapshot()
   ```
3. Commit the updated `renv.lock` file to the repository.

## Troubleshooting

- If you encounter issues with package versions, ensure your `requirements.txt` and `renv.lock` files are up to date.
- For problems with the container, try rebuilding it from scratch: delete the Docker image and rebuild using the "Remote-Containers: Rebuild Container" command in VS Code.
- If you're using the pre-built image and encounter issues, try pulling the latest version of the image or switch to building the image locally.

## License

This project is licensed under the [LICENSE NAME] - see the [LICENSE](LICENSE) file for details.

## References

1. Santo Fortunato. "Community detection in graphs". In: Physics reports 486.3-5 (2010), pp. 75–174.
