import numpy as np
import pandas as pd
from datetime import datetime
import pickle


# ls = [45643, 48747, 52668, 53661, 56621, 55069, 53725, 49468, 46043, 41306, 37849, 33608, 31927, 29111, 29031, 29463, 32135, 31879, 31975, 31559, 32808, 31559, 31703, 29671, 30871, 31239, 31687, 30951, 32247, 31847, 32695, 31223, 33736, 35752, 17716, 608, 1248, 28630, 29831, 29207, 30503, 29223, 27622, 25382, 24662, 24565, 24101, 23701, 23013, 21573, 21205, 20613, 19908, 19732, 19204, 18772, 18436, 16996, 17156, 16612, 16275, 16452, 15875, 16676, 15603, 16051, 15107, 15923, 14435, 14403, 13331, 14115, 13219, 13667, 12178, 13123, 11858, 11666, 11106, 11970, 10738, 11698, 10082, 11810, 9986, 11106, 12547, 14659, 13843, 15667, 15667, 16099, 16163, 18692, 21941, 10738, 320, 720, 3376, 24197, 21285, 21829, 20068, 20372, 18452, 19412, 17668, 18436, 17156, 18228, 15267, 16003, 14051, 15443, 14643, 17620, 17876, 20965, 20420, 20308, 18196, 20997, 21125, 24565, 24405, 26870, 26854, 30519, 29335, 31991, 30535, 32071, 29671, 31799, 30695, 32439, 30263, 32776, 31303, 33608, 33368, 35432, 33832, 34280, 33384, 36424, 37465, 40921, 41290, 44426, 45323, 48411, 50204, 59118, 57998, 21125, 18148, 43498, 50860, 59150, 64399, 64831, 64463, 65007, 65119, 65039, 64799, 64575, 64767, 64815, 64479, 64783, 64911, 64911, 64415, 64463, 64415, 62767, 58878, 56317, 54717, 52892, 52796, 51100, 48363, 44522, 41002, 37193, 35064, 33272, 31927, 30727, 31559, 31431, 33064, 32551, 33432, 31495, 31975, 32279, 32968, 32391, 35816, 36008, 38297, 38649, 41066, 42778, 46235, 46811, 56077, 55485, 19620, 8530, 38441, 43690, 48043, 50828, 56109, 58558, 62959, 63583, 64063, 64303, 64623, 64191, 64031, 61535, 59646, 55709, 53052, 47515, 44874, 38969, 36120, 31175, 32695, 32519, 36520, 37209, 41434, 43946, 48971, 50524, 56349, 57422, 60382, 61214, 62799, 61487, 62687, 59982, 58846, 56621, 56285, 53309, 51516, 47339, 43482, 38713, 36680, 34072, 33160, 31575, 32023, 29479, 30247, 31319, 34584, 7377, 1024, 384, 29351, 30599, 30951, 31399, 32039, 31495, 32215, 31799, 32984, 32535, 33112, 32439, 32215, 31591, 31751, 31799, 32039, 31751, 32023, 32327, 32023, 32151, 33256, 34152, 35672, 37017, 38233, 39113, 40025, 40025, 40249, 40137, 40073, 39353, 39657, 39193, 37977, 37097, 36392, 35944, 35768, 35304, 35208, 32920, 32567, 33800, 34360, 34264, 34488, 35304, 34760, 34984, 34296, 39417, 36152, 768, 544, 17908, 35464, 34232, 35880, 36200, 35848, 35848, 35096, 34472, 33624, 33192, 32295, 32087, 31191, 31079, 30103, 30007, 28951, 29095, 28054, 28823, 28150, 28727, 29543, 31031, 30871, 32471, 32279, 32711, 31431, 31911, 31335, 31959, 31175, 31543, 30503, 30919, 30135, 30695, 30215, 30023, 29591, 29991, 29591, 29879, 28999, 29095, 27430, 28871, 28695, 29799, 28855, 29447, 28887, 29719, 28919, 30471, 35016, 19700, 576, 288, 24838, 31751, 30311, 32455, 31767, 32471, 31639, 31895, 31431, 31127, 30695, 30695, 30007, 29959, 29415, 29351, 28422, 28646, 27606, 27782, 27526, 27814, 28198, 29527, 30935, 32039, 31831, 32695, 32247, 32968, 32295, 32615, 32151, 32439, 32167, 32535, 31319, 31991, 31239, 31703, 30919, 31047, 31015, 31399, 31031, 31719, 30743, 30967, 30423, 31255, 30695, 31255, 29783, 30263, 30935, 31255, 31415, 31175, 30631, 31383, 30935, 31287, 36504, 31015, 640, 656, 23461, 33256, 32631, 35144, 35784, 35640, 35752, 35368, 34440, 34312, 33112, 33096, 32535, 31943, 31687, 31495, 31287, 30359, 30423, 29671, 28887, 28983, 29863, 30439, 31719, 33032, 33128, 34104, 34200, 34504, 35000, 34776, 34536, 34520, 34696, 34552, 34472, 35016, 34328, 34088, 34344, 34360, 34952, 33976, 34328, 34120, 33784, 33800, 34120, 33240, 34072, 33352, 32551, 31975, 33496, 33032, 33512, 33048, 33496, 33192, 33624, 33368, 39257, 33992, 288, 288, 26582, 32647, 33672, 35848, 36408, 35672, 36776, 36104, 36760, 35480, 35768, 34664, 34776, 33560, 33976, 32439, 31879, 31127, 30871, 29831, 29895, 29847, 30199, 31495, 32920, 33480, 34824, 35176, 36072, 35816, 36969, 35800, 36568, 36056, 36520, 35576, 35912, 35672, 35288, 34968, 34584, 34296, 34488, 34376, 34296, 33432, 33592, 33208, 33864, 33832, 33160, 32311, 31687, 32151, 33384, 32872, 33048, 32824, 33336, 33704, 33272, 38153, 37433, 6145, 464, 21925, 33208, 33016, 36873, 36776, 37513, 37961, 37849, 37481, 37049, 36232, 35416, 35000, 34000]
# to_keep=ls[:141]
# def normalize_ecg(values):
#     min_val = min(values)
#     max_val = max(values)
#     norm=[]
    
#     for j in range(len(values)):
#         normalized_val = (values[j]-min_val)/(max_val-min_val)
#         norm.append(normalized_val)
#     return norm


# ecg_vals = normalize_ecg(to_keep)
# json_message={
#     'ECG' : to_keep,
#     'yearOfBirth': 1998,
#     'prevHeartCond': True,
#     'BPM': 98.2
# }


def get_patient_age_category(patient_age):
    if patient_age<16:
        age_category = 0
    elif patient_age>=16 and patient_age<=25:
        age_category = 1
    elif patient_age>=26 and patient_age<=40:
        age_category = 2
    elif patient_age>=41 and patient_age<=60:
        age_category = 3
    elif patient_age>=61 and patient_age<=80:
        age_category = 4
    else:
        age_category = 5
    
    return age_category


def get_bpm_abnormality(patient_bpm, age_categ):
    if age_categ!=0:
        
        if patient_bpm<60:
            anomaly = 'Bradycardia'
        elif patient_bpm<=100:
            anomaly = 'Normal'
        else:
            anomaly = 'Tachycardia'

            
    else:
        if patient_bpm<110:
            anomaly = 'Bradycardia'
        elif patient_bpm<=150:
            anomaly = 'Normal'
        else:
            anomaly = 'Tachycardia'
    
    return anomaly


def get_bpm_anomaly_category(bpm_anomaly):
    
    if bpm_anomaly == 'Normal':
        bpm_ano = 1
    elif bpm_anomaly == 'Bradycardia':
        bpm_ano = 0
    elif bpm_anomaly == 'Tachycardia':
        bpm_ano = 2
    else:
        bpm_ano = 1
    
    return bpm_ano


def load_ecg_model(model_name = 'ecg_disease.sav'):
    loaded_ecg_model = pickle.load(open(model_name, 'rb'))
    return loaded_ecg_model


def load_bpm_model(model_name = 'heartbeat_anomaly_model.sav'):
    loaded_bpm_model = pickle.load(open(model_name, 'rb'))
    return loaded_bpm_model


def translate_ecg_predictions(pred): 
    if pred:
        return "Normal"
    else:
        return "Coronary Artery Disease (CAD)"


def get_ecg_pred(ecg_vals, loaded_ecg_model):
    ecg_pred_data = ecg_vals
    pred_ecg = loaded_ecg_model.predict(ecg_pred_data)
    return translate_ecg_predictions(pred_ecg)
    return (pred_ecg)


def get_bpm_pred(patient_bpm, age_category, loaded_bpm_model):
    bpm_pred_data = pd.DataFrame()
    bpm_pred_data['age_category'] = [age_category]
    bpm_pred_data['bpm_readings'] = [patient_bpm]
    
    bpm_pred_data = bpm_pred_data.values
    
    pred_bpm = loaded_bpm_model.predict(bpm_pred_data)
    return pred_bpm


def get_patient_data(json_message):
    ecg_vals = json_message.get('ECG')
    yearOfBirth = json_message.get('yearOfBirth')
    prevHeartCond = json_message.get('prevHeartCond')
    patient_bpm = json_message.get('BPM')
    
    patient_age = datetime.now().year - yearOfBirth
    age_category = get_patient_age_category(patient_age)
    
    anomaly_found = prevHeartCond
    bpm_anomaly = get_bpm_abnormality(patient_bpm, patient_age)
    bpm_anomaly_categ = get_bpm_anomaly_category(bpm_anomaly)
    
    
    
    return ecg_vals, patient_age, age_category, patient_bpm, bpm_anomaly, bpm_anomaly_categ
    


# ecg_vals, patient_age, age_category, patient_bpm, bpm_anomaly, bpm_anomaly_categ = get_patient_data(json_message)

# pred = get_ecg_pred([ecg_vals], loaded_ecg_model)


# get_bpm_pred(patient_bpm, age_category , loaded_bpm_model)


# df = pd.read_pickle('data.pkl')



# dfdata = df.iloc[0]['ecg_readings']



# get_ecg_pred([dfdata], loaded_ecg_model)

