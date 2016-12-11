import dotenv
import forecastio
import os
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

address = "380 St Kilda Road, Melbourne 3000"
term = "computer store"

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator


def get_businesses(location, term):
    auth = Oauth1Authenticator(
        consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        token=os.environ['TOKEN'],
        token_secret=os.environ['TOKEN_SECRET']
    )

    client = Client(auth)

    params = {
		'term': term,
		'lang': 'en'
	}

    response = client.search(location, **params)

    businesses = []

    for business in response.businesses:
        businesses.append({"phone": business.phone,
            "name": business.name
        })

    return businesses
#    for d in businesses:
#        return "-- {}".format(d['name'])

#businesses = get_businesses(address,term)
#print (businesses)
#for d in businesses:
#    print ("-- {}".format(d['name']))




