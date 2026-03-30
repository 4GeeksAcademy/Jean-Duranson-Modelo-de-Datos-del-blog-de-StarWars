from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(80), nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean(), default=True)

    # Relación sin usar "list"
    favorites: Mapped["Favorite"] = relationship(
        "Favorite", 
        back_populates="user", 
        uselist=True
    )

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "is_active": self.is_active
        }

class Character(db.Model):
    __tablename__ = 'character'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    gender: Mapped[str] = mapped_column(String(50), nullable=True)
    hair_color: Mapped[str] = mapped_column(String(50), nullable=True)
    eye_color: Mapped[str] = mapped_column(String(50), nullable=True)

    favorites: Mapped["Favorite"] = relationship(
        "Favorite", 
        back_populates="character", 
        uselist=True
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    population: Mapped[str] = mapped_column(String(50), nullable=True)
    climate: Mapped[str] = mapped_column(String(50), nullable=True)
    terrain: Mapped[str] = mapped_column(String(50), nullable=True)

    favorites: Mapped["Favorite"] = relationship(
        "Favorite", 
        back_populates="planet", 
        uselist=True
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain
        }

class Favorite(db.Model):
    __tablename__ = 'favorite'
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    planet_id: Mapped[int] = mapped_column(ForeignKey('planet.id'), nullable=True)
    character_id: Mapped[int] = mapped_column(ForeignKey('character.id'), nullable=True)
    vehicle_id: Mapped[int] = mapped_column(ForeignKey('vehicle.id'), nullable=True)

    user: Mapped["User"] = relationship(
        "User", 
        back_populates="favorites",
        uselist=False
    )
    planet: Mapped["Planet"] = relationship(
        "Planet", 
        back_populates="favorites",
        uselist=False
    )
    character: Mapped["Character"] = relationship(
        "Character", 
        back_populates="favorites",
        uselist=False
    )
    vehicle: Mapped["Vehicle"] = relationship(
        "Vehicle", 
        back_populates="favorites", 
        uselist=False
    )

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }
    
class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    model: Mapped[str] = mapped_column(String(100), nullable=True)
    vehicle_class: Mapped[str] = mapped_column(String(100), nullable=True)
    passengers: Mapped[str] = mapped_column(String(50), nullable=True)

    # Relación con favoritos
    favorites: Mapped["Favorite"] = relationship(
        "Favorite", 
        back_populates="vehicle", 
        uselist=True
    )

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "vehicle_class": self.vehicle_class,
            "passengers": self.passengers
        }