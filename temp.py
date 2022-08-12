###### Funciones Web Scraping  #### 

#Diffbot 

#Credenciales
user =      'katia.bedolla@porternovelli.mx'
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

#Newspaper 
import newspaper      

"""NOTA: Si no esta instalada abrir Anaconda Prompt y correr lo siguiente: pip install newspaper3k"""
from newspaper import Article, fulltext, Config, ArticleException

#En el siguiente link consiguen su User Agent 

"https://developers.whatismybrowser.com/"  
#agregamos el User a la siguiente lista

user_agent_list = [
   #Chrome
     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',

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

import urllib.request,sys,time

#Function 
def get_content_news(url): 
      user_agent = random.choice(user_agent_list)
      config = Config()


     
      config.browser_user_agent = user_agent
      time.sleep(.05)  

      a  =  Article(url, config=config)

      try:
           a.download()
           a.parse()
           paragraphs = a.text
           paragraphs = re.sub(r'<a href=.+?(?=)>|<br/>|\\xa0|\n|</a>|\xa0|<strong>|</strong>|<br/>•|<i(.*?)</i>|<img(.*?)>','',str(paragraphs))
           if type(paragraphs)==str and  len(paragraphs) >0:
                  print("URL Content from {} is correct".format(url))
                  return paragraphs
         
           #elif type(paragraphs) == newspaper.article.ArticleException:
         
                  #print("URL Content from {} is ArticleException".format(url))
                  #return paragraphs
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


# -- Functions to be adapted to the project --
import time     
inicio = time.time()
for index, row in df_MS.iterrows():
    if row['Source'] == 'GN':
        continue
    elif row['Source'] == 'CIMS':
        # apply the function get_content_news to each row in the dataframe
        df_MS.loc[index, 'Mention Content'] = get_content_news(row['Mention URL'])
        print(index)
    elif df_MS['Source'] == 'Synthesio':
        # apply the function get_content_news to each row in the dataframe
        df_MS.loc[index, 'Mention Content'] = get_content_news(row['Mention URL'])
        print(index)
    elif df_MS['Source'] == 'Subs':
        df_MS.iloc[index, 'Mention Content'] = get_content_news(row['Mention URL'])
        print(index)
    else:
        pass
fin = time.time()
print("Terminó el proceso. El tiempo de ejecución fue de",fin-inicio)