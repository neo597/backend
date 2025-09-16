from fastapi import APIRouter
from app.controllers.madre_controller import MadreController
from app.models.madre import MadreBase

router = APIRouter(prefix="/madres", tags=["Madres"])

@router.get("/")
async def list_madres():
    return MadreController.list_madres()

@router.get("/{madre_id}")
async def get_madre(madre_id: str):
    return MadreController.get_madre(madre_id)

@router.post("/")
async def create_madre(madre: MadreBase):
    return MadreController.create_madre(madre)

@router.put("/{madre_id}")
async def update_madre(madre_id: str, madre_data: dict):
    return MadreController.update_madre(madre_id, madre_data)

@router.delete("/{madre_id}")
async def delete_madre(madre_id: str):
    return MadreController.delete_madre(madre_id)


# from fastapi import APIRouter
# from app.controllers import madre_controller
# from app.models.madre import Madre

# router = APIRouter(prefix="/madres", tags=["Madres"])

# @router.post("/")
# def create_madre(madre: Madre):
#     return madre_controller.create_madre(madre)

# @router.get("/")
# def get_madres():
#     return madre_controller.get_madres()

# @router.get("/{id}")
# def get_madre(id: str):
#     return madre_controller.get_madre(id)

# @router.put("/{id}")
# def update_madre(id: str, madre: Madre):
#     return madre_controller.update_madre(id, madre)

# @router.delete("/{id}")
# def delete_madre(id: str):
#     return madre_controller.delete_madre(id)
