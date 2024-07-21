# System modules
import sys
import os
import pathlib

# https://pypi.org/project/pg8000/ 
# Install with python -m pip install pg8000 or set path to local copy
sys.path.append(<path to pg8000 Python module here>)

import dateutil
import six             
import asn1crypto       
import scramp          
import importlib
import pg8000.native

con = pg8000.dbapi.connect(database='analytics', user="admin", password="password", host='<host_ip_here>', port='5433')

finish_date: str = "2023-10-12 16:23:59"
build_id: int = 19497474
build_type: str = "My_Build"
change: int = 851885
url: str = "https://mybuildserver.com/viewLog.html?buildId=11111"
status: str = "SUCCESS"
agent: str = "my_agent"
duration: int = 1140000

cur = con.cursor()
cur.execute(f"""INSERT INTO example_01 (finish_date, build_id, build_type, change, url, status, agent, duration)""" +
            f""" VALUES ('{finish_date}', '{build_id}', '{build_type}', '{change}', '{url}', '{status}', '{agent}', '{duration}');""")
            
con.commit()
cur.close()
con.close()
sys.exit()

