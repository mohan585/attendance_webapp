from deta import App,Deta
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz
import api_it
# datetime object containing current date and time
IST = pytz.timezone('Asia/Kolkata')
datetime_ist = datetime.now(IST)
dt_string = datetime_ist.strftime('%Y:%m:%d %H:%M:%S ')



app = App(FastAPI())

@app.get("/")
def http():
    return "Hello Deta, I am running with HTTP"

@app.lib.cron()
def cron_job(event):
    api_it.students_data_update_it()
    return f"Attendence Updated {dt_string}"


