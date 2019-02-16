# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 22:18:05 2019

@author: Pranav
"""
__author__ = "Pranav Sahasrabudhe"
__maintainer__ = "Pranav Sahasrabudhe"
__email__ = "ssb.pranav@outlook.com"
__status__ = "Prototype"
#Imports
import urllib.request,urllib.parse,urllib.error,urllib.response
from bs4 import BeautifulSoup
import xlsxwriter

# Create a workbook and add a worksheet.
import re
try:
    
    
    workbook = xlsxwriter.Workbook('D:\Scraped_data.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0,'Date')
    worksheet.write(0, 1,'URL')
    worksheet.write(0, 2,'MD5')
    worksheet.write(0, 3,'IP')
    worksheet.write(0, 4,'Tools')
            
    
except:
    print('Can\'t create an excel file')
def scrapeData(url):
    try:
        fh=urllib.request.urlopen(url).read()
        soup=BeautifulSoup(fh,'html.parser')
    except urllib.error.URLError:
        print('Invaid URL')
    #########################Date
        row=0
        tags=soup('a')
        
        for tag in tags:
            if re.findall('>([0-9][0-9]-[0-9][0-9])<',str(tag)):
                dates=""
                
                date_start=re.findall('>([0-9][0-9]-[0-9][0-9])<',str(tag))
                
                for i in date_start:
                    for j in i:
                        dates+=''.join(j)
                
                worksheet.write(row+1, 0, str(dates))
                row += 1    
                
        
    
                
    ######URLmd5_tags=soup('a')
        row=0    
        
        for tag in tags:
            if re.findall('>.+\.pdf<',str(tag)) :
                url=""            
                urls=re.findall('>(.+\.pdf)<',str(tag))
                for i in urls:
                    for j in i:
                        url+=''.join(j)
                
                worksheet.write(row+1, 1, str(url))   
                row += 1
                
            elif re.findall('>.+\.exe<',str(tag)): 
                url=""
                urls=re.findall('>(.+\.exe)<',str(tag))
                for i in urls:
                    for j in i:
                        url+=''.join(j)
                
                worksheet.write(row+1, 1, str(url))   
                row += 1
                
            elif re.findall('>.+\.yad<',str(tag)) :
                urls=re.findall('>(.+\.yad)<',str(tag))
                url=""
                for i in urls:
                    for j in i:
                        url+=''.join(j)
                
                worksheet.write(row+1, 1, str(url))   
                row += 1
                
            
            elif re.findall('>.+\.jpg<',str(tag)) :
                url=""
                urls=re.findall('>(.+\.jpg)<',str(tag))
                for i in urls:
                    for j in i:
                        url+=''.join(j)
                
                worksheet.write(row+1, 1, str(url))   
                row += 1
                
                
                    
       
    #####MD5    
        row=0
        for tag in tags:
            if 'MD5=' in tag.get('href'):
                md5=""
                md5_start=re.findall('=([a-zA-Z0-9].+)',tag.get('href'))
                for i in md5_start:
                    for j in i:
                        md5+=''.join(j)
                worksheet.write(row+1, 2, str(md5))
                    
                row += 1
                
        
    ##########IP
        row=0
        for tag in tags:
            if 'IP=' in tag.get('href'):
                ip=""
                
                ip_start=re.findall('=(.+)',tag.get('href'))
                for i in ip_start:
                    for j in i:
                        ip+=''.join(j)
                
                
                worksheet.write(row+1, 3, str(ip))
                row += 1
                
    ###########Tools
        row=0
        for tag in range(len(tags)): 
                tool='PEP UQ'
                worksheet.write(row+1, 4, tool)                
                row += 1
        workbook.close()
    
            
    
    finally:
        print('Data Sucessfully scrapped in excel')
url='http://vxvault.net/ViriList.php'
if __name__=="__main__":
    scrapeData(url)