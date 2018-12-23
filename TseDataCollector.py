# -*- coding: utf-8 -*-
import requests as req
import re
import pandas as pd
import numpy as np
#getting data from their feeds extracting them  then storing 
#some usefull data
#DataLinks
Geram24='http://www.tgju.org/chart-summary-ajax/geram24'
Seke='http://www.tgju.org/chart-summary-ajax/sekeb'
Dollar='http://www.tgju.org/chart-summary-ajax/price_dollar_rl'
ShakhesKol='http://www.tsetmc.com/tsev2/chart/data/Index.aspx?i=43685683301327984&t=value'
#history="http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i=%s&TOP=999999&A=1"%name
dideban="http://www.tsetmc.com/tsev2/data/MarketWatchPlus.aspx"
Sectors="http://cdn.tsetmc.com/tsev2/res/loader.aspx?t=g&_438"
IdxPage="http://www.tsetmc.com/Loader.aspx?Partree=151315&Flow=1"
myData=0
def GetLink(link):
    resp=req.get(link)
    return resp.text

def SaveToFile(name,data):
    f=open(name,'a',encoding='utf8')
    f.write(data)
    f.close()
    
#def ExtractDaily(name,day):
    
def ExtractDideban():
    resp=GetLink(dideban)
    #separate each line make that comma separated put col1 and 19 to a table
    #work with csv
    # data=re.findall('@(.*?)@',resp)
    # data=data[1]
    # m=data.split(';')
    data=resp.split('@')
    data=data[2].split(';')
    #arr=np.array(data[2])
    myArr=[]
    for x in data:
        myArr.append(x.split(','))
    
    #data=re.sub(';','\n',data[1])
    df = pd.DataFrame(myArr,columns=['Page','Id','AbrName','CompName','1','2','3','4','5','6','7','8','9','10','11','12','13','14','Cat','15','16','17','18'])
    df.to_csv('DidehBanData.csv', encoding='utf-8')
    

def ExtractTradeHist(page,id):
    Hist= "http://members.tsetmc.com/tsev2/data/InstTradeHistory.aspx?i=%s&TOP=999999&A=1"%page
    data=GetLink(Hist)
    data=re.sub(';','\n',data)
    data=re.sub('@',',',data)
    SaveToFile('TradHist%s.csv'%id,data)

def ExtractIndex():
    data=GetLink(ShakhesKol)
    index=data.split(';')
    myArr=[]
    for x in index:
        myArr.append(x.split(','))

def DataCollectorRun():


def DataCollectorCheckLastUpdate():
#read text file with name update.txt
#
def DataCollectorUpdate():
#get current date 
#get last data date 
#calculate number of query 

def GetSymbols():
    ExtractDideban() 
    DidehBan = pd.read_csv('DidehBanData.csv')
    pd.DataFrame(DidehBan,columns=['page','Id','Cat'])
    #open DidehbanData  
    #finding col numbers

ExtractDideban()