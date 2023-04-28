from __future__ import print_function
import time
import os
import OmniCore
from OmniCore.rest import ApiException
from pprint import pprint
from generatetoken import fetchToken
# Defining the host is optional and defaults to https://api.korewireless.com/omnicore
# See configuration.py for a list of all supported configuration parameters.

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Step 1 Generate Client Token,Inputs are clientId And Client Secret Which can be fetched from ui keys console,
# If Token is not expired new token is not used, if token is expired new token is generated.

access_token = fetchToken("Insert previous token if used,leave empty if no previous token",
                          'Insert Client Id Here', 'Insert Client Secret Here')

# API key is a static key which can be fetched from keys console
# Configure access token and apikey
configuration = OmniCore.Configuration(
    host="https://api.korewireless.com/omnicore",
    access_token=access_token,
    api_key={"apiKey": "Insert Api Key Here"}
)


# Enter a context with an instance of the API client
with OmniCore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = OmniCore.DeviceApi(api_client)
    registry_id = 'Insert Registry Here'  # str | Registry ID
    subscription_id = 'Insert Subscription Here'  # str | Subscription ID
    gateway_id = 'shaizgw00'  # str | Device ID

    try:
        # Get Device
        api_response = api_instance.get_device(
            registry_id, subscription_id, gateway_id)
        print("The response of DeviceApi->get_device:\n")
        print("Device Id:%s" % api_response.id)
        print("Device Full Name:%s" % api_response.name)
        print("Certificate 1:%s" %
              api_response.credentials[0].public_key)
        print("Log Level:%s" % api_response.log_level)
        print("Created On:%s" % api_response.created_on)
        print("Updated On:%s" % api_response.updated_on)

    except Exception as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
