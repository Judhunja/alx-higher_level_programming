#!/usr/bin/python3
""" This module contains a class Base """
import json
import os.path
import csv


class Base:
    """ Initializes a class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON representation of list_objs to a
        file

        Args:
            list_objs: list of instances that inherits from Base
        """
        if not list_objs or list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"

        clean_objs = []
        for obj in list_objs:
            clean_objs.append(cls.to_dictionary(obj))

        json_str = cls.to_json_string(clean_objs)

        with open(filename, "w+", encoding="utf-8") as file:
            file.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string representation
        json_string
        """
        if not json_string or json_string == []:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        sets dummy values to dummy attributes
        """
        if cls.__name__ == "Rectangle":
            class_ins = cls(1, 1)
        if cls.__name__ == "Square":
            class_ins = cls(1)
        class_ins.update(**dictionary)
        return class_ins

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        variables = ["id", "width", "height", "x", "y"]

        if len(args) == 5:
            for j, arg in enumerate(args):
                setattr(self, variables[j], arg)
        else:
            for j, arg in enumerate(args):
                if j == 0:
                    self.id = arg
                elif j == 1:
                    self.width = arg
                    self.height = arg
                elif j == 2:
                    self.x = arg
                elif j == 3:
                    self.y = arg

        if not args:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances whose type depends on
        the current class(cls)
        """
        list_instances = []
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return list_instances

        json_dicts = []
        with open(filename, 'r', encoding="utf-8") as json_file:
            json_dicts = json_file.read()

        python_dicts = cls.from_json_string(json_dicts)

        for d in python_dicts:
            instance = cls.create(**d)
            list_instances.append(instance)

        return list_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV """
        filename = f"{cls.__name__}.csv"

        if not list_objs or list_objs is None:
            list_objs = []

        dict_objs = []

        for obj in list_objs:
            dict_objs.append(cls.to_dictionary(obj))

        with open(filename, "w+", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(dict_objs)

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV """

        filename = f"{cls.__name__}.csv"

        loaded_objs = []

        if not os.path.exists(filename):
            return loaded_objs

        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for obj in reader:
                loaded_objs.append(obj)

        return loaded_objs
