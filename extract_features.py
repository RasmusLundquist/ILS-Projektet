import json
fields =   ['request_text',
            'request_text',
            'request_title',
            'request_title',
            'requester_account_age_in_days_at_request',
            'requester_days_since_first_post_on_raop_at_request',
            'requester_number_of_comments_at_request',
            'requester_number_of_comments_in_raop_at_request',
            'requester_number_of_posts_at_request',
            'requester_number_of_posts_on_raop_at_request',
            'requester_number_of_subreddits_at_request',
            'requester_user_flair',
            'requester_user_flair',
            'requester_user_flair',
            'requester_username',
            'unix_timestamp_of_request_utc',
            'unix_timestamp_of_request_utc',
            'unix_timestamp_of_request_utc',
            'unix_timestamp_of_request_utc',
            'requester_received_pizza(class)']

features =   ['request_text_contains_please',
            'request_text_contains_uppercase'
            'request_title_contains_help',
            'request_title_contains_uppercase',
            'requester_account_age_in_days',
            'requester_days_since_first_post_on_raop',
            'requester_number_of_comments_on_reddit',
            'requester_number_of_comments_on_raop',
            'requester_number_of_posts_on_reddit',
            'requester_number_of_posts_on_raop',
            'requester_number_of_subreddits',
            'has_no_flair',
            'has_shroom',
            'has_pif',
            'requester_username_contains_pizza',
            'week_before_christmas',
            'new_year_week',
            'week_before_thanksgiving',
            'is_weekend',
            'requester_received_pizza(class)']


json_file = open('resources/train.json', 'r')

json_data = json.loads(json_file.read())

json_file.close()

out_file = open('resources/raop.csv', 'w+')

out_file.write('{}\n'.format(','.join(features)))

for entry in json_data:
    row = ','.join([str(float(entry[processing(field, fields, i, entry)])) for field, i in fields])
    out_file.write('{}\n'.format(row))



    def processing(field, fields, i, entry):
        h = 1337;
        switcher = {
            "request_text": process_text(field, i, entry)


        }
        return(switcher.get(field, "nothing"))

    def process_text(field):
        if(i>0):
            #process entry på det sätt som vi ska göra för första fallet dvs request_text_contains_please
            return(1)
        elif(i<2):
            #process entry på det sätt som vi ska göra för andra fallet dvs 'request_text_contains_uppercase'
            return(2)