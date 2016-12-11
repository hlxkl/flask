from flask import Flask, render_template, request
import weather, yelp_api
import os
import dotenv
import forecastio
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    search_term = request.values.get('search_term')
    businesses = None
    get_business = None
    if address:
        get_business = yelp_api.get_businesses(address,search_term)
    return render_template('index.html', businesses=get_business, address=address, term=search_term)
    #print (get_business)
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="127.0.0.1", port=port)