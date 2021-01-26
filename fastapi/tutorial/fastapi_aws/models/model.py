from fastapi import APIRouter
import pickle

router = APIRouter()

# file paths/name
filename_model = './app/api/api_v1/models/svc_model_diabetic_detection.sav'
filename_scaler = './app/api/api_v1/models/minmax_scaler_diabetic_detection.sav'

#  load the scaler and model from disk
loaded_scaler = pickle.load(open(filename_scaler, 'rb'))
loaded_model = pickle.load(open(filename_model, 'rb'))

@router.get("/diabetic_detect/")
async def mode_predict(NumTimesPrg : int, PlGlcConc : int, BloodP : int, SkinThick : int, TwoHourSerIns : int, BMI : float, DiPedFunc : float, Age : int):

    # params to array
    df = [[NumTimesPrg, PlGlcConc, BloodP, SkinThick, TwoHourSerIns, BMI, DiPedFunc, Age]]
   
    # scale
    new_df_scaled = loaded_scaler.transform(df)
    
    # predict
    result = loaded_model.predict(new_df_scaled)[0]

    return {"result": str(result)}


    # return NumTimesPrg, PlGlcConc, BloodP, SkinThick, TwoHourSerIns, BMI, DiPedFunc, Age