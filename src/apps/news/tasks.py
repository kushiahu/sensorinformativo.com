from celery import shared_task


@shared_task
def publish_news():
	print('Publicando noticia programada')
