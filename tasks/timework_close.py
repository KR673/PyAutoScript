from utils.log import log
import utils.commands as commands


def run():
    pid = commands.get_java_pid('Bootstrap')
    log('pid : {}', pid)

    if pid == 0:
        log('未找到指定程序')
        return

    (out, err) = commands.kill_pid(pid)
    log('kill pid. [pid={}]', pid)
