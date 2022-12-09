#! /usr/bin/python3

import base64, sys, requests, os
import PureCloudPlatformClientV2
from pprint import pprint
from PureCloudPlatformClientV2.rest import ApiException
import pymysql

def run():

  print("-------------------------------------------------------------")
  print("- Dialer Call List Management -")
  print("-------------------------------------------------------------")

  # Credentials
  CLIENT_ID = "" 
  CLIENT_SECRET = ""
  ORG_REGION = "ap_northeast_2"  # eg. us_east_1

  # Set environment
  region = PureCloudPlatformClientV2.PureCloudRegionHosts[ORG_REGION]
  PureCloudPlatformClientV2.configuration.host = region.get_api_host()

  # OAuth when using Client Credentials
  api_client = PureCloudPlatformClientV2.api_client.ApiClient() \
              .get_client_credentials_token(CLIENT_ID, CLIENT_SECRET)


  # Use your own IDs here
  contact_list_id = ""
  campaign_id = ""

  # MariaDB Connect
  con = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='customer', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
  with con.cursor() as cur:
    tmp = cur.execute('SELECT * FROM cust')
    rows = cur.fetchall()

  # Genesys Cloud Objects
  outbound_api = PureCloudPlatformClientV2.OutboundApi(api_client)
  contact_data = []


  for i in range(tmp):

    contact_data.extend(
      [
        {
          'callable': True,
          'contact_list_id': contact_list_id,
          'contactable_status': None,
          'data': rows[i],
          'id': None,
          'latest_sms_evaluations': None,
          'phone_number_status': None
        }
      ]
    )


  try:
      outbound_api.post_outbound_contactlist_contacts(contact_list_id, contact_data)
  except ApiException as e:
      print(f"Exception when calling OutboundApi->post_outbound_contactlist_contacts: {e}")
      sys.exit()

  print("Contact added to list.")


  # Get the campaign's configuration
  try:
      campaign_info = outbound_api.get_outbound_campaign(campaign_id)
  except ApiException as e:
      print(f"Exception when calling OutboundApi->get_outbound_campaign: {e}")
      sys.exit()

  pprint(f"Campaign info: {campaign_info}")

  return  '''<!DOCTYPE HTML><html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    <h1><a href="/">GS Neotek</a></h1>
    <h2>Complete!!</h2>
  </body>
</html>'''