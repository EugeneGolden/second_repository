import sys
import json

class ConfigurationLoader:
    def __init__(self, filename = "configuration.txt"):
        f = open( filename )
        jsonData = f.read()
        self.config = json.loads(jsonData)

    def getPassword(self):
        return self.config.get("password")

filename = "configuration.txt"
cl = ConfigurationLoader( filename )
print cl.getPassword()
