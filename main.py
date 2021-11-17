from flask import Flask, request, jsonify
from preprocessing import process_ecg

app = Flask(__name__)

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
    
    data = {'clean_ecg': clean_list, 'rpeaks': rpeaks, 'ybeat': rpeaks, 'bpm': bpm.item()}
    return jsonify(isError=False, data=data, statusCode=200), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

