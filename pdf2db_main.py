import os 
import pdf2db_header_page
import pdf2db_get_coordinates
import pdf2db_normal_page

import sys
import logging
import time
import datetime
import requests
import json
from bs4 import BeautifulSoup
import cx_Oracle

timeSleep = 60 #second
backupFolder = './backup_folder/'
imgFolder = './img_folder/'
pdfFolder = './pdf_folder/'
xlsxFolder = './xlsx_folder/'
def sql_connect():
    try:
        conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};SERVER=10.0.31.6;DATABASE=MiraeAsset;uid=mirae;pwd=Mirae123@@@')
        return conn
    except Exception as e:
        print(e)


def sql_query_df(sql):
    conn = sql_connect()
    result = pd.read_sql(sql)
    conn.close
    return result


## Oracle Database
# check os and indicate the Oracle Client Libraries location 
try:
    if sys.platform.startswith("darwin"):
        lib_dir = os.path.join(os.environ.get("HOME"), "Downloads", "instantclient_19_10")
        cx_Oracle.init_oracle_client(lib_dir=lib_dir)
    elif sys.platform.startswith("win64"):
        cx_Oracle.init_oracle_client(lib_dir=r"E:/Source code/vsdclient-sftp/document/program/instantclient_19_3")
except Exception as err:
    print("Whoops!")
    print(err);
    sys.exit(1);

# Oralce Database connection information
username = 'quote'
password = '123456'
#dns = 'mas-scan.masvn.local/sat.masvn.local'
dns = '10.0.25.24:1521/oracledb'
port = 1521
encoding = 'UTF-8'
conn = None


def orcl_connect():
    try:
        conn = cx_Oracle.connect(username, password, dns, encoding=encoding)
        return conn
    except cx_Oracle.Error as error:
        print(error)


def orcl_disconnect():
    if(conn):
        conn.close()


def orcl_insert_company_info(sql):
    try:
        #conn = orcl_connect()
        with conn.cursor() as cur:
            cur.execute(sql)
            conn.commit()
    except cx_Oracle.Error as error:
        print(error)

def __checkPdfFiles__():
    files = []
    for file in os.listdir(pdfFolder):
        if file.endswith('.pdf'):
            files.append(os.path.join(pdfFolder + file))
    return files

if __name__ == "__main__":
    file_list = __checkPdfFiles__()
    if len(file_list) < 0:
        print('Pdf files not exit')
        exit()
    #print(file_list)
    for file in file_list:
        print(file)
        all_data = []
        coordinates_pages = pdf2db_get_coordinates.__main__(file)
        #print(coordinates_pages)
        for infor in coordinates_pages:
            header_page = infor[0]
            #print(header_page)
        
            if len(infor) > 1:
                columns = infor[1:]
                #print(pdf2db_header_page.__main__(file, header_page))
                all_data += (pdf2db_header_page.__main__(file, header_page))
            else:
                #print(header_page )
                #print(pdf2db_normal_page.__main__(file, header_page + 1, columns))
                all_data+=(pdf2db_normal_page.__main__(file, header_page + 1, columns))
            #print(columns)
        #print(all_data)
        conn = orcl_connect()    
        for x in range(len(all_data)):
            insert_sql = "INSERT INTO HOSE_PT values('" + file[13:21] + "','" + str(all_data[x][0])\
            + "','" + str(all_data[x][1]).replace('nan','0').replace(',','')                       \
            + "','" + str(all_data[x][2]).replace('nan','0').replace(',','')                       \
            + "','" + str(all_data[x][3]).replace('nan','0').replace(',','')                       \
            + "','" + str(all_data[x][4]).replace('nan','0').replace(',','')                       \
            + "','" + str(all_data[x][5]).replace('nan','0').replace(',','')                       \
            + "','" + str(all_data[x][6]).replace('nan','0').replace(',','')                       \
            + "','" + str(all_data[x][7]).replace('nan','0').replace(',','')                       \
            + "','" + str(all_data[x][8]).replace('nan','0').replace(',','')                       \
            + "')"                                                                                  
            print(insert_sql)
            orcl_insert_company_info(insert_sql)
        orcl_disconnect()
            
        result = sql_query_df("SELECT * FROM HOSE_PT")
        print(result)