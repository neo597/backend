from fastapi import APIRouter
from app.controllers.neonato_controller import NeonatoController
from app.models.neonato import NeonatoBase

router = APIRouter(prefix="/neonatos", tags=["Neonatos"])

@router.get("/")
async def list_neonatos():
    return NeonatoController.list_neonatos()

@router.get("/{neonato_id}")
async def get_neonato(neonato_id: str):
    return NeonatoController.get_neonato(neonato_id)

@router.post("/")
async def create_neonato(neonato: NeonatoBase):
    return NeonatoController.create_neonato(neonato)

@router.put("/{neonato_id}")
async def update_neonato(neonato_id: str, neonato_data: dict):
    return NeonatoController.update_neonato(neonato_id, neonato_data)

@router.delete("/{neonato_id}")
async def delete_neonato(neonato_id: str):
    return NeonatoController.delete_neonato(neonato_id)


# from fastapi import APIRouter
# from app.controllers import neonato_controller
# from app.models.neonato import Neonato

# router = APIRouter(prefix="/neonatos", tags=["Neonatos"])

# @router.post("/")
# def create_neonato(neonato: Neonato):
#     return neonato_controller.create_neonato(neonato)

# @router.get("/")
# def get_neonatos():
#     return neonato_controller.get_neonatos()

# @router.get("/{id}")
# def get_neonato(id: str):
#     return neonato_controller.get_neonato(id)

# @router.put("/{id}")
# def update_neonato(id: str, neonato: Neonato):
#     return neonato_controller.update_neonato(id, neonato)

# @router.delete("/{id}")
# def delete_neonato(id: str):
#     return neonato_controller.delete_neonato(id)
