import os
import smtplib
from email.message import EmailMessage
from google import genai

# 1. Pobranie zmiennych środowiskowych
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")

if not all([GEMINI_API_KEY, SENDER_EMAIL, SENDER_PASSWORD, RECEIVER_EMAIL]):
    raise ValueError("Brak niektórych zmiennych środowiskowych (sekretów)!")

# 2. Wygenerowanie treści przez Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

prompt = (
    "Napisz krótkie i ciekawe streszczenie z jednego nowego eksperymentu lub badania psychologicznego. Evidence based, nowoczesna psychologia z ostatnich lat "
    "Sformatuj ją ładnie w kilku akapitach."
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

email_content = response.text

# 3. Wysłanie maila
msg = EmailMessage()
msg.set_content(email_content)
msg.Subject = "Twoja codzienna dawka psychologii 🧠"
msg.From = SENDER_EMAIL
msg.To = RECEIVER_EMAIL

# Konfiguracja dla Gmaila (lub innego serwera SMTP)
# Domyślnie używamy portu 465 dla SSL lub 587 dla TLS
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
    smtp.send_message(msg)

print("Mail został pomyślnie wysłany!")
