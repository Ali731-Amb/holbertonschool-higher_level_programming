#!/usr/bin/python3
"""
Définition de la classe City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Classe City liée à la table 'cities'
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    # Lien vers l'ID de la table states
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)