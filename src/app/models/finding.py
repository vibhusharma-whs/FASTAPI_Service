from typing import Optional
from enum import Enum

from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.models.core import IDModelMixin, CoreModel


class FindingBase(CoreModel):
    """
    All common characteristics of our Finding resource
    """
    finding_class_id = int
    application_id = int
    uri = str
    signature = str
    state = int
    create_time = TIMESTAMP
    update_time = TIMESTAMP


class FindingCreate(FindingBase):
    pass

class FindingInDB(IDModelMixin, FindingBase):
    finding_class_id = int
    application_id = int
    uri = str
    signature = str
    state = int
    create_time = TIMESTAMP
    update_time = TIMESTAMP


class FindingPublic(IDModelMixin, FindingBase):
    pass

