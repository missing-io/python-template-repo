import os
import socket


def get_os_info():
    hostname = os.uname()[1]
    application_name = os.getenv("ENV_VAR_2", "python-template")
    os_info = {"Hostname": hostname, "Application_Name": application_name}

    return os_info
