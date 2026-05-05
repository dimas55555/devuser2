from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "travel"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)


class Trip(Base):
    __tablename__ = "trips"
    __table_args__ = {"schema": "travel"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String)

    user_id = Column(UUID(as_uuid=True), ForeignKey("travel.users.id"))
    user = relationship("User")


class Location(Base):
    __tablename__ = "locations"
    __table_args__ = {"schema": "travel"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String)

    trip_id = Column(UUID(as_uuid=True), ForeignKey("travel.trips.id"))


class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = {"schema": "travel"}

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    type = Column(String)

    trip_id = Column(UUID(as_uuid=True), ForeignKey("travel.trips.id"))