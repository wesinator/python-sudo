# python-sudo
Simple function to run subprocess command as another user (calling `sudo -u`)

#### Usage:

This module does not take a user password for security and efficiency reasons (aiming for no user interaction to run).

Configure the sudoers file to allow running commands as another user (not necessarily the superuser):

##### `sudo visudo`:
 - `parent_user ALL=(run_user) NOPASSWD: ALL`

https://serverfault.com/questions/883434/sudo-nopasswd-not-working-on-a-specific-command


```python
from sudo import run_as_sudo

# run `whoami` from user 'user'
cmd = "whoami"
sudo_user = "user"

run_as_sudo(sudo_user, cmd)

# optional shell, timeout (secs)
run_as_sudo(sudo_user, cmd, shell=True, timeout=20)
```
