from app.core.firebase_config import db
from app.models.neonato import NeonatoBase
from datetime import date, time, datetime

class NeonatoController:

    @staticmethod
    def _serialize(data: dict) -> dict:
        """
        Convierte campos date/time a string antes de guardar en Firestore.
        """
        for key, value in data.items():
            if isinstance(value, (date, time, datetime)):
                data[key] = value.isoformat()
        return data

    @staticmethod
    def list_neonatos():
        docs = db.collection("neonatos").stream()
        return [doc.to_dict() for doc in docs]

    @staticmethod
    def get_neonato(neonato_id: str):
        doc = db.collection("neonatos").document(neonato_id).get()
        if doc.exists:
            return doc.to_dict()
        return {"error": "Neonato no encontrado"}

    @staticmethod
    def create_neonato(neonato: NeonatoBase):
        data = NeonatoController._serialize(neonato.dict())
        db.collection("neonatos").document(neonato.id_neonato).set(data)
        return {"message": "Neonato registrado", "data": data}

    @staticmethod
    def update_neonato(neonato_id: str, neonato_data: dict):
        data = NeonatoController._serialize(neonato_data)
        ref = db.collection("neonatos").document(neonato_id)
        ref.update(data)
        return {"message": "Neonato actualizado", "data": data}

    @staticmethod
    def delete_neonato(neonato_id: str):
        db.collection("neonatos").document(neonato_id).delete()
        return {"message": "Neonato eliminado"}



# from fastapi import HTTPException
# from firebase import db
# from app.models.neonato import Neonato

# collection = db.collection("neonatos")

# def create_neonato(neonato: Neonato):
#     doc_ref = collection.document(neonato.id)
#     if doc_ref.get().exists:
#         raise HTTPException(status_code=400, detail="Neonato ya existe")
#     doc_ref.set(neonato.dict())
#     return neonato

# def get_neonatos():
#     docs = collection.stream()
#     return [doc.to_dict() for doc in docs]

# def get_neonato(id: str):
#     doc = collection.document(id).get()
#     if not doc.exists:
#         raise HTTPException(status_code=404, detail="Neonato no encontrado")
#     return doc.to_dict()

# def update_neonato(id: str, neonato: Neonato):
#     doc_ref = collection.document(id)
#     if not doc_ref.get().exists:
#         raise HTTPException(status_code=404, detail="Neonato no encontrado")
#     doc_ref.update(neonato.dict())
#     return neonato

# def delete_neonato(id: str):
#     doc_ref = collection.document(id)
#     if not doc_ref.get().exists:
#         raise HTTPException(status_code=404, detail="Neonato no encontrado")
#     doc_ref.delete()
#     return {"msg": "Neonato eliminado"}
