import asyncio
import random
from telegram import (
    InlineKeyboardButton, InlineKeyboardMarkup, Update
)
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

# Token de tu bot
TOKEN = '7856798577:AAGzCAJxbf6-jkUYMlZGVwkpQ8m-R6oIgqI'

# Estado del ciclo
bucle_activo = False
tarea_bucle = None

# Lista de mensajes con botones y firma
mensajes = [
    {
        "texto": "📚 ¿Necesitas hacer cambios en tus notas o en tu documentación? Conozco los procesos y puedo ayudarte a facilitar ese trámite de manera segura. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "📝 Si quieres gestionar modificaciones en tu calificación o certificados, puedo orientarte y ofrecerte soluciones rápidas y confiables. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "🎯 ¿Buscas resolver temas relacionados con tus notas o documentación académica? Aquí estoy para ayudarte a gestionar todo de forma efectiva. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "💻 ¿Requieres realizar ajustes en tus registros o certificados? Con experiencia en el tema, puedo ayudarte a gestionar esos cambios de manera discreta. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "🎉 Si necesitas gestionar modificaciones en tus registros académicos, te puedo apoyar en cada paso para que el proceso sea sencillo y seguro. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "🤓 ¿Quieres solucionar temas relacionados con tus calificaciones o certificados? Tengo las habilidades para ayudarte a gestionar todo eficazmente. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "💥 Si necesitas hacer cambios en tus notas o en tus registros, puedo facilitarte la gestión y asesorarte en todo momento. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "📈 Quiero ayudarte a gestionar cambios en tu documentación académica, ofreciéndote soluciones rápidas y confiables. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "🚀 Mi experiencia me permite apoyarte en la gestión de cambios en tus registros sin complicaciones ni riesgos. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    },
    {
        "texto": "🎓 ¿Necesitas realizar ajustes en tus calificaciones o certificados? Estoy aquí para ayudarte a gestionar todo de forma profesional y discreta. ",
        "enlace": "https://t.me/BOBNOTASPERU"
    }
]

# Función para eliminar mensajes automáticamente después de un tiempo
async def eliminar_mensaje(chat_id, message_id, context, retraso=5):
    await asyncio.sleep(retraso)
    try:
        await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
    except:
        pass

# Ciclo para enviar mensajes aleatorios con botón
async def ciclo_mensajes(chat_id, context):
    global bucle_activo
    while bucle_activo:
        mensaje_obj = random.choice(mensajes)
        # Crear botón con enlace
        boton = InlineKeyboardButton("📎 Ver Referencias", url=mensaje_obj["enlace"])
        keyboard = InlineKeyboardMarkup([[boton]])

        # Preparar el texto completo con firma
        texto_completo = mensaje_obj["texto"] + "\n\n@PROFEBOB"

        # Enviar mensaje
        msg = await context.bot.send_message(
            chat_id=chat_id,
            text=texto_completo,
            reply_markup=keyboard,
            parse_mode='Markdown'
        )
        # Autoeliminar mensaje después de 5 segundos
        asyncio.create_task(eliminar_mensaje(chat_id, msg.message_id, context, retraso=5))
        await asyncio.sleep(5)  # Espera antes del siguiente mensaje

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global bucle_activo, tarea_bucle

    chat_id = update.effective_chat.id

    # Enviar bienvenida
    await update.message.reply_text(
        "🔰 *BIENVENID@ A PROFEBOB PERÚ* 🔐\n\n"
        "📍 *Servicios discretos y seguros:*\n"
        "📚 Cambios de notas académicos\n"
        "🧾 Certificados titulos actualizados\n"
        "💸 Descuentos en pensiones\n"
        "🔒 Opciones tech personalizadas\n\n"
        "📌 *CONTÁCTAME:* @profebob\n"
        "📎 *Revisa las referencias y únete a los que ya confiaron* 🔍",
        parse_mode='Markdown'
    )

    # Mostrar botones
    await context.bot.send_message(
        chat_id=chat_id,
        text="📝 *Menú:*",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📞 Contactarme con Bob", url="https://t.me/PROFEBOB")],
            [InlineKeyboardButton("🔗 Ver referencias", url="https://t.me/BOBNOTASPERU")]
        ]),
        parse_mode='Markdown'
    )

    # Iniciar ciclo si no está activo
    if not bucle_activo:
        bucle_activo = True
        tarea_bucle = asyncio.create_task(ciclo_mensajes(chat_id, context))

# Configuración y arranque del bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ BOT INICIADO Y LISTO")
    try:
        app.run_polling()
    except Exception as e:
        print(f"❌ Error: {e}")