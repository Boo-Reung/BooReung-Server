# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
# from django_apscheduler.jobstores import register_events, DjangoJobStore
# from .views import blockCarpool, deleteCompletedCarpool
# from django.conf import settings


# def start():
#     scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
#     register_events(scheduler)

#     scheduler.add_job(
#         blockCarpool,
#         trigger=CronTrigger(hour="0", minute="00"),
#         max_instances=1,
#         name="blockCarpool",
#     )
#     scheduler.add_job(
#         deleteCompletedCarpool,
#         trigger=CronTrigger(hour="0", minute="00"),
#         max_instances=1,
#         name="deleteCompletedCarpool",
#     )

#     scheduler.start()