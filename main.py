from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json



app = FastAPI()


class param(BaseModel):
    
    
    Pregnancies :int
    Glucose :int
    BloodPressure :int
    SkinThickness :int
    Insulin :int
    BMI :float
    DiabetesPedigreeFunction :float
    Age :int
   
    
   
diabetic_model = pickle.load(open('random_classfier.pki','rb')) 



@app.post('/predic')
def predict(input_param : param):   
    
    input_data = input_param.json()
    input_dict = json.loads(input_data)
    
    
    preg = input_dict['Pregnancies']
    glu = input_dict['Glucose']
    blp = input_dict['BloodPressure']
    skin = input_dict['SkinThickness']
    ins = input_dict['Insulin']
    bmi = input_dict['BMI']
    dia = input_dict['DiabetesPedigreeFunction'] 
    age = input_dict['Age']



    input_list = [preg,glu,blp,skin,ins,bmi,dia,age]

    prediction = diabetic_model.predict([input_list])

    if prediction[0]==0:
        
        print('person is diabetic')
        
    else:
        print('notttty_diabetic')    

    