from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, ForeignKey, Integer

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "travel"}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)


class Trip(Base):
    __tablename__ = "trips"
    __table_args__ = {"schema": "travel"}

    id = Column(Integer, primary_key=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey("travel.users.id"))

    user = relationship("User")


class Location(Base):
    __tablename__ = "locations"
    __table_args__ = {"schema": "travel"}

    id = Column(Integer, primary_key=True)
    name = Column(String)
    trip_id = Column(Integer, ForeignKey("travel.trips.id"))


class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = {"schema": "travel"}

    id = Column(Integer, primary_key=True)
    type = Column(String)
    trip_id = Column(Integer, ForeignKey("travel.trips.id"))