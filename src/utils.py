import yaml


class Command:
    def __init__(self):
        self.data = yaml.load(open("./commands.yaml"))

    def find_command(self, command: str):

        print("command")
        print("command")
        print(command)

        for data in self.data.get("commands"):

            if command.strip().lower() == data.get("command").get("code").strip().lower():
                return data.get("command").get("exec")

        return None