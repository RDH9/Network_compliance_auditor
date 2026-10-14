
class FakeConnection:
    def __init__(self):
        self.commands = []

    def send_command(self, command):
        self.commands.append(command)
        return "SSH Enabled - version 2.0"

