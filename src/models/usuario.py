
from pydantic import BaseModel, Field
from datetime import datetime

class usuario:
    actor_id: int
    nombre: str | Field(min_length=50, max_length=50)
    apellido: str | Field(min_length=50, max_length=50)
    fechaDeNacimiento: datetime
    sexo: str | Field(max_length=1)