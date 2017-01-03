from celery import Task

# django-haystack indexing automatically
from haystack.management.commands import update_index


class UpdateIndexTask(Task):

    def run(self):
        update_index.Command().handle()
