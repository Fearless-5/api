from flask import Flask
from faker import Faker
from countryinfo import CountryInfo

fake = Faker()
coun = CountryInfo(fake.country())
app = Flask(__name__)
@app.route("/")
def home():
    return {
        "name": fake.name(),
        "url": fake.url(),
        "country": fake.country(),
        "email": fake.email(),
        "country": {
            "name": coun.name(),
            "currencies": coun.currencies(),
            "capital": coun.capital(),
            "language": coun.languages(),
            "population": coun.population(),
        }
    }
    
app.run(host="0.0.0.0", port=3050)
