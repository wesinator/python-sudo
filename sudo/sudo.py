#!/usr/bin/env python3
import subprocess


def run_as_sudo(sudo_user, command_str, shell=False, timeout=None):
    sudo_args = ["sudo", "-u", sudo_user]
    sudo_cmd_str = ' '.join(sudo_args)

    if shell:
        subprocess.run(sudo_cmd_str + " {}".format(command_str), shell=shell, timeout=timeout)
    else:
        subprocess.run(sudo_args + command_str.split(), shell=shell, timeout=timeout)
