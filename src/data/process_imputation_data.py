import numpy
from src.data.process_data import AirbnbPricePredictor
from docs.data_config import *
import pandas as pd


class MissingDataPredictor(AirbnbPricePredictor):

    def __init__(self, input_csv: str, save_csv_path: str):
        super().__init__(input_csv, save_csv_path)
        self.input_csv = input_csv
        self.save_path_processed = save_csv_path + imputation_file
        self.before_processing = self.read_input()
        self.view_df = None

    """@staticmethod
    def detect_feature_outliers(input_df: pd.DataFrame, z_score_threshold: int) -> list:
        outlier_list_columns = []
        for i, item in enumerate(input_df.columns):
            if input_df[item].dtype == int or input_df[item].dtype == numpy.int64 or input_df[item].dtype == float or \
                    input_df[item].dtype == numpy.float64:
                z_score = input_df[item].apply(lambda x:
                                               abs((x - input_df[item].mean()) / (input_df[item].std()))).to_list()
                if any(y > z_score_threshold for y in z_score):
                    outlier_list_columns.append(item)
        return outlier_list_columns"""
    def imputation_process_df(self):
        df = self.before_processing
        df['beds_to_acc_ratio'] = df['beds'] / df['accommodates']
        df['bathrooms_to_acc_ratio'] = df['bathrooms'] / df['accommodates']
        df['bedrooms_to_acc_ratio'] = df['bedrooms'] / df['accommodates']
        test_df = df[((df['beds'] > 5) | (df['bathrooms'] > 4) | (df['bedrooms'] > 6))]
        test_df = test_df[~((df['beds_to_acc_ratio'] > 0.2) & (df['bathrooms_to_acc_ratio'] > 0.2) &
                            (df['bedrooms_to_acc_ratio'] > 0.2))]
        test_df = test_df.reset_index()
        index_to_drop = test_df['index'].to_list()
        df.drop(df.index[index_to_drop], inplace=True)
        return df

    def make_processed_data(self):
        raw_df = self.imputation_process_df()
        raw_df['review_scores_rating'].fillna('nan', inplace=True)
        train_df = raw_df[raw_df['review_scores_rating'] != 'nan']
        train_df.drop(features_to_remove, axis=1, inplace=True)
        self.view_df = train_df
        self.save_df(train_df, self.save_path_processed)
        print('raw data saved successfully....')


review_score_predictor = MissingDataPredictor(imputation_raw_input, save_path)
review_score_predictor.make_processed_data()
test = review_score_predictor.view_df
df = review_score_predictor.imputation_process_df()




































#df = pd.read_csv(raw_imputation_path)

"""df['bathrooms'].describe()
df['bedrooms'].describe()
df['beds'].describe()"""



# temp_df.to_csv(r'C:\Users\ashok\OneDrive\Desktop\test.csv')


"""mean = df['review_scores_rating'].mean()
std = df['review_scores_rating'].std()
df['z_review_scores_rating'] = df['review_scores_rating'].apply(lambda x: abs((x - mean) / std))
"""


"""for i, item in enumerate(df.columns):
    if type(df[item][0]) == numpy.int64 or type(df[item][0]) == numpy.float64:
        z_score = df[item].apply(lambda x: abs((x-df[item].mean())/df[item].std())).to_list()
        if any(y > 10 for y in z_score):
            print(item)"""

# print('before dropping: {}'.format(len(df)))




