from sqlalchemy import create_engine
from models import User

if __name__ == '__main__':
    print("CONNECTING to the database...")
    engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

    print("Dropping tables...")
    User.metadata.drop_all(engine)

    print("Creating tables...")
    User.metadata.create_all(engine)

    print("Done")
