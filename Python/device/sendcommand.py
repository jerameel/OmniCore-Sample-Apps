from __future__ import print_function
import time
import os
import base64
import OmniCore
from OmniCore.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://demo-api.omnicore.cloud.korewireless.com/model-state-management
# See configuration.py for a list of all supported configuration parameters.


# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = OmniCore.Configuration(
    host="https://demo-api.omnicore.cloud.korewireless.com/model-state-management",
    access_token="eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NzZiNzIxNDAwYmZhZmEyOWQ0MTFmZTYwODE2YmRhZWMyM2IzODIiLCJ0eXAiOiJKV1QifQ.eyJyb2xlIjoiVGVuYW50QWRtaW4iLCJzdWJzY3JpcHRpb25JZCI6ImtvcmV3aXJlbGVzcy1kZXZlbG9wbWVudCIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9nY3AtaW90LWNvcmUtZGVtby0zNjE2MTQiLCJhdWQiOiJnY3AtaW90LWNvcmUtZGVtby0zNjE2MTQiLCJhdXRoX3RpbWUiOjE2NzY1MzQ2MzAsInVzZXJfaWQiOiJCb2RaZEQ0YVhpWHRSMVNUR0pKWTlTaGZuTW0yIiwic3ViIjoiQm9kWmRENGFYaVh0UjFTVEdKSlk5U2hmbk1tMiIsImlhdCI6MTY3ODE2MDk0MiwiZXhwIjoxNjc4MTY0NTQyLCJlbWFpbCI6InNoZWh6YWRAa29yZXdpcmVsZXNzLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJzaGVoemFkQGtvcmV3aXJlbGVzcy5jb20iXX0sInNpZ25faW5fcHJvdmlkZXIiOiJwYXNzd29yZCIsInRlbmFudCI6ImtvcmV3aXJlbGVzcy1jb20taWUzZ3IifX0.ZqQYWmZ7JWvKOTwAt-OEon7RhPimEpPU9fxUrpJPrBc4mp682nZ1QYlGqjg9MzgxYQ5OMp5TeQbhSv0yyjnfQheOPcgweS4_hIUUV9PbXEOiyhD8UMjp3GNXDSNST6HHzZwqtAOBUG33LQNcJeEhNmgu6Skx_1GrFbv4A3GLDE0tkJXfI3OqYJbtXUkoHtt6mQ0tftY2M5FQ2RIjFvpmvnqneEz2M9Anavh9j_Uix7Ay-sXACz6S8YRAlV8VJ9I50jYV4M37ZcOksc0mo6n0wT9eg-UgMrEIGAZvO2ID-b0TOY5iIaQxKhEEENeHTwywOC2K0JCCWp6LKKOvZA6BSA"
)


def encode_to_base64(input: str):
    try:
        sample_string_bytes = input.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string: str = base64_bytes.decode("ascii")
        return base64_string
    except Exception as e:
        print("Exception when encoding as base64 %s\n" % e)


# Enter a context with an instance of the API client
with OmniCore.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = OmniCore.DeviceApi(api_client)
    subscriptionid = 'korewireless-development'  # str | Subscription ID
    registry_id = 'shaiz-registry-sdk'  # str | Registry ID
    device_id = 'shaizdev00'  # str | Device ID
    data_to_send = "Hi from omnicore"
    base64_string: str = encode_to_base64(data_to_send)
    # DeviceCommand | application/json
    device = OmniCore.DeviceCommand(binaryData=base64_string)
    device.subfolder = ""

    try:
        api_response = api_instance.send_command_to_device(
            subscriptionid, registry_id, device_id, device)
        print("The response of DeviceApi->send_command_to_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeviceApi->send_command_to_device: %s\n" % e)
