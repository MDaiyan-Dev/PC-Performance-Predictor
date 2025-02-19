# PC Temperature & Performance Dashboard

A sleek, real-time monitoring and predictive analytics dashboard for PC performance, built with Flask, Plotly, Bootstrap, and integrated deep learning models. This project simulates CPU and GPU temperatures and uses an LSTM-based model to predict performance loss, while a CNN model detects anomalies from time-series data representations.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)

## Overview

The **PC Temperature & Performance Dashboard** is designed to help users monitor the real-time temperature of their PC's CPU and GPU, and predict performance loss using a data-driven, deep learning approach. The LSTM model applies a linear formula—where every degree difference from an optimal 65°C results in a 1.7% performance change—to forecast performance loss. In parallel, a CNN model is set up to detect anomalies in the temperature data, with plans to evolve it into a robust classifier once trained on real-world data.

This project started as a proof-of-concept and has grown into a full-fledged dashboard with a modern, responsive UI built with Bootstrap. It’s perfect for demonstrating applied AI/ML in a real-time monitoring context.

## Features

- **Real-Time Temperature Monitoring:**  
  Displays simulated CPU and GPU temperature data on a dynamic Plotly graph.
  
- **Performance Loss Prediction:**  
  Uses an LSTM-based model (currently using a linear formula) to predict performance loss based on average temperature.
  
- **Anomaly Detection:**  
  Integrates a CNN model for future anomaly detection on temperature data.
  
- **Modern UI:**  
  A responsive and attractive interface built using Bootstrap 5.
  
- **API Endpoints:**  
  - `/simulate`: Simulates temperature data.
  - `/predict_forecast`: Predicts performance loss percentage.
  - `/predict_anomaly`: Detects anomalies in temperature data.
  
- **Containerization Ready:**  
  Designed for easy deployment via Docker and integration into CI/CD pipelines.

## Tech Stack

- **Backend:** Flask, Python 3.11
- **Frontend:** HTML, Bootstrap 5, Plotly.js
- **Deep Learning:** TensorFlow (LSTM & CNN models)
- **Containerization:** Docker (with a Dockerfile provided)
- **Version Control:** Git & GitHub

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/pc-temperature-dashboard.git
   cd pc-temperature-dashboard
   ```

2. **Create and Activate a Virtual Environment (Python 3.11):**

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows use: .\venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Docker:**  
   Ensure Docker is installed if you plan to containerize the application.

## Usage

1. **Start the Flask Server:**

   ```bash
   python app.py
   ```

   or

   ```bash
   $env:FLASK_APP="app.py"
   flask run
   ```

2. **Open the Dashboard:**  
   Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) in your web browser.

3. **Interact with the Dashboard:**  
   - Update simulation parameters and the page will automatically reload.
   - View real-time temperature data for CPU and GPU.
   - Use the "Predict Performance Loss %" button to see the LSTM model’s output.
   - Use the "Predict Anomaly" button for CNN model predictions.

## Endpoints

- **`/simulate`**  
  Simulates and returns current CPU and GPU temperatures.

- **`/predict_forecast`**  
  Processes the last 10 simulated temperature readings and returns a predicted performance loss percentage.

- **`/predict_anomaly`**  
  Uses the CNN model to return an anomaly status for the temperature data.

## Future Improvements

- **Deep Learning Models:**  
  Train the LSTM on real historical data and improve the CNN model for accurate anomaly detection.
  
- **Data Integration:**  
  Connect to real sensor data for live monitoring.
  
- **Enhanced Deployment:**  
  Set up CI/CD pipelines, automated testing, and robust error handling.
  
- **Security & Scaling:**  
  Implement HTTPS, secure API endpoints, and consider auto-scaling strategies for production deployment.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Crafted with passion and a drive for innovation by [Your Name].




#THE LSTM AND CNN MODELS ARE DUMMY PLACEHOLDER MODELS. THE REAL MODELS ARE CURRENTLY BEING TRAINED FOR IMPLEMENTATION AND FINAL DEPLOYMENT!!
