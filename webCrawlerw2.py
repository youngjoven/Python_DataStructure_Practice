import requests, pandas, glob2
from bs4 import BeautifulSoup
from datetime import datetime

def mainSetting():
    while True:
        print("***********************")
        print("**1. NewsWebCrawling **")
        print("**2. Merge the files **")
        print("**3. exit            **")
        print("***********************")
        option=input("Choose one ")

        if  option == "1":
            date=input("Enter news date: ")
            pageCount=input("Enter page count : ")
            crawling(date, pageCount)
        elif option == "2":
            checkFileName("all")
        elif option == "3":
            return -1
        else:
            print("Error command")

def crawling (date,pageCount):
    now=datetime.now()
    list=[]
    for i in range(1,int(pageCount)):
        requestHelp= requests.get("http://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1=100&date=" + str(date) + "page=")
        contentsHelp= requestHelp.content
        soup=BeautifulSoup(contentsHelp, "html.parser")
        #print(soup)
        allFindul = soup.find("ul",{"class":"type06_headline"})
        allFindli = allFindul.find_all("li")
        for item in allFindli:
            d={}
            try:
                title=item.find("dt",{"class":""}).find("a")
                links=item.find("dt",{"class":""}).find("a")['href']
                d["title"]=title
                d["links"]=links
            except:
                d["title"]="None"
                d["links"]="None"
            try:
                img=item.find("dt",{"class":"photo"}).find("img")['src']
                d["imgSrc"]=img
            except:
                d["imgSrc"]="None"
            list.append(d)
    df=pandas.DataFrame(list)
    df.to_csv('%s-%s-%s-%s-%s-%s.csv' % (now.year, now.month, now.day, now.hour, now.minute, now.second))

def checkFileName(fileName):
    now=datetime.now()
    if len(glob2.glob("*.csv"))==0:
        print("No file found in this directories")
        return -1
    else:
        if fileName =="all":
            result=[]
            for i in glob2.glob("*.csv"):
                result.append(pandas.read_csv(i))
            outputFileName = '%s-%s-%s-%s-%s-%s merging.csv' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
            resultDf=pandas.concat(result, ignore_index=True)
            resultDf.to_csv(outputFileName, encoding='utf-8-sig')
            return outputFileName
        else:
            return fileName

mainSetting()