# Maky - Data Platforms, Integration, and Cloud Solutions

This project is a hands-on journey through the core concepts of modern data engineering and IoT solutions, based on the "Data platforms, data integration and cloud solutions" course. 

It's a practical exploration of how to build a system that fetches data from an external source, processes it, stores it across multiple database types, and integrates with cloud storage. It serves as a living document and a portfolio piece demonstrating key skills in the field.

## ✨ Features

*   **Data Fetching:** Connects to the Futurama API to pull character data.
*   **Multi-Database Storage:** Persists the fetched data in both a NoSQL (MongoDB) and a SQL (MySQL) database.
*   **Cloud Integration:** Uploads a sample IoT sensor data file to a real cloud object store (Amazon S3).
*   **Web Interface:** A simple Flask web app to display data from the MongoDB database.

## 🚀 Getting Started

To get this project running, you will need an AWS account and your credentials configured.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Maky-Kaba/maky_data_platform
    cd maky_data_platform
    ```

2.  **Launch the database services:** This starts the MongoDB and MySQL containers.
    ```bash
    docker-compose up -d
    ```

3.  **Set up the Python environment:**
    ```bash
    python3 -m venv ven
    source venv/bin/activate
    ```

4.  **Install dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

5.  **Configure AWS Credentials:**
    ```bash
    aws configure
    ```
    *(You will need your AWS Access Key ID and Secret Access Key for this step.)*

6.  **Run the full data pipeline:** This fetches API data, saves it to the databases, and uploads the sensor file to S3.
    ```bash
    python main.py
    ```
    *(Note: You must update the `bucket_name` variable in `main.py` to your own S3 bucket name for the upload to succeed.)*

## 🛠️ Technology Stack

*   **Cloud:** Amazon Web Services (AWS) - S3
*   **Databases:** MongoDB, MySQL
*   **Containerization:** Docker & Docker Compose
*   **Backend:** Python 3, Flask
*   **Python Libraries:** requests, pymongo, mysql-connector-python, boto3
*   **Tooling:** uv, Git, GitHub, Google Cloud Shell