"""
| Created: 2016-09-06
| Updated: 2016-11-25
"""


class DataType1(object):
    """
    Class description
    """

    def __init__(self, attribute1=None):
        """
        Constructor
        """
        self.__attribute1 = attribute1

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
