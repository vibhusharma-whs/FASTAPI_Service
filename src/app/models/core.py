from sqlalchemy.sql.sqltypes import TIMESTAMP
from pydantic import BaseModel


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here.
    """


class IDModelMixin(BaseModel):
    id: int
