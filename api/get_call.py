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


  # Use your own IDs here
  contact_list_id = ""
  contact_id = a # str | Contact ID

  # Genesys Cloud Objects
  outbound_api = PureCloudPlatformClientV2.OutboundApi(api_client)

  try:
      # Get a contact.
      api_response = outbound_api.get_outbound_contactlist_contact(contact_list_id, contact_id)
      tmp = pprint(api_response)
      return tmp 
  except ApiException as e:
      return print("Exception when calling GetOutboundContactlistContactRequest->get_outbound_contactlist_contact: %s\n" % e)

# Contact ID
run('')