def classify_intent(message: str):
    message = message.lower()

    intents = {
        "check_order_status": {
            "keywords": ["order", "status", "track", "tracking", "where is my order", "order update"],
            "response": "Sure! Can you provide your order ID so I can check the status?"
        },
        "cancel_order": {
            "keywords": ["cancel", "stop order", "abort order", "change order"],
            "response": "I can help cancel your order. What’s the order number?"
        },
        "refund_policy": {
            "keywords": ["refund", "money back", "return policy", "return", "refund process"],
            "response": "Our refund policy allows returns within 7 days. Would you like to start a refund request?"
        },
        "speak_to_agent": {
            "keywords": ["human", "agent", "representative", "support", "talk to someone", "customer service"],
            "response": "I’m escalating your request to a support agent now."
        },
        "shipping_info": {
            "keywords": ["shipping", "delivery time", "ship", "delivery", "when will it arrive"],
            "response": "Shipping usually takes 3-5 business days, depending on your location."
        },
        "payment_methods": {
            "keywords": ["payment", "pay", "credit card", "paypal", "payment options", "methods of payment"],
            "response": "We accept Visa, Mastercard, American Express, PayPal, and Apple Pay."
        },
        "product_availability": {
            "keywords": ["available", "stock", "in stock", "out of stock", "product availability", "do you have"],
            "response": "Please tell me the product name or code you want to check availability for."
        },
        "account_help": {
            "keywords": ["account", "login", "password", "sign in", "reset password", "forgot password"],
            "response": "I can help with your account. Are you trying to reset your password or having trouble logging in?"
        },
        "discounts_offers": {
            "keywords": ["discount", "offer", "sale", "promo code", "coupon"],
            "response": "We currently have seasonal discounts. Would you like me to send you available promo codes?"
        },
        "technical_issue": {
            "keywords": ["error", "bug", "problem", "not working", "issue", "technical"],
            "response": "I’m sorry you’re experiencing issues. Can you please describe the problem in detail?"
        },
        "greeting": {
            "keywords": ["hello", "hi", "hey", "good morning", "good evening", "greetings"],
            "response": "Hello! How can I assist you today?"
        },
        "farewell": {
            "keywords": ["bye", "goodbye", "see you", "thanks", "thank you", "thank you very much"],
            "response": "Thank you for contacting us! Have a wonderful day!"
        },
        "store_hours": {
            "keywords": ["hours", "open", "close", "working hours", "business hours", "when are you open"],
            "response": "Our store hours are Monday to Friday, 9 AM to 6 PM."
        },
        "order_modification": {
            "keywords": ["change order", "modify order", "update order", "edit order"],
            "response": "If your order hasn’t shipped yet, I can help update it. Please provide the order number."
        },
        "shipping_cost": {
            "keywords": ["shipping cost", "delivery charges", "shipping fees", "how much to ship"],
            "response": "Shipping fees depend on your location and order size. Would you like an estimate?"
        },
        "return_process": {
            "keywords": ["return", "send back", "return item", "exchange"],
            "response": "You can return items within 7 days. I can guide you through the return process if you like."
        }
    }

    for intent, data in intents.items():
        if any(keyword in message for keyword in data["keywords"]):
            return intent, data["response"]

    return "fallback", "Sorry, I didn’t get that. Can you please rephrase or ask something else?"
