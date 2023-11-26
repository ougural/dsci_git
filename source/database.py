#from bs4 import BeautifulSoup
#import requests
from cassandra.cluster import Cluster
from uuid import uuid4

cluster = Cluster(['0.0.0.0'], port = 9042)
session = cluster.connect("park")

session.execute("""
    CREATE TABLE park.parks (
    park_id UUID PRIMARY KEY,
    name TEXT,
    location TEXT,
    description TEXT,
    rating_overall DECIMAL,
    rating_hiking DECIMAL,
    rating_camping DECIMAL
);
""")

session.execute("""
    CREATE TABLE park.reviews (
    park_id UUID,
    review_id UUID,
    username TEXT,
    review_text TEXT,
    review_date DATE,
    rating_overall INT,
    rating_trails INT,
    rating_camping INT,
    rating_fishing INT,
    PRIMARY KEY (park_id, review_id)
);
""")

session.execute("""
    CREATE TABLE park.users (
    username TEXT PRIMARY KEY,
    password TEXT
);
""")

session.execute("""
    CREATE TABLE park.user_destinations (
    username TEXT,
    park_name TEXT,
    review_id UUID,
    PRIMARY KEY (username, park_name)
);
""")

'''url = "https://www.parks.ca.gov/?page_id=21805"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
names = soup.find_all("a")
temp = "State"
parkNames = []
for name in names:
    tempName = name.string
    if tempName and temp in tempName:
        parkNames.append(tempName)
print(parkNames)
for name in parkNames:
    session.execute(
        "INSERT INTO parks (park_id, park_name) VALUES (uuid(), %s)",
        (name,)
    )'''

