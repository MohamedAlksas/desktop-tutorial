from netmiko import ConnectHandler

# Router connection details
router = {
    'device_type': 'cisco_ios_telnet',  # Use Telnet
    'host': '192.168.127.66',
    'username': 'cisco',               # Username (modify if different)
    'password': 'cisco',               # Login password
    'secret': 'cisco',                 # Enable mode password
}

try:
    # Establish connection
    connection = ConnectHandler(**router)
    print("Connected to router via Telnet")

    # Enter Privileged mode
    connection.enable()
    print("Entered Privileged EXEC mode")

    # Enter configuration mode
    connection.config_mode()
    print("Entered Config mode")

    # Change the enable password
    new_password = "newpass"
    connection.send_command(f"enable password {new_password}")
    print(f"Changed enable password to {new_password}")

    # Exit configuration mode
    connection.exit_config_mode()
    print("Exited Config mode")

    # Save the configuration
    output = connection.send_command("write memory")
    print("Configuration saved:")
    print(output)

    # Close the connection
    connection.disconnect()
    print("Connection closed")

except Exception as e:
    print(f"An error occurred: {e}")