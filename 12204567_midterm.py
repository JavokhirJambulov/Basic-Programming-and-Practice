# 12204567 Javokhir Jambulov
# Importing library for User Interface
import tkinter as tk

# Create a dictionary to store devices
network_devices = {}


# Function to set IP address
def set_ip_address(device_name, ip_address):
    if device_name in network_devices and 'IP Address' in network_devices[device_name]:
        info_text.insert(tk.END,
                         f"{device_name} already has an IP address assigned: {network_devices[device_name]['IP Address']}\n")
    else:
        # Check if the IP address is already assigned to another device
        if any('IP Address' in data and data['IP Address'] == ip_address for data in network_devices.values()):
            info_text.insert(tk.END, f"The IP address {ip_address} is already assigned to another device.\n")
        else:
            network_devices[device_name] = {'IP Address': ip_address}
            info_text.insert(tk.END, f"Assigned IP address {ip_address} successfully to {device_name}\n")
            save_data_to_file()


# Function to set MAC address
def set_mac_address(device_name, mac_address):
    if device_name in network_devices and 'MAC Address' in network_devices[device_name]:
        info_text.insert(tk.END,
                         f"{device_name} already has a MAC address assigned: {network_devices[device_name]['MAC Address']}\n")
    else:
        # Check if the Mac address is already assigned to another device
        if any('MAC Address' in data and data['MAC Address'] == mac_address for data in network_devices.values()):
            info_text.insert(tk.END, f"The MAC address {mac_address} is already assigned to another device.\n")
        else:
            network_devices[device_name]['MAC Address'] = mac_address
            info_text.insert(tk.END, f"Assigned MAC address {mac_address} successfully to {device_name}\n")
            save_data_to_file()


# Function to save data to a text file
def save_data_to_file():
    with open("network_data.txt", "w") as file:
        for device, data in network_devices.items():
            file.write(f"{device} - {data}\n")


# Function to load data from a text file
def load_data_from_file():
    try:
        with open("network_data.txt", "r") as file:
            for line in file:
                device, data = line.strip().split(" - ")
                network_devices[device] = eval(data)
    except FileNotFoundError:
        pass


# Function to delete a device
def delete_device(device_name):
    if device_name in network_devices:
        del network_devices[device_name]
        info_text.insert(tk.END, f"Device {device_name} has been deleted.\n")
        save_data_to_file()
    else:
        info_text.insert(tk.END, f"Device {device_name} not found in the network.\n")


# Function to display device information
def display_device_info():
    info_text.delete(1.0, tk.END)  # Clear previous information
    for device, data in network_devices.items():
        info_text.insert(tk.END, f"{device} - {data}\n")


# Function to handle the login
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Replace these values with your actual username and password
    actual_username = "Jack"
    actual_password = "123"

    if entered_username == actual_username and entered_password == actual_password:
        # Successful login, open the main application window
        login_window.destroy()
        open_main_window()
    else:
        login_status_label.config(text="Invalid username or password")


# Function to open the main application window
def open_main_window():
    # Create the main root window
    root = tk.Tk()
    root.title("Network Management System")
    root.geometry("680x610")

    # Create and arrange UI elements
    device_label = tk.Label(root, text="Device Name:")
    device_label.grid(row=0, column=0, padx=10, pady=5)

    device_entry = tk.Entry(root)
    device_entry.grid(row=0, column=1, padx=10, pady=5)

    ip_label = tk.Label(root, text="IP Address:")
    ip_label.grid(row=1, column=0, padx=10, pady=5)

    ip_entry = tk.Entry(root)
    ip_entry.grid(row=1, column=1, padx=10, pady=5)

    mac_label = tk.Label(root, text="MAC Address:")
    mac_label.grid(row=2, column=0, padx=10, pady=5)

    mac_entry = tk.Entry(root)
    mac_entry.grid(row=2, column=1, padx=10, pady=5)

    set_ip_button = tk.Button(root, text="Set IP Address",
                              command=lambda: set_ip_address(device_entry.get(), ip_entry.get()))
    set_ip_button.grid(row=3, column=0, padx=10, pady=5)

    set_mac_button = tk.Button(root, text="Set MAC Address",
                               command=lambda: set_mac_address(device_entry.get(), mac_entry.get()))
    set_mac_button.grid(row=3, column=1, padx=10, pady=5)

    delete_entry = tk.Entry(root)
    delete_entry.grid(row=4, column=0, padx=10, pady=5)

    delete_button = tk.Button(root, text="Delete Device", command=lambda: delete_device(delete_entry.get()))
    delete_button.grid(row=4, column=1, padx=10, pady=5)

    global info_text  # Declare info_text as a global variable
    info_text = tk.Text(root)
    info_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    display_button = tk.Button(root, text="Display Device Info", command=display_device_info)
    display_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

    root.mainloop()


# Create the login window
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("400x400")

username_label = tk.Label(login_window, text="Username:")
username_label.pack(pady=10)

username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack(pady=10)

password_entry = tk.Entry(login_window, show="*")  # Show asterisks for password
password_entry.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack(pady=10)

login_status_label = tk.Label(login_window, text="")
login_status_label.pack(pady=10)

# Load data from the text file on application start
load_data_from_file()

# Open the login window
login_window.mainloop()
