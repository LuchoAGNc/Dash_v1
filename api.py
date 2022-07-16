"""API para el diplomado de Python de la Universidad de Córdoba"""


from fastapi import FastAPI
from typing import List
from Clases import OutputModelo, InputModelo, APIModelBackEnd

app = FastAPI(title="API Grupo 5", version="1.0.0")
"""Objeto FastAPI usado para el deployment de la API :)"""


@app.post("/predict", response_model=List[OutputModelo])
async def predict_proba(inputs: List[InputModelo]):
    """Endpoint de predicción de la API"""

    response = list()
 
    for Input in inputs:

        model = APIModelBackEnd(
            Input.Genero, Input.Edad, Input.Historial_familiar, Input.C_rico_calorias, 
            Input.F_Consumo_verduras, Input.N_comidas,
            Input.F_actvidad_fisica, Input.T_uso_dispositivos, Input.Consumo_calorias, Input.C_alcohol, Input.Medio_transporte
        )
        response.append(model.predecir()[0])
        
    return response