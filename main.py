#Developed By Mr.Aryan
#My Telegram ID: @IPvenom
#My Github: https://github.com/VenomScriptss/
#Code version 1

import os
import time
import subprocess


# Tool:
def check_status():
    expected_settings = {
        "net.ipv4.tcp_fin_timeout": "30",
        "net.ipv4.tcp_window_scaling": "1",
        "net.core.rmem_default": "65536",
        "net.core.wmem_default": "65536",
        "net.core.rmem_max": "16777216",
        "net.core.wmem_max": "16777216",
        "net.ipv4.tcp_ecn": "1",
        "net.ipv4.tcp_frto": "2",
        "net.ipv4.tcp_sack": "1",
        "net.ipv4.tcp_congestion_control": "bbr",
    }
    for setting, value in expected_settings.items():
        try:
            result = os.popen(f"sysctl -n {setting}").read().strip()
            if result != value:
                return False
        except:
            return False
    return True



def os_full(ex: bool = False):
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release") as os_release:
            lines = os_release.readlines()
            for line in lines:
                if line.startswith("PRETTY_NAME="):
                    return line.split('=')[1].strip()
    if ex:
        error("Not Supported OS, Please Change To Ubuntu 16+ And Try Again")
    else:
        return None


def os_ver(ex: bool = False):
    of = os_full(ex)
    if of:
        main_ver = of.split()[0]
        return main_ver.split('.')[0]
    else:
        return None


def check_os(ex: bool = False):
    if os.path.exists("/etc/debian_version"):
        with open("/etc/os-release") as os_release:
            lines = os_release.readlines()
            for line in lines:
                if line.startswith("ID="):
                    ov = os_ver(ex)
                    if ov:
                        if not line.split('=')[1].strip() == "ubuntu" and int(ov) < 16:
                            if ex:
                                error("Not Supported OS, Please Change To Ubuntu 16+ And Try Again")
                            else:
                                return False
                        else:
                            if not ex:
                                return True
                    else:
                        return False
    else:
        if ex:
            error("Not Supported OS, Please Change To Ubuntu 16+ And Try Again")
        else:
            return False

def enable_service():
    subprocess.getoutput("sysctl -w net.ipv4.tcp_fin_timeout=30")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_window_scaling=1")
    subprocess.getoutput("sysctl -w net.core.rmem_default=65536")
    subprocess.getoutput("sysctl -w net.core.wmem_default=65536")
    subprocess.getoutput("sysctl -w net.core.rmem_max=16777216")
    subprocess.getoutput("sysctl -w net.core.wmem_max=16777216")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_ecn=1")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_frto=2")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_sack=1")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_congestion_control=bbr")
    subprocess.getoutput("sysctl -p")


def disable_service():
    subprocess.getoutput("sysctl -w net.ipv4.tcp_fin_timeout=60")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_window_scaling=0")
    subprocess.getoutput("sysctl -w net.core.rmem_default=4096")
    subprocess.getoutput("sysctl -w net.core.wmem_default=4096")
    subprocess.getoutput("sysctl -w net.core.rmem_max=131071")
    subprocess.getoutput("sysctl -w net.core.wmem_max=131071")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_ecn=2")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_frto=0")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_sack=0")
    subprocess.getoutput("sysctl -w net.ipv4.tcp_congestion_control=cubic")
    subprocess.getoutput("sysctl -p")


# Design:
def clear():
    os.system("clear")


def red(text):
    return f'\033[1;31;31m{text}\033[0m'


def green(text):
    return f'\033[1;31;32m{text}\033[0m'


def blue(text):
    return f'\033[1;34;49m{text}\033[0m'


def yellow(text):
    return f'\033[1;33m{text}\033[0m'


def info(msg):
    return f'{blue("[")}{green("INFO")}{blue("]")} {yellow(msg)}.'


def error(msg):
    print(f'\n\n{blue("[")}{red("ERROR")}{blue("]")} {yellow(msg)}.')
    exit(1)


def title(sleep: bool = True):
    text = f"""
{green("████████╗░░░░░░███████╗░█████╗░░██████╗████████╗")}
{green("╚══██╔══╝░░░░░░██╔════╝██╔══██╗██╔════╝╚══██╔══╝")}
░░░██║░░░█████╗█████╗░░███████║╚█████╗░░░░██║░░░
░░░██║░░░╚════╝██╔══╝░░██╔══██║░╚═══██╗░░░██║░░░
{red("░░░██║░░░░░░░░░██║░░░░░██║░░██║██████╔╝░░░██║░░░")}
{red("░░░╚═╝░░░░░░░░░╚═╝░░░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░")}

    {green("|")} {blue("Telegram (PV)")}: {yellow("@IPvenom")}
    {green("|")} {blue("Telegram (Chanel)")}: {yellow("@VenomScript")}
    {green("|")} {blue("GitHup")}: {yellow("https://github.com/VenomScriptss")}
+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+
"""
    if sleep:
        for word in text:
            print(word, end="", flush=True)
            time.sleep(0.003)
    else:
        print(text)


def main_page(sleep: bool = True):
    status = check_status()
    txt1 = green("Enable") if status else red("Disable")
    txt2 = "Reactivate" if status else "Activate"
    txt3 = "." if status else "Again."
    text = f"""
{info(f"T-Fast Is {txt1}")}
{blue(">")} {green("1-")} {yellow(f"{txt2} T-Fast.")}
{blue(">")} {green("2-")} {yellow(f"Disable T-Fast {txt3}")}

{blue("[")}{green("?")}{blue("]")} {yellow("Please Enter One Between 1 And 2: ")}"""
    if sleep:
        for word in text:
            print(word, end="", flush=True)
            time.sleep(0.001)
    else:
        print(text)


def enable_service_text(sleep: bool = True):
    text = f"""\n\n{info(f'T-Fast Is {green("Enabled")}')}\n\n"""
    if sleep:
        for word in text:
            print(word, end="", flush=True)
            time.sleep(0.001)
    else:
        print(text)


def disable_service_text(sleep: bool = True):
    text = f"""\n\n{info(f'T-Fast Is {red("Disabled")}')}\n\n"""
    if sleep:
        for word in text:
            print(word, end="", flush=True)
            time.sleep(0.001)
    else:
        print(text)


clear()
title(check_os())
check_os(True)
main_page()
try:
    num = int(input())
except:
    error("Please Enter The Correct Number [1-2]")
if num == 1:
    enable_service()
    enable_service_text()
elif num == 2:
    disable_service()
    disable_service_text()
else:
    error("Please Enter The Correct Number [1-2]")


#Developed By Mr.Aryan
#My Telegram ID: @IPvenom
#My Github: https://github.com/VenomScriptss/
#Code version 1
