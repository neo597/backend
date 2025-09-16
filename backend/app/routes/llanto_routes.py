from fastapi import APIRouter, UploadFile, File, Form
from app.controllers.llanto_controller import LlantoController
from app.models.llanto import LlantoBase

router = APIRouter(prefix="/llantos", tags=["Llantos"])

@router.get("/")
async def list_llantos():
    return LlantoController.list_llantos()

@router.get("/{llanto_id}")
async def get_llanto(llanto_id: str):
    return LlantoController.get_llanto(llanto_id)

@router.post("/")
async def create_llanto(llanto: LlantoBase):
    return LlantoController.create_llanto(llanto)

@router.delete("/{llanto_id}")
async def delete_llanto(llanto_id: str):
    return LlantoController.delete_llanto(llanto_id)

@router.post("/subir/")
async def subir_llanto(id_neonato: str = Form(...), archivo: UploadFile = File(...)):
    return LlantoController.subir_llanto(archivo, id_neonato)


# from fastapi import APIRouter, UploadFile, File, Form
# from app.controllers import llanto_controller
# from app.models.llanto import Llanto

# router = APIRouter(prefix="/llantos", tags=["Llantos"])

# @router.post("/")
# def create_llanto(
#     id: str = Form(...),
#     id_neonato: str = Form(...),
#     nombre_neonato: str = Form(None),
#     id_madre: str = Form(None),
#     audio: UploadFile = File(...)
# ):
#     llanto = Llanto(id=id, id_neonato=id_neonato, nombre_neonato=nombre_neonato, id_madre=id_madre)
#     return llanto_controller.create_llanto(llanto, audio)

# @router.get("/")
# def get_llantos():
#     return llanto_controller.get_llantos()

# @router.get("/{id}")
# def get_llanto(id: str):
#     return llanto_controller.get_llanto(id)

# @router.put("/{id}")
# def update_llanto(id: str, llanto: Llanto):
#     return llanto_controller.update_llanto(id, llanto)

# @router.delete("/{id}")
# def delete_llanto(id: str):
#     return llanto_controller.delete_llanto(id)
