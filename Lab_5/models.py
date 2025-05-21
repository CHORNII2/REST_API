from pydantic import BaseModel, Field
from typing import Optional
from pydantic_mongo import ObjectIdField

class Book(BaseModel):
    id: Optional[str] = ObjectIdField(alias="_id")
    title: str
    author: str
    year: int

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectIdField: str
        }
