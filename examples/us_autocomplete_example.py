import os

from smartystreets_python_sdk import StaticCredentials, ClientBuilder
from smartystreets_python_sdk.us_autocomplete import Lookup as AutocompleteLookup, geolocation_type


def run():
    auth_id = "Your SmartyStreets Auth ID here"
    auth_token = "Your SmartyStreets Auth Token here"

    # We recommend storing your secret keys in environment variables instead---it's safer!
    # auth_id = os.environ['SMARTY_AUTH_ID']
    # auth_token = os.environ['SMARTY_AUTH_TOKEN']

    credentials = StaticCredentials(auth_id, auth_token)

    client = ClientBuilder(credentials).build_us_autocomplete_api_client()
    lookup = AutocompleteLookup('4770 Lincoln Ave O')

    client.send(lookup)

    print('*** Result with no filter ***')
    print()
    for suggestion in lookup.result:
        print(suggestion.text)

    # Documentation for input fields can be found at:
    # https://smartystreets.com/docs/us-autocomplete-api#http-request-input-fields

    lookup.add_city_filter('Ogden')
    lookup.add_state_filter('IL')
    lookup.add_prefer('Fallon, IL')
    lookup.max_suggestions = 5
    lookup.geolocate_type = geolocation_type.NONE
    lookup.prefer_ratio = 0.333333
    lookup.add_state_filter('IL')
    lookup.max_suggestions = 5

    suggestions = client.send(lookup)  # The client will also return the suggestions directly

    print()
    print('*** Result with some filters ***')
    for suggestion in suggestions:
        print(suggestion.text)


if __name__ == "__main__":
    run()
