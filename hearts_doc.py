'''
example_doc = {
    "title" : "A Midsummer Night's Dream",
    "creation_timestamp" : 123456789,
    "data" : [
        {
            "indentation" : 0,
            "content" : "The heart is the strongest muscle!",
            "hearts" : 3
        },
        {
            "indentation" : 1,
            "content" : "first",
            "hearts" : 0
        }
    ]
}
'''
from datetime import datetime
import json

class Line(object):
    def __init__(self, message="", hearts=0, indentation=0, color="black", size="12px"):
        self.message = message
        self.hearts = hearts
        self.indentation = indentation
        self.color = color
        self.size = size

    def to_dict(self):
        return {
            "message" : self.message,
            "hearts" : self.hearts,
            "indentation" : self.indentation,
            "color" : self.color,
            "size" : self.size
        }

    def to_json(self):
        return json.dumps(self.to_dict())


class HeartsDoc(object):
    def __init__(self, title="Untitled", lines=None):
        self.creation_time = datetime.now()
        self.id = hash("{}{}".format(title, self.creation_time))
        self.title = "Untitled"
        if lines:
            self.lines = lines
        else:
            lines = []

    def add_line(self, line, index):
        self.lines.insert(line, index)

    def add_heart(self, index):
        self.lines[index].hearts += 1

    def remove_heart(self, index):
        self.lines[index].hearts -= 1

    def change_line(self, line, index):
        self.lines[index] = line

    def timestamp(self):
        return self.creation_time.strftime("%Y/%m/%d %H:%M:%S")

    def to_dict(self):
        return {
            "title" : self.title,
            "timestamp" : self.timestamp(),
            "lines" : self.lines
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    def save(filename):
        pass