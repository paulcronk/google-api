from google2pandas import *

query = {\
    'ids'           : '53872948',
    'metrics'       : 'pageviews',
    'dimensions'    : ['date', 'pagePath', 'browser'],
    'filters'       : ['pagePath=~iPhone', 'and', 'browser=~Firefox'],
    'start_date'    : '8daysAgo',
    'max_results'   : 10}

ga = GoogleAnalyticsQuery(token_file_name='analytics.dat')
df, metadata = ga.execute_query(**query)
