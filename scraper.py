import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import schedule
import time
from bs4 import BeautifulSoup
import time
from datetime import datetime
import csv
import pandas as pd
from selenium.webdriver.support.ui import Select

import psycopg2
import pandas as pd
from sqlalchemy import create_engine


url = 'https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')



chrome_browser = webdriver.Chrome('./chromedriver.exe',options=options)

chrome_browser.get(url)
ddelement= Select(chrome_browser.find_element_by_xpath('//*[@id="sel_year"]'))
ddelement.select_by_value('2021')

go_button = chrome_browser.find_element_by_xpath('//*[@id="bonus_frm"]/div/table/tbody/tr/td[3]/input')
go_button.click()

time.sleep(10)

html = chrome_browser.page_source

mc = pd.read_html(html)

print(mc)

xm = mc[1:]
pritesh = np.squeeze(xm,axis= 0)
df = pd.DataFrame(pritesh)
print(df)
x = 'GAIL'

test =df.loc[df[0] == x]
print(test)
print('before renaming')
print(list(test.columns))
test.columns = ['Stock_ticker', 'dividend_type', 'dividend_precentage','date_announcement','date_record','ex_dividend_date']
print(test)
print('after renaming')
print(list(test.columns))
test.to_csv('scrapped_data_latest1.csv', encoding='utf-8',  index=False)
print('The data transfered to csv')


conn_string = 'postgresql://Avitest:9167199744@localhost/accounts_nse_bse_dividend_alerts'

  
db = create_engine(conn_string)
conn = db.connect()
  
  
# our dataframe

  
# Create DataFrame
test.to_sql('accounts_nse_bse_dividend_alerts', con=conn, if_exists='replace',
          index=False)
conn = psycopg2.connect(conn_string
                        )
conn.autocommit = True
cursor = conn.cursor()
  
sql1 = '''select * from accounts_nse_bse_dividend_alerts;'''
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)
  
conn.commit()
conn.close()


