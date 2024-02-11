import numpy as np
import pandas as pd
import cloudpickle

#Automcompletar rápido
#%config IPCompleter.greedy=True

from janitor import clean_names

from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import Binarizer
from sklearn.preprocessing import QuantileTransformer
from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

from sklearn.compose import ColumnTransformer

from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingRegressor


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline

#1. CARGA DE DATOS: aqui no necesitamos cargar los datos. Los datos son los que metamos en la app nosotros
#2. VARIABLES Y REGISTROS FINALES: tampoco lo necesitamos para la app, es el propio usuario el que nos lo va a dar en la app

### cambios de estructura
#def limpiar_nombres(df):
#    df = clean_names(df) 

### variables finales:

# variables_finales = ['abs',
#  'age_08_04',
#  'airco',
#  'automatic_airco',
#  'cc',
#  'cd_player',
#  'color',
#  'gears',
#  'guarantee_period',
#  'hp',
#  'km',
#  'metallic_rim',
#  'mfg_year',
#  'mfr_guarantee',
#  'mistlamps',
#  'model',
#  'powered_windows',
#  'quarterly_tax',
#  'sport_model',
#  'weight']

def ejecutar_modelo(df):
   

#df = df[variables_finales]
    ruta_proyecto = 'C:/Users/HP/Desktop/Cosas_Sergio/CURSOS/0__Mis_proyectos/Compra-venta coche usado/00_sbg_toyota_corolla'
    nombre_pipe_ejecucion = 'pipe_ejecucion.pickle'

    ruta_pipe_ejecucion = ruta_proyecto + '/04_Modelos/' + nombre_pipe_ejecucion

    with open(ruta_pipe_ejecucion, mode='rb') as file:
        pipe_ejecucion = cloudpickle.load(file)

    scoring = pipe_ejecucion.predict(df)

    return scoring











