from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Missile(Base):
    __tablename__ = "missiles"

    missile_id = Column(Integer, primary_key=True, index=True)
    missile_name = Column(String(80), nullable=False, unique=True)
    missile_country = Column(String(80))
    missile_range = Column(Integer)
    missile_category = Column(String(200))
    missile_payload_weight = Column(Integer)
    missile_payload_type = Column(String(200))
    missile_payload_nuke = Column(String(200))
    missile_nuke_type = Column(String(200))
    missile_description = Column(String(200))
    missile_image_url = Column(String(250))
    missile_class = Column(String(15))
    missile_class_additional = Column(String(200))
    missile_launcher = Column(String(200))

    def __repr__(self):
        return 'ItemModel(name=%s, price=%s,store_id=%s)' % (self.name, self.price, self.store_id)


class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False, unique=True)
    items = relationship("Item", primaryjoin="Store.id == Item.store_id", cascade="all, delete-orphan")

    def __repr__(self):
        return 'Store(name=%s)' % self.name