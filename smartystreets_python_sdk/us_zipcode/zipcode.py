class ZipCode:
    def __init__(self, obj):
        """
        See "https://smartystreets.com/docs/cloud/us-zipcode-api#zipcodes"
        """
        self.zipcode = obj.get('zipcode')
        self.zipcode_type = obj.get('zipcode_type')
        self.default_city = obj.get('default_city')
        self.county_fips = obj.get('county_fips')
        self.county_name = obj.get('county_name')
        self.state_abbreviation = obj.get('state_abbreviation')
        self.state = obj.get('state')
        self.latitude = obj.get('latitude')
        self.longitude = obj.get('longitude')
        self.precision = obj.get('precision')
        self.alternate_countries = obj.get('alternate_counties', [])
