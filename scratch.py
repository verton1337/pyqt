from subprocess import call, Popen, PIPE
import platform
import chardet


COMMAND = 'cmd.exe' if platform.system().lower() == 'windows' else 'ls'

# мы не знаем в чем нужно декодировать
# но нам помогает модуль chardet
PROC = Popen(COMMAND)


