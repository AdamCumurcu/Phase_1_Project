#---------- Functions to Gather Business Data from Yelp ----------#

#Function to call gather information from yelp
def yelp_call(url_params, api_key):
    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer ' + api_key}
    data = requests.get(url, headers = headers, params = url_params)
    return data

#Function to parse the gathered yelp results to make them easier to insert into the DB
def parse_results(results):
    results = results.json()['businesses']
    parsed_data = []
    for business in results:
        if 'price' not in business:
            biz_info = (business['id'], business['name'], business['is_closed'],
                business['review_count'], business['rating'], 'NaN',
                business['location']['address1'], business['location']['city'], business['location']['state'],
                business['location']['zip_code'], business['coordinates']['latitude'], business['coordinates']['longitude'])
            parsed_data.append(biz_info)
        else:
            biz_info = (business['id'], business['name'], business['is_closed'],
                business['review_count'], business['rating'], business['price'],
                business['location']['address1'], business['location']['city'], business['location']['state'],
                business['location']['zip_code'], business['coordinates']['latitude'], business['coordinates']['longitude'])
            parsed_data.append(biz_info)
    return parsed_data

#Function to open the csv file, concat the current data, and save the data. 
def df_safe(csv_filepath, parsed_results):
    parsed_results = pd.DataFrame(parsed_results)
    return parsed_results.to_csv(csv_filepath, mode = 'a', index = False, header = False)


#---------- Functions to the Reviews from Businesses ----------#

#Function to gather the reviews associated with yelp business reviews
def yelp_call_review(business, creds):
    url = 'https://api.yelp.com/v3/businesses/'+ business +'/reviews'
    headers = {'Authorization': 'Bearer ' + creds['key']}
    data = requests.get(url, headers = headers)    
    return data.json()['reviews']

#Function to parse the results of the yelp review call to make them easier to insert into the DB
def parse_results_review(results, business):
    parsed_data = []
    for review in results:
        biz_info = (business, review['id'], review['text'], review['rating'], review['time_created'],
                   review['user']['name'])
        parsed_data.append(biz_info)
    return parsed_data

#Function to open the csv file, concat the current data, and save the data3
def df_safe_review(csv_review_filepath, parsed_results):
    parsed_results = pd.DataFrame(parsed_results)
    return parsed_results.to_csv(csv_review_filepath, mode = 'a', index = False, header = False)


#---------- Percent Functions ----------#

#Ratings - This function returns the percentage of ratings with the 'rating' rating
def ratings_percent(dataset, rating):
    return round(((len(dataset[dataset['Rating'] == rating ]))/len(dataset['Rating']))*100, 2)

#Price - This function returns the percentage of prices with the 'price' pricing
#It excludes rows that do not contain a value for 'price'
def price_percent(dataset, price):
    return round(((len(dataset[dataset['Price'] == price ]))/(len(dataset[dataset['Price'].isna() != True ])))*100, 2)
