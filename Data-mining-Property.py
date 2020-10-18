#!/usr/bin/env python
# coding: utf-8

# In[158]:


import random
import pip
from bs4 import BeautifulSoup
import lxml
import html5lib
import requests
import re
import csv
import pandas as pd 
import time
import datetime
from datetime import date
import random
from geopy.geocoders import Nominatim
import os
from os.path import join as pjoin
from time import sleep
from random import randint
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import logging
import re
from contextlib import suppress
import sys


# In[2]:


# Nominatim
user_agent = 'user_me_{}'.format(randint(10000,99999))
geolocator = Nominatim(user_agent=user_agent)
sleep_sec = 2
def reverse_geocode(geolocator, adressen, sleep_sec):
    try:
        return geolocator.geocode(adressen)
    except GeocoderTimedOut:
        logging.info('TIMED OUT: GeocoderTimedOut: Retrying...')
        sleep(randint(1*100,sleep_sec*100)/100)
        return reverse_geocode(geolocator, adressen, sleep_sec)
    except GeocoderServiceError as e:
        logging.info('CONNECTION REFUSED: GeocoderServiceError encountered.')
        logging.error(e)
        return None
    except Exception as e:
        logging.info('ERROR: Terminating due to exception {}'.format(e))
        return None


# In[3]:


def combine2(Prisogm):
    if 4>len(Prisogm)>2:
        Pris2 =  Prisogm[1] + Prisogm[2]
        return Pris2
    if 5>len(Prisogm)>3:
        Pris2 =  Prisogm[1] + Prisogm[2] + Prisogm[3]
        return Pris2
    if 6>len(Prisogm)>4:
        Pris2 =  Prisogm[1] + Prisogm[2] + Prisogm[3] + Prisogm[4]
        return Pris2
    if 7>len(Prisogm)>5:
        Pris2 =  Prisogm[1] + Prisogm[2] + Prisogm[3] + Prisogm[4] + Prisogm[5]
        return Pris2


# ### By og Url lister

# In[103]:


Byer = ["Kristiansand","Arendal","Gjøvik","Hamar","Lillehammer"
        ,"Kristiandsund","Molde","Ålesund","Bodø","Oslo",
        "Haugesund","Karmøy","Sandnes","Stavanger","Harstad","Tromsø",
        "Trondheim", "Porsgrunn","Sandefjord","Skien","Tønsberg",
        "Bergen","Bærum","Drammen","Eidsvoll","Fredrikstad","Lillestrøm",
        "Kongsberg","Lørenskog","Nordre_Follo","Sarpsborg","Ullensaker"]


# In[ ]:


Urls = ["https://www.finn.no/realestate/homes/search.html?filters=&location=0.22042&location=1.22042.20179",
        "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22042&location=1.22042.20166",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22034&location=1.22034.20085",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22034&location=1.22034.20063",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22034&location=1.22034.20084",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20015&location=1.20015.20281",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20015&location=1.20015.20280",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20015&location=1.20015.20282",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20018&location=1.20018.20367",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20061",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20012&location=1.20012.20197",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20012&location=1.20012.20217",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20012&location=1.20012.20195",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20012&location=1.20012.20196"
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22054&location=1.22054.20412",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22054&location=1.22054.20413",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.20016&location=1.20016.20318",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22038&location=1.22038.20146",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22038&location=1.22038.20134",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22038&location=1.22038.20134",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22038&location=1.22038.20134",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22038&location=1.22038.20133",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22046&location=1.22046.20220",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20045",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20110",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20058",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20024",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.22105",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20111",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20052",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.22104",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20023",
       "https://www.finn.no/realestate/homes/search.html?filters=&location=0.22030&location=1.22030.20056"]
len(Urls)


# ### Lage folders

# In[104]:


path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Boligpriser/"
for by in Byer:
    try:
        os.mkdir(path+by)
    except OSError:
        continue


# ### Indeks byer

# In[134]:


for (i, item) in enumerate(Byer, start=0):
    print(i, item)
By = Byer[0]


# ### Kode

# In[161]:


for url in Urls:
    if url == Urls[0]:
        By = Byer[0] 
        end_page_num = 12
    if url == Urls[1]:
        By = Byer[1] 
        end_page_num = 10
    if url == Urls[2]:
        By = Byer[2] 
        end_page_num = 5        
    if url == Urls[3]:
        By = Byer[3] 
        end_page_num = 5        
    if url == Urls[4]:
        By = Byer[4] 
        end_page_num = 4        
    if url == Urls[5]:
        By = Byer[5] 
        end_page_num = 6               
    if url == Urls[6]:
        By = Byer[6] 
        end_page_num = 6        
    if url == Urls[7]:
        By = Byer[7] 
        end_page_num = 7
    if url == Urls[8]:
        By = Byer[8] 
        end_page_num = 60
    if url == Urls[8]:
        By = Byer[8] 
        end_page_num = 9        
    if url == Urls[9]:
        By = Byer[9] 
        end_page_num = 7        
    if url == Urls[10]:
        By = Byer[10] 
        end_page_num = 10        
    if url == Urls[11]:
        By = Byer[11] 
        end_page_num = 12        
    if url == Urls[12]:
        By = Byer[12] 
        end_page_num = 11        
    if url == Urls[13]:
        By = Byer[13] 
        end_page_num = 15        
    if url == Urls[14]:
        By = Byer[14] 
        end_page_num = 5
    if url == Urls[15]:
        By = Byer[15] 
        end_page_num = 10
    if url == Urls[16]:
        By = Byer[16] 
        end_page_num = 20        
    if url == Urls[17]:
        By = Byer[17] 
        end_page_num = 5        
    if url == Urls[18]:
        By = Byer[18] 
        end_page_num = 6        
    if url == Urls[19]:
        By = Byer[19] 
        end_page_num = 6        
    if url == Urls[20]:
        By = Byer[20] 
        end_page_num = 7        
    if url == Urls[21]:
        By = Byer[21] 
        end_page_num = 18        
    if url == Urls[22]:
        By = Byer[22] 
        end_page_num = 7        
    if url == Urls[23]:
        By = Byer[23] 
        end_page_num = 7        
    if url == Urls[24]:
        By = Byer[24] 
        end_page_num = 7        
    if url == Urls[25]:
        By = Byer[25] 
        end_page_num = 7        
    if url == Urls[26]:
        By = Byer[26] 
        end_page_num = 9        
    if url == Urls[27]:
        By1 = Byer[27] 
        end_page_num = 4      
    if url == Urls[28]:
        By2 = Byer[28] 
        end_page_num = 6        
    if url == Urls[29]:
        By = Byer[29] 
        end_page_num = 6 
    if url == Urls[30]:
        By = Byer[30] 
        end_page_num = 5
    if url == Urls[31]:
        By = Byer[31] 
        end_page_num = 7 
 

    filename_CSV = ("Boligpriser_i_{}".format(By)+"_total " + str(datetime.date.today())+".csv")

    path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Boligpriser/{}".format(By)

    csv_file1 = open(os.path.join(path, filename_CSV), 'w')
    csv_writer = csv.writer(csv_file1)
    csv_writer.writerow(["ID", 'Beskrivelse', 'Adressen', "Pris","Totalpris","Fellesutgifter",
                         "Antall_Soverom","m2","Eiertype","Tidspunkt hentet"])


    i = 1
    while i <= end_page_num:

        annonnser = requests.get(url+"&page={}".format(i))
        soup = BeautifulSoup(annonnser.text, "lxml")  
        time.sleep(random.uniform(3, 12))



        for ad in soup.find_all("article"):

            ids = [tag['id'] for tag in ad.select('a[id]')]
            ids = int(ids[0])

            beskrivelse = ad.find("a",class_="ads__unit__link").text

            Prisogm = ad.find("div",class_="ads__unit__content__keys").text.replace("m²","").replace("kr","").split()
            if len(Prisogm)>5:
                Pris = "Nybygg"
            elif Prisogm == []:
                continue
            elif len(Prisogm) == 2:
                Prisogm[1] == "Solgt"
                Pris = "Solgt"
            
            elif len(Prisogm) == 1:
                Pris = "Solgt"
            else: 
                Testing2 = combine2(Prisogm)
                try:    
                    Pris = int(Testing2)
                except ValueError:
                    Pris = 0


            ad = str(ad)

            totalpris_1 = re.search('Totalpris:(.*)kr', ad)
            if totalpris_1 == None:
                totalpris = 0
            else:
                totalpris_2 = str(totalpris_1.group(1))
                totalpris_3 = totalpris_2.split(" ")
                totalpris_4 = str(totalpris_3[1])
                totalpris  = int(re.sub(r"\D", "",totalpris_4))

            m2 = Prisogm[0]

            fellesutgifter = re.search('Fellesutg.:(.*)kr</', ad)
            if fellesutgifter == None:
                fellesutgifter_Int = 0
            else:
                fellesutgifter_Str = str(fellesutgifter.group(1))
                fellesutgifter_Int = int(re.sub(r"\D", "",fellesutgifter_Str))

            soverom_Search = re.search('<div class="ads__unit__content__list"(.*)soverom', ad)
            if soverom_Search == None:
                antallSoverom = 1
            else:
                Soverom = str(soverom_Search.group(1))
                Soverom1 = int(re.sub(r"\D", "",Soverom))
                listOfnumbers = [int(x) for x in str(Soverom1)]
                antallSoverom = listOfnumbers[-1]

            Adressen = re.search('ads__unit__content__details"><div>(.*)</div></div><div class="ads__unit__content__keys"><', ad)
            Adressen1 = str(Adressen.group(1))
            Adressen1 = str(''.join(Adressen1.split(",")[0:2]))
            
            eiertype_Selveier = re.search('Selveier', ad)
            eiertype_Andel = re.search('Andel', ad)
            eiertype_Aksje = re.search('Aksje', ad)

            if eiertype_Andel and eiertype_Selveier and eiertype_Aksje ==  None:
                Eiertype = "Ukjent"
            elif eiertype_Andel != None:
                Eiertype = str(eiertype_Andel.group())
            elif eiertype_Selveier != None:
                Eiertype = str(eiertype_Selveier.group())
            elif eiertype_Aksje != None:
                Eiertype = str(eiertype_Aksje.group())

            csv_writer.writerow([ids, beskrivelse, Adressen1, Pris, totalpris,
                                 fellesutgifter_Int, antallSoverom, m2, Eiertype, 
                                date.today()])

        i += 1
    csv_file1.close()

if url == Urls[7]:
    sys.exit()    


# # Bodø 

# In[15]:


By = "Oslo"


end_page_num = 4


filename_CSV = ("Boligpriser_i_{}".format(By)+"_total " + str(datetime.date.today())+".csv")

path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Boligpriser/{}".format(By)

csv_file1 = open(os.path.join(path, filename_CSV), 'w')
csv_writer = csv.writer(csv_file1)
csv_writer.writerow(["ID", 'Beskrivelse', 'Adressen', "Pris","Totalpris","Fellesutgifter",
                     "Antall_Soverom","m2","Eiertype","Tidspunkt hentet"])


# ([ids, beskrivelse, Adressen1, Pris, totalpris,
 #                            fellesutgifter_Int, antallSoverom, m2, Eiertype, selger_Str, 
#                            date.today()])
i = 3
while i <= end_page_num:
        
    annonnser = requests.get("https://www.finn.no/realestate/homes/search.html?filters=&location=0.20061&page={}".format(i))
    soup = BeautifulSoup(annonnser.text, "lxml")  
    time.sleep(random.uniform(3, 12))
    
    

    for ad in soup.find_all("article"):

        ids = [tag['id'] for tag in ad.select('a[id]')]
        ids = int(ids[0])
        
        beskrivelse = ad.find("a",class_="ads__unit__link").text

        Prisogm = ad.find("div",class_="ads__unit__content__keys").text.replace("m²","").replace("kr","").split()
        if len(Prisogm)>5:
            Pris = "Nybygg"
        elif Prisogm == []:
            continue
        elif Prisogm[1] == "Solgt":
            Pris = "Solgt"
        else: 
            Testing2 = combine2(Prisogm)
            Pris = int(Testing2)      
        
        ad = str(ad)

        totalpris_1 = re.search('Totalpris:(.*)kr', ad)
        if totalpris_1 == None:
            totalpris = 0
        else:
            totalpris_2 = str(totalpris_1.group(1))
            totalpris_3 = totalpris_2.split(" ")
            totalpris_4 = str(totalpris_3[1])
            totalpris  = int(re.sub(r"\D", "",totalpris_4))

        m2 = Prisogm[0]
        
        fellesutgifter = re.search('Fellesutg.:(.*)kr</', ad)
        if fellesutgifter == None:
            fellesutgifter_Int = 0
        else:
            fellesutgifter_Str = str(fellesutgifter.group(1))
            fellesutgifter_Int = int(re.sub(r"\D", "",fellesutgifter_Str))
            
        soverom_Search = re.search('<div class="ads__unit__content__list"(.*)soverom', ad)
        if soverom_Search == None:
            antallSoverom = 1
        else:
            Soverom = str(soverom_Search.group(1))
            Soverom1 = int(re.sub(r"\D", "",Soverom))
            listOfnumbers = [int(x) for x in str(Soverom1)]
            antallSoverom = listOfnumbers[-1]

        Adressen = re.search('ads__unit__content__details"><div>(.*)</div></div><div class="ads__unit__content__keys"><', ad)
        Adressen1 = str(Adressen.group(1))
        
        eiertype_Selveier = re.search('Selveier', ad)
        eiertype_Andel = re.search('Andel', ad)
        eiertype_Aksje = re.search('Aksje', ad)

        if eiertype_Andel and eiertype_Selveier and eiertype_Aksje ==  None:
            Eiertype = "Ukjent"
        elif eiertype_Andel != None:
            Eiertype = str(eiertype_Andel.group())
        elif eiertype_Selveier != None:
            Eiertype = str(eiertype_Selveier.group())
        elif eiertype_Aksje != None:
            Eiertype = str(eiertype_Aksje.group())
            
        csv_writer.writerow([ids, beskrivelse, Adressen1, Pris, totalpris,
                             fellesutgifter_Int, antallSoverom, m2, Eiertype, 
                            date.today()])

    i += 1
csv_file1.close()


# ## Del 2

# In[8]:


By = "Bodø"


end_page_num = 1


filename_CSV = ("Boligpriser_i_{}".format(By)+"_total " + str(datetime.date.today())+".csv")

path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Boligpriser /{}".format(By)

csv_file1 = open(os.path.join(path, filename_CSV), 'w')
csv_writer = csv.writer(csv_file1)
csv_writer.writerow(["ID", 'Beskrivelse', 'Adressen', "Selger","Boligtype","m2","Pris","Tidspunkt hentet"])

i = 1
while i <= end_page_num:
        
    annonnser = requests.get("https://www.finn.no/realestate/lettings/search.html?filters=&location=0.20018&location=1.20018.20367&page={}".format(i))
    soup = BeautifulSoup(annonnser.text, "lxml")  
    time.sleep(random.uniform(3, 12))
    
    

    for ad in soup.find_all("article"):

        ids = [tag['id'] for tag in ad.select('a[id]')]
        ids = int(ids[0])
        
        
        beskrivelse = ad.find("a",class_="ads__unit__link").text

        adressen1 = ad.find("div",class_="ads__unit__content__details").text.split(",")
        adressen = adressen1[0]+ " " + By 

        eierform1 = ad.find("div",class_="u-float-left").text
        eierform = re.split('(?=[A-Z])', eierform1)
        
        selger = eierform[1]

        boligtype = eierform[-1]

        Prisogm = ad.find("div",class_="ads__unit__content__keys").text.replace("m²","").replace("kr","").split()

        Testing2 = combine2(Prisogm)
                                
        m2 = Prisogm[0]

        csv_writer.writerow([ids, beskrivelse, adressen, selger, boligtype, m2, Testing2, date.today()])

    i += 1
csv_file1.close()

Yesterday = (date.today()-datetime.timedelta(days=1))

Yesterday_str = str((date.today()-datetime.timedelta(days=1)))

path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)
Master_liste1 = pd.read_csv(path + "/Master_{}".format(By) + "_liste_sist_oppdatert_{}".format(Yesterday_str) + ".csv")
#Master_liste = pd.read_csv(path + "/Master_{}".format(By) + "_liste_sist_oppdatert_{}".format("2020-07-19") + ".csv")



filename = ("Nye_Leieboliger_{}".format(By) + " " + str(datetime.date.today())+".csv")

path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)

# CSV fil som inneholder de nye boligene som er lagt ut
csv_file1 = open(os.path.join(path, filename), 'w')
csv_writer = csv.writer(csv_file1)
csv_writer.writerow(["ID", 'Beskrivelse', 'Adressen', "Selger","Boligtype","m2","Pris","Tidspunkt hentet","Latitude","Longitude"])

i = 1
while i <= end_page_num:
    
    annonnser = requests.get("https://www.finn.no/realestate/lettings/search.html?filters=&location=0.20018&location=1.20018.20367&page={}".format(i))
    soup = BeautifulSoup(annonnser.text, "lxml") 
    time.sleep(random.uniform(3, 12))
    
    

    for ad in soup.find_all("article"):

        ids = [tag['id'] for tag in ad.select('a[id]')]
        ids = int(ids[0])
        
        # Turning one ID into a list
        list_id =[ids]
        
        # Turning one ID into a set
        set_id = set(list_id)
        
        # Testing whether the ID from the finn.no page has been scraped before
        is_subset = set_id.issubset(Master_liste1.ID)

        if is_subset is True:
            continue 
        
        beskrivelse = ad.find("a",class_="ads__unit__link").text

        adressen1 = ad.find("div",class_="ads__unit__content__details").text.split(",")
        adressen = adressen1[0]+" {}".format(By)

        eierform1 = ad.find("div",class_="u-float-left").text
        eierform = re.split('(?=[A-Z])', eierform1)
        
        selger = eierform[1]

        boligtype = eierform[-1]

        Prisogm = ad.find("div",class_="ads__unit__content__keys").text.replace("m²","").replace("kr","").split()

        Testing2 = combine2(Prisogm)
                        
        location = reverse_geocode(geolocator, adressen, sleep_sec)
        
        if location is not None:
            latitude = (location.latitude)
            longitude = (location.longitude)
        else:
            longitude = 0
            latitude = 0

        m2 = Prisogm[0]

        csv_writer.writerow([ids, beskrivelse, adressen, selger, boligtype, m2, Testing2, date.today(),
                            latitude,longitude])

    i += 1
csv_file1.close()


### Appending the the new apartments to the old master list

path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)

new_rentals = pd.read_csv(path+"/Nye_Leieboliger_{}".format(By)+" {}".format(date.today()) + ".csv")



Master_liste_gammel = pd.read_csv(path + "/Master_{}".format(By) + "_liste_sist_oppdatert_{}".format(Yesterday_str)+".csv")

Master_liste2 = pd.concat([new_rentals, Master_liste_gammel])

Master_liste2.to_csv(path + "/Master_{}".format(By) + "_liste_sist_oppdatert_{}".format(Yesterday_str)+".csv",)

# renaming the file

os.rename(path + "/Master_{}".format(By) + "_liste_sist_oppdatert_{}".format(Yesterday_str)+".csv",
          path + "/Master_{}".format(By) + "_liste_sist_oppdatert_{}".format(date.today())+".csv")





# In[ ]:




