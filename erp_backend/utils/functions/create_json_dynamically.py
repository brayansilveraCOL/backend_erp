import json
from collections import deque


def create_json_form(serializer, values):
    """
    this function received serializer Class and the array values in the order they are in the serializer
    so you can create the json and send it to the instance serializer
    :param serializer:
    :param values:
    :return: return String json
    """
    fields = serializer.get_fields()
    deque_convert = deque(fields)
    arr = []
    for element in deque_convert:
        arr.append(element)
    values_dictionary = dict(zip(arr, values))
    app_json = json.dumps(values_dictionary)
    return app_json
