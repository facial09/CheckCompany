from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 리스트 준비하기
final_list=[]

# 해당 사이트 접속

browser = webdriver.Chrome('/Users/shlee/Desktop/section3.project/chromedriver')
url = "https://www.jobplanet.co.kr/companies?sort_by=review_avg_cache&industry_id=700"
browser.get(url)



# 컬럼 만드는 함수 작성

def mkscore():
    soup = BeautifulSoup(browser.page_source, "html")
    columns = soup.find_all("div",class_='rate_pie_set')
    columns_2 = soup.find_all("div",class_='job_tooltip_box hover block')
    company = str(soup.find("h1", class_ = 'name').text)
    
    pie_namelist = []
    pie_percentlist = []
    name_collist =[]
    name_vallist = []
    
    time.sleep(3)
    for i in columns:
        pie_name = str(i.find(class_='rate_label').text)
        pie_percent = int(i.find(class_='txt_point').text[:2])
        pie_namelist.append(pie_name)
        time.sleep(3)

    for i in columns_2:
        name_col = str(i.find(class_='rate_bar_title').text)
        name_val = float(i.find(class_='txt_point').text)
        name_collist.append(name_col)
        name_vallist.append(name_val)
        time.sleep(3)

    col_total = {'name': company , 
            '복지 및 급여' : name_vallist[0],
                '워라벨' : name_vallist[1],
                '사내문화': name_vallist[2],
                '승진 기회 및 가능성': name_vallist[3],
                '경영진': name_vallist[4],
                '기업 추천율':pie_percentlist[0],
                'CEO 지지율':pie_percentlist[1],
                '성장 가능성' :pie_percentlist[2],
                '총점' : soup.find("span",class_='rate_point').text
                }
    final_list.append(col_total)
    return final_list

# 한 페이지 크롤링 돌리는 함수

def crowling():
    for i in range(1,11):
        time.sleep(3)
        browser.find_element(By.XPATH,f'//*[@id="listCompanies"]/div/div[1]/section[{i}]/div/div/div/a/img').click()
        time.sleep(3)
        now_url = browser.current_url
        if 'reviews' not in now_url:
            time.sleep(3)
            elem = browser.find_element(By.CLASS_NAME, 'viewReviews')
            elem.click()
            time.sleep(3)
            mkscore()
            browser.back()
            browser.back()

        else:  
            time.sleep(3)
            mkscore()
            time.sleep(3)
            browser.back()

# 다음 페이지 넘기고 10개 크롤링 하는 최종 구문

for num in range(1,20):
    if num == 3:
        time.slee(3)
        crowling()
        time.sleep(3)
        
    else:    
        time.sleep(3)
        crowling()
        time.sleep(3)
        browser.find_element(By.XPATH,'//*[@id="listCompanies"]/div/div[2]/article/a[7]').click()
        time.sleep(3)