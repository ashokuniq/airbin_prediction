import pandas as pd
import re


# function to read a csv from a given input path and returns a dataframe
def read_input(input_csv_path) -> pd.DataFrame:
    return pd.read_csv(input_csv_path)


# replace symbols with space
def remove_symbols(input_list):
    return [re.sub(' +', ' ', re.sub('[^a-zA-Z0-9]', ' ', item)).strip() for item in input_list]








"""# replace symbols with space
def remove_symbols(input_list):
    symbols_removed_list = [re.sub('[^a-zA-Z0-9]', ' ', item) for item in input_list]
    space_normalized_list = [re.sub(' +', ' ', item) for item in symbols_removed_list]
    return space_normalized_list"""
