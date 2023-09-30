from mysql.scheme import User, Sale, session


def getUsers():
    return session.query(User).all()


def getUser(userId: int):
    user = session.query(User).filter(User.id == userId).first()
    return user


def addUser(user: dict) -> int:
    user_new = User(name=user['name'], surname=user['surname'], phone=user['phone'])
    session.add(user_new)
    session.commit()
    return user_new.id


def editUser(user: dict) -> bool:
    user_update = getUser(user['id'])
    if user_update:
        user_update.name = user['name']
        user_update.surname = user['surname']
        user_update.phone = user['phone']
        session.commit()
        return user_update.id
    return False


def deleteUser(userId: int) -> int:
    user = getUser(userId)
    session.delete(user)
    session.commit()
    return userId


def getSales():
    return session.query(Sale).all()


def getSale(saleId: int):
    sale = session.query(Sale).filter(Sale.id == saleId).first()
    return sale


def addSale(sale: dict) -> int:
    sale_new = User(nameProduct=sale['nameProduct'], userId=sale['userId'], date=sale['date'], price=sale['price'])
    session.add(sale_new)
    session.commit()
    return sale_new.id


def editSale(sale: dict) -> bool:
    sale_update = getSale(sale['id'])
    if sale_update:
        sale_update.nameProduct = sale['nameProduct']
        sale_update.userId = sale['userId']
        sale_update.date = sale['date']
        sale_update.price = sale['price']
        session.commit()
        return sale_update.id
    return False


def deleteSale(saleId: int) -> int:
    sale = getSale(saleId)
    session.delete(sale)
    session.commit()
    return saleId
