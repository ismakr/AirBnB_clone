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
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, time_f))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
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
        self.created_at = str(self.created_at.isoformat())
        self.updated_at = str(self.updated_at.isoformat())
        self.__dict__.update({"__class__": self.__class__.__name__})
        return self.__dict__
