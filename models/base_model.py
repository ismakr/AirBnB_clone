#!/usr/bin/python3
"""basemodel class"""
import uuid
from datetime import datetime
import time
import models


class BaseModel:
    """class Base"""

    def __init__(self, *args, **kwargs):
        """constructor"""
        time_f = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_f)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """return str"""
        return f"[{self.__class__.__name__}] ({self.id}) \
{self.__dict__}"

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict.update({"__class__": self.__class__.__name__})
        return obj_dict
