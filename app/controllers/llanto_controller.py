from app.core.firebase_config import db, bucket
from app.models.llanto import LlantoBase
from datetime import datetime
import uuid

class LlantoController:

    @staticmethod
    def list_llantos():
        docs = db.collection("llantos").stream()
        return [doc.to_dict() for doc in docs]

    @staticmethod
    def get_llanto(llanto_id: str):
        doc = db.collection("llantos").document(llanto_id).get()
        if doc.exists:
            return doc.to_dict()
        return {"error": "Llanto no encontrado"}

    @staticmethod
    def create_llanto(llanto: LlantoBase):
        data = llanto.dict()
        llanto_id = str(uuid.uuid4())
        data["id_llanto"] = llanto_id
        db.collection("llantos").document(llanto_id).set(data)
        return {"message": "Llanto registrado", "data": data}

    @staticmethod
    def delete_llanto(llanto_id: str):
        db.collection("llantos").document(llanto_id).delete()
        return {"message": "Llanto eliminado"}

    @staticmethod
    def subir_llanto(file, id_neonato: str):
        # Subir a Firebase Storage
        filename = f"llantos/{uuid.uuid4()}_{file.filename}"
        blob = bucket.blob(filename)
        blob.upload_from_file(file.file, content_type=file.content_type)

        url_audio = blob.generate_signed_url(datetime.timedelta(days=365))

        nuevo_llanto = {
            "id_llanto": str(uuid.uuid4()),
            "id_neonato": id_neonato,
            "archivo_url": url_audio,
            "fecha": datetime.now().isoformat()
        }

        db.collection("llantos").document(nuevo_llanto["id_llanto"]).set(nuevo_llanto)
        return {"message": "Llanto subido correctamente", "url": url_audio}



# import uuid
# from fastapi import HTTPException, UploadFile
# from firebase import db, bucket
# from app.models.llanto import Llanto

# collection = db.collection("llantos")

# def create_llanto(llanto: Llanto, audio: UploadFile):
#     # Subir audio a Firebase Storage
#     file_id = str(uuid.uuid4())
#     blob = bucket.blob(f"audios/{file_id}.mp3")
#     blob.upload_from_file(audio.file, content_type="audio/mpeg")
#     audio_url = blob.public_url

#     data = llanto.dict()
#     data["audio_url"] = audio_url

#     doc_ref = collection.document(llanto.id)
#     if doc_ref.get().exists:
#         raise HTTPException(status_code=400, detail="Llanto ya existe")
#     doc_ref.set(data)
#     return data

# def get_llantos():
#     docs = collection.stream()
#     return [doc.to_dict() for doc in docs]

# def get_llanto(id: str):
#     doc = collection.document(id).get()
#     if not doc.exists:
#         raise HTTPException(status_code=404, detail="Llanto no encontrado")
#     return doc.to_dict()

# def update_llanto(id: str, llanto: Llanto):
#     doc_ref = collection.document(id)
#     if not doc_ref.get().exists:
#         raise HTTPException(status_code=404, detail="Llanto no encontrado")
#     doc_ref.update(llanto.dict())
#     return llanto

# def delete_llanto(id: str):
#     doc_ref = collection.document(id)
#     if not doc_ref.get().exists:
#         raise HTTPException(status_code=404, detail="Llanto no encontrado")
#     doc_ref.delete()
#     return {"msg": "Llanto eliminado"}
