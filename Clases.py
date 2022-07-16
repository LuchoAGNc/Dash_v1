from pydantic import BaseModel as BM
from pydantic import Field
from typing import Literal
import joblib
import pandas as pd


class InputModelo(BM):
    
    Edad: int = Field( ge=0, le=120, description="Edad de la persona")
    Historial_familiar: Literal["Si", "No"]
    C_rico_calorias: Literal["Si", "No"]
    F_Consumo_verduras: int = Field( ge=1, le=3, description="Frecuencia con la que come verduras")
    N_comidas: int = Field( ge=1, le=4, description="Numero de comidas consnumidas al dia")
    F_actvidad_fisica: float = Field( ge=0, le=3, description="Frecuencia con la que realiza actividad fisica")
    T_uso_dispositivos: float = Field(ge=0, le=3, description="Tiempo de uso de dispositivo elctronicos")
    Consumo_calorias: Literal["Si", "No"]
    C_alcohol: Literal["No", "Algunas_veces", "Frecuentemente", "Siempre"]
    Medio_transporte: Literal['Transporte_Publico', 'Caminar', 'Automovil', 'Moto','Bicicleta']
    
    
class OutputModelo(BM):
    """
    Clase que define la salida del modelo según la verá el usuario.
    """

    Tipo_obesidad: Literal['Peso_normal', 'Sobrepeso_Nivel_I', 'Sobrepeso_Nivel_II', 'Obesidad_Tipo_I', 'Peso_insuficiente', 'Obesidad_Tipo_II', 'Obesidad_Tipo_III']

    class Config:
        scheme_extra = {
            "example": {
                "Tipo_obesidad": 'Peso_normal',
            }
        }
    
class APIModelBackEnd:
    """
    Clase que se encarga la parte de prediccion.
    """
    def __init__(
        self, 
        Genero, 
        Edad, 
        Historial_familiar,
        C_rico_calorias,
        F_Consumo_verduras,
        N_comidas,
        F_actvidad_fisica,
        T_uso_dispositivos,
        Consumo_calorias,
        C_alcohol,
        Medio_transporte
        ):
        self.Edad = Edad
        self.Historial_familiar = Historial_familiar
        self.C_rico_calorias = C_rico_calorias
        self.F_Consumo_verduras = F_Consumo_verduras
        self.N_comidas = N_comidas
        self.F_actividad_fisica = F_actvidad_fisica
        self.T_uso_dispositivos = T_uso_dispositivos
        self.Consumo_calorias = Consumo_calorias
        self.C_alcohol = C_alcohol
        self.Medio_transporte = Medio_transporte
    
    def _load_model(self, model_filename: str = "random_m.pkl"):
        self.model = joblib.load(model_filename)

    def _preparar_datos(self):
        Edad = self.Edad
        Historial_familiar = self.Historial_familiar
        C_rico_calorias = self.C_rico_calorias
        F_Consumo_verduras = self.F_Consumo_verduras
        N_comidas = self.N_comidas
        F_actividad_fisica = self.F_actividad_fisica
        T_uso_dispositivos = self.T_uso_dispositivos
        Consumo_calorias = self.Consumo_calorias
        C_alcohol = self.C_alcohol
        Medio_transporte = self.Medio_transporte

        Historial_familiares = [0] * 2
        C_ricos_calorias = [0] * 2
        Consumos_calorias = [0] * 2
        C_alcoholes = [0] * 4
        Medio_transportes = [0] * 5

        data_predict = pd.DataFrame(
            columns=[
                "Edad",
                "F_Consumo_verduras",
                "N_comidas",
                "F_actvidad_fisica",
                "T_uso_dispositivos",
                "Genero_Femenino",
                "Genero_Masculino",
                "Historial_familiar_No",
                "Historial_familiar_Si",
                "C_rico_calorias_No",
                "C_rico_calorias_Si",
                "Consumo_calorias_No",
                "Consumo_calorias_Si",
                "C_alcohol_Algunas_veces",
                "C_alcohol_Frecuentemente",
                "C_alcohol_No",
                "C_alcohol_Siempre",
                "Medio_transporte_Automovil",
                "Medio_transporte_Bicicleta",
                "Medio_transporte_Caminar",
                "Medio_transporte_Moto",
                "Medio_transporte_Transporte_Publico",
            ],
            data=[[Edad, F_Consumo_verduras, F_Consumo_verduras, T_uso_dispositivos, *Historial_familiares, 
            *C_ricos_calorias, *Consumos_calorias, *C_alcoholes, *Medio_transportes]],
        )
        
        data_predict[
            [
                x
                for x in data_predict.columns
                if ((str(Historial_familiar) in x) and (x.startswith("Historial_familiar_")))
            ],
        ] = 1

        data_predict[
            [
                x
                for x in data_predict.columns
                if ((str(C_rico_calorias) in x) and (x.startswith("C_rico_calorias_")))
            ]
        ] = 1

        data_predict[
            [
                x
                for x in data_predict.columns
                if ((str(N_comidas) in x) and (x.startswith("N_comidas_")))
            ]
        ] = 1

        data_predict[
            [
                x
                for x in data_predict.columns
                if ((str(F_actividad_fisica) in x) and (x.startswith("F_actividad_fisica_")))
            ]
        ] = 1

        data_predict[
            [
                x
                for x in data_predict.columns
                if ((str(Consumo_calorias) in x) and (x.startswith("Consumo_calorias_")))
            ]
        ] = 1

        data_predict[
            [
                x
                for x in data_predict.columns
                if ((str(C_alcohol) in x) and (x.startswith("C_alcohol")))
            ]
        ] = 1
        
        data_predict[
            [
                x
                for x in data_predict.columns
                if ((str(Medio_transporte) in x) and (x.startswith("Medio_transporte")))
            ]
        ] = 1

        return data_predict

    def predecir(self, y_name="Tipo_obesidad"):
        self._cargar_modelo()
        x = self._preparar_datos()
        prediction = pd.DataFrame(self.model.predict(x)).rename(
            columns={0: y_name}
        )
        prediction[y_name]=prediction[y_name].apply(lambda x: 0 if x<0 else int(x))
        return prediction.to_dict(orient="records")