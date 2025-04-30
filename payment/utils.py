import logging

from datetime import datetime, timedelta
from core.settings import users_collection


def update_user_payment(user_id: int, amount: int):
    payment_date = datetime.now()

    if amount == 35000:
        payment_valid_date = payment_date + timedelta(days=30)
        payment_type = "monthly"
    elif amount == 12000:
        payment_valid_date = payment_date + timedelta(weeks=1)
        payment_type = "weekly"
    else:
        logging.error(f"Xato: {amount} so‘m to‘lov summasi noto‘g‘ri!")
        return

    filter_query = {"_id": user_id}
    update_data = {
        "$set": {
            "is_paid": True,
            "payment_date": payment_date,
            "payment_valid_date": payment_valid_date,
            "payment_type": payment_type
        }
    }

    result = users_collection.update_one(filter_query, update_data)

    if result.matched_count:
        logging.info(f"User {user_id}. To'lov muvaffaqiyatli amalga oshirildi. Summa: {amount}")
    else:
        logging.error(f"User {user_id} topilmadi.")


def update_not_finished_user_payment(user_id: int):
    filter_query = {"_id": user_id}
    update_data = {
        "$set": {
            "is_paid": False,
            "payment_date": None,
            "payment_valid_date": None,
            "payment_type": None
        }
    }

    result = users_collection.update_one(filter_query, update_data)

    if result.matched_count:
        logging.info(f"User {user_id}'ning to'lovi bekor qilindi.")
    else:
        logging.error(f"User {user_id} topilmadi.")
