#! /usr/bin/python3

import PureCloudPlatformClientV2
from PureCloudPlatformClientV2.rest import ApiException
from pprint import pprint

def run(a):

  CLIENT_ID = "" 
  CLIENT_SECRET = ""
  ORG_REGION = "ap_northeast_2"  # eg. us_east_1

  # Set environment
  region = PureCloudPlatformClientV2.PureCloudRegionHosts[ORG_REGION]
  PureCloudPlatformClientV2.configuration.host = region.get_api_host()

  # OAuth when using Client Credentials
  api_client = PureCloudPlatformClientV2.api_client.ApiClient() \
              .get_client_credentials_token(CLIENT_ID, CLIENT_SECRET)

  outbound_api = PureCloudPlatformClientV2.OutboundApi(api_client)

  # create an instance of the API class
  contact_list_id = "" # str | Contact List ID
  contact_ids = [a] # list[str] | ContactIds to delete.

  try:
      # Delete contacts from a contact list.
      outbound_api.delete_outbound_contactlist_contacts(contact_list_id, contact_ids)
  except ApiException as e:
      print("Exception when calling DeleteOutboundContactlistContactsRequest->delete_outbound_contactlist_contacts: %s\n" % e)

  return  '''<!DOCTYPE HTML><html>
  <head>
    <title>Flask app</title>
  </head>
  <body>
    <h1><a href="/">GS Neotek</a></h1>
    <h2>Complete!!</h2>
  </body>
</html>'''