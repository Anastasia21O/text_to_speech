from .bd import engine

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import Column, Integer, String, MetaData, ForeignKey, Date

meta = MetaData()

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    phone = Column(String)

    def __repr__(self):
        return "<User(name='%s', surname='%s', phone='%s')>" % (
            self.name, self.sorname, self.phone)


class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nameProduct = Column(String)
    userId = Column(ForeignKey("user.id"))
    date = Column(Date)
    price = Column(Integer)

    user = relationship("User", lazy='joined')

    def __repr__(self):
        return "<Sale(nameProduct='%s', userId='%s', date='%s', price='%s')>" % (
            self.nameProduct, self.userId, self.date, self.price)


Base.metadata.create_all(engine)
session.commit()
