import logging

from decimal import Decimal, ROUND_DOWN
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from payme import Payme
from payme.views import PaymeWebHookAPIView
from payme.models import PaymeTransactions

from payment.models import Order
from core.settings import SITE_URL, PAYME_ID
from payment.utils import update_user_payment, update_not_finished_user_payment


class PaymeCallBackAPIView(PaymeWebHookAPIView):

    def handle_successfully_payment(self, params, result, *args, **kwargs):
        """
        Handle the successful payment. You can override this method
        """
        logging.info(f"Successfully payment: {params}")
        try:
            transactions = PaymeTransactions.get_by_transaction_id(
                transaction_id=params["id"]
            )

            order = Order.objects.get(id=transactions.account_id)  # noqa
            order.is_finished = True
            order.save()

            update_user_payment(order.user_id, order.total)

        except Exception as e:
            logging.error(f"handle_successfully_payment error: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def handle_cancelled_payment(self, params, result, *args, **kwargs):
        """
        Handle the cancelled payment. You can override this method
        """
        logging.info(f"Cancelled payment: {params}")

        try:
            transactions = PaymeTransactions.get_by_transaction_id(
                transaction_id=params["id"]
            )

            if transactions.state == PaymeTransactions.CANCELED:
                order = Order.objects.get(id=transactions.account_id)  # noqa
                order.is_finished = False
                order.save()

                update_not_finished_user_payment(order.user_id)

        except Exception as e:
            logging.error(f"handle_cancelled_payment error: {e}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PaymeInitializationView(APIView):
    @extend_schema(
        summary="Payme orqali to‘lovni boshlash",
        description="Foydalanuvchiga Payme orqali to‘lov qilish uchun URL qaytaradi.",
        request={
            "application/json": {
                "type": "object",
                "properties": {
                    "user_id": {"type": "integer", "example": 12345},
                    "amount": {"type": "number", "example": 45000},
                    "payment_method": {"type": "string", "example": "payme"},
                },
                "required": ["user_id", "amount"],
            }
        },
        responses={
            200: {
                "type": "object",
                "properties": {
                    "payment_url": {"type": "string", "example": "https://checkout.Payme.uz/..."}
                },
            },
            400: {"description": "Xato: user_id yoki amount noto‘g‘ri"},
        },
    )
    def post(self, request):
        user_id = request.data.get("user_id")
        amount = request.data.get("amount")
        payment_method = request.data.get("payment_method")

        if not isinstance(user_id, int) or not isinstance(amount, (int, float, str)):
            return Response({"error": "user_id butun son bo‘lishi kerak va amount raqam bo‘lishi kerak"},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            order = Order.objects.create(user_id=user_id, total=int(amount))  # noqa
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_DOWN)
        except Exception as e:
            return Response({"error": f"Noto‘g‘ri amount qiymati {e}"}, status=status.HTTP_400_BAD_REQUEST)

        if payment_method == "payme":
            payme = Payme(
                payme_id=PAYME_ID
            )
            payment_link = payme.initializer.generate_pay_link(
                id=order.id,
                amount=amount,
                return_url=SITE_URL
            )

            return Response({"payment_url": payment_link, "order_id": order.id}, status=status.HTTP_200_OK)

        return Response({"error": "payment_method noto‘g‘ri"}, status=status.HTTP_400_BAD_REQUEST)
