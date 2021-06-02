import os
from time import sleep


login = os.path.isfile('/root/.login/login')

if not login:
    os.mkdir('/root/.login')
    os.mkdir('/root/.login/backup')
    os.system('cp /root/.bashrc /root/.login/backup/')
    os.system('cp /etc/profile.d/termux-proot.sh /root/.login/backup/')
    if not os.path.isfile('/root/.login/login.py'):
        with open('/root/.login/login.py', 'w') as a:
            a.write('''import os

os.system('clear')
if os.path.isfile('/root/.login/active.txt'):
    os.remove('/root/.login/active.txt')
    os.system('sudo login')
else:
    pass''')
    with open('/root/.bashrc', 'a') as a:
        a.write('\n# Login pass\nif [ -f ~/.login/pass.py ]; then\n    python3 /root/.login/pass.py\nfi')
    if not os.path.isfile('/root/.login/pass.py'):
        with open('/root/.login/pass.py', 'w') as a:
            a.write('''import os

if not os.path.isfile('/root/.login/active.txt'):
    with open('/root/.login/active.txt', 'w') as a:
        a.write("Enabled")''')
    with open('/etc/profile.d/termux-proot.sh', 'a') as a:
        a.write('\n# Login\nif [ -f /root/.login/active.txt ]; then\n    python3 /root/.login/login.py\nfi')
    os.system('passwd')
    with open('/root/.login/login', 'w') as a:
        a.write('1')
    with open('/root/.login/active.txt', 'w') as a:
        a.write('Enabled\n')
    print('\033[32mLogin enabled!\033[m')
else:
    print('\033[33mLogin is already activated!')
    disable = input('Do you want to disable login? [Y/n]\033[m ').strip().upper()
    if disable == 'Y':
        os.system('mv /root/.login/backup/.bashrc /root/.bashrc')
        os.system('mv /root/.login/backup/termux-proot.sh /etc/profile.d/termux-proot.sh')
        os.system('rm -rd .login')
        print('\033[32mLogin disabled!\033[m')
    elif disable == 'N':
        print('\033[33mExiting...\033[m')
        sleep(2)
    else:
        print('\033[31mInvalid option!\033[m')
        print('\033[33mExiting...\033[m')
        sleep(2)
