# System modules
import sys
import os
import pathlib

# https://pypi.org/project/pg8000/ 
# Install with python -m pip install pg8000 or set path to local copy
sys.path.append(<path to mysql Python module here>)

import mysql.connector

mydb = mysql.connector.connect(
  host="<host_ip_here>",
  user="root",
  password="password",
  database="test"
)

mycursor = mydb.cursor()

finish_date: str = "2023-10-12 16:23:59"
build_id: int = 19497474
build_type: str = "My_Build"
change: int = 851885
url: str = "https://mybuildserver.com/viewLog.html?buildId=11111"
status: str = "SUCCESS"
agent: str = "my_agent"
duration: int = 1140000

mycursor.execute(f"""INSERT INTO example_01 (`finish_date`,`build_id`, `build_type`, `change`, `url`, `status`, `agent`, `duration`)""" +
                 f""" VALUES ('{finish_date}', '{build_id}', '{build_type}', '{change}', '{url}', '{status}', '{agent}', '{duration}');""")
                 
mydb.commit()
mycursor.close()
mydb.close()
sys.exit()
