from app.extensions import celery, mail
from flask import render_template
from flask_login import current_user
from flask_mail import Message
from app.models import User, Quote
import random
from datetime import datetime, timezone
from celery import shared_task


#Send quote task
@shared_task()
def send_quote_email(user_id):
    user : User = User.query.get(user_id)

    #Validation and auxiliary prints to read logs and debugging
    if not user:
        print("The user haven't been found")
        return

    if not user.daily_quote_enabled:
        print("Quotes sending is disabled")
        return

    quotes_count = Quote.query.count()

    if quotes_count == 0:
        print("No quotes in the database")
        return

    #Work of sending quotes from choosen specific group of quotes
    user_preferences = user.daily_quote_category

    if user_preferences == 'all':
        quotes_count = Quote.query.count()
        if quotes_count > 0:
            random_offset = random.randint(0, quotes_count - 1)
            quote = Quote.query.offset(random_offset).first()

    elif user_preferences == 'liked':
        liked = current_user.liked_quotes.all()
        if liked:
            quote = random.choice(liked)

    else:
        quotes_in_category = Quote.query.filter_by(category=user_preferences).all()
        if quotes_in_category:
            quote = random.choice(quotes_in_category)

    try:
        msg = Message(
            subject="Your Daily Quote",
            sender=celery.conf.get("MAIL_DEFAULT_SENDER"),
            recipients=[user.email]
        )

        msg.html = render_template('main/daily_quote.html', user=user, quote=quote)
        mail.send(msg)
        print(f"Quote has been sent to {user.email}")

    except Exception as e:
        print(f"Error during sending an email to {user.email}: {e}")


#Celery Beat task to check if it is time to send email to specific user
@shared_task()
def schedule_daily_quotes():
    print("schedule_daily_quotes is being worked")

    users = User.query.filter_by(daily_quote_enabled=True).all()

    now = datetime.now(timezone.utc).time()

    #Check all user with daily_quote_enabled True if it is time to send an e-mail
    for user in users:
        if user.daily_quote_time.hour == now.hour+2 and user.daily_quote_time.minute == now.minute:
            send_quote_email.delay(user.id)
            print(f"Sending email to {user.username} has been planned at {user.daily_quote_time}.")
        else:
            print(f"User {user.username} has set time at {user.daily_quote_time}, now is {now+2}.")

    print("Task schedule_daily_quotes has been finished")