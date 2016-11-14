"""
Created on Sep 6, 2016

@author: author name
"""
from program.utils import util1
from program.data_types import data_type1


class Program(object):
    """
    Class description
    """

    def __init__(self, attribute1=None):
        """
        Constructor
        """
        self.__attribute1 = attribute1
        self.__util = util1.Util1()
        self.__data_type1 = data_type1.DataType1()

    def get_attribute1(self):
        """
        Method description goes here.

        :return: description of what the method returns goes here.
        """
        return self.__attribute1

    def set_attribute1(self, new_attribute1):
        """
        Method description goes here.

        :param new_attribute1: description of parameter goes here.
        :return: description of what the method returns goes here.
        """
        self.__attribute1 = new_attribute1
