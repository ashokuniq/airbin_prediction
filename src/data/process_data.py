import random
import pandas as pd
from docs.data_config import *
import warnings

warnings.filterwarnings('ignore')


class AirbnbPricePredictor:

    def __init__(self, input_csv: str, save_csv_path: str):
        self.save_path = save_csv_path + file
        self.input_csv = input_csv

    # read input from a input path and return a dataframe
    def read_input(self) -> pd.DataFrame:
        return pd.read_csv(self.input_csv)

    # cleans the dataset
    def process_df(self):
        pro_df = self.read_input()
        print("Input data read is successful....")
        # dropping the features which are not required
        pro_df.drop(
            ['first_review', 'last_review', 'thumbnail_url', 'host_since', 'host_response_rate', 'number_of_reviews'],
            axis=1, inplace=True)

        # filling nans with appropriate values related to domain knowledge
        pro_df['host_has_profile_pic'].fillna('f', inplace=True)
        pro_df['host_identity_verified'].fillna('f', inplace=True)

        # dropping samples which has nans in limited samples
        pro_df.dropna(subset=['bathrooms', 'beds', 'bedrooms', 'zipcode'], inplace=True)

        # fixes for issues 1 & 2 in data report
        pro_df['neighbourhood'].fillna('nan', inplace=True)
        pro_df['zip_cluster_one'] = pro_df['zipcode'].apply(lambda x: x[0])
        pro_df['zip_cluster_two'] = pro_df['zipcode'].apply(lambda x: x[0:2])
        pro_df['zip_cluster_three'] = pro_df['zipcode'].apply(lambda x: x[0:3])
        pro_df.drop(pro_df[pro_df['zip_cluster_one'] == '7'].index, inplace=True)
        pro_df.drop(pro_df[pro_df['zip_cluster_two'] == '21'].index, inplace=True)
        pro_df['zipcode'][40025] = '91304'
        pro_df.drop(pro_df[pro_df['zipcode'] == '1m'].index, inplace=True)

        # fixes for issue 3 in data report
        # solving for first three digits
        three_cluster = pro_df.groupby(['zip_cluster_three']).agg({'neighbourhood': list}).reset_index()
        three_cluster['neighbourhood'] = three_cluster['neighbourhood'].apply(lambda x: self.filter_nans(list(set(x))))
        # solving for first two digits
        two_cluster = pro_df.groupby(['zip_cluster_two']).agg({'neighbourhood': list}).reset_index()
        two_cluster['neighbourhood'] = two_cluster['neighbourhood'].apply(lambda x: self.filter_nans(list(set(x))))
        # solving for first digit
        one_cluster = pro_df.groupby(['zip_cluster_one']).agg({'neighbourhood': list}).reset_index()
        one_cluster['neighbourhood'] = one_cluster['neighbourhood'].apply(lambda x: self.filter_nans(list(set(x))))
        # creating a dict of neighbours
        n_dict = dict(zip(three_cluster['zip_cluster_three'].to_list(), three_cluster['neighbourhood'].to_list()))
        n_dict.update(dict(zip(two_cluster['zip_cluster_two'].to_list(), two_cluster['neighbourhood'].to_list())))
        n_dict.update(dict(zip(one_cluster['zip_cluster_one'].to_list(), one_cluster['neighbourhood'].to_list())))
        # replace nans with neighbours based on nearest zipcode
        pro_df = pro_df.apply(lambda x: self.fill_nans(x, n_dict), axis=1)
        pro_df.drop(pro_df[pro_df['neighbourhood'] == 'nan'].index, inplace=True)
        print("Processing successful....")
        self.save_df(pro_df, self.save_path)
        print("Save successful....")

    # take dataframe as an input and saves it in a destination
    @staticmethod
    def save_df(input_df: pd.DataFrame, path: str):
        input_df.to_csv(path)

    def find_nans(self):
        nans_df = self.read_input()
        for column_name in nans_df.columns:
            if nans_df[column_name].isna().sum() > 0:
                print(column_name + " has " + str(nans_df[column_name].isna().sum()) + " nans ")

    @staticmethod
    def filter_nans(input_list):
        new_list = [x for x in input_list if x != 'nan']
        return new_list

    @staticmethod
    def fill_nans(input_df_row, dictionary):
        if input_df_row['neighbourhood'] == 'nan' \
                and input_df_row['zipcode'][:3] in dictionary \
                and len(dictionary[input_df_row['zipcode'][:3]]) > 1:
            input_df_row['neighbourhood'] = random.choice(dictionary[input_df_row['zipcode'][:3]])
            return input_df_row
        elif input_df_row['neighbourhood'] == 'nan' \
                and input_df_row['zipcode'][:2] in dictionary \
                and len(dictionary[input_df_row['zipcode'][:2]]) > 1:
            input_df_row['neighbourhood'] = random.choice(dictionary[input_df_row['zipcode'][:2]])
            return input_df_row
        elif input_df_row['neighbourhood'] == 'nan' \
                and input_df_row['zipcode'][0] in dictionary \
                and len(dictionary[input_df_row['zipcode'][0]]) > 1:
            input_df_row['neighbourhood'] = random.choice(dictionary[input_df_row['zipcode'][0]])
            return input_df_row
        else:
            return input_df_row


airbnb_price = AirbnbPricePredictor(input_path, save_path)
print('outside name-main line of code')
if __name__ == '__main__':
    print('inside name-main line of code')
    airbnb_price.process_df()
print('towards the end of script')





























"""for i, item in enumerate(pro_df.columns):
    if pro_df[item].isna().sum() > 0:
        print(item + " has " + str(pro_df[item].isna().sum()) + " nans ")"""

"""df['neighbourhood'].nunique()
df['review_scores_rating'] = df['review_scores_rating'].fillna(0)
temp_df = df[df['review_scores_rating'] == 0]
df['number_of_reviews'].describe()"""

# dropping the features which are not required
"""pro_df.drop(['first_review', 'last_review', 'thumbnail_url', 'host_since', 'host_response_rate', 'number_of_reviews'],
            axis=1, inplace=True)

# filling nans with appropriate values related to domain knowledge
pro_df['host_has_profile_pic'].fillna('f', inplace=True)
pro_df['host_identity_verified'].fillna('f', inplace=True)

# dropping samples which has nans in limited samples
pro_df.dropna(subset=['bathrooms', 'beds', 'bedrooms', 'zipcode'], inplace=True)
"""
# fixes for issues 1 & 2 in data report
"""df['zip_cluster_two'] = df['zipcode'].apply(lambda x: x[0:2])
df.drop(df[df['zip_cluster_two'] == '21'].index, inplace=True)
df['zip_cluster_one'] = df['zipcode'].apply(lambda x: x[0])
df.drop(df[df['zip_cluster_one'] == '7'].index, inplace=True)
df['zipcode'][40025] = 91304
df.drop(df[df['zipcode'] == '1m'].index, inplace=True)"""
"""
pro_df['zip_cluster_three'] = pro_df['zipcode'].apply(lambda x: x[0:3])
pro_df['neighbourhood'].fillna('nan', inplace=True)

temp_df = pro_df.groupby(['zip_cluster_three']).agg({'neighbourhood': list}).reset_index()
temp_df['neighbourhood'] = temp_df['neighbourhood'].apply(lambda x: list(set(x)))"""

# temp_df['list_count'] = temp_df['neighbourhood'].apply(lambda x: len(x))
# temp_df.to_csv(r'C:\Users\ashok\OneDrive\Desktop\test.csv')
# t2 = df[df['zip_cluster'] == '1m']
# df['neighbourhood'].isna().sum()

"""
temp_df = pro_df.groupby(['zip_cluster_three']).agg({'review_scores_rating': list}).reset_index()
temp_df['review_scores_rating'] = temp_df['review_scores_rating'].apply(lambda x: list(set(x)))
temp_df.to_csv(r'C:\\Users\\ashok\\OneDrive\\Desktop\\test.csv')

type(pro_df['review_scores_rating'][3])

raw_data = airbnb_price.read_input()"""