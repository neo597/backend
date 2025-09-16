from app.core.firebase_config import db
from app.models.madre import MadreBase

class MadreController:

    @staticmethod
    def list_madres():
        docs = db.collection("madres").stream()
        return [doc.to_dict() for doc in docs]

    @staticmethod
    def get_madre(madre_id: str):
        doc = db.collection("madres").document(madre_id).get()
        if doc.exists:
            return doc.to_dict()
        return {"error": "Madre no encontrada"}

    @staticmethod
    def create_madre(madre: MadreBase):
        data = madre.dict()
        db.collection("madres").document(madre.id_madre).set(data)
        return {"message": "Madre registrada", "data": data}

    @staticmethod
    def update_madre(madre_id: str, madre_data: dict):
        ref = db.collection("madres").document(madre_id)
        ref.update(madre_data)
        return {"message": "Madre actualizada"}

    @staticmethod
    def delete_madre(madre_id: str):
        db.collection("madres").document(madre_id).delete()
        return {"message": "Madre eliminada"}


# from fastapi import HTTPException
# from firebase import db
# from app.models.madre import Madre

# collection = db.collection("madres")

# def create_madre(madre: Madre):
#     doc_ref = collection.document(madre.id)
#     if doc_ref.get().exists:
#         raise HTTPException(status_code=400, detail="Madre ya existe")
#     doc_ref.set(madre.dict())
#     return madre

# def get_madres():
#     docs = collection.stream()
#     return [doc.to_dict() for doc in docs]

# def get_madre(id: str):
#     doc = collection.document(id).get()
#     if not doc.exists:
#         raise HTTPException(status_code=404, detail="Madre no encontrada")
#     return doc.to_dict()

# def update_madre(id: str, madre: Madre):
#     doc_ref = collection.document(id)
#     if not doc_ref.get().exists:
#         raise HTTPException(status_code=404, detail="Madre no encontrada")
#     doc_ref.update(madre.dict())
#     return madre

# def delete_madre(id: str):
#     doc_ref = collection.document(id)
#     if not doc_ref.get().exists:
#         raise HTTPException(status_code=404, detail="Madre no encontrada")
#     doc_ref.delete()
#     return {"msg": "Madre eliminada"}
