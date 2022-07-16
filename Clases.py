from pydantic import BaseModel as BM
from pydantic import Field
from typing import Literal
import joblib
import pandas as pd


class InputModelo(BM):
        
    Genero: Literal["Femenino", "Masculino"]
    Edad: int = Field( ge=0, description="Edad de la persona")
    Historial_familiar: Literal["Si", "No"]
    C_rico_calorias: Literal["Si", "No"]
    F_Consumo_verduras: int = Field( ge=1, le=3, description="Frecuencia con la que come verduras")
    N_comidas: int = Field( ge=1, le=4, description="Numero de comidas consnumidas al dia")
    Meriendas: Literal['Algunas_veces', 'Frecuentemente', 'Siempre', 'No']
    Fumador: Literal["Si", "No"]
    F_actvidad_fisica: float = Field( ge=0, le=3, description="Frecuencia con la que realiza actividad fisica")
    T_uso_dispositivos: float = Field(ge=0, le=3, description="Tiempo de uso de dispositivo elctronicos")
    Consumo_calorias: Literal["Si", "No"]
    C_alcohol: Literal["No", "Algunas_veces", "Frecuentemente", "Siempre"]
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