#!/usr/bin/env python
# coding: utf-8

# In[27]:


#/opt/miniconda3/bin/python3

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


# ### Nomatim
# 

# In[28]:



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


# In[29]:


def combine2(Prisogm):
    if len(Prisogm)>2:
        Pris2 =  Prisogm[1] + Prisogm[2]
        return Pris2


# In[30]:





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

def combine2(Prisogm):
    if len(Prisogm)>2:
        Pris2 =  Prisogm[1] + Prisogm[2]
        return Pris2


# In[ ]:





# ### By og Url lister

# In[113]:


Byer = ["Kristiansand","Arendal","Gjøvik","Hamar","Lillehammer"
        ,"Kristiandsund","Molde","Ålesund","Bodø","Oslo",
        "Haugesund","Karmøy","Sandnes","Stavanger","Harstad","Tromsø",
        "Trondheim", "Porsgrunn","Sandefjord","Skien","Tønsberg",
        "Bergen","Bærum","Drammen","Eidsvoll","Fredrikstad","Lillestrøm",
        "Kongsberg","Lørenskog","Nordre_Follo","Sarpsborg","Ullensaker"]


# In[129]:


Urls = ["https://www.finn.no/realestate/lettings/search.html?filters=&location=0.22042&location=1.22042.20179",
        "https://www.finn.no/realestate/lettings/search.html?filters=&location=0.22042&location=1.22042.20166",
       "https://www.finn.no/realestate/homes/lettings.html?filters=&location=0.22034&location=1.22034.20085",
       "https://www.finn.no/realestate/homes/lettings.html?filters=&location=0.22034&location=1.22034.20063",
       "https://www.finn.no/realestate/homes/lettings.html?filters=&location=0.22034&location=1.22034.20084",
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

# In[111]:


path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Boligpriser/"
for by in Byer:
    try:
        os.mkdir(path+by)
    except OSError:
        continue


# ### Indeks byer

# In[118]:


for (i, item) in enumerate(Byer, start=0):
    print(i, item)
By = Byer[0]


# In[107]:


Yesterday_str = str((date.today()-datetime.timedelta(days=1)))
Yesterday_str


# # Kode

# In[133]:


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

    filename_CSV = ("Leieboliger_{}".format(By)+"_total " + str(datetime.date.today())+".csv")

    path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)

    csv_file1 = open(os.path.join(path, filename_CSV), 'w')
    csv_writer = csv.writer(csv_file1)
    csv_writer.writerow(["ID", 'Beskrivelse', 'Adressen', "Selger","Boligtype","m2","Pris","Tidspunkt hentet"])

    
    i = 1
    while i <= end_page_num:

        annonnser = requests.get(url+"&page={}".format(i))
        soup = BeautifulSoup(annonnser.text, "lxml")  
        time.sleep(random.uniform(3, 12))



        for ad in soup.find_all("article"):

            ids = [tag['id'] for tag in ad.select('a[id]')]
            ids = int(ids[0])


            beskrivelse = ad.find("a",class_="ads__unit__link").text

            eierform1 = ad.find("div",class_="u-float-left").text
            eierform = re.split('(?=[A-Z])', eierform1)

            selger = eierform[1]

            boligtype = eierform[-1]

            Prisogm = ad.find("div",class_="ads__unit__content__keys").text.replace("m²","").replace("kr","").split()

            Testing2 = combine2(Prisogm)

            m2 = Prisogm[0]


            ad = str(ad)
            Adressen = re.search('ads__unit__content__details"><div>(.*)</div></div><div class="ads__unit__content__keys"><', ad)
            Adressen1 = str(Adressen.group(1))
            adressen = str(''.join(Adressen1.split(",")[0:2]))

            csv_writer.writerow([ids, beskrivelse, adressen, selger, boligtype, m2, Testing2, date.today()])

        i += 1
    csv_file1.close()





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

        annonnser = requests.get(url+"&page={}".format(i))
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

            ad = str(ad)
            Adressen = re.search('ads__unit__content__details"><div>(.*)</div></div><div class="ads__unit__content__keys"><', ad)
            Adressen1 = str(Adressen.group(1))
            adressen = str(''.join(Adressen1.split(",")[0:2]))

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


    ### Counting how many new apartment that has been added and saving the
    ### new rentals to the main summary df

    filename = "Nye leieobjekter per dag {}".format(By)+" - sist oppdatert " + str(datetime.date.today())+".csv"
    path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)


    csv_file1 = open(os.path.join(path, filename), 'w')
    csv_writer = csv.writer(csv_file1) 

    # Denne kan redigeres

    csv_writer.writerow(["Totalt_antall_annonser_ute","Dato", "Nye_utleiboliger_annonsert", "Snitt_Leiepris", "Snitt_m2", "Antall_bofelleskap", "Antall_leiligheter",
                        "Antall_parkeringer", "Antall_hybler", "Antall_rekkehus","Antall_privat"])

    antall_nye = len(new_rentals)

    # Fjerne alle bofelleskap som har oppgitt over 30m2 grunnet at det fører til
    # misvisende pris/m2
    uten_bofelleskap = new_rentals[~((new_rentals.Boligtype == "Rom i bofellesskap"))]
    bofelleskap = new_rentals[((new_rentals.Boligtype == "Rom i bofellesskap"))]
    bofelleskap_uten_høy_m2 = bofelleskap[~((pd.to_numeric(bofelleskap.m2) >= 30))]

    fjernet_høym2 = uten_bofelleskap.append(bofelleskap_uten_høy_m2)

    try:
        snitt_leiepris = sum(fjernet_høym2["Pris"].dropna()) // len(fjernet_høym2["Pris"].dropna())
    except:
        continue
    try:
        snitt_m2 = sum(fjernet_høym2["m2"].dropna()) // len(fjernet_høym2["Pris"].dropna())
    except:
        continue
    filename_CSV = ("/Leieboliger_{}".format(By)+"_total " + str(datetime.date.today())+".csv")
    path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)
    total_Liste_Boliger = pd.read_csv(path + filename_CSV)

    antall_AnnonserUte = len(total_Liste_Boliger)
    antall_bofelleskap = sum(new_rentals.Boligtype.str.count("Rom i bofellesskap"))
    antall_leiligheter = sum(new_rentals.Boligtype.str.count("Leilighet"))
    antall_parkeringer = sum(new_rentals.Boligtype.str.count("Parkering"))
    antall_hybler = sum(new_rentals.Boligtype.str.count("Hybel"))
    antall_Rekkehus = sum(new_rentals.Boligtype.str.count("Rekkehus"))
    antall_Privat = sum(new_rentals.Selger.str.count("Privat"))
    antall_Heimstaden = sum(new_rentals.Selger.str.count("Heimstaden"))
    antall_Utleiemegleren = sum(new_rentals.Selger.str.count("Utleiemegleren"))
    antall_Krogsveen = sum(new_rentals.Selger.str.count("Krogsveen"))
    antall_Merkantilbygg = sum(new_rentals.Selger.str.count("Merkantilbygg"))
    antall_Leiebolig = sum(new_rentals.Selger.str.count("Leiebolig"))
    antall_Persepolis = sum(new_rentals.Selger.str.count("Persepolis"))



    csv_writer.writerow([antall_AnnonserUte,date.today(), antall_nye, snitt_leiepris ,snitt_m2, antall_bofelleskap, antall_leiligheter,
                        antall_parkeringer, antall_hybler, antall_Rekkehus, antall_Privat])
    # "Oslo"  antall_Utleiemegleren, antall_Krogsveen, antall_Merkantilbygg, antall_Leiebolig
    csv_file1.close()


    ### Legge til date_rented

    filename_appended_today = "/Master_{}".format(By)+"_liste_sist_oppdatert_{}".format(date.today())+".csv"
    filename_uten_LongLat_dd = "/Leieboliger_{}".format(By)+"_total " + str(datetime.date.today())+".csv"


    appended_today = pd.read_csv((path + filename_appended_today),index_col=0)
    appended_today = appended_today.drop(["Unnamed: 0.1"], axis = 1)

    Nyeste_Komplett_liste_av_boliger = pd.read_csv((path + filename_uten_LongLat_dd))
    x = appended_today.ID.isin(Nyeste_Komplett_liste_av_boliger.ID)

    Date_rented_ny = []
    for false in x:
        if false==False:
            Date_rented_ny.append((date.today()))
        else:
            Date_rented_ny.append(None)


    appended_today["Date_rented_ny"] = Date_rented_ny

    pd.concat([appended_today['Date_rented_ny'], appended_today['Date_rented']], copy=True,join='inner')

    Rented = appended_today['Date_rented'].fillna(appended_today['Date_rented_ny'])
    appended_today = appended_today.drop(["Date_rented","Date_rented_ny"],axis=1)
    appended_today["Date_rented"] = Rented


    appended_today.reset_index(drop = True).to_csv(path + filename_appended_today)


    ### Legge til oppsummering av nye leieobjekter.





    Master_summary_new_apartments = pd.read_csv("/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)+"/Nye leieobjekter per dag {}".format(By)+" - sist oppdatert {}".format(Yesterday_str)+".csv",index_col = 0)
    New_summary_new_apartments = pd.read_csv("/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)+"/Nye leieobjekter per dag {}".format(By)+ " - sist oppdatert {}".format(date.today())+".csv")

    Master_summary_new_apartments = pd.concat([Master_summary_new_apartments, New_summary_new_apartments])

    Master_summary_new_apartments.reset_index(drop = True).to_csv("/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)+"/Nye leieobjekter per dag {}".format(By)+" - sist oppdatert {}".format(Yesterday_str)+".csv")


    # Renaming the file so that the date is correct
    filename_gammel = "/Nye leieobjekter per dag {}".format(By)+" - sist oppdatert {}".format(Yesterday_str)+".csv"
    filename_ny = "/Nye leieobjekter per dag {}".format(By)+" - sist oppdatert {}".format(date.today())+".csv"
    path = "/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)

    os.rename((path + filename_gammel),(path + filename_ny))
    # Delete total og nye boliger fra samme dag
    os.remove("/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)+"/Leieboliger_{}".format(By)+"_total " + str(datetime.date.today())+".csv")
    os.remove("/Users/Lars/Documents/Programmering/Test Finn.no webscraper/Eiendoms data /{}".format(By)+"/Nye_Leieboliger_{}".format(By) + " " + str(datetime.date.today())+".csv")

    if url == Urls[1]:
        sys.exit()  

