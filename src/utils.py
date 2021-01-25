import yaml

class Command:

    def __init__(self):
        self.data = yaml.load(open("./commands.yaml"))

    def find_command(self, command : str):

        for data in self.data.get("commands"):

            if command.strip() == data.get("command").get("code"):
                return data.get("command").get("exec")

        return None