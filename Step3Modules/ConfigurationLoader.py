import sys
import json

class ConfigurationLoader:
    def __init__(self, filename = "configuration.txt"):
        #self.filename = filename
        f = open( filename )
        jsonData = f.read()
        self.config = json.loads(jsonData)

    def getPassword(self):
        return self.config.get("password")


cl = ConfigurationLoader()
print cl.getPassword()
