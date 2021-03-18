## Imputation data information

1. The processed data set has 72811 samples and 27 features
2. 'review_scores_rating' has 16356 nans 


### Fixed issues
1. Created a new columns 'beds_to_acc_ratio', 'bathrooms_to_acc_ratio', 'bedrooms_to_acc_ratio' by dividing 'accommodates' column
2. Calculated z_score and set threshold as 0.2
