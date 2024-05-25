# payments/stripe.py

import stripe
from config.config import STRIPE_SECRET_KEY

stripe.api_key = STRIPE_SECRET_KEY

def process_payment(amount, currency, card_number, exp_month, exp_year, cvc):
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency=currency,
            payment_method_types=['card'],
            payment_method_data={
                'card': {
                    'number': card_number,
                    'exp_month': exp_month,
                    'exp_year': exp_year,
                    'cvc': cvc
                }
            }
        )
        return payment_intent
    except stripe.error.CardError as e:
        # Since it's a decline, stripe.error.CardError will be caught
        print('Status is: %s' % e.http_status)
        print('Code is: %s' % e.code)
        # param is '' in this case
        print('Param is: %s' % e.param)
        print('Message is: %s' % e.user_message)
    except stripe.error.RateLimitError as e:
        # Too many requests made to the API too quickly
        pass
    except stripe.error.InvalidRequestError as e:
        # Invalid parameters were supplied to Stripe's API
        pass
    except stripe.error.AuthenticationError as e:
        # Authentication with Stripe's API failed
        # (maybe you changed API keys recently)
        pass
    except stripe.error.APIConnectionError as e:
        # Network communication with Stripe failed
        pass
    except stripe.error.StripeError as e:
        # Display a very generic error to the user, and maybe send
        # yourself an email
        pass
    except Exception as e:
        # Something else happened, completely unrelated to Stripe
        pass