from app.device_connection import execute_command
from fake_connection import FakeConnection

def test_execute_command_returns_output():
    fake_connection = FakeConnection() 
    output = execute_command(fake_connection, "show ip ssh")
    assert output == "SSH Enabled - version 2.0"
    assert fake_connection.commands == ["show ip ssh"]

