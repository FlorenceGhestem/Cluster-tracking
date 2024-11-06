
# Development Environment Setup

To run the code in this repository, you'll need to set up a development environment using Docker and Visual Studio Code (VS Code).

## Prerequisites

1. **Docker**: Docker is a tool that allows you to create, deploy, and run applications in a standardized and isolated environment called a container. You'll need to install Docker on your machine. You can download it from the official Docker website: [https://www.docker.com/get-started](https://www.docker.com/get-started)

2. **Visual Studio Code (VS Code)**: VS Code is a popular code editor that we'll be using to work with the code in this repository. You can download it from the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/)

3. **Remote Development extension for VS Code**: This extension allows you to work with containers and remote development environments. You can install it from the VS Code marketplace.

## Setting up the Development Environment

1. **Install Docker**: If you haven't already, install Docker on your machine. You can download it from the official Docker website: [https://www.docker.com/get-started](https://www.docker.com/get-started)

2. **Install Visual Studio Code**: Download and install Visual Studio Code from the official website: [https://code.visualstudio.com/](https://code.visualstudio.com/)

3. **Install the Remote Development extension**: In VS Code, install the Remote Development extension by Microsoft. This extension allows you to work with containers and remote development environments.

4. **Clone the GitHub repository**: Clone the GitHub repository containing the code to your local machine (open bash terminal)

   ```{.sh}
   git clone https://github.com/FlorenceGhestem/Cluster-tracking.git
   cd Cluster-tracking
   ```

5. **Pull the pre-built Docker image**: Pull the pre-built Docker image from the GitHub Container Registry (GHCR):

   ```{.sh}
   docker pull ghcr.io/florenceghestem/cluster-tracking/cluster-tracking-env:latest
   ```

6. **Open the repository in Visual Studio Code**:

   ```{.sh}
   code .
   ```

7. **Reopen the repository in the development container**:
   - When prompted by VS Code, click "Reopen in Container" or use the command palette (Ctrl+Shift+P) and select "Remote-Containers: Reopen in Container".
   - VS Code will use the pre-built `cluster-tracking-env` image to create your development container.

Now you're all set! You should be able to see the project files and start working in the development environment.

Some key things to note:

- The pre-built Docker image `ghcr.io/florenceghestem/cluster-tracking/cluster-tracking-env:latest` is used to create the development container.
- The `devcontainer.json` file in the `.devcontainer` directory defines the configuration for the development container, including the extensions and settings for VS Code.
- When you open the repository in VS Code and choose to "Reopen in Container", VS Code will automatically set up the development environment using the pre-built image and the devcontainer configuration.

Let me know if you have any other questions!
Now you're ready to start working with the code!

## Using the Development Environment

### Running Python Scripts

1. Open a terminal in VS Code (Terminal -> New Terminal).
2. Run the Python script:

   ```{.sh}
   python src/python/cluster_tracking.py
   ```

### Running the R Shiny App

1. Open a terminal in VS Code.
2. Start R by typing:

   ```{.sh}
   R
   ```

3. In the R console, run:

   ```r
   shiny::runApp("src/R/app.R", host = "0.0.0.0", port = 3838)
   ```

4. Access the Shiny app in your browser at `http://localhost:3838`.

Got it, here's an updated section on modifying the environment:

## Modifying the Environment

The development environment for this project is already set up and available as a pre-built Docker image hosted on the GitHub Container Registry (GHCR). This means you don't need to build the image yourself unless you want to make changes to the development environment.

If you need to modify the development environment, for example, to update the dependencies, you can follow these steps:

1. Edit the `Dockerfile` in the `.devcontainer` directory to make the necessary changes, such as adding or updating Python or R packages.
2. **Create a GitHub Personal Access Token**:
   - Go to your GitHub account settings: <https://github.com/settings/tokens>
   - Click on "Generate new token" (classic)
   - Select the "write:packages" scope and click "Generate token"
   - Copy the generated token, you'll need it in the next step

3. **Log in to the GitHub Container Registry**:
   - Open a terminal or command prompt
   - Run the following command to authenticate with GHCR:

     ```{.sh}
     echo <your_github_personal_access_token> | docker login ghcr.io -u <your_github_username> --password-stdin
     ```

     Replace `<your_github_personal_access_token>` with the token you generated in the previous step, and `<your_github_username>` with your GitHub username.

4. **Build the Docker image**:
   - Navigate to the directory containing your Dockerfile
   - Run the following command to build the image:

     ```{.sh}
     docker build -t ghcr.io/<your_github_username>/cluster-tracking/cluster-tracking-env:latest -f .\.devcontainer\Dockerfile .
     ```

     Replace `<your_github_username>` with your GitHub username.

5. **Push the Docker image to GHCR**:
   - Run the following command to push the image to the registry:

     ```{.sh}
     docker push ghcr.io/<your_github_username>/cluster-tracking/cluster-tracking-env:latest
     ```

After completing these steps, the updated Docker image will be available in the GHCR, and other users can use it in their development environment.

It's important to note that you should only push a new image if you're confident that the changes you've made don't break the development environment. To prevent pushing a broken image, you can test the updated environment locally before pushing the image to the registry.

## Updating Dependencies

### Python Dependencies

1. Update the `requirements.txt` file with any new Python packages you need.
2. Rebuild the container as described in the "Modifying the Environment" section.

### R Dependencies

1. In the R console within the container, use `renv::install()` to install new R packages.
2. Update the `renv.lock` file:

   ```r
   renv::snapshot()
   ```

3. Commit the updated `renv.lock` file to the repository.
4. Rebuild the container as described in the "Modifying the Environment" section.
