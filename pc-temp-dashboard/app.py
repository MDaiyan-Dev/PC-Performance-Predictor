from models.Forecast_model import forecast_temperature
from models.Classification_model import classify_anomaly
import numpy as np
from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)
# Global variables to store recent temperatures
cpu_history = []
gpu_history = []


# Default simulation parameters for CPU/GPU temperature simulation
simulation_params = {
    "cpu_temp_min": 30,
    "cpu_temp_max": 80,
    "gpu_temp_min": 30,
    "gpu_temp_max": 80,
    "noise_level": 5,
    "update_interval": 1  # in seconds
}

@app.route('/')
def index():
    # Render the dashboard with the current simulation parameters.
    return render_template('index.html', params=simulation_params)

@app.route('/update_params', methods=['POST'])
def update_params():
    global simulation_params
    data = request.json
    # Update simulation parameters with data from the client.
    simulation_params.update(data)
    return jsonify({"status": "success", "params": simulation_params})

@app.route('/simulate', methods=['GET'])
def simulate():
    import random, time
    global cpu_history, gpu_history

    # Simulate temperature values
    cpu_temp = random.uniform(simulation_params["cpu_temp_min"], simulation_params["cpu_temp_max"])
    gpu_temp = random.uniform(simulation_params["gpu_temp_min"], simulation_params["gpu_temp_max"])
    
    # Introduce some noise.
    cpu_temp += random.uniform(-simulation_params["noise_level"], simulation_params["noise_level"])
    gpu_temp += random.uniform(-simulation_params["noise_level"], simulation_params["noise_level"])

    # Compute slowdown for display (dummy calculation here)
    avg_temp = (cpu_temp + gpu_temp) / 2
    slowdown = max(0, min(100, (avg_temp - 30) * 1.5))

    # Save the simulated temperatures
    cpu_history.append(cpu_temp)
    gpu_history.append(gpu_temp)
    # Ensure we keep only the 10 most recent values
    if len(cpu_history) > 10:
        cpu_history.pop(0)
    if len(gpu_history) > 10:
        gpu_history.pop(0)

    return jsonify({
        "timestamp": time.time(),
        "cpu_temp": round(cpu_temp, 2),
        "gpu_temp": round(gpu_temp, 2),
        "slowdown": round(slowdown, 2)
    })


from models.Forecast_model import forecast_temperature  # Ensure you're importing correctly

@app.route('/predict_forecast', methods=['POST'])
def predict_forecast():
    global cpu_history, gpu_history
    # Ensure we have at least 10 data points from each sensor
    if len(cpu_history) < 10 or len(gpu_history) < 10:
        return jsonify({"error": "Not enough data for prediction"}), 400

    # Compute average of the last 10 readings for both CPU and GPU
    avg_cpu = sum(cpu_history[-10:]) / 10
    avg_gpu = sum(gpu_history[-10:]) / 10
    overall_avg = (avg_cpu + avg_gpu) / 2

    # Use the forecast function by passing a list with overall_avg
    # (since forecast_temperature computes np.mean on the list)
    predicted_slowdown = forecast_temperature([overall_avg])
    return jsonify({"forecast": predicted_slowdown})


@app.route('/predict_anomaly', methods=['POST'])
def predict_anomaly():
    # In a real app, you'd receive an image (e.g., as base64), decode it, etc.
    # Here we simulate by generating a dummy image.
    dummy_image = np.random.rand(64, 64, 1)
    classification = classify_anomaly(dummy_image)
    return jsonify({"anomaly": classification})


if __name__ == '__main__':
    app.run(debug=True)
