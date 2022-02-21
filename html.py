from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv


START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("/users/samik/c127/chromedriver")
browser.get(START_URL)
time.sleep(10)
header=["name","distance","mass","radius"]
planet_data=[]
new_planet_data=[]
        
    
def scrape():
         soup=BeautifulSoup(browser.page_source,"html.parser")
         for ul_tag in soup.find_all("ul",attrs={"class","stars"}):
             li_tags=ul_tag.find_all("li")
             templist=[]
             for index,li_tag in enumerate(li_tags):
                 if index==0:
                     templist.append(li_tag.find_all("a")[0].contents[0])
                     
                 else :
                     try:
                         templist.append(li_tag.contents[0])
                     except:
                         templist.append("")
             hyperlink_li_tag=li_tag[0]
             templist.append("https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars+hyperlink_li_tag.find_all"("a",href=True)[0]["href"])
            
             planet_data.append(templist)
         browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click() 
    
scrape()
for index,data in enumerate(planet_data):
  with open("now.csv", "w") as f: 
      csvwriter = csv.writer(f) 
      csvwriter.writerow(header) 
      csvwriter.writerows(planet_data) 
      
             

