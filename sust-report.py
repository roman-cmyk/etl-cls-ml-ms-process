'''
This script uses H2 data as input
to generate the Sustentability report.
'''
from calendar import month
import pandas as pd

h2_data = pd.read_csv('h2_data.csv') # specify the path to the H2 data

h2_months = ['January', 'February', 'March', 'April', 'May', 'June'] # list of months in H2

qs = ['Q3', 'Q4'] # list of quarters in H2

h = ['H2'] # required H

sust_columns = ["No", # required columns for excel files
"Corte",
"Source",
"Type",
"Host",	
"Link",	
"Link Image",	
"Tier",
"Media Type",	
"MediaList",	
"CIMS",	
"Date(ET)",	
"Full Month",	
"Month",	
"Q",	
"H",	
"Author Name",	
"Language",	
"Country",	
"Sub",	
"Title",	
"Contents",	
"Sentiment",	
"Company",	
"DOUBLE_CHECK",	
"Prevailing Category",	
"Resumen_Categorias",	
"Mayusculas_Contents",	
"Mayusculas_Title",	
"CLEAN_Contents",	
"1_GRAM_Contents",	
"COMPETIDORES",	
"COMPETIDORES_FOUND",	
"Is It Title Related?",	
"Is It Content Related?",	
"Is Related overall?",	
"Is It Related?",	
"SOV ALL",	
"SOV Focused",	
"Direct Business/Non-Direct Business",	
"Local/Global",	
"News Cycle",	
"Secondary News Cycle/News Moment",	
"Microsoft Sentiment",	
"Google Sentiment",	
"Facebook Sentiment",	
"Apple Sentiment",	
"Amazon Sentiment",	
"IBM Sentiment",	
"Zoom Sentiment",	
"Salesforce Sentiment",	
"Clean_Host",	
"TAM_CONTENTS",	
"Full Content",	
"BRAND_MENTIONS_Microsoft",	
"PRODUCT_MENTIONS_Microsoft",	
"RESULTS_CAT_NOTA_Microsoft",	
"CAT_NOTA_Microsoft",	
"RESULTS_CAT_NOTA_Apple",	
"CAT_NOTA_Apple",	
"RESULTS_CAT_NOTA_Amazon",	
"CAT_NOTA_Amazon",	
"RESULTS_CAT_NOTA_Facebook",	
"CAT_NOTA_Facebook",	
"RESULTS_CAT_NOTA_Google",	
"CAT_NOTA_Google",	
"RESULTS_CAT_NOTA_IBM",	
"CAT_NOTA_IBM",	
"RESULTS_CAT_NOTA_Zoom",	
"CAT_NOTA_Zoom",	
"RESULTS_CAT_NOTA_Salesforce",	
"CAT_NOTA_Salesforce",	
"Amazon",	
"Zoom",	
"Facebook",	
"Apple",	
"Google",	
"IBM",	
"Salesforce",	
"Microsoft",	
"MICROSOFT_PRODUCTS",	
"MICROSOFT_PRODUCTS_FOUND",	
"GOOGLE_PRODUCTS",	
"GOOGLE_PRODUCTS_FOUND",	
"AMAZON_PRODUCTS",	
"AMAZON_PRODUCTS_FOUND",	
"APPLE_PRODUCTS",	
"APPLE_PRODUCTS_FOUND",	
"FACEBOOK_PRODUCTS",	
"FACEBOOK_PRODUCTS_FOUND",	
"IBM_PRODUCTS",	
"IBM_PRODUCTS_FOUND",	
"ZOOM_PRODUCTS",	
"ZOOM_PRODUCTS_FOUND",	
"SALESFORCE_PRODUCTS",	
"SALESFORCE_PRODUCTS_FOUND",	
"SUSTAINABILITY",	
"SUSTAINABILITY_FOUND"]


'''
This section is used to check the integrity of the data.
    * Check if the data belongs to H2, Qs and months.
    * Check if the data is valid to be used in the report: (H2, Q, Month and Sub)
    * Check if the data is consistent: volume by sub in the period.
    * Check how the data is structured: size and number of columns.
    * Check if the data is in the correct format: pandas dataframe.
    * Check if we are missing any data manipulation step.
'''
def check_data(df):
    if df['Full Month'].isin(h2_months) and df['Q'].isin(qs) and df['H'].isin(h):
        print('Data is valid')
    else:
        print('Data is not valid')

check_data(h2_data)

# keep only required columns for analysis
sust_df = h2_data[sust_columns]
print(sust_df.shape)

# keep only usable data
sust_df = sust_df[sust_df['SUSTAINABILITY_FOUND'] > 0]
print(sust_df.shape)

# creating an excel file by sub for data analysis
for sub in sust_df['Sub'].unique():
    sust_df_sub = sust_df[sust_df['Sub'] == sub]
    sust_df_sub.to_excel('sust-report-{}.xlsx'.format(sub), index=False, encoding='utf-8')
    print('File created: sust-report-{}.xlsx'.format(sub))