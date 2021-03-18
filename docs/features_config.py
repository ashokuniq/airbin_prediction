# list of interested columns
imputation_features = ['log_price', 'property_type', 'room_type', 'amenities', 'accommodates', 'bathrooms', 'bed_type',
                       'cancellation_policy', 'cleaning_fee', 'city', 'host_has_profile_pic', 'host_identity_verified',
                       'instant_bookable', 'neighbourhood', 'review_scores_rating', 'zipcode', 'bedrooms', 'beds']

features_to_remove = ['Unnamed: 0', 'id', 'latitude', 'longitude', 'name', 'zip_cluster_one',
                      'zip_cluster_two', 'zip_cluster_three']

# raw imputation processed input path which is the processed output path of MissingData class
imputation_processed_raw_input = r'C:\Users\ashok\OneDrive\Desktop\AirPricePrediction' \
                       r'\airbnbprediction\data\processed\processed_imputation_df.csv'


# raw imputation input path which is the processed output path of Airbnb class
imputation_raw_input = r'C:\Users\ashok\OneDrive\Desktop\AirPricePrediction' \
                       r'\airbnbprediction\data\processed\processed_df.csv'

# filename of the processed file
file = '\\imputation_features.csv'

# path to save the processed csv
save_path = r'C:\Users\ashok\OneDrive\Desktop\AirPricePrediction\airbnbprediction\data\processed'
