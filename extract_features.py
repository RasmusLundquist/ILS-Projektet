import json

import datetime

UnlikelyFloat = float('nan') #This number must not exist in JSon-data. It will be output to csv file in case of missing or misinterpreted values.

month  =   ['placeholder',
            'January',
            'February',
            'March',
            'April',
            'May',
            'June',
            'July',
            'August',
            'September',
            'October',
            'November',
            'December']

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


switcher = {'request_text_contains_please' : ('containsPlease', ['please']),
            'request_text_contains_uppercase' : ('caps', []),
            'request_title_contains_help' : ('containsPlease', ['help']),
            'request_title_contains_uppercase' : ('caps', []),
            'requester_account_age_in_days' : ('default', []),
            'requester_days_since_first_post_on_raop' : ('default', []),
            'requester_number_of_comments_on_reddit' : ('default', []),
            'requester_number_of_comments_on_raop' : ('default', []),
            'requester_number_of_posts_on_reddit' : ('default', []),
            'requester_number_of_posts_on_raop' : ('default', []),
            'requester_number_of_subreddits' : ('default', []),
            'has_no_flair' : ('flairIsNone', ['null']),
            'has_shroom' : ('flairIsShroom', ['shroom']),
            'has_pif' : ('flairIsPIF', ['PIF']),
            'requester_username_contains_pizza' : ('containsPlease', ['pizza']),
            'week_before_christmas' : ('wBeforeChristmas', []),
            'new_year_week' : ('nyWeek', []),
            'week_before_thanksgiving' : ('wbThanksgiving', []),
            'is_weekend' : ('isWeekend', []),
            'requester_received_pizza': ('default', [])
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
            #for (field, feature) in zip(self.jsonFields, self.csvFeatures):
            finalrow = ','.join([str(float(self.generateFunction(feature)(self.generateArgument(feature), entry[field]))) for (field, feature) in zip(self.jsonFields, self.csvFeatures)])
            self.out_file.write('{}\n'.format(finalrow))
            finalrow=''

        self.out_file.close()

    def containsPlease(self, *args):
        checkString = args[1]
        numberOfTermsInText = 0
        for term in args[0]:
            if term in checkString:
                numberOfTermsInText += 1
        return numberOfTermsInText



    def flairIsShroom(self, *args):
        if args[1] == "shroom":
            return 1.0
        else:
            return 0.0

    def flairIsPIF(self, *args):
        if args[1] == "PIF":
            return 1.0
        else:
            return 0.0

    def flairIsNone(self, *args):
        pif = self.flairIsPIF(*args)
        shroom = self.flairIsShroom(*args)
        if shroom == 0.0 and pif == 0.0:
            return 1.0
        else:
            return 0.0

    def caps(self, *args):
        countOfCapsChars = 0.0
        countOfTotalChars = 0.0
        for word in args[1].split(' '):
            for i in range(0, len(word)):
                if word[i].isupper():
                    countOfCapsChars += 1
                countOfTotalChars += 1

        if(countOfTotalChars == 0):
            result = 0.0
        else:
            result = countOfCapsChars / countOfTotalChars

        return result

    def isWeekend(self, *args):
        date = datetime.datetime.utcfromtimestamp(args[1])
        if date.weekday() == 4 or date.weekday() == 5 or date.weekday() == 6:
            return 1.0
        else:
            return 0.0
            
    def wBeforeChristmas(self, *args):
        dt = datetime.datetime
        ut = dt.utcfromtimestamp(args[1])
        (y, m, d, x1, x2, x3, x4, x5 ,x6) = dt.timetuple(ut)
        
        if month[m] == 'December' and d in range(17, 26):
            return 1.0
        
        return 0.0
    
    def nyWeek(self, *args):
        dt = datetime.datetime
        ut = dt.utcfromtimestamp(args[1])
        (y, m, d, x1, x2, x3, x4, x5 ,x6) = dt.timetuple(ut)
        
        if (month[m] == 'December' and d in range(24, 32)) or (month[m] == 'January' and d in range(1, 8)):
            return 1.0
        
        return 0.0        

    def wbThanksgiving(self, *args):
        dt = datetime.datetime
        ut = dt.utcfromtimestamp(args[1])
        (y, m, d, x1, x2, x3, x4, x5 ,x6) = dt.timetuple(ut)
        #Thanksgiving is celebrated on the fourth thursday in November and is four days long.
        if ((month[m] == 'November') and (d in range(22, 31))) or ((month[m] == 'December') and (d == 1)):
            return 1.0
        
        return 0.0
    

    def default(self, *args):

        lastarg = args[-1]

        if(isinstance(lastarg, float)):
            return lastarg
        
        if(isinstance(lastarg, int)):
            return lastarg

        if(isinstance(lastarg, bool)):
            if(lastarg == True):
                return 1
            return 0

        return UnlikelyFloat

process = ProcessJson('resources/train.json', fields, 'resources/raop.csv', features, switcher)

process.process()
