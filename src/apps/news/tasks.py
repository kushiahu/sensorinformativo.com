from celery import shared_task


@shared_task
def publish_news():
	return 2 + 2
