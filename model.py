from dao import connection

DATABASE_URL = "sqlite:///hotel.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)