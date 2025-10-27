from celery import shared_task

@shared_task
def send_welcome_email(user_id):
    # fetch user, send email logic
    print(f'email sent for {user_id}') 

