# FastAPI CI/CD with GitHub Actions

This project demonstrates a CI/CD pipeline for a FastAPI application using GitHub Actions. The pipeline includes testing the application on multiple Python versions and operating systems, and building and pushing a Docker image to GitHub Container Registry.

## Project Structure

- `webapicicd/.github/workflows/cicd.yaml`: GitHub Actions workflow file.
- `webapicicd/requirements.txt`: Python dependencies for the project.
- `webapicicd/app`: Directory containing the FastAPI application code.

## Prerequisites

- Python 3.9 or higher
- Docker
- GitHub account

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/webapicicd.git
    cd webapicicd
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application:**
    ```sh
    uvicorn app.main:app --reload
    ```

## GitHub Actions CI/CD Pipeline

The CI/CD pipeline is defined in the `cicd.yaml` file and includes the following jobs:

1. **Test:**
    - Runs on Ubuntu and Windows.
    - Tests the application on Python versions 3.9 to 3.12.
    - Installs dependencies and runs `pytest`.

2. **Build and Push Docker Image:**
    - Runs on Ubuntu.
    - Builds and pushes the Docker image to GitHub Container Registry.

### Secrets

Add the following secrets to your GitHub repository:

- `GITHUB_TOKEN`: GitHub token for authentication.

## Usage

- **Trigger the pipeline:** The pipeline is triggered on push and pull request events to the `main` branch.
- **View the pipeline:** Go to the Actions tab in your GitHub repository to view the status of the pipeline.

## License

This project is licensed under the MIT License.