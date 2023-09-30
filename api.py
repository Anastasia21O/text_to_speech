from fastapi import APIRouter

from service import getUsers, addUser, editUser, deleteUser, getSales, addSale, editSale, deleteSale

router = APIRouter(tags=["text_to_speach"])


@router.get("/users")
def text_to_speach_say():
    return getUsers()


@router.post("/addUser")
def text_to_speach_bytes(user: dict):
    return addUser(user)


@router.put("/editUser")
def text_to_speach_bytes(user: dict):
    return editUser(user)


@router.put("/deleteUser")
def text_to_speach_bytes(userId: int):
    return deleteUser(userId)


@router.get("/sales")
def text_to_speach_say():
    return getSales()


@router.post("/addSale")
def text_to_speach_bytes(sale: dict):
    return addSale(sale)


@router.put("/editSale")
def text_to_speach_bytes(sale: dict):
    return editSale(sale)


@router.put("/deleteSale")
def text_to_speach_bytes(saleId: int):
    return deleteSale(saleId)
