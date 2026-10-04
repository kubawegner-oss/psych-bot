{\rtf1\ansi\ansicpg1252\cocoartf2870
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;\f1\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww38200\viewh20260\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs26 \cf0 \expnd0\expndtw0\kerning0
import os\
import smtplib\
from email.mime.multipart import MIMEMultipart\
from email.mime.text import MIMEText\
import google.generativeai as genai\
\
# 1. Konfiguracja klucza API z sekret\'f3w GitHub\
API_KEY = os.environ.get("GEMINI_API_KEY")\
genai.configure(api_key=API_KEY)\
\
def generate_psych_note():\
    # U\uc0\u380 ywamy darmowego i szybkiego modelu flash\
    model = genai.GenerativeModel('gemini-2.5-flash')\
    \
    prompt = """\
    Wciel si\uc0\u281  w rol\u281  popularyzatora nauki i psychologa. Wybierz jedno fascynuj\u261 ce, wsp\'f3\u322 czesne badanie z dziedziny psychologii (np. psychologii poznawczej, spo\u322 ecznej lub neuronauki). \
    Przygotuj zwi\uc0\u281 z\u322 \u261 , porann\u261  notatku w j\u281 zyku polskim wed\u322 ug poni\u380 szego schematu:\
    \
    1. **Tytu\uc0\u322  badania / Temat**\
    2. **O co chodzi\uc0\u322 o?** (Kr\'f3tki kontekst w 2-3 zdaniach)\
    3. **Co odkryto?** (G\uc0\u322 \'f3wny, zaskakuj\u261 cy lub ciekawy wniosek)\
    4. **Co to oznacza dla Ciebie?** (Praktyczna wskaz\'f3wka do wdro\uc0\u380 enia w codziennym \u380 yciu)\
    \
    Pisz lekko, anga\uc0\u380 uj\u261 co i profesjonalnie. Ca\u322 o\u347 \u263  zamknij w maksymalnie 200-250 s\u322 owach.\
    """\
    \
    response = model.generate_content(prompt)\
    return response.text\
\
def send_email(content):\
    sender_email = os.environ.get("SENDER_EMAIL")\
    sender_password = os.environ.get("SENDER_PASSWORD")\
    receiver_email = os.environ.get("RECEIVER_EMAIL")\
    \
    msg = MIMEMultipart()\
    msg['From'] = sender_email\
    msg['To'] = receiver_email\
    msg['Subject'] = "
\f1 \uc0\u55358 \u56800 
\f0  Poranna dawka psychologii: Nowe badania"\
    \
    msg.attach(MIMEText(content, 'plain', 'utf-8'))\
    \
    # Przyk\uc0\u322 adowa konfiguracja dla Gmaila (wymaga has\u322 a aplikacji)\
    server = smtplib.SMTP('smtp.gmail.com', 587)\
    server.starttls()\
    server.login(sender_email, sender_password)\
    server.sendmail(sender_email, receiver_email, msg.as_string())\
    server.quit()\
\
if __name__ == "__main__":\
    print("Generuj\uc0\u281  notatk\u281 ...")\
    note = generate_psych_note()\
    print("Wysy\uc0\u322 am e-mail...")\
    send_email(note)\
    print("Gotowe!")}