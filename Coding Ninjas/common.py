from email import encoders, message
from email.mime.base import MIMEBase
import imaplib
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from httpx import get
from urllib.parse import urljoin
from datetime import datetime
from six import iteritems, text_type

def getTabSeriesNumber(option, Session):
	nameIncrementSPData = 0
	try:
		query = "select current FROM tabSeries WHERE NAME = '" + option + "'"
		seriesNameSP8 = Session.execute(query)
		nameIncrementSPData = ''
		for data in seriesNameSP8:
			seriesNameSP = data[0]
			nameIncrementSPData = seriesNameSP
	except Exception as e:
		print('Error in getTabSeriesNumber method:', str(e))
	return nameIncrementSPData

def updateTabSeries(option, Session, nameIncrementSP):
	try:
		if nameIncrementSP != 0:
			query = f"UPDATE tabSeries SET CURRENT = '{nameIncrementSP}' WHERE NAME = '{option}'"
			Session.execute(query)
	except Exception as e:
		print('Error updateTabSeries method:', str(e))


def getdfconfigdetails():
	configdata = ''
	try:
		templates_dir = os.path.dirname(__file__)
		file_path = os.path.join(templates_dir, "dfconfig.cfg")
		configdata = ''
		with open(file_path) as file_handle:
			configdata = file_handle.read()
		if configdata == '':
			print('Invalid config data')
		else:
			configdata = json.loads(str(configdata))
	except Exception as e:
		Except = f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}"
		print('Error in getdfconfigdetails method: ', Except)
	return configdata


def getbasepathdetails():
	configdata = ''
	try:
		templates_dir = os.path.dirname(__file__)
		file_path = os.path.join(templates_dir, "dfconfig.cfg")
		configdata = ''
		with open(file_path) as file_handle:
			configdata = file_handle.read()
		if configdata == '':
			print('Invalid config data')
		else:
			configdata = json.loads(str(configdata))
			basePath = configdata['basePath']
	except Exception as e:
		Except = f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}"
		print('Error in getdfconfigdetails method: ', Except)
	return basePath


def get_session(session, jsondata):
	try:
		if not jsondata or jsondata == '':
			jsondata = getdfconfigdetails()
		dbPath = jsondata['dburl']
		if dbPath.strip(' ') == '':
			print("Not a valid connection string")
		if not session:
			engine = create_engine(dbPath)
			SessionMDB = sessionmaker(bind=engine)
			session = SessionMDB()
		return session
	except Exception as e:
		Except = f"{type(e).__name__} at line {e.__traceback__.tb_lineno} of {__file__}"
		print('Error in getSession method: ', Except)

