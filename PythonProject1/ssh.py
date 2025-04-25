from netmiko import ConnectHandler

# Router connection details
router = {
    'device_type': 'cisco_ios',  # Use SSH for Cisco IOS
    'host': '192.168.127.66',    # Router's IP address
    'username': 'admin',         # Username configured on the router
    'password': 'cisco',         # Password for the user
    'secret': 'cisco',           # Enable mode password (if required)
}

try:
    # Establish SSH connection
    connection = ConnectHandler(**router)
    print("Connected to router via SSH")

    # Enter Privileged EXEC mode
    connection.enable()
    print("Entered Privileged EXEC mode")

    # Enter configuration mode
    connection.config_mode()
    print("Entered Config mode")

    # Change the enable password
    new_password = "newpass"
    connection.send_command(f"enable secret {new_password}")
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