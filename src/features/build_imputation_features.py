import numpy as np

from docs.utils import read_input, remove_symbols
from src.data.process_data import AirbnbPricePredictor
from docs.features_config import imputation_processed_raw_input
import re

"""from matplotlib import pyplot
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed"""


class ImputationFeatureBuilder:

    def __init__(self):
        self.df = read_input(imputation_processed_raw_input)
        self.df.drop(['Unnamed: 0'], axis=1, inplace=True)


imp = ImputationFeatureBuilder()
df = imp.df
df['amenities'] = df['amenities'].apply(lambda x: x.split(","))
df['amenities'] = df['amenities'].apply(lambda x: remove_symbols(x))
print(df['amenities'][0])
df['bed_type'].nunique()
df['neighbourhood'].nunique()
df['cleaning_fee'].nunique()
# df['converted_cleaning_fee'] = df['cleaning_fee'].apply(lambda x: x for x in )