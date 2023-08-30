import pickle
import pandas as pd


def make_prediction(input: dict) -> float:
    model_path = 'main_app/static/models/finalized_model.pkl'
    model = pickle.load(open(model_path, 'rb'))
    try:
        pred = int(model.predict(pd.DataFrame(input, index=[0])))
    except TypeError:
        pred = 0
    except ValueError:
        pred = 0
    return pred
