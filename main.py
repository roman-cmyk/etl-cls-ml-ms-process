# -- Application Details --
'''
App details:
    * App Name: MS Data Pipeline - CLF
    
    * Owner: Porter Novelli
    
    * Team: Data Analytics / Data Engineering
    
    * Environment: Development
    
    * Team Members: David Arce,
        Javier Santiago,
        Fernando Ojeda,
        Roman de la Rosa
    
    * Lead: Hector Bermudez
    
    * Cloud Provider: Microsoft Azure (in Dev.)
    
    * Repository URL: Azure DevOps []
'''
os.getcwd()
# -- Import Libraries --
import pandas as pd
import pandas.io.formats.excel
pandas.io.formats.excel.header_style = None
import numpy as np
import random
from operator import index
import datetime as dt
import os
import base64
import glob
import json
import time
import requests
import re
import urllib.request, sys, time
import newspaper
from newspaper import Article, fulltext, Config, ArticleException
import fuzzywuzzy
from bs4 import BeautifulSoup
import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk import bigrams
from nltk import ngrams
import collections
from functions import *
# -- Read EML & Keywords --


# -- Read Data Sources --

     # -- Build Synthesio DataFrame Template --
# -- Define synthesio dataframe -- #
synthTemplate = pd.DataFrame(columns=[
    'Id',
    'Date',
    'Time',
    'Media Type',
    'Site Name',
    'Site Domain',
    'Mention URL',
    'Publisher Name',
    'Publisher Username',
    'title',
    'Mention Content',
    'Topics',
    'Subtopics',
    'Sentiment',
    'Star Rating',
    'Country',
    'State',
    'City',
    'Language',
    ])
print (synthTemplate.shape)
synthTemplate.head()

     # -- Read CIMS Data --
# Use synthesio template to create cims dataframe
CimsSynth = synthTemplate.copy(deep=True)
CimsSynth

'''
Reading all .csv files from CIMS in a specific
folder using 'glob' library
'''
path = '/content/cims'
cims_csv_files = glob.glob(os.path.join(path, "*.csv"))
for f in cims_csv_files:
    cimsRawData = pd.concat([pd.read_csv(f, delimiter = ';', error_bad_lines = False, encoding = 'utf-8') for f in cims_csv_files])
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
print(cimsRawData.shape)
cimsRawData.head(3)


# -- Formatting CIMS to Synthesio -- #
CimsSynth['Id'] = cimsRawData['Article ID']
CimsSynth['Date'] = pd.to_datetime(cimsRawData['Published date'
        ]).dt.date
CimsSynth['Time'] = pd.to_datetime(cimsRawData['Published date'
        ]).dt.time
CimsSynth['title'] = cimsRawData['Headline']
CimsSynth['Country'] = cimsRawData['Country']
CimsSynth['Language'] = cimsRawData['Language']
CimsSynth['Source'] = 'CIMS'
CimsSynth['Mention URL'] = cimsRawData['Url']
CimsSynth['Site Domain'] = 'httsp://' + cimsRawData['Outlet Name']
CimsSynth['Publisher Name'] = cimsRawData['Author Name']

print (CimsSynth.shape)
CimsSynth.head(3)

'''
Checkpoint: rows & columns number: CIMS
'''
print(CimsSynth.columns, "\n","Rows number:", CimsSynth.shape[0],"\n", "Columns number:", CimsSynth.shape[1])
CimsSynth.head(3)

     # -- Read GN Data --
'''
This function reads ".json" from GN
'''
def read_json(file_path):
    data = {}
    with open(file_path, encoding = 'utf-8') as json_file:
        arq = json.load(json_file)
    data['Notas'] = arq
    return data

'''
This function is usd to create a dataframe from the json file: Global News
'''
def crear_df_json(data):
    df_n = pd.DataFrame(columns=[
        'IdNoticia',
        'Fecha',
        'Hora',
        'TipoDeMedio',
        'País',
        'Sección',
        'Título',
        'Cuerpo',
        'Tier',
        'NroCaracteres',
        'Tono',
        'LinkImagen',
        'CPE',
        'Moneda',
        'Audiencia',
        'Tema',
        'Empresa',
        'NroPagina',
        'Dimension',
        'CirculacionMedio',
        'AutorConductor',
        'ResumenAclaracion',
        'LinNota',
    ])
    for item in data['Notas']:
        dftemp = pd.DataFrame.from_dict(item, orient='index')
        dftemp = dftemp.T
        df_n = df_n.append(dftemp)
    df_n = df_n.reset_index()
    return df_n

'''
Read .rar GN files and export them as .json ones
'''
from zipfile import *
import glob
zip_files = glob.glob('/content/gn/zip/*.zip') # Change it based on your computer path
unzipped_files=r'/content/gn/unzip' # Change it based on your computer path
for zip_file in zip_files:
   file_name = zip_file.split('\\')[-1]
   print('Processing file:', file_name)
   name_unzipped=file_name.replace('.zip','.json')
   zipdata = ZipFile(zip_file)
   zipinfos = zipdata.infolist()
   for zipinfo in zipinfos:
     zipinfo.filename =name_unzipped
     zipdata.extract(zipinfo,unzipped_files)
     print('Extracted to unzipped folder as: ',name_unzipped)


'''
Define required empty dataframe for Global News
'''
df_notas = pd.DataFrame(columns=[
    'IdNoticia',
    'Fecha',
    'Hora',
    'TipoDeMedio',
    'Medio',
    'País',
    'Programa - Sección',
    'Título',
    'Tier',
    'NroCaracteres',
    'Tono',
    'LinkImagen',
    'CPE',
    'Moneda',
    'Audiencia',
    'Tema',
    'Empresa',
    'NroPagina',
    'Dimensión',
    'CirculaciónMedio',
    'AutorConductor',
    'ResumenAclaracion',
    'LinkNota',
    'Id_Noticia',
    'Cuerpo',
    'Link_Original',
    'Fecha_Nota'])
df_notas

'''
Path to unzipped json files
'''
unzipped_files = '/content/gn/unzip/content/gn/zip' # Change it based on your computer path
lista_zip = glob.glob(unzipped_files + '*.json')
lista_zip

'''
Read JSON files folder locally
'''
path = '/content/gn/unzip/content/gn/zip' # Change it based on your computer path
lista_zip = []

for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            lista_zip.append(os.path.join(r, file))
lista_zip

for file in lista_zip:
    data = read_json(file)
    df_json = crear_df_json(data)
    print(df_json.shape)
    df_notas = df_notas.append(df_json, 'sort = False')
    print(df_notas.shape)
df_notas.head(3)
df_notas = df_notas.reset_index(drop=True)
print(df_notas.shape)
df_notas.head(3)

## -- Create a copy of synthesio template
globalNewsSynth = synthTemplate.copy(deep=True)
globalNewsSynth

# -- Formatting Global News to Synthesio -- #
globalNewsSynth['Id'] = df_notas['IdNoticia']
globalNewsSynth['Date'] = pd.to_datetime(df_notas['Fecha'
        ]).dt.date
globalNewsSynth['Time'] = df_notas['Hora']
globalNewsSynth['title'] = df_notas['Título']
globalNewsSynth['Country'] = df_notas['País']
globalNewsSynth['Source'] = 'GN'
globalNewsSynth['Mention URL'] = df_notas['LinkNota']
globalNewsSynth['Media Type'] = df_notas['TipoDeMedio']
globalNewsSynth['Mention Content'] = df_notas['Cuerpo']
globalNewsSynth['Site Name'] = df_notas['Medio']

print (globalNewsSynth.shape)
globalNewsSynth.head(3)

'''
Checkpoint: rows & columns number: Global News
'''
print(globalNewsSynth.columns, "\n","Rows number:", globalNewsSynth.shape[0],"\n", "Columns number:", globalNewsSynth.shape[1])
globalNewsSynth.head(3)

     # -- Read Synthesio Data --
'''
Reading all .xlsx files from Synthesio in a specific
folder using 'glob' library
'''
path = '/content/synthesio'
synthesio_xlsx_files = glob.glob(os.path.join(path, "*.xlsx"))
for f in synthesio_xlsx_files:
    synthesioRawData = pd.concat([pd.read_excel(f, engine='openpyxl') for f in synthesio_xlsx_files])
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
print(synthesioRawData.shape)
synthesioRawData.head(3)

## -- Create a copy of synthesio template
synthesioSynth = synthTemplate.copy(deep=True)
synthesioSynth

# -- Formatting Synthesio -- #
synthesioSynth['Id'] = synthesioRawData['Id']
synthesioSynth['Date'] = pd.to_datetime(synthesioRawData['Date'
        ]).dt.date
synthesioSynth['Time'] = synthesioRawData['Time']
synthesioSynth['title'] = synthesioRawData['title']
synthesioSynth['Country'] = synthesioRawData['Country']
synthesioSynth['Source'] = 'Synthesio'
synthesioSynth['Mention URL'] = synthesioRawData['Mention URL']
synthesioSynth['Media Type'] = synthesioRawData['Media Type']
synthesioSynth['Mention Content'] = synthesioRawData['Mention Content']
synthesioSynth['Site Name'] = synthesioRawData['Site Name']

print (synthesioSynth.shape)
synthesioSynth.head(3)

'''
Checkpoint: rows & columns number: Synthesio
'''
print(synthesioSynth.columns, "\n","Rows number:", synthesioSynth.shape[0],"\n", "Columns number:", synthesioSynth.shape[1])
synthesioSynth.head(3)

     # -- Read Subs Coverage Data --
path= '/content/subs/'
for file in os.listdir(path):
    if file.endswith(".xlsx"):
        subs = pd.DataFrame()
        print(file)
        df = pd.read_excel(path+file, sheet_name=None)
        df = pd.concat(df, ignore_index=True)
        subs = subs.append(df)
        df.to_csv(path+file.replace('.xlsx', '.csv'), index=False)
        print('converted to csv')
        print('\n')
    else:
        print('not an excel file')
        print('\n')

'''
Reading all .csv files from Subs in a specific
folder using 'glob' library
'''
path = '/content/subs'
subs_csv_files = glob.glob(os.path.join(path, "*.csv"))
for f in subs_csv_files:
    subsRawData = pd.concat([pd.read_csv(f, delimiter = ',', error_bad_lines = False, encoding = 'utf-8') for f in subs_csv_files])
    print('Location:', f)
    print('File Name:', f.split("\\")[-1])
print(subsRawData.shape)
subsRawData.head(3)

## -- Create a copy of synthesio template
subsSynth = synthTemplate.copy(deep=True)
subsSynth

subsRawData['Date'] = subsRawData['Date'].astype(str)

# -- Formatting Subs Coverage -- #
subsSynth['Date'] = pd.to_datetime(subsRawData['Date'], errors='coerce')
subsSynth['Time'] = pd.to_datetime(subsRawData['Date'], errors='coerce').dt.time
subsSynth['title'] = subsRawData['Title']
subsSynth['Country'] = subsRawData['Country']
subsSynth['Source'] = 'Subs'
subsSynth['Mention URL'] = subsRawData['URL']
subsSynth['Site Name'] = subsRawData['Media Outlet']

print(subsSynth.shape)
subsSynth.head(3)

     # -- Read Other Sources --
'''
This section is dedicated to manipulate
any other source of data that is not included in the previous ones.
'''

# ** -- DATA INTEGRITY CHECK -- **
'''
This section is used to check the integrity of the data.
    * Check if the data is complete.
    * Check if the data is valid.
    * Check if the data is consistent.
    * Check if the data is accurate.
    * Check how the data is structured.
    * Check if the data is in the correct format.
    * Check if we are missing any data manipulation step.
    * CHECK IF REMOVED DUPLICATES WERE THE CORRECT ONES.
'''

# -- Verify duplicates in Global News: Print News --
'''
Pending to be implemented
'''
    
# -- Remove Duplicated Records --
preliminarData = pd.concat([CimsSynth,
                            globalNewsSynth,
                            synthesioSynth,
                            subsSynth])
print(preliminarData.shape)
preliminarData.head(3)

preliminarData.drop_duplicates(subset=None, keep='first', inplace=True)
print(preliminarData.shape)
preliminarData.head(3)

'''
Checkpoint: rows & columns number: Preliminar Data
'''
print(preliminarData.columns, "\n","Rows number:", preliminarData.shape[0],"\n", "Columns number:", preliminarData.shape[1])
preliminarData.head(3)



# **-- PUSH TO DATATABLES (RAW DATA) --**

    # -- BigQuery Table: CIMS --


    # -- BigQuery Table: GM --


    # -- BigQuery Table: Synthesio --


    # -- BigQuery Table: Subs Coverage --


    # -- BigQuery Table: Other Sources --

# **-- CONTENT EXTRACTION: CRAWLING PROCESS --**
#Diffbot API
user = 'katia.bedolla@porternovelli.mx'
API_TOKEN = '7a7668b8111a6e4d5750c12a8c93b56d'

class DiffbotClient(object):

    base_url = 'http://api.diffbot.com/'

    def request(self, url, token, api, fields=None, version=3, **kwargs):
        """
        Returns a python object containing the requested resource from the diffbot api
        """
        params = {"url": url, "token": token}
        if fields:
            params['fields'] = fields
        params.update(kwargs)
        response = requests.get(self.compose_url(api, version), params=params)
        response.raise_for_status()
        return response.json()

    def compose_url(self, api, version_number):
        """
        Returns the uri for an endpoint as a string
        """
        version = self.format_version_string(version_number)
        return '{}{}/{}'.format(self.base_url, version, api)
    @staticmethod
    def format_version_string(version_number):
        """
        Returns a string representation of the API version
        """
        return 'v{}'.format(version_number)


def get_content_diffbot(url):
    diffbot = DiffbotClient()
    token = API_TOKEN
    api = "analyze"
    try:
        response = diffbot.request(url, token, api)
        if 'objects' in response:
            if len(response['objects'])>0:
                if 'text' in response['objects'][0]:
                    #print("URL Content from {} is correct".format(url))
                    return response['objects'][0]['text']
                else:
                    #print("URL Content from {} NOT FOUND".format(url))
                    return "No Content"
            else:
                #print("URL Content from {} NOT FOUND".format(url))
                return "Empty URL, Nothing found"
        else:
            #print("URL Content from {} NOT FOUND".format(url))
            return "Empty URL, Nothing found"
    except:
        return "Something went wrong with url"


user_agent_list = [
   #Chrome
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',

    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]

#Function 
def get_content_news(url): 
      user_agent = random.choice(user_agent_list)
      config = Config()

      config.browser_user_agent = user_agent

      a  =  Article(url, config=config)
      time.sleep(1)  

      try:
           a.download()
           a.parse()
           paragraphs = a.text
           paragraphs = re.sub(r'<a href=.+?(?=)>|<br/>|\\xa0|\n|</a>|\xa0|<strong>|</strong>|<br/>•|<i(.*?)</i>|<img(.*?)>','',str(paragraphs))
           if type(paragraphs)==str and  len(paragraphs) >0:
                  print("URL Content from {} is correct".format(url))
                  return paragraphs
           elif paragraphs == '' or  type(paragraphs) == newspaper.article.ArticleException:
                 ext_diff= get_content_diffbot(url) 
                 print("URL Content from {} is correct from diffbot".format(url))

                 return ext_diff
      except Exception as exce:
            
             print("URL Content from {} is OtherError".format(url))
             try:
                 ext_diff= get_content_diffbot(url)
                 print("URL Content from {} is correct from diffbot".format(url))

                 return ext_diff
             except: 
                     print("URL Content from {} is OtherError".format(url))


start = time.time()
for index,row in preliminarData.iterrows():   
     
    if (row['Source'] == 'CIMS'):

        preliminarData.at[index, 'Mention Content'] =  get_content_news(row['Mention URL'])
        print(index)

    elif (row['Source'] == 'Synthesio'):
        
        content_syn =  get_content_news(row['Mention URL'])
        
    elif (row['Source'] == 'Subs'):
        content_syn = get_content_news(row['Mention URL'])

        if (content_syn =="No Content") or (content_syn =="Empty URL, Nothing found") or (content_syn =="Something went wrong with url"):
            
                    preliminarData.at[index, 'Mention Content'] = row['Mention Content']
        else:
                    preliminarData.at[index, 'Mention Content'] = content_syn
                    print(index)
end = time.time()
print(start-end)

# **-- CHECK POINT:**
'''
This section shows if the content extraction process
was successful or not for each reccord.
And if the content extraction process was successful,
it will be pushed to the next step.
Otherwise, incomplete data will be pushed for a different
crawling process.
'''