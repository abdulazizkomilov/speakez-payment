# 💸 Django Payme Integration

This project demonstrates a complete integration of the **Payme payment system** with a **Django** backend. It provides a secure and reliable way to accept online payments from users using Payme, one of the most popular payment platforms in Uzbekistan.

---

## 🚀 Features

- ✅ Seamless Payme payment gateway integration
- 🔐 Secure request verification with HMAC
- 📦 Django project structure with environment-based configuration
- 📄 Sample payloads and API responses for testing
- 🧪 Test transactions in development mode

---

## 🏗️ Tech Stack

- **Backend**: Django 4+
- **Payment**: Payme (Merchant API)
- **Database**: PostgreSQL (or SQLite for local)
- **Others**: Python 3.11+, Docker (optional)

---

## 📦 Requirements

- Python 3.11+
- Django 4.0 or newer
- Payme Merchant credentials (Test or Live)
- PostgreSQL / SQLite

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/abdulazizkomilov/speakez-payment.git
cd speakez-payment
```

2. **Create and activate virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Create `.env` file**
```bash
cp .env.example .env
# Add your PAYME_ID, PAYME_KEY, DEBUG=True/False, etc.
```

5. **Apply migrations and run**
```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔌 Payme Setup

1. Log into your Payme Merchant account
2. Add your **callback URL** (e.g., `https://yourdomain.com/api/payme/`)
3. Use the test or live credentials in your `.env`
4. Start making payment requests from frontend or Postman

---

## 🔐 Environment Variables

Configure the following in your `.env` file:

```env
SECRET_KEY_DJANGO=
SITE=
SITE_URL_API=
DEBUG_DJANGO=
ALLOWED_HOSTS_DJANGO=
PAYME_ID=
PAYME_KEY=
PAYME_KEY_TEST=
PAYME_ACCOUNT_FIELD=
PAYME_AMOUNT_FIELD=
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
MONGO_URI=
```

---

## Github Secrets

Add the following secrets to your repository:

```bash
DOCKER_USERNAME
DOCKER_PASSWORD
IMAGE_NAME
IMAGE_TAG
PROD_SERVER_HOST
PROD_SSH_PRIVATE_KEY
SERVER_USER
```

---

## 📂 Project Structure (Simplified)

```
django-payme/
├── payment/
│   ├── views.py         # Payment logic
│   ├── urls.py          # API endpoints
│   └── utils.py         # Signature validation, helpers
│   └── ...              # Other core files
├── core/
│   └── settings.py      # Django settings
│   └── ...              # Other core files
├── manage.py
└── ...                  # Other core files
└── requirements.txt
```

---

## 🧪 Testing Payments

You can use Postman or frontend integration to simulate Payme payments. Make sure to use proper headers and JSON payloads as described in Payme API documentation.

---

## 📄 Documentation

- [Payme Merchant API Documentation (UZ)](https://developer.help.paycom.uz/)
- [Django Official Docs](https://docs.djangoproject.com/en/stable/)

---

## 🤝 Contributing

Pull requests and issues are welcome. Please follow PEP8 and Django best practices.

---

> Made with ❤️ by [Abdulaziz](https://t.me/abdulaziz9963)

