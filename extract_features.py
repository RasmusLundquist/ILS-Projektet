import json

UnlikelyFloat = -2446663.45452 #This number must not exist in JSon-data. It will be output to csv file in case of missing or misinterpreted values.

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
            'requester_received_pizza']

features = ['request_text_contains_please',
            'request_text_contains_uppercase',
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
            'requester_received_pizza']


switcher = {'request_text_contains_please' : ('func1', ['please']),
            'request_text_contains_uppercase' : ('default', ['please']),
            'request_title_contains_help' : ('default', ['please']),
            'request_title_contains_uppercase' : ('default', ['please']),
            'requester_account_age_in_days' : ('default', ['please']),
            'requester_days_since_first_post_on_raop' : ('default', ['please']),
            'requester_number_of_comments_on_reddit' : ('default', ['please']),
            'requester_number_of_comments_on_raop' : ('default', ['please']),
            'requester_number_of_posts_on_reddit' : ('default', ['please']),
            'requester_number_of_posts_on_raop' : ('default', ['please']),
            'requester_number_of_subreddits' : ('default', ['please']),
            'has_no_flair' : ('default', ['please']),
            'has_shroom' : ('default', ['please']),
            'has_pif' : ('default', ['please']),
            'requester_username_contains_pizza' : ('default', ['please']),
            'week_before_christmas' : ('default', ['please']),
            'new_year_week' : ('default', ['please']),
            'week_before_thanksgiving' : ('default', ['please']),
            'is_weekend' : ('default', ['please']),
            'requester_received_pizza': ('default', ['please'])
            }






#for entry in json_data:
#   row = ','.join([str(float(entry[processing(field, fields, i, entry)])) for field, i in fields])
#  out_file.write('{}\n'.format(row))

class ProcessJson():

    def __init__(self, jsonFile, jsonFields, csvFile, csvFeatures, dictSwitcher):

        self.json_file = open(jsonFile, 'r')

        self.json_data = json.loads(self.json_file.read())

        self.json_file.close()

        self.out_file = open(csvFile, 'w+')

        self.out_file.write('{}\n'.format(','.join(csvFeatures)))

        self.jsonFields = jsonFields

        self.csvFeatures = csvFeatures

        self.dictSwitcher = dictSwitcher

    def generateFunction(self, feature):

        (f,a) = self.dictSwitcher.get(feature, ('default',None))
        funcName = str(f)
        print(funcName)
        function = getattr(self, funcName, lambda x: 'bad')
        return function

    def generateArgument(self, feature):

        (f,a) = self.dictSwitcher.get(feature, ('default',None))
        print(a)
        return a

    def process(self):

        finalrow = ''
        for entry in self.json_data:
            for (field, feature) in zip(self.jsonFields, self.csvFeatures):
                f = self.generateFunction(feature)
                a = self.generateArgument(feature)
                finalrow = finalrow + finalrow.join([str(float(f(a, entry[field])))]) + ','
            self.out_file.write('{}\n'.format(finalrow))
            finalrow=''

        self.out_file.close()

    def func1(self, *args):
        print args[0]
        return 99.0

    def default(self, *args):
        arglen = len(args)

        lastarg = args[arglen-1]

        if(isinstance(lastarg, float)):
            return lastarg

        if(isinstance(lastarg, bool)):
            if(lastarg == True):
                return 1
            return 0

        return UnlikelyFloat

process = ProcessJson('resources/train.json', fields, 'resources/raop.csv', features, switcher)

process.process()
