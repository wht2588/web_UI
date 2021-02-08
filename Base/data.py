import json
import os


class Data:

    @classmethod
    def get_json_data(cls, name):
        """
        解析json文件
        :param name: 文件名字 json文件必须在Data目录下
        :return:
        """
        with open("./Data" + os.sep + name, "r", encoding="utf-8") as f:
            return json.load(f)
