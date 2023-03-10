from datetime import datetime
import sys


def log(templates, *arg):
    time_format = '%Y-%m-%d %H:%M:%S'
    template = '{} ' + templates
    now = datetime.now()
    msg = template.format(now.strftime(time_format), *arg)
    print(msg)
    with open(sys.path[0] + '\\logs\\{}-log.text'.format(now.strftime('%Y-%m-%d')), 'a', encoding='utf-8') as file:
        file.writelines(msg + '\n')
