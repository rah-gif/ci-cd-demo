# 🚀 CI/CD Pipeline Automation

![Python](https://img.shields.io/badge/Python-3.9-blue) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-2088FF) ![Pytest](https://img.shields.io/badge/Testing-Pytest-yellow) ![License](https://img.shields.io/badge/License-MIT-green)

A hands-on experiment to master **Continuous Integration and Continuous Deployment (CI/CD)** pipelines using GitHub Actions. This repository demonstrates a fully automated workflow that builds a Python application, runs unit tests, and deploys a static site.

---

## 🛠️ Project Overview

This project was built to understand the core principles of DevOps automation:

1.  **Automated Testing**: Every commit triggers a suite of unit tests using `pytest`.
2.  **Workflow Management**: Using `.github/workflows` to define build and deploy logic.
3.  **Static Deployment**: Automatically deploying documentation/static content to GitHub Pages upon successful build.

### key Components

- `app.py`: A simple Python module with core logic (Addition, Tax Calculation).
- `test_app.py`: Unit tests ensuring code reliability.
- `.github/workflows/ci.yml`: The CI pipeline that verifies code integrity.
- `.github/workflows/deploy.yml`: The CD pipeline that handles deployment.

---

## ⚙️ The Pipeline

### 1. Continuous Integration (CI)

Triggered on every `push` or `pull_request` to `main`.

- **Environment**: `ubuntu-latest`
- **Steps**:
  1.  Checkout code.
  2.  Set up Python 3.9.
  3.  Install dependencies (`pytest`).
  4.  Run unit tests (`pytest test_app.py`).

### 2. Continuous Deployment (CD)

Triggered only after CI checks pass on `main`.

- **Target**: GitHub Pages
- **Process**:
  1.  Checkout code.
  2.  Upload static artifacts (`site/` directory).
  3.  Deploy to GitHub Pages environment.

---

## 🧗‍♂️ Challenges & Learnings

Building this pipeline was a valuable learning experience in modern DevOps practices:

- **YAML Configuration**: Mastering the syntax for GitHub Actions workflows and understanding strict indentation rules.
- **Dependency Management**: Ensuring the test environment exactly mimics the local development setup using `requirements.txt`.
- **Permissions**: Troubleshooting GitHub Token permissions (`id-token: write`, `pages: write`) needed for secure deployment.
- **Integration**: Seamlessly connecting the Build phase to the Deploy phase without manual intervention.

---

## 🚀 How to Run Locally

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/rah-gif/ci-cd-demo.git
    cd ci-cd-demo
    ```

2.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Tests**
    ```bash
    pytest
    ```

---

## 🤝 Contributing

This is an experimental repository for learning purposes. However, suggestions for optimizing the pipeline are welcome!

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Developed by Chethana Rahul**
