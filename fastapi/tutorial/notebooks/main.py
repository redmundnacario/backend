from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

# file paths/name
filename_model = 'svc_model_diabetic_detection.sav'
filename_scaler = 'minmax_scaler_diabetic_detection.sav'

#  load the scaler and model from disk
loaded_scaler = pickle.load(open(filename_scaler, 'rb'))
loaded_model = pickle.load(open(filename_model, 'rb'))


@app.get('/params/')
def mode_predict(NumTimesPrg : int, PlGlcConc : int, BloodP : int, SkinThick : int, TwoHourSerIns : int, BMI : float, DiPedFunc : float, Age : int):

    # params to array
    df = [[NumTimesPrg, PlGlcConc, BloodP, SkinThick, TwoHourSerIns, BMI, DiPedFunc, Age]]
   
    # scale
    new_df_scaled = loaded_scaler.transform(df)
    
    # predict
    result = loaded_model.predict(new_df_scaled)[0]

    return {"result": str(result)}
    # return NumTimesPrg, PlGlcConc, BloodP, SkinThick, TwoHourSerIns, BMI, DiPedFunc, Age