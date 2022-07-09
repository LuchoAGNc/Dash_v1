import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, HistGradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import pickle

df = pd.read_csv('ObesityDataNew.csv')

x = pd.get_dummies(df[['Genero', 'Edad', 'Historial_familiar', 'C_rico_calorias',
       'F_Consumo_verduras', 'N_comidas', 'Meriendas', 'Fumador', 'F_actvidad_fisica',
       'Consumo_calorias', 'Consumo_agua', 'C_alcohol', 'Medio_transporte']].copy())
y  = df[['Tipo_obesidad']].copy()

X_train, X_test, y_train, y_test = train_test_split(x,y)

ran_for = RandomForestClassifier()
hist_grad = HistGradientBoostingClassifier()
dec_cls = DecisionTreeClassifier()
svc_m = SVC()

ran_for = ran_for.fit(X_train, y_train)
hist_grad = hist_grad.fit(X_train, y_train)
dec_cls = dec_cls.fit(X_train, y_train)
svc_m = svc_m.fit(X_train, y_train)

with open('ran_for.pkl', 'wb') as ra:
    pickle.dump(ran_for, ra)

with open('hist_grad.pkl', 'wb') as hi:
    pickle.dump(hist_grad, hi)

with open('dec_cls.pkl', 'wb') as de:
    pickle.dump(dec_cls, de)

with open('svc_m.pkl', 'wb') as sv:
    pickle.dump(svc_m, sv)