#!/usr/bin/python
import os
import twitter
import logging
import csv
import datetime

from config import con_key, con_secret, access_token, access_secret

logging.basicConfig(level=logging.DEBUG)
dir_path = '/Users/nick/writing/'
suffixes_of_interest = ['md', 'mdown']
word_count = 0

for (root, subdirs, files) in os.walk(dir_path):
  filtered_list = [os.path.join(root, x) for x in files if x.split('.')[-1] in suffixes_of_interest]
  for file in filtered_list:
    print file
    with open(file, 'r') as f:
      file_count = len(f.read().split())
      word_count += file_count

logging.info(word_count)

with open('wordcount.csv', 'r+') as csvfile:
  reader = csv.reader(csvfile)
  for row in reader:
    last_date = datetime.datetime.strptime(row[0],"%Y-%m-%d").date()
    last_count = int(row[1])
  
  writer = csv.writer(csvfile)
  writer.writerow([datetime.date.today(), word_count])

if (datetime.date.today() > last_date):
  print last_date
  # we have a new count
  difference = word_count - last_count
  if (difference > 0):
    api = twitter.Api(consumer_key=con_key,
                      consumer_secret=con_secret,
                      access_token_key=access_token,
                      access_token_secret=access_secret)
    logging.debug(api.VerifyCredentials())

    status_text = '@npdoty wrote %s words yesterday.' % difference
    status = api.PostUpdate(status_text)
    logging.info(status.text)
  else:
    logging.info("No new writing today.")
else:
  logging.info("already have a log entry from today")