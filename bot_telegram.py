import telegram
import asyncio
import schedule
import time
from datetime import datetime

# CONFIGURACIÓN (reemplaza estos valores)
BOT_TOKEN = "8016098401:AAFkfaCQG8HRnXnf9xz790zLCg6zVfy4lnw"
CHAT_ID = "1110304109"  # Usa el CHAT_ID que obtuviste

bot = telegram.Bot(token=BOT_TOKEN)

async def send_monthly_message():
    """Envía el mensaje mensual"""
    try:
        message = f"""
📅 **Recordatorio Mensual** ⏰

¡Hoy es día 10! 
Fecha: {datetime.now().strftime('%d/%m/%Y')}

Este es tu recordario automático.
¡Que tengas un excelente día! 🌟
Recuerda pagar el nauta
        """
        
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message,
            parse_mode='Markdown'
        )
        print(f'✅ Mensaje enviado el {datetime.now()}')
    except Exception as e:
        print(f'❌ Error: {e}')

def check_and_send():
    """Verifica si es día 10 y envía el mensaje"""
    if datetime.now().day == 10:
        asyncio.run(send_monthly_message())

# Programar verificación diaria
schedule.every().day.at("09:00").do(check_and_send)

print('🤖 Bot iniciado - Enviará mensajes los días 10 a las 9:00 AM')

while True:
    schedule.run_pending()
    time.sleep(1)