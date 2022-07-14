from pydantic import BaseModel as BM
from pydantic import Field
from typing import Literal
import joblib
import pandas as pd


class InputModelo(BM):
        
    Genero: Literal["Female", "Male"]
    Edad: int = Field( ge=0, description="Edad de la persona")
    Historial_familiar: Literal["yes", "no"]
    C_rico_calorias: Literal["yes", "no"]
    F_Consumo_verduras: int = Field( ge=1, le=3, description="Frecuencia con la que come verduras")
    N_comidas: int = Field( ge=1, le=4, description="Numero de comidas consnumidas al dia")
    Meriendas: Literal['Sometimes', 'Frequently', 'Always', 'no']
    Fumador: Literal["yes", "no"]
    F_actvidad_fisica: float = Field( ge=0, le=3, description="Frecuencia con la que realiza actividad fisica")
    Consumo_calorias: Literal["yes", "no"]
    C_alcohol: Literal['no', 'Sometimes', 'Frequently', 'Always']
    Medio_transporte: Literal['Public_Transportation', 'Walking', 'Automobile', 'Motorbike','Bike']
    
    
class OutputModelo(BM):
    """
    Clase que define la salida del modelo según la verá el usuario.
    """

    Tipo_obesidad: Literal['Peso_normal', 'Sobrepeso_Nivel_I', 'Sobrepeso_Nivel_II', 'Obesidad_Tipo_I', 'Peso_insuficiente', 'Obesidad_Tipo_II', 'Obesidad_Tipo_III']

    class Config:
        scheme_extra = {
            "example": {
                "employee_left": 0.69,
            }
        }
    
class APIModelBackEnd:
    """
    Clase que se encarga la parte de prediccion.
    """