from utils.command_exec import execute
import re


def get_java_pid(process_name):
    # 执行jps命今, 获取其返回值
    (out, err) = execute(['jps'])
    content_list = out.split('\r\n')
    if (len(content_list)) <= 0:
        exit()

    # 获取名称为[process_name]的进程ID
    for content_line in content_list:
        pattern = r'(\w+)\s+' + process_name
        matcher = re.match(pattern, content_line)
        if matcher:
            pid = re.match(pattern, content_line).group(1)
            if int(pid) > 0:
                return pid
    return 0


def get_memory_use(pid):
    (out, err) = execute(["tasklist", '|', 'findstr', pid])
    content_list = out.split('\r\n')
    if (len(content_list)) <= 0:
        exit()
    content = content_list[0].split(' ')
    return int(content[-2].replace(',', ''))


def gc_pid(pid):
    # 执行jps命今, 获取其返回值
    return execute(['jcmd', pid, 'GC.run'])

def kill_pid(pid):
    return execute(['taskkill', '/f', '/pid', pid])