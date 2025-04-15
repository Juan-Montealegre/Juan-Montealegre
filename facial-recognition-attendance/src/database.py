from sqlalchemy import create_engine, Column, Integer, String, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    face_encoding = Column(LargeBinary, nullable=False)  # Almacena la codificación facial

class AttendanceRecord(Base):
    __tablename__ = 'attendance_records'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    date = Column(String, default=datetime.utcnow().strftime("%Y-%m-%d"))
    time = Column(String, default=datetime.utcnow().strftime("%H:%M:%S"))

DATABASE_URL = "sqlite:///attendance.db"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def add_user(username, face_encoding):
    session = Session()
    user = User(username=username, face_encoding=face_encoding)
    session.add(user)
    session.commit()
    session.close()

def get_users():
    session = Session()
    users = session.query(User).all()
    session.close()
    return users

def add_attendance_record(username):
    session = Session()
    record = AttendanceRecord(username=username)
    session.add(record)
    session.commit()
    session.close()

def get_attendance_records():
    session = Session()
    records = session.query(AttendanceRecord).all()
    session.close()
    return records