#!/usr/bin/python3
"""fielstogare class"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        ky = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[ky] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        ser_obj = {}
        for k in FileStorage.__objects.keys():
            ser_obj[k] = FileStorage.__objects[k].to_dict()
        with open(FileStorage.__file_path, "w") as fl:
            json.dump(ser_obj, fl)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as fl:
                try:
                    ser_obj = json.load(fl)
                except Exception:
                    pass
