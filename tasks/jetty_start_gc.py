from utils.log import log
import utils.commands as commands


def run():
    pid = commands.get_java_pid('JettyStart')
    log('pid : {}', pid)

    if pid == 0:
        log('pid == 0')
        return
    memory_use = commands.get_memory_use(pid)
    log('memory_user: {}', memory_use)

    if memory_use <= 5 * 1024 * 1024:
        return

    commands.gc_pid(pid)
    log('execute gc')
