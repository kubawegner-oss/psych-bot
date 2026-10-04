import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import google.generativeai as genai

API_KEY = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

def generate_psych_note():
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = """
    Wciel się w rolę popularyzatora nauki i psychologa. Wybierz jedno fascynujące, współczesne badanie z dziedziny psychologii (np. psychologii poznawczej, społecznej lub neuronauki). 
    Przygotuj zwięzłą, poranną notatkę w języku polskim według poniższego schematu:
    
    1. **Tytuł badania / Temat**
    2. **O co chodziło?** (Krótki kontekst w 2-3 zdaniach)
    3. **Co odkryto?** (Główny, zaskakujący lub ciekawy wniosek)
    4. **Co to oznacza dla Ciebie?** (Praktyczna wskazówka do wdrożenia w codziennym życiu)
    
    Pisz lekko, angażująco i profesjonalnie. Całość zamknij w maksymalnie 200-250 słowach.
    """
    
    response = model.generate_content(prompt)
    return response.text

def send_email(content):
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    receiver_email = os.environ.get("RECEIVER_EMAIL")
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "🧠 Poranna dawka psychologii: Nowe badania"
    
    msg.attach(MIMEText(content, 'plain', 'utf-8'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

if __name__ == "__main__":
    print("Generuję notatkę...")
    note = generate_psych_note()
    print("Wysyłam e-mail...")
    send_email(note)
    print("Gotowe!")
