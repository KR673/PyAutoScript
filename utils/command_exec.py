import subprocess
from typing import Tuple


def execute(commands: list) -> Tuple[str, str]:
    """
    执行命令, 获取返回值
    :param commands:
    :return:
    """
    proc = subprocess.Popen(commands, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return str(out, 'ansi'), str(err, 'ansi') if err is not None else err
