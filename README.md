//This file is where i correct my readme file

# Maky - Data Platforms, Integration, and Cloud Solutions

This project is a hands-on journey through the core concepts of modern data engineering and IoT solutions, based on the "Data platforms, data integration and cloud solutions"
 course. 

It's a practical exploration of how to build a system that fetches data from an external source, processes it, stores it, and presents it through a web interface. It serves as a living document and a portfolio piece demonstrating key skills in the field.

## ✨ Features

*   **Data Fetching:** A Python script that connects to the Futurama API to pull character data.
*   **Local Storage:** Saves the retrieved data into a structured `output/` directory as individual JSON files.
*   **Web Interface:** A simple but effective web front-end built with Flask that dynamically reads the stored data and displays it in the browser.

## 🚀 Getting Started

To get this project running on your own machine (or in a fresh Cloud Shell environment), follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Maky-Kaba/maky_data_platform
    cd maky_data_platform
    ```

2.  **Set up the Python environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the necessary dependencies:**
    ```bash
    uv pip install -r requirements.txt
    ```

4.  **Run the data pipeline:**
    ```bash
    python main.py
    ```

5.  **Launch the web application:**
    ```bash
    python web_app.py
    ```
    You can then view the application by navigating to `http://localhost:8080` in your browser.

## 🛠️ Technology Stack

*   Python 3
*   Flask (for the web interface)
*   Requests (for API communication)
*   uv (as a modern package manager)
*   Git & GitHub (for version control)
*   Google Cloud Shell (as the development environment)
