from cassandra.cluster import Cluster
from uuid import uuid4

def create_schema(session):
    # Create Keyspace
    session.execute("""
        CREATE KEYSPACE IF NOT EXISTS parks_keyspace
        WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """)

    # Create Table
    session.execute("""
        CREATE TABLE IF NOT EXISTS parks_keyspace.parks (
            park_id uuid PRIMARY KEY,
            name text,
            location text,
            size float,
            features list<text>
        )
    """)

def insert_park(session, name, location, size, features):
    # Insert a park
    session.execute(
        """
        INSERT INTO parks_keyspace.parks (park_id, name, location, size, features)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (uuid4(), name, location, size, features)
    )

def main():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()

    create_schema(session)

    # Insert some sample parks
    insert_park(session, "Sunnydale Park", "Sunnydale", 100.5, ["lake", "playground"])
    insert_park(session, "Greenfield Park", "Greenfield", 75.2, ["forest", "picnic area"])

    # Close the session and cluster connection
    session.shutdown()
    cluster.shutdown()

if __name__ == "__main__":
    main()
