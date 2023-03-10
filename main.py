"""
Demonstrates how to schedule a job to be run in a process pool on 3 second intervals.
"""

from apscheduler.schedulers.blocking import BlockingScheduler
from tasks import timework_close
from tasks import jetty_start_gc

if __name__ == '__main__':
    """
    自动化执行任务
    * [cron使用](https://apscheduler.readthedocs.io/en/3.x/modules/triggers/cron.html)
    """
    scheduler = BlockingScheduler()
    scheduler.add_job(timework_close.run, 'cron', hour='19')
    scheduler.add_job(jetty_start_gc.run, 'cron', minute='*/10')
    scheduler.start()
