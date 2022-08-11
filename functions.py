# Define TimeStamp Format
def get_timestampYMD():
    import datetime
    return datetime.datetime.today().strftime('%Y-%m-%d_%H-%M-%S')

# Upload Stopwords
def define_stopwords():
    sw_es=stopwords.words('spanish')
    sw_pt=stopwords.words('portuguese')
    sw_en=stopwords.words('english')
    sw_es_title=[word.title() for word in sw_es]
    sw_pt_title=[word.title() for word in sw_pt]
    sw_en_title=[word.title() for word in sw_en]
    return sw_es, sw_pt, sw_en, sw_es_title, sw_pt_title, sw_en_title

def get_mayusculas(texto):
    texto=str(texto)
    palabras_importantes=[]
    mayusculas=(r"([A-Z][a-zÁ-ÿ0-9]{1,20}\s?\,?\.?\s?)")
    texto=re.sub('[^\w\s]',' ',texto)
    texto=re.sub('[0-9]+', '', texto)  
    tokenizer=RegexpTokenizer(r'\w+')
    texto=tokenizer.tokenize(texto)
    texto=[word for word in texto if word not in sw_pt]
    texto=[word for word in texto if word not in sw_es]
    texto=[word for word in texto if word not in sw_en]
    texto=[word for word in texto if word not in sw_pt_title]
    texto=[word for word in texto if word not in sw_es_title]
    texto=[word for word in texto if word not in sw_en_title]
    tokens=[word.strip() for word in texto if word is not None]
    tokens=[word.strip() for word in tokens if len(word)>1]
    palabras_importantes=[word for word in tokens if word.istitle()]
    return palabras_importantes

# Adjust Country & Subs
def country_sub(country):
    if country =='Panama' or country =='PA' or country=='panama' or country=='Panamá':
        return ['Panama','Central']
    elif country =='Costa Rica' or country =='CR' or country=='costa rica' or country == 'Costa Rica ':
        return ['Costa Rica','Central', ]
    elif country =='Honduras' or country =='HN' or country=='honduras':
        return ['Honduras','Central']
    elif country =='Nicaragua' or country =='NI' or country=='nicaragua':
        return ['Nicaragua','Central']
    elif country =='Guatemala' or country =='GT' or country=='guatemala':   
        return ['Guatemala','Central']
    elif country =='El Salvador' or country =='SV' or country=='el salvador' or country=='All Central ' or country ==  'All Central ' or country== 'El Salvador ':
        return ['El Salvador','Central']
    elif country =='Venezuela' or country =='VE' or country=='venezuela':
        return ['Venezuela','Central']
    elif country =='Puerto Rico' or country =='PR' or country=='puerto rico':
        return ['Puerto Rico','Caribbean']
    elif country =='Dominican Republic' or country =='DO' or country=='dominican republic' or country=='republica dominicana' or country=='Rep. Dominicana':
        return ['Dominican Republic','Caribbean']
    elif country =='Trinidad & Tobago' or country =='TT' or country=='trinidad & tobago' or country=='Trinidad y Tobago' or country=='T&T' or  country == 'Trinidad and Tobago':
        return ['Trinidad & Tobago','Caribbean']
    elif country =='Jamaica' or country =='JM' or country=='jamaica':
        return ['Jamaica','Caribbean']
    elif country =='Peru' or country =='PE' or country=='peru' or country=='Perú':
        return ['Peru','South']
    elif country =='Ecuador' or country =='EC' or country=='ecuador' or country=='equador' or country=='EQUADOR':
        return ['Ecuador','South']
    elif country =='Bolivia' or country =='BO' or country=='bolivia':
        return ['Bolivia','South']
    elif country =='Paraguay' or country =='PY' or country=='paraguay' or country=='paraguai' or country=='Paraguai':
        return ['Paraguay','South']
    elif country =='Uruguay' or country =='UY' or country=='uruguay'or country=='uruguai' or country=='Uruguai':
        return ['Uruguay','South']
    elif country =='Mexico' or country =='MX' or country=='mexico' or country=='México' or country=='méxico':
        return ['Mexico','Mexico']
    elif country =='PanLatam' or country =='panlatam' or country =='Latinoamérica':
        return ['PanLatam','Panlatam']
    elif country =='PanCentral' or country =='pancentral':
        return ['PanCentral','Panlatam']
    elif country =='Argentina' or country =='AR' or country=='argentina':
        return ['Argentina','Argentina']
    elif country =='Brazil' or country =='BR' or country=='brazil' or country=='brasil' or country=='Brasil':
        return ['Brazil','Brazil']
    elif country =='Chile' or country =='CL' or country=='chile':
        return ['Chile','Chile']
    elif country =='Colombia' or country =='CL' or country=='colombia':
        return ['Colombia','Colombia']
    else:
        return ['Revisar','Revisar']

# Adjust Quarters & Months
def find_quarters(month):
    if month =='1': 
        return ['January','07','Q3','H2']
    elif month =='2': 
        return ['February','08','Q3','H2']
    elif month =='3': 
        return ['March','09','Q3','H2']
    elif month =='4': 
        return ['April','10','Q4','H2']
    elif month =='5': 
        return ['May','11','Q4','H2']
    elif month =='6': 
        return ['June','12','Q4','H2']
    elif month =='7': 
        return ['July','01','Q1','H2']
    elif month =='8': 
        return ['August','02','Q1','H2']
    elif month =='9': 
        return ['September','03','Q1','H2']
    elif month =='10': 
        return ['October','04','Q2','H2']
    elif month =='11': 
        return ['November','05','Q2','H2']
    elif month =='12': 
        return ['December','06','Q2','H2']

# Remove Punctuation Symbols
def remove_punct(texto):
    try:
        texto=texto.replace(".",' ').replace(";",' ').replace(":",' ').replace(",",' ')
        texto=texto.replace("(",' ').replace(")",' ').replace("|",' ').replace('"',' ')
        texto=texto.replace("%",' ').replace("$",' ').replace("/",' ').replace('\'',' ')
        texto=texto.replace("-",' ').replace("_",' ').replace("*",' ').replace('+',' ')
        texto=texto.replace("#",' ').replace("@",' ').replace("!",' ').replace('?',' ')
    except:
        pass
    return texto

# Clean Text After Preprocessing
def clean_text(texto):
    texto=texto.lower()
    texto=remove_punct(texto)
    return texto

# Tokenize Text
def tokenizar(texto):
    nuevo_texto = texto
    nuevo_texto = re.sub('http\S+', ' ', nuevo_texto)
    regex = '[\\!\\"\\#\\$\\%\\&\\\'\\(\\)\\*\\+\\,\\-\\.\\/\\:\\;\\<\\=\\>\\?\\@\\[\\\\\\]\\^_\\`\\{\\|\\}\\~]'
    nuevo_texto = re.sub(regex , ' ', nuevo_texto)
    nuevo_texto = re.sub("\d+", ' ', nuevo_texto)
    nuevo_texto = re.sub("\\s+", ' ', nuevo_texto)
    nuevo_texto = nuevo_texto.split(sep = ' ')
    nuevo_texto = [token for token in nuevo_texto if len(token) > 1]
    nuevo_texto=[word for word in nuevo_texto if word not in sw_total]
    return(nuevo_texto)

def crear_dicc_keywords(df_keywords):
    df_keywords=df_keywords.fillna('exxxtract')
    area_dict = df_keywords.to_dict('list')
    for k,v in area_dict.items():
        nv=list(set(v))
        nv=[x for x in v if x != 'exxxtract']
        nv=list(set(nv))
        area_dict[k]=nv
    return area_dict

def convert_to_words(list):
    new_list=[]
    for item,item2 in zip(list,category_list_found):
        if int(item)>0: 
            new_list.append(item2.replace('_FOUND',''))
    return new_list

def read_json(file_path):
    data={}
    with open(file_path,encoding="utf8") as json_file:
        arq = json.load(json_file)
    data['Notas']=arq
    return data

# Función para crear un DataFrame vacío con las columnas que vamos a necesitar
def crear_df_json(data):                                                                                  
    df_n=pd.DataFrame(columns=['IdNoticia', 'Fecha', 'Hora', 'TipoDeMedio', 'Medio', 'País', 'Sección','Título', 'Cuerpo', 'Tier',
                               'NroCaracteres', 'Tono', 'LinkImagen','CPE', 'Moneda', 'Audiencia', 'Tema', 'Empresa', 'NroPagina',
                               'Dimensión', 'CirculacionMedio', 'AutorConductor', 'ResumenAclaracion','LinkNota']) # Dataframe columnas en una lista
    for item in data['Notas']:                                                                            #1)Loop para leer cada una de las notas dentro de data2,
        dftemp=pd.DataFrame.from_dict(item,orient='index')                                                #2)Crear un DF para cada una de las notas 
        dftemp=dftemp.T                                                                                   #3)Hacer una transposición para organizarlas en filas
        df_n=df_n.append(dftemp)                                                                          #4)Agregar al DF vacio cada DF individual
    df_n=df_n.reset_index()                                                                               #5)Una vez ejecutado el loop, verificamos el DF con todas las notas.
    return df_n

# Encuentra una palabra dentro de un texto
def find_single_word_in_tokenized_text(row,keyword):
    if len([x for x in row if x ==keyword])>=1: 
        return [x for x in row if x ==keyword] 
    else:
        return ' ' 

#Función para categorizar una nota
def categoriza_nota(Brands,Priority_products,text):
    text=str(text)
    text=text.replace('[','').replace(']','')
    menciones=re.findall(Brands,text)
    if menciones:
        dicc_menciones={}
        dicc_menciones[list(set(menciones))[0]]=len(menciones)
    else:
        dicc_menciones={}
    productos_enc=[]
    for item in Priority_products:
        if item:
            p_enc=re.findall(item,text)
            productos_enc.append(p_enc)
        else:
            None
    dicc={}
    for item2 in productos_enc:
        if item2:
            dicc[list(set(item2))[0]]=len(item2)
        else:
            None
    flat_products = [x for sublist in productos_enc for x in sublist]
    cuenta=len(menciones)+len(flat_products)
    if cuenta>=3:
        cat_nota='Prominent'
    elif cuenta>1 and cuenta<3:
        cat_nota='Relevant'
    elif cuenta==1:
        cat_nota='Passive'
    else:
        cat_nota='Non_related'
    return dicc_menciones,dicc,cat_nota

# Mas de 3 menciones de producto+marca = Prominent
# 1<mención de Marca + Producto<3 = Relevant
# 1=Pasive
# 0=Null

import urllib.request
import random

def define_user_agent_list():
    user_agent_list = [
       #Chrome
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
    return user_agent_list

def get_full_content(url):
    for i in range(1,6):
        user_agent = random.choice(user_agent_list)
        headers = {'User-Agent': user_agent}

        if url:
            try:
                #req = Request(url, headers=headers) 
                req = urllib.request.Request(url,headers={'User-Agent': user_agent})
                response = urllib.request.urlopen(req)
                html = response.read()

                #html = urlopen(req).read() 
                soup = BeautifulSoup(html)
                paragraphs=re.findall(r'<p>(.*?)</p>',str(soup))
                paragraphs=re.sub(r'<a href=.+?(?=)>|</a>|\xa0|<strong>|</strong>|<i(.*?)</i>|<img(.*?)>','',str(paragraphs))
                paragraphs2=''.join(paragraphs)
                paragraphs2=paragraphs2.replace('\n','').replace('\t','').replace('\r','')
            except:
                paragraphs2='Sin Informacion'
                print('ups')

    return(paragraphs2)

def clean_and_tokenize(texto):
    texto=str(texto).lower()
    texto=re.sub('[^\w\s]',' ',texto)
    tokenizer=RegexpTokenizer(r'\w+')
    texto=tokenizer.tokenize(texto)
    texto=[word for word in texto if word not in sw_pt]
    texto=[word for word in texto if word not in sw_es]
    texto=[word for word in texto if word not in swsp]
    tokens=[word.strip() for word in texto if word is not None]
    tokens=[word.strip() for word in tokens if len(word)>1]
    return tokens

def find_most_common(texto,filtradas,qty):
    tokens=clean_and_tokenize(texto)
    tokens2=[word for word in tokens if word not in filtradas]
    bigrm = list(nltk.bigrams(tokens2))
    found=collections.Counter(bigrm)
    tops=found.most_common(qty)
    mf=[]
    for i in range(0,len(tops)):
        terms=tops[i][0]
        freq=tops[i][1]
        most_frequent=(terms,freq)
        mf.append(most_frequent)
    return mf

def MC_WORDS(df,filtro_company,qty):
    filtradas=[]
    df['Contents_MC']=df['Contents'].apply(lambda row : str(row).replace('http://','').replace('https://','').replace('www',''))
    for filtro in filtro_company:
        df['Contents_MC']=df['Contents'].apply(lambda row : str(row).replace(filtro,''))
    lista02=df['Contents'].tolist()
    mc03=find_most_common(lista02,filtradas,qty)
    return mc03

def MC_WORDS2(df,filtro_company,qty):
    filtradas=[]
    df['Full Text_MC']=df['Full Text'].apply(lambda row : str(row).replace('http://','').replace('https://','').replace('www',''))
    for filtro in swsp:
        df['Full Text_MC']=df['Full Text'].apply(lambda row : str(row).replace(filtro,''))
    lista02=df['Full Text_MC'].tolist()
    mc03=find_most_common(lista02,filtradas,qty)
    return mc03

def define_swsp():
    swsp=['de','la','que','el','en','y','a','los','del','se','las','por','un','para','con','no',
          'una','su','al','lo','como','más','pero','sus','le','ya','o','este','sí','porque','esta',
          'entre','cuando','muy','sin','sobre','también','me','hasta','hay','donde','quien','desde',
          'todo','nos','durante','todos','uno','les','ni','contra','otros','ese','eso','ante','ellos',
          'e','esto','mí','antes','algunos','qué','unos','yo','otro','otras','otra','él','tanto','esa',
          'estos','mucho','quienes','nada','muchos','cual','poco','ella','estar','estas','algunas','algo',
          'nosotros','mi','mis','tú','te','ti','tu','tus','ellas','nosotras','vosostros','vosostras','os',
          'mío','mía','míos','mías','tuyo','tuya','tuyos','tuyas','suyo','suya','suyos','suyas','nuestro',
          'nuestra','nuestros','nuestras','vuestro','vuestra','vuestros','vuestras','esos','esas','estoy',
          'estás','está','estamos','estáis','están','esté','estés','estemos','estéis','estén','estaré',
          'estarás','estará','estaremos','estaréis','estarán','estaría','estarías','estaríamos','estaríais',
          'estarían','estaba','estabas','estábamos','estabais','estaban','estuve','estuviste','estuvo',
          'estuvimos','estuvisteis','estuvieron','estuviera','estuvieras','estuviéramos','estuvierais',
          'estuvieran','estuviese','estuvieses','estuviésemos','estuvieseis','estuviesen','estando','estado',
          'estada','estados','estadas','estad','he','has','ha','hemos','habéis','han','haya','hayas',
          'hayamos','hayáis','hayan','habré','habrás','habrá','habremos','habréis','habrán','habría',
          'habrías','habríamos','habríais','habrían','había','habías','habíamos','habíais','habían','hube',
          'hubiste','hubo','hubimos','hubisteis','hubieron','hubiera','hubieras','hubiéramos','hubierais',
          'hubieran','hubiese','hubieses','hubiésemos','hubieseis','hubiesen','habiendo','habido','habida',
          'habidos','habidas','soy','eres','es','somos','sois','son','sea','seas','seamos','seáis','sean',
          'seré','serás','será','seremos','seréis','serán','sería','serías','seríamos','seríais','serían',
          'era','eras','éramos','erais','eran','fui','fuiste','fue','fuimos','fuisteis','fueron','fuera',
          'fueras','fuéramos','fuerais','fueran','fuese','fueses','fuésemos','fueseis','fuesen','sintiendo',
          'sentido','sentida','sentidos','sentidas','siente','sentid','tengo','tienes','tiene','tenemos',
          'tenéis','tienen','tenga','tengas','tengamos','tengáis','tengan','tendré','tendrás','tendrá',
          'tendremos','tendréis','tendrán','tendría','tendrías','tendríamos','tendríais','tendrían','tenía',
          'tenías','teníamos','teníais','tenían','tuve','tuviste','tuvo','tuvimos','tuvisteis','tuvieron',
          'tuviera','tuvieras','tuviéramos','tuvierais','tuvieran','tuviese','tuvieses','tuviésemos',
          'tuvieseis','tuviesen','teniendo','tenido','tenida','tenidos','tenidas','tened','https','co','mucha','rt','poner','br',
          'interlocutor','interlocutora', 'INTERLOCUTORA','INTERLOCUTOR']
    return swsp

def remove_swsp(texto):                    
    tokens = [t for t in texto.split()]
    clean_tokens = tokens[:]
    for token in tokens:
        if token in swsp:
            clean_tokens.remove(token)
    return clean_tokens

#Divide un texto en eneagramas
def clean_text_wt(texto):
    clean_tokens=clean_and_tokenize(texto)
    texto = ' '.join(clean_tokens)
    return texto

#Divide un texto en eneagramas
def divide_en_ngramas(texto,n):
    if len(texto)>0:
        n_grams=[]
        enegramas = ngrams(texto.split(), n)
        for grams in enegramas:
            i=0
            division=''
            while i<n: 
                division=division+' '+grams[i]
                i+=1
            n_grams.append(division.lstrip())
    else:
        return ''
    return n_grams

def detect_ngram_in_text(texto,keyword):
    tam_keyword=len(keyword.split(' '))
    if tam_keyword==1:

        texto_fuente=clean_and_tokenize(texto)
        if keyword in texto_fuente:
            return 1
        else: 
            return 0
    else:
        texto_fuente=divide_en_ngramas(texto,tam_keyword)
        if keyword in texto_fuente:
            return 1
        else: 
            return 0
        
def detect_ngram_in_text2(texto,keyword):
    tam_keyword=len(keyword.split(' '))
    if tam_keyword==1:

        texto_fuente=clean_and_tokenize(texto)
        if keyword in texto_fuente:
            return 1
        else: 
            return 0
    else:
        texto_fuente=divide_en_ngramas(texto,tam_keyword)
        if keyword in texto_fuente:
            return 1
        else: 
            return 0

def encuentra_matches(row,keyword):
    row=str(row)
    matched=process.extract(keyword,row.split(' '))
    best_options=[]
    for item in matched:
        if item[1]>=91:
            best_options.append(item[0])
    return best_options

def find_keyword_in_clean_text(row,keyword):
    patterns= [keyword]  
    for p in patterns:
        match= re.findall(p, row)
    return match

def define_words_to_verify():
    words_to_verify=['Microsoft','Office 365', 'Bing', 'Cortana', 'Dynamics', 'Azure Cosmos', 'O365',  'Microsoft Cognitive',  'Internet Explorer',  'Minecraft',
                     'Windows Server','Github','GitHub','Scarlett','Power BI', 'Edge', 'OneNote',  'PowerPoint',  'Windows',  'Power Point', 
                     'Office', 'Cortana Intelligence Suite', 'Power Apps', 'LinkedIn', 'Age of Empires','ID@Xbox','SharePoint', 'Xbox Project Scarlett', 'Xbox One','Xbox Scarlett',
                     'Surface Pro', 'Surface', 'Azure', 'OneDrive', 'Outlook', 'SQL Server', 'Xbox One','Microsoft Flight Simulator', 'Halo', 'Word',
                     'Paint',  'Excel',  'Xbox',  'One Drive',  'Azure Al',  'HoloLens',  'Microsoft Bot Framework',  'Teams', 'TEAMS','Windows Defender',
                     'Skype', 'Skype for Business','Apple','iPad','Mac','OSX','Siri','iPhone','iMac','HomePod',
                     'ARKit','MacOS','Macbook','watchOS','Airpods','FaceTime','tvOS','SwiftUI', 'Amazon','Amazon Web Services',
                     'AWS','AWS Educate','Echo','Alexa','Amazon Athena','Amazon Connect', 'AWS QuickSight', 'Sagemaker','Echo',
                     'Chime', 'Slack', 'Facebook','Workplace','Facebook Messenger','WhatsApp','Rooms','Oculus','fb.gg','Facebook Gaming',
                     'Google', 'Android','Google Assistant','Google Home','Google Cloud','GSuite','G Suite','Gsuite','G suite',
                     'Gmail','Chromebook','Jamboard','Pixel', 'Google Classroom','Hangouts','Google VR','Google Daydream','Google Drive','Google Glass',
                     'Stadia','Google BigQuery','Google BigTable', 'Google Cloud Spanner','Google Data Studio','Google Meet','Google Workspace', 'IBM',
                     'Watson','Watson for Oncology','IBM Cloud', 'Cognitiva', 'Red Hat', 'BlueMix', 'ZOOM','Zoom','Windows 11','Salesforce','Tableau']
    return words_to_verify


def define_words_sov_focused():
    sov_focused=['Microsoft','Office 365','Cortana', 'Dynamics', 'Azure Cosmos', 'O365',  'Microsoft Cognitive',  'Internet Explorer',  'Minecraft',
                     'Windows Server','Github','GitHub','Scarlett','Power BI', 'Edge', 'OneNote',  'PowerPoint',  'Windows',  'Power Point', 
                     'Office', 'Cortana Intelligence Suite', 'Power Apps', 'LinkedIn', 'Age of Empires','ID@Xbox','SharePoint', 'Xbox Project Scarlett', 'Xbox One','Xbox Scarlett',
                     'Surface Pro', 'Surface', 'Azure', 'OneDrive', 'Outlook', 'SQL Server', 'Xbox One','Microsoft Flight Simulator', 'Halo', 'Word',
                     'Paint',  'Excel',  'Xbox',  'One Drive',  'Azure Al',  'HoloLens',  'Microsoft Bot Framework',  'Teams', 'TEAMS','Windows Defender',
                     'Skype', 'Skype for Business','Apple','Mac','OSX','Siri','iMac','HomePod',
                     'ARKit','MacOS','Macbook','FaceTime','tvOS','SwiftUI', 'Amazon','Amazon Web Services',
                     'AWS','AWS Educate','Echo','Alexa','Amazon Athena','Amazon Connect', 'AWS QuickSight', 'Sagemaker','Echo', 'Athena',
                     'Chime', 'Slack', 'Facebook','Workplace','Facebook Messenger', 'Rooms','Oculus','fb.gg','Facebook Gaming',
                     'Google','Google Assistant','Google Home','Google Cloud','GSuite','G Suite','Gsuite','G suite',
                     'Gmail','Chromebook','Jamboard','Google Classroom','Hangouts','Google VR','Google Daydream','Google Drive','Google Glass',
                     'Stadia','Google BigQuery','Google BigTable', 'Google Cloud Spanner','Google Data Studio','Google Meet','Google Workspace', 'IBM',
                     'Watson','Watson for Oncology','IBM Cloud', 'Cognitiva', 'Red Hat', 'BlueMix', 'ZOOM','Zoom','zoom','Windows 11','Salesforce','Tableau']
    return sov_focused

def define_customer_name():
    customer_name=['NBA',"Zscaler","Zipy","Zinobe","Zenvia","Zenta Group","Yumbel de Las Condes","YPF","Yapp","Xandr","Wyleex","Woza Labs","Workday","Woolworths Australia","Womint","Womcy",
                   "Woman in Entrepreneurship","WoMakersCode","WOM","WizdomCRM","Wise","Win.gt","Wiga","WhatShed","Webee","Walgreens","VU Security","VPNet","Voxall","Volvo","Volkswagen","Vmware",
                   "Vicunha Têxtil","Via Varejo","Veeam Backup","Veeam","Vaticano","Vale Fund","UTEC","USTA","USA Department of Defense","US Army","Uroff","UPS","UPRRP","UPR","U-planner","UP","UOL",
                   "Univisión","Univisio","University of Puerto Rico","University College Cork","University Action Pro Education and Culture","Universidade do Algarve",
                   "Universidad Tecnológica del Salvador","Universidad Tecnológica de El Salvador","Universidad Tecnologica de El Salvador","Universidad Tecnológica",
                   "Universidad Privada San Francisco de Asís","Universidad Politécnica Salesiana sede Guayaquil","Universidad ORT","Universidad Nacional Autónoma de México","Universidad Minuto de Dios",
                   "Universidad Latina","Universidad La Salle Bolivia","Universidad La Salle","Universidad Javeriana","Universidad Internacional de las Américas","Universidad Insurgentes",
                   "Universidad Industrial de Santander","Universidad Hispanoamericana","Universidad Franz Tamayo","Universidad Fidélitas","Universidad Federal de Paraíba",
                   "Universidad Externado de Colombia","Universidad El Bosque","Universidad del País Vasco","Universidad del Pacífico","Universidad de Puerto Rico en Río Piedras",
                   "Universidad de Puerto Rico","Universidad de Panama","Universidad de Chile","Universidad Continental","Universidad Central","Universidad Católica","Universidad Catolica",
                   "Universidad Castro Carazo","Universidad Boliviana de Informática","Universidad Autónoma del Estado de México","Universidad Autónoma del","Universidad Autónoma de Tamaulipas",
                   "Universidad Autónoma de Sinaloea","Universidad Autónoma de San Luis Potosí","Universidad Autónoma de Nuevo León","Universidad Autonoma de Bucaramangara","Universidad Autónoma de",
                   "Universidad Andrés Bello","Universidad Anahuac Puebla","Universidad Adolfo Ibáñez","Univalle Santa Cruz","United Capital","UNIMINUTO","Unilever","Unifranz","Unifin","Uniclick",
                   "Unicef","Uniara- Universidade de Araraquara","UNAM","UNAB","Ulalá","UISA","UIN","UIA","UFPB","UDEM","UCL","UC","UAT","UASLP","UAS","UANL","Ualá","UAEM","Tuya Smart","TUX","TSMC",
                   "TSE","Trust for the Americas","Tribunal Supremo Electoral","Tribunal de Justiça do Estado de São Paulo","Tribunal de Justiça de São Paulo","Tribunal de Justiça",
                   "Tribunal de Contas de Rondônia","TP Digital","Toyota","Totto y Lili Pink","Totto","Total","Toastmaster","TJSP","TIVIT","Tirando x Colombia","TiMi","TIM","Tigo Business",
                   "Tiendanube","ThoughtWorks","TheAbleGamers","Thales","Texas Tech University Costa Rica","Texas Tech University","Tesorería General de la República","Teradata","Tempest","Temasek",
                   "Televisa","Teleperformance","Telefónica Tech","Telefônica","Telefónica","Telefonica","Telecom","Telecaribe","Telecable","Tecnología de la Información y Comunicación de ORT Argentina.",
                   "Tecnalia","Tech Data","Tec de Monterrey","Teatro El Parque","TCS","Talento Digital Los Creadores","Synnex Westcon-Comstor","Synnex Westcon Comstor","Swiss Medical Group",
                   "Swiss Medical","Suzano","Suramericana","Supremo Tribunal Federal","Suprema Corte de Justicia","Superintendencia Nacional de los Registros Públicos – SUNARP",
                   "Superintendencia de Notariado y Registro","SUNEDU","Submergence Group.","Submarine Telecoms Forum","Subcomisión de Acusaciones Constitucionales","STJ","Starbucks",
                   "Standard Chartered","Spotify","Speck","SpaceX","SoulCode Academy","SOU.cloud","SOS Mata Atlântica","Sompo","Solo Network","Solinftec","Solea","SoftwareONE","Softline","SNS","SNP",
                   "Snap Finance","Sloan","Sistema Nacional de Emprego","Sistema Nacional de Empleo","Sistema de Atención Médica de Emergencias","Sistema de Atención Médica de Emergencia","SINE",
                   "Simpletech","Simens","Sierra Col","Siemens","Shopify","Shifta","SGD","SG Financial Technology y TUX","SG Financial Technology and TUX","SG Financial Technology",
                   "Servicio Nacional de Salud","Servicio Nacional de Correos","Servicio Nacional de Capacitación y Empleo","Servicio Nacional de Aprendizaje","Servicio de Administración Tributaria",
                   "Serpro","SEP","Sensormatic Solutions América Latina","Sener","Sence","Senac","SENA","Seguros SURA","Seduc","Sedesu","Secretarías de Desarrollo Económico",
                   "Secretaria Estadual de Educação de Parana","Secretaria Estadual de Educação","Secretaría del Desarrollo Sustentable","Secretaría de Transparencia","Secretaría de Innovación",
                   "Secretaria de Governo Digital","Secretaría de Educación de Bogotá","Secretaría de Educación","Secretaría de Bienestar","Sebrae Nacional y M8 Partners","Sebrae Nacional","Sebrae",
                   "SEAQ","SCOTIABANK","Schneider-Neureither & Partner","Schlumberger","SAT","SAS","Sapore","SAP","São Luiz Hospital","Santo Tomas de Aquino University","Santher","Santander",
                   "SandBox.","Sandbox","San Bartolomé La Merced","Samsung Smarthings","Samsung Electronics","Samsung","Samsonite","SAME","Salidas Inclusivas","Salesforse","Salesforce","Sabin",
                   "S4Go","S.Coop","Ruta N","RTVC","Roomie","Rock Solid Technologies","Rimac","Right To Play","Renault","Reliance","RedSalud","Rede D’Or","Red pública estatal de Rio Grande do Sul",
                   "Red Hat","Red Cultural del Mercosur","Rebanking","Ray-ban","Rappi","Qualcomm","Qlik","QCI y Toshiba","Q10","pyladies Medellín","Pure Storage","Pure Cloud Block Store","Pulse","PUCRS",
                   "Prosegur","ProMare","Prodesp","Prisma","Presidio","Presidencia de la República y el Ministerio de Ciencia y Tecnología","Preparatoria Venustiano Carranza",
                   "Prefeitura do Rio de Janeiro","Porto Seguro","PoolPo","Pontifícia Universidade Católica do Rio Grande do Sul","Pontificia Universidad Javeriana de Colombia","Poder Judicial","PLD",
                   "Platzi","Plan Ceibal","Pizza Hut","Pioneros","Pioneras","Pinterest","Philips","Pfizer","Petz","Petrobras","Pepsico","Pentágono","Pentagono","Pentagon","PC Arts","PBSF",
                   "Paula Souza center and Minha Chance program","Pattern Cinco","Partido de la Liberación Dominicana","Partido Conservador","PAO","Pandora",
                   "Panamanian Chamber of Commerce, Industries and Agriculture","Palantir Technologies","Palantir","Pacto del Bicentenario","OXIO","Overwatch League","OSDE",
                   "Organizações de Gerenciamento de Destino","Organización Mundial del Turismo","Organização Mundial do Turismo","Organização Internacional do Trabalho","Orange","Oracle","ONPE",
                   "OnePlus","OMT","Omnilogic","OLX","OIT","Oi Soluções","Oi Cloud","Ogtic","Oficina Nacional de Procesos Electorales","Oficina Descentralizada de Procesos Electorales","Office Depot",
                   "OEA","Odecma","Nutanix","Nubity","Novartis","Notaries of Colombia","Notarías Digitales","Nokia","Noble Corral","Niantic","NFL","Nexxt Solutions","Nexsys","News Corp",
                   "Neural Creations de Perú","Neural Creations","Netskope","NetSecurity","Netflix","Neogrid","NEO Consulting","Neiker-Instituto Vasco de Investigación y Desarrollo Agrario","Neiker",
                   "Neat","NBA","Navantia","Nationwide","National Learning Service","National Domestic Workers Alliance","Natiboo","NASA","Narda Lepes","Naranja X","N5","Musgrave","Museu de Arte Moderna",
                   "Museo del Palacio","Museo del Noreste","Museo de Historia Mexicana","Municipio de San Juan","Municipio de Providencia","Municipalidad de Lima","Munich Re",
                   "Multisensory Reading Centers","Mudafy","MTPE","MSP","MSCI Inc.","MPRJ","Movistar","Motorola","Morgan Stanley","Molifer","Mofiler","Moderna","Modern Talent Hub","Mobbyt","MOB Telecom",
                   "MKDA","Mitsubishi","MIT","Misión Tic","Mintic","Minsait","Ministry of information and communication technologies","Ministry of Industry, Commerce and SMBs","Ministry of Education",
                   "Ministério Público do Rio de Janeiro","Ministerio Público de la provincia de Buenos Aires","Ministerio deTecnologías de la Información y las Comunicaciones",
                   "Ministerio de Trabajo y Promoción del Empleo","Ministerio de Tecnologías de la Información y las Comunicaciones de Colombia",
                   "Ministerio de Tecnologías de la Información y las Comunicaciones","Ministerio de Salud Pública","Ministerio de Salud Chile","Ministerio de la Juventud",
                   "Ministerio de Industria Comercio y MiPymes","Ministerio de Hacienda","Ministerio de Educación Pública","Ministerio de Educación de Panamá","Ministerio de Educación de Ecuador",
                   "Ministerio de Educación","Ministerio de Educacion","Ministerio de Economía y Finanzas","Ministerio de Economía","Ministerio de Desarrollo Productivo","Ministerio de Comercio",
                   "Ministério da Educação","Ministério da Economia","Minerd","MINEDUCYT","Minedu","MINED","Minasul","Microsoft Colombia","Microland","MICM","MICITT","Mi Tierrita","Mexico","Met Office",
                   "Merk","Meriti","Mercedes-Benz","Mercadolibre","Mercado Libre","Mercado de Alimentos","MEP","Memed and Acsa Cardoso","Memed","MELI","MEF","Meduca","Medl","Medifé",
                   "Medicos sin Fronteras","Méderi","MEC","MCSC","Mavenir","Masters de Golfe","Mastercard","Marsh","Manzanillo port","Mandic Cloud Solutions","MAM Educativo","MAM","Makaia","Mainsoft",
                   "Magnamed","Magento","Mães da Sé","Macquarie University","M8 Partners","Lumen Technologies","Lumen","Louis Vuitton","Lopito","Lopez y Asociados","Loja Integrada","Logicalis",
                   "Liverpool","Listin Diario","Linux Foundation","Lincoln","Lili Pink","LIH","Liga Nacional de Básquet","Liga Nacional de Basquet","Liga Nacional de Baloncesto",
                   "Liceo Panamericano Centenario","Leonardo Amagada","Lenovo DCG","Lenovo","Lazarillo","Laboratorios Ballerina","Laboratorio ELSA","Laboratorio de Gobierno","Laboratoria",
                   "Laboratioria","LAB Escénico","La Nación","La Liga","L´Oréal","Kuppo","KrugerCorp","Kredito","Kovi","Konecta","Kölbi","Kindite","KIA","Khipu","Karten Space","Kaizen",
                   "Kaiser Permanente","Kairos App","Jurado Nacional de Elecciones","Junta Reglamentadora de Servicio Público","Junta de Supervisión Fiscal","Junior Achievement Americas.",
                   "Junior Achievement","JRSP","JP Morgan Chase","Joint Development Foundation Projects LLC.","JNE","Jeep","JEDI","JCE","Jabra PanaCast","Jabra","IWG","ITSE","Itaú","ITA","ISFODOSU",
                   "IPN","IPHE","IonQ","Invillia","International Finance Corporation","Intermaco","InterAmerican Academy","Inter","Intel","Intcomex","INTA","Instituto Técnico Superior Especializado",
                   "Instituto Tecnico Ricaldone","Instituto Superior de Formacion Docente Salome Ureña","Instituto Politécnico Nacional","Instituto Nacional de Salud","Instituto Nacional de México",
                   "Instituto Nacional de Empleo y Formación Profesional","Instituto Interamericano de Cooperación para la Agricultura","Instituto Francés de Chile","Instituto de Tecnologia e Sociedade",
                   "Instituto de la Juventud","Instituto de Capacitación para el Trabajo de Campeche","Instituto Colombiano para la Evaluación de la Educación","InRad","InovaHC","inovabra habitat",
                   "iNNpulsa Colombia","Innovacien","Ingram Micro Cloud","Ingram Micro","Ingram","Ingeniosas: Ciencia y Tecnología para Todas","Infosys","Infobip","Inefop","Indra","Inc","INACAP","INA",
                   "Imazon","Ileana & Howie","Ikerlan","IICA","iFood","IFC","IData","Icfes","ICE","ICATCAM","Ibermática","Hugo","HSBC","HP","Hospital Network Einstein","Hospital Jaraguá do Sul",
                   "Hospital Jaragua","Hospital Ángeles Metropolitano","Hospital Angeles Metropolitano","Hospital Albert Einstein","Honeywell","Holcim","Hitachi Vantara","Hitachi","Hilab",
                   "Hewlett Packard Enterprise","Hermes Germany GmbH","Herdez","Heifer International","HCFMUSP","HBO","Hazi Fundazioa","Hart InterCivic","HackU","Gympass","Grupo Siesa",
                   "Grupo Nacional Provincial","Grupo Lafise","Grupo Fleury","Grupo Financiero Agromercantil","Grupo Éxito","Grupo Equatorial","Grupo Don Mario","Grupo Bolívar Davivienda","Grupo BMG",
                   "Grupo Bimbo","Grupo Banco Mundial","Grupo Aval","Grupo Atlas de Seguridad Integral","Grupo Açotubo","GRAMMY","Governo do Rio Grande do Sul","Governo de São Paulo","Governo de Goias",
                   "Gorriz","Goldman Sachs Group Inc.","Goldman Sachs","Gobierno Nueva York","Gobierno Digital","Gobierno de São Paulo","Gobierno de New York","Gobierno de Mexico","Gobierno de Italia",
                   "Gobierno de Guatemala","Gobierno de Estados Unidos","Gobierno de El Salvador","Gobierno de Colombia","Gobierno de Chile","Gobierno de Canada","Gobierno de Brasil","GM","Globo",
                   "Globe Italia","Globant","Globalweb","Global.health","Global Sports Innovation Center","Global Health","GK Software","GiveDirectly","GitHub","GGL","German School",
                   "Gerencia de Regulación y Estudios Económicos","General Motors","Geely","GE Technical Institute","GDM","GBM","Garlan","Gamers Club","G&J Pepsi-Cola Bottlers",
                   "Fundo das Nações Unidas para a Infância","Fundo Baobá","Fundación Raspberry Pi","Fundación País Digital","Fundación Luker","Fundación Luke","Fundación Linux","Fundación Lavazza",
                   "Fundación Kodea","Fundación Gabo","Fundación Eidos","Fundación de Computación Nativa en la Nube","Fundación Data Observatory","Fundación CineStell","Fundación Alcaraván",
                   "Fundação Vale","Fundação de Rotarianos de São Paulo","Fundação de Amparo à Pesquisa do Estado do Rio de Janeiro","Fujistu","Fuerza del Pueblo","Freshwater Advisors","Fracción","FPD",
                   "Fosis","Fortnite","Fortinet","Foro de Periodismo Argentino","Fórmula 1","Ford","Fopea","Fondo Biotech de Israel","FLG SA","FLG","Flex","Flecha roja","Flamengo","Fit Market",
                   "Fiscalía General","FIEG","Fiat Los Granaderos","Fiat Chrysler","Fiat","Fedofútbol","FedEx","Federación Nacional de Cafeteros","FCA","Farmacias Batres","Fapesp","FAPERJ",
                   "Facultad de Medicina de la Pontificia Universidad Javeriana de Colombia","Facultad de Ingenieria y Ciencias de la Univeridad Adolfo Ibáñez","Faculdade FAEL",
                   "Faculdade Educacional da Lapa","F1","Eye Capital","EY Chile","EY","Extreme Digital Solutions","Expedia","Evertec","Evernorth","Everis","Eurotux","EUROCYBCAR","Etsy","estatales","ESO",
                   "Escuelas de Iniciación Deportiva del Instituto Municipal del Deporte","Escuela Normal Profesor Manuel José Almada de Chascomús","Escuela Nacional de la Judicatura del Poder Judicial",
                   "Escuela Nacional de la Judicatura","Escuela de Trabajo Social de la Universidad Colegio Mayor de Cundimarca","Escuela de Ingeniería Informática","Escuela de Bellas Artes",
                   "Escuela Comunicación UASD","Equinix","Equatorial group","Entel","ENSA Servicios","ENG","EnergyCloud","Energy Cloud","Endeavor","Enacom",
                   "Empresa Brasileira de Pesquisa e Inovação Industrial","Emprendedor y Semilla","Emprende Tu Mente","Embratel","Embrapii","Elev8","ElectrifAi",
                   "El Instituto Panameño de Habilitación Especial","El Instituto de Radiología","El Fondo de Solidaridad e Inversión Social","El Colegio San José","El Banco Popular Dominicano",
                   "Ejército de Estados Unidos","Einstein Healthcare Network","EIDOS Global","Eidos","EducationUSA Costa Rica del Centro Cultural Costarricense Norteamericano","EDS","Edrans",
                   "EDP Universíty","Ecopetrol","Eco-Kindergarten Mi Tierrita","Eatfit University","Dynatrace","Dronak","Drixit Technologies","Drixit","Domilogística","DOE","DO","DMOs","Dlocal",
                   "Distrito de Colombia","Disney+","Disney","Dish Network Corporation","Dish","Dirección de Educación","Digital Innovation One","Digicel Bussines","Digicel Business",
                   "DICK’S Sporting Goods","Deutsche Bank","Department of Education","Department of Agriculture","Departamento Meteorológico del Reino Unido","Departamento de Salud.",
                   "Departamento de Prosperidad Social","Departamento de Energía de los Estados Unidos","Departamento de Educación","Departamento de Capacitación de la Dirección Nacional de Tecnología y Recursos del Instituto Panameño de Habilitación Especial",
                   "Delta Airlines","Delta Air Lines","Delta","Dell","Dedalus","DE","Data Science Fem","Data Observatory","Darktrace","Daimler","Daabon","Customer Name Q4","Cupeyville School","CSN",
                   "CSJJ","CSIRO","CSI- RO","Cruz Roja Americana","Cruise","Critertec","Credijusto","Crea","CPIC","CPC","Covalent","Coursera","Cosmo Consult","Corte Suprema de Justicia","Corte Suprema",
                   "Corte Superior Nacional de Justicia Penal Especializada","Corte Superior de Justicia de Junín","Corte Superior de Justicia","Corporación Financiera Internacional","Corinthians",
                   "Coppel","Copersucar","COPARMEX","Copa Airlines","COP26","Cooperativa Minasul","Control de la Magistratura","Contraloría General de la republica","CONTPAQi","Contempora Seguros",
                   "Consultiva Wealth Management","Consorcio de Clima y Sostenibilidad del MIT","Conservation International y Goldman Sachs","Conselho Nacional de Justiça","Consejo Mexicano de Negocios",
                   "Consejo Departamental de Justicia","Consejo de Promoción de la Competitividad","Consejo Coordinador Empresarial y Credijusto","Consejo Coordinador del Modelo de Gestión Penitenciaria",
                   "Connect Bogotá","Confederación de Empleadores de la República Mexicana","Conalep","CONACERD","Compliance PME","Compensar","Compasso UOL","Commvault",
                   "Comisión Presidencial de Gobierno Abierto y Electrónico","Comisión Permanente","Comisión para el Mercado Financiero","Comisión Especial Investigadora Multipartidaria","COMIPEMS",
                   "Columbia Sportswear","Colombina","Colombian Chamber of Electronic Commerce","Colnodo","Colegios Mayor","Colegio St. Clare´s","Colegio Pioneros","Colegio Markham",
                   "Colégio Marista Centro-Norte","Colegio Jacarandá","Colegio de Profesionales en Informática y Computación","Colegio de Economistas de Bolivia",
                   "Colegio de Contadores Bachilleres y Públicos del Guayas","Colegio Antártica Chilena","Coinbase","Cofopri","Codelco","Coca-Cola Beverages Africa","Cobuilder","CNJ","Cmind","CMF",
                   "Clúster Bogotá de Software y TI","Clúster Bogotá de Software","Clinica Mayo","Clínica Foianini de Santa Cruz de la Sierra","Clínica Foianini","Clínica Ángel Foianini",
                   "Clínica Alemana","ClearSale","Claro","Claranet","Ciudad del Saber","Citrix","Citibanamex","Cisco Meraki","Cisco","Circuito de Agrupaciones de Carnaval","Circo de Norte de Santander",
                   "Cinepolis","Cinemateca de Bogotá","CINDE","Cigna's","Cigna","Cielo","Chipotle","Chedraui","Cetaqua","CES","Certsys","Cerner","Centro Paula Souza",
                   "Centro para la Cuarta Revolución Industrial","Centro Digital San Faustino","Centro Cultural Manuelcha Prado","Centro Australiano de Egiptologia da Macquarie University",
                   "Centro ¡Supérate!","Central Board of Secondary Education","Central American Bottling Company","Center for Journalists an National Association of Hispanic Journalists","Cenfotec",
                   "CENAPEC","CEmprende","Celonis","Celeritech","CECC","CCIAP","CCCE","CCBA","CBSE","CBRE","CBC","Casio","CasaTIC","Casa Blanca","Carrefour","Carlsberg","Carao Ventures y CINDE",
                   "Carao Ventures","CAPRO","Capgemini","Canonical","Canal Regional Telecaribe","Camisea","Cámara de Empresas Chinas en Chile","Cámara de Empresas Chinas",
                   "Cámara de Comercio Industrias y Agricultura de Panamá","Cámara de Comercio de Tobago","Cámara de Comercio de Bogotá","Câmara de Comercialização de Energia Elétrica",
                   "Cámara de Centros de Formación Profesional de El Salvador","Cámara de Centros de Formación Profesional","Caja de Salud","C&W Business","Business IT","Business Data Evolution",
                   "Bupa Chile","Bupa","Bundesliga","BUAP","BTG Pactual","BS2 Bank","BRLink","Británico","Brasoftware y Odebrecht","Brasoftware","Braskem","Bradesco","BR Distribuidora","BP",
                   "Bose","Bolivia","BMW","Blizzard","Biomedical","Bimbo","BID Lab","BID","Biblioteca Nacional del Perú","BeyondCorp","Best Buy","Benemérita Universidad Autónoma de Puebla",
                   "Bel-Ray Chile","BCAM","BBVA","Baufest","Basque Center for Applied Mathematics","Bartlett School of Architecture","Barceloneta","Bantrab","Banpara","Banorte","Bancolombia",
                   "Bancoldex","Banco Sabadell","Banco Popular","Banco Nacional","Banco Itaú","Banco Interamericano de Desarrollo","Banco Hipotecario","Banco Galicia","Banco de Chile","Banco de Bogotá",
                   "Banco Comafi","Banco Central","Banco BBVA","Baires Rocks","Axway","AX4B","AVEVA","Avaya","AVANET","AUPPA","Attach","Atlanticonnect","Atento","AT&T",
                   "Associação Brasileira de Psiquiatria","Assmca","Asociación Nacional de Periodistas Hispanos","Asociación Mexicana de Secretarios de Desarrollo Económico",
                   "Asociación de Universidades Particulares de Panamá","Asociación Argentina de Capital Privado","Aseinfo","ASCAP","Asamblea legislativa","ASAFintech","Aruba","Artrocentro","Argi",
                   "Argencon","Arezzo&Co","Arezzo","Area3","Arcos Dorados","Arcor","ARCAP","Arc Publishing","APM Terminals","ANTV","ANIDA","Andino School","AMSDE","American Airlines","AMD","AmCham",
                   "AMC Theatres","Amadeus","Altice","Alo Partners","Allianz Global Corporate & Specialty","Allianz","Alliance To End Plastic Waste","Algramo","Algebia","Algar Tech","Alestra",
                   "Aleph CRM","AlChavo.com","Alcaldía de Medellín","Albert Einstein","AirPak","Air Computers","AIG","Agrotools","Agrosul","Agrolly","Agrodanieli","Aginco",
                   "Agência Mural de Jornalismo das Periferias","Agencia de Investigación Australiana","AGCS","Agasus","Aethra","ADT","Adobe","Administración de Servicios de Salud Mental y Contra la Adicción",
                   "Adidas","Adaptive Biotechnologies","Acura","Action Industrial Innovación","Acsa Cardoso","Accor","Accenture Plc","Accenture","Academia San Ignacio de Loyola","Academia Menonita",
                   "Abraço Cultural","ABP","Ablegamers","ABB","A3","1Qbit","EMBRAPII"]
    return customer_name

def define_cities_people():
    cities_people=[]

# A)	Identificar a través del Script si existe mención de las marcas o sus productos en el título.
def wtv_in_title(row, wtv):
    encontradas=[]
    for item in wtv:
        if item in row:
            encontradas.append(item)
        else:
            continue
    if len(encontradas)>0:
        return 'Yes'
    else:
        return 'No'

def verify_related_overall(row1,row2):
    if row1=='Yes' and row2=='Yes':
        return 'Yes ->Title & Contents'
    elif row1=='Yes' and row2=='Revisar':
        return 'Yes ->Revisar Contents'
    elif row1=='Yes' and row2=='No':
        return 'Yes -> Title pero no en Contents'
    elif row1=='No' and row2=='Yes':
        return 'Yes -> solo Contents'
    elif row1=='No' and row2=='Revisar':
        return 'No -> revisar Contents'
    elif row1=='No' and row2=='No':
        return 'No relacionada'
    else:
        return 'Combinación inválida'

def verify_is_related(row1):
    if row1=='Yes ->Title & Contents':
        return 'Yes'
    elif row1=='Yes ->Revisar Contents':
        return 'Review'
    elif row1=='Yes -> Title pero no en Contents':
        return 'Yes'
    elif row1=='Yes -> solo Contents':
        return 'Yes'
    elif row1=='No -> revisar Contents':
        return 'Review'
    elif row1=='No relacionada':
        return 'No'
    else:
        return 'Combinación inválida'

###### COMPANY SENTIMENT
#array(['Non_related', 'Passive', 'Relevant', 'Prominent'], dtype=object)
def company_sentiment(row1):
    if row1=='Non_related':
        return 'NA'
    elif row1=='Passive':
        return 'Neutral'
    elif row1=='Relevant':
        return 'Positive'
    elif row1=='Prominent':
        return 'Positive'
    else:
        return 'Combinación inválida'
    
#### LOCAL/GLOBAL
#if len(row)>0 then 'Local' else 'Global'
def verify_local_global(row1):
    if len(row1)>0:
        return 'Local'
    elif len(row1)==0:
        return 'Global'
    else:
        return 'Combinación inválida'
    
#### BUSINESS IN CONTENT
def verify_business_in_content(row1,row2):
    business_a_revisar=['Android' 'Pixel', 'Prime Video', 'iPhone', 'iOS',
                        'Airpods','Bing', 'Netflix', 'Iphone', 'Instragram',
                        'Metaverso', 'metaverso','Whatsapp', 'whatsapp','Gates', 'Bill', 
                        'Spotify','Spotify','bill' ,'Zuckerberg']
    encontradas=[]
    revisar=[]
    for business in business_a_revisar:
        if business in row1 or business in row2:
            encontradas.append(business)
        else:
            continue
    if len(encontradas)>0 :
        #print('Nota con wtv y content a revisar ')
        return 'NDB'
    elif len(encontradas)==0:
        #print('Nota con wtv dentro de content')
        return 'DB'
    else:
        #print('Wtv no encontrada dentro del contenido')
        return 'Combinación inválida'

#Verify SOV
def verify_sov(row1,wtv):
     wnr  = define_wnr()
     fwlen_t = len(set(wtv).intersection(row1))
     mwlen_t = len(wnr.intersection(row1))
     if  mwlen_t == 0  and  fwlen_t > 0:
          return "Yes"
     elif  mwlen_t > 0  and  fwlen_t == 0:
          return "No"     
     elif mwlen_t > 0 and mwlen_t <=3 and  fwlen_t >3:
          return "Yes"
     else:
          return  "No"

#Verify Focus          
def verify_sov_focus(row1,wtv):
     wnr  = define_wnr()
     wnr  = list(wnr) + ['Instagram','Facebook', 'WhatsApp', 'Netflix', 'Prime' ]
     fwlen_t = len(set(wtv).intersection(row1))
     mwlen_t = len(set(wnr).intersection(row1))
     if  mwlen_t == 0  and  fwlen_t > 0:
          return "Yes"
     elif  mwlen_t > 0  and  fwlen_t == 0:
          return "No"     
     elif mwlen_t > 0  and  fwlen_t > 3:
          return "Yes"
     else:
          return  "No"

def verify_customer_name(row1,row2,customer_name):
    encontradas=[]
    for item in customer_name:
        if item in row1 or item in row2:
            encontradas.append(item)
        else:
            continue
    if len(encontradas)>0 :
        #print('Nota con wtv y content a revisar ')
        return 'Yes'
    else:
        #print('Wtv no encontrada dentro del contenido')
        return 'No'



#### NEW FUNCTIONS ####
def define_wnr():
    wnr = set(['AMLO','Andrés Manuel López Obrador','Andres Manuel Lopez Obrador',
               'Andres Manuel','Lopez Obrador','mañanera','Andrés Manuel','López Obrador', 'López',
               'PRESIDENTE ANDRÉS MANUEL LÓPEZ OBRADOR', 'manuel','obrador', "Obrador" ,
               'Scarlett' , 'Johansson', 'Scarlett Johansson'  "Anaya", "Monreal", "Chris" , 
               "Evans", "Chris Evans", "Noroña", "PAN", "MORENA", "PRI", "Acción", "Movimiento",
               "Ciudadano",  "MC", "PRD"  , "Peña Nieto", "Peña", "dictadura", "Ortega",'Alfaro',
               'Lozoya', 'Dune', 'vacuna', 'Buzz','Aburto', 'Colosio','Guevara',
               "Daniel Ortega", "votaciones" ,"Maya", "Gortari", "polarización", "Fox",  "VOX", 
               "Felipe Calderón", "Calderón",'calderón', 'Adele','Calamar','Salma Hayek', 'Hayek', 
               'François', 'Pinault', 'Pinal', 'cine' ,'Cine' ,'oro','Oro' 'Macron', 'Merkel', 'podcast',
                'Buffet', 'PODCAST','podcast','Podcast', 'Gatell', 'Ebrard', 'Nerea', 'Ocaña', 'Trevi','FGR', 'INE', 'Yuya',
                'Chumel', 'AIFA','CFE', 'Pemex', 'Coparmex', 'UIF', 'Pablo', 'Gómez','Bukele', 'Canelo',
                'Peniley', 'Krauze', 'sicario', 'Oxxo', 'DiCaprio', 'Natti', 'BioNTech', 'política', 'Cómics' , 'Wonder',
                'Clouthier', 'Nacif', 'Shabazz', 'Tatiana', 'Inegi', 'INEGI', 'déficit', 'balanza', 'eléctrica',
                'homicidio', 'violación', 'sexual', 'Viajar', 'película', 'cintas', 'Estatal', 'Federal' ,
                'muerte', 'murío', 'muere', 'fallecidos','muertos', 'criminales','prisiones','Sinaloa','Zacatecas', 
                'Ómicron','OMS','vacunas','Janssen', 'Sputnik' , 'Phizer', 'Astra' , 'ESCUCHA', 'OCDE', 'carbón', 'Checo',
                'Verstapen', 'Hamilton', 'Deezer', 'FIL', 'Zócalo', 'Cuba' , 'Noticias', 'Evo', 'Vladimir', 'Putin', 'guerra', 'Guerra',
                'Zelensky', 'War', 'war'])
    return  wnr

#Function that compares words not related  vs related
def func_wnr(words):
    mwlen = len(wnr.intersection(words))
    fwlen = len(key_words.intersection(words))
    if mwlen > 0 and fwlen == 0:
        return "not"
    elif mwlen == 0 and fwlen > 0:
        return "yes"
    elif mwlen > 0 and fwlen <=3:
        return "prob_not"
    elif mwlen > 0 and fwlen >3:
        return "prob_yes"
    else: 
        return "prob_not"
#Funciones categorización titled and content related

def func_wnr_prob_yes(words):
     wnr  = define_wnr()
     fwlen = len(key_words_foc.intersection(words))
     mwlen = len(wnr.intersection(words))
     if  mwlen == 0 and   fwlen > 0:
          return "Yes"
     elif  mwlen > 0 and mwlen <=3 and  fwlen >3 :
          return  "Yes"
     else:
          return  "No"

def func_wnr_prob_no(words):
     wnr  = define_wnr()
     fwlen = len(key_words_foc.intersection(words))
     mwlen = len(wnr.intersection(words))
     if  mwlen == 0 and   fwlen > 0:
          return "Yes"
     elif  mwlen > 0 and mwlen <=3 and  fwlen >3:
          return "Yes"
     else:
          return  "No"


def wtv_in_content(words):
    wnr  = define_wnr()
    fwlen = len(key_words_foc.intersection(words))
    mwlen = len(wnr.intersection(words))
    if  mwlen == 0 and  fwlen > 0:
        return "Yes"
    elif  mwlen > 0 and  fwlen == 0:
        return "No"
    elif  mwlen > 0 and  fwlen > 0 and fwlen <=3 :
        return  "No"
    elif  mwlen > 0 and  fwlen >4:
        return  "Revisar"
    else:
        return  "No"


""" SOV"""
def verify_sov(row1,wtv):
    wnr  = define_wnr()
    fwlen_t = len(set(wtv).intersection(row1))
    mwlen_t = len(wnr.intersection(row1))
    if  mwlen_t == 0  and  fwlen_t > 0:
        return "Yes"
    elif  mwlen_t > 0  and  fwlen_t == 0:
        return "No"     
    elif mwlen_t > 0 and mwlen_t <=3  and  fwlen_t >3:
        return "Yes"
    else:
        return  "No"

""" Verify SOV Focus      """    
def verify_sov_focus(row1,wtv):
     wnr  = define_wnr()
     #Agregamos 
     wnr  = list(wnr) + ['Instagram','Facebook', 'WhatsApp', 'Netflix', 'Prime' ]
     fwlen_t = len(set(wtv).intersection(row1))
    
     mwlen_t = len(set(wnr).intersection(row1))


     if  mwlen_t == 0  and  fwlen_t > 0:
          return "Yes"
     elif  mwlen_t > 0  and  fwlen_t == 0:
          return "No"     
     elif mwlen_t > 0  and  fwlen_t > 3:
          return "Yes"
     else:
          return  "No"
