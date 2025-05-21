# app/models/models.py

import enum

from sqlalchemy import Column, Enum, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class OrderStatus(enum.IntEnum):
    PENDING = 0
    PREPARING = 1
    READY = 2


class Product(Base):
    __tablename__ = "Product"

    code = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    active = Column(Integer, default=1)


class Order(Base):
    __tablename__ = "Order"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String, nullable=False)
    table_number = Column(String, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING)

    items = relationship("OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "OrderItem"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("Order.id"))
    product_code = Column(Integer, ForeignKey("Product.code"))
    quantity = Column(Integer, nullable=False)
    note = Column(Text, nullable=True)

    order = relationship("Order", back_populates="items")
    product = relationship("Product")
