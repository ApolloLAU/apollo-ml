from flask import Flask, request, jsonify
from preprocessing import process_ecg
from model import get_patient_age_category, get_bpm_abnormality, load_ecg_model, load_bpm_model, translate_ecg_predictions, get_ecg_pred, get_bpm_pred, get_patient_data
import os

app = Flask(__name__)

loaded_ecg_model = load_ecg_model(model_name = 'models/ecg_disease.sav')
loaded_bpm_model = load_bpm_model(model_name = 'models/heartbeat_anomaly_model.sav')

@app.route('/preprocess_ecg', methods=['POST'])
def process_signal():
    data = request.get_json()
    ecg_vals = data.get('ECG')
    clean, rpeaks, ybeat, bpm = process_ecg(ecg_vals, 100)

    clean_list = clean.tolist()
    rpeaks['ECG_R_Peaks'] = rpeaks['ECG_R_Peaks'].tolist()
    print(type(clean_list), flush=True)
    print(type(rpeaks), flush=True)
    print(type(rpeaks), flush=True)
    print(type(bpm.item()), flush=True)
    
    data = {'clean_ecg': clean_list, 'rpeaks': rpeaks, 'ybeat': ybeat, 'bpm': bpm.item()}
    return jsonify(isError=False, data=data, statusCode=200), 200

@app.route('/predict_ecg', methods=['POST'])
def predict_ecg():
    data = request.get_json()
    ecg_vals, patient_age, age_category, patient_bpm, bpm_anomaly, bpm_anomaly_categ = get_patient_data(data)

    pred = get_ecg_pred([ecg_vals], loaded_ecg_model)
    pred2 = get_bpm_pred(patient_bpm, age_category, loaded_bpm_model)

    out = {'ecg_prediction': pred, 'bpm_prediction': pred2[0]}

    return jsonify(isError=False, data=out, statusCode=200), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv('PORT', 8000))

