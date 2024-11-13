from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

# Set up the database connection and session
DATABASE_URI = 'sqlite:///ice_cream_shop.db'  # Your database URI here

# Create the engine and sessionmaker
engine = create_engine(DATABASE_URI, echo=True)  # Set echo=True for debugging

SessionLocal = sessionmaker(autoflush=False, bind=engine)

# Create all tables in the database (if they don't already exist)
def create_tables():
    Base.metadata.create_all(engine)

# Return a new session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Base.metadata.drop_all(bind=engine)

# Call create_tables to create tables when the app starts
create_tables()
