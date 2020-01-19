# python-sudo
Modular Python to execute any subprocess commands as another user (not necessarily superuser/root)

calling `sudo -u`

#### Usage:

This module does not take a user password for security and efficiency reasons (aiming for no user interaction to run).

Configure the sudoers file to allow running commands as another user (not necessarily the superuser):

##### [`sudo visudo`](https://serverfault.com/questions/883434/sudo-nopasswd-not-working-on-a-specific-command):
 - `parent_user ALL=(run_user) NOPASSWD: ALL`


```python
from sudo import run_as_sudo

# run `whoami` from user 'user'
cmd = "whoami"
sudo_user = "user"

run_as_sudo(sudo_user, cmd)

# optional shell, timeout (secs)
run_as_sudo(sudo_user, cmd, shell=True, timeout=20)
```
