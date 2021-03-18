## Data Information

1. The dataset has 74k samples 
2. Compared to all the features 'first_review', 'last_review', 'thumbnail_url', 'host_since' and 'host_response_rate' had the highest number of nans plus features are not meaningful and so it is decided to remove the feature
3. 'host_has_profile_pic' has 188 nans and 'host_identity_verified' has 185 nans with respect to situation, it is decided to fill nans with 'f'
4. 'bathrooms', 'beds', 'bedrooms' and 'zipcode' has very fewer nans and there are useful features and so it is decided to remove samples
5. 'neighborhood' is an important feature, and so we are mapping it approximately using 'zipcode'
6. 'number_of_reviews' has an unpredictable distribution hence it is decided to temporarily remove it
7. 'review_scores_rating' has 16356 nans 

### Fixed issues
1. Fixed 'zipcode' in index no 40025 as 91304. since the value of the zipcode is Near91304
2. Dropped sample of 'zipcode' which has the value as 1m
3. Fixed 'neighbourhood' which has value as nan, replaced with random neighbourhood by comparing with the nearest 'zipcode'
4. 
