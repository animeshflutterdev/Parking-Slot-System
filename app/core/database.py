from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker
from pathlib import Path
from app.core.logger import log

# DATABASE_URL = "sqlite:///./parking_lot.db"

# engine = create_engine(
#     DATABASE_URL,
#     connect_args={"check_same_thread": False},
#     echo=True # This prints all SQL queries. off in prod
# )

# SessionLocal = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
# )

# Base = declarative_base()=

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(f"BASE_DIR --> {BASE_DIR}")

DATABASE_URL = (
    f"sqlite:///{BASE_DIR}/parking_slot_system.db"
)

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


try:
    with engine.connect() as connection:
        print("✅ Database connected successfully")

except SQLAlchemyError as e:
    log.error(message="db_error",data={"error": str(e)}, fileName="db_error")
    print("❌ Database connection failed")
    print(e)