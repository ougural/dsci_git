from cassandra.cluster import Cluster
from uuid import uuid4

cluster = Cluster(['0.0.0.0'], port = 9042)
session = cluster.connect("park")

session.execute("""
    CREATE TABLE park.parks (
    park_id UUID PRIMARY KEY,
    park_name TEXT,
    location TEXT,
    description TEXT,
    rating_overall DECIMAL,
    rating_hiking DECIMAL,
    rating_camping DECIMAL,
    rating_fishing DECIMAL,
    activities SET<TEXT>
);
""")

session.execute("""
    CREATE TABLE park.pictures (
    park_id UUID,
    picture_id UUID,
    picture_url TEXT,
    description TEXT,
    upload_date TIMESTAMP,
    PRIMARY KEY (park_id, picture_id)
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
    password TEXT,
    email TEXT
);
""")

session.execute("""
    CREATE TABLE user_destinations (
    username TEXT,
    park_name TEXT,
    review_id UUID,
    PRIMARY KEY (username, park_name)
);
""")
