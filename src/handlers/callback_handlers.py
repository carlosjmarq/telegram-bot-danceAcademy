from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from constants.inline_keyboards import CLASSKEYBOARD, COSTKEYBOARD, DANCECLASSBOARD, DANCECOURSEBOARD, GENREINSTRUCTORBOARD, SITESBOARD, INSTRUCTORBOARD
from constants.text import SELECTCLASSTEXT, PRICECOURSETEXT, PRICECLASSTEXT, PROMOTIONTEXT

userdata = {}
async def callback_query_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.effective_chat or not update.callback_query: return
    query = update.callback_query
    print (query.data)

    if query.data == "clases":
        await context.bot.send_message(chat_id=update.effective_chat.id, text= SELECTCLASSTEXT, reply_markup= CLASSKEYBOARD)
    elif query.data == "costos":
        await context.bot.send_message(chat_id=update.effective_chat.id, text= SELECTCLASSTEXT, reply_markup= COSTKEYBOARD)
    elif query.data == "clases/clases_particulares":
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "¿Qué género quieres aprender?", reply_markup= DANCECLASSBOARD)
    elif "clase_seleccionada" in query.data:
        userdata["Clases"]=query.data.split("/")[-1]
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "Seleccione el género del instructor", reply_markup= GENREINSTRUCTORBOARD)
    elif "genero_instructor" in query.data:
        userdata["genero_de_instructor"]=query.data.split("/")[-1] if not "no_importa" in query.data else None
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "¿En qué sede te gustaría ver clases?", reply_markup= SITESBOARD)
    elif "sedes" in query.data:
        userdata["sedes"]=query.data.split("/")[-1] if not "domicilio" in query.data else None
        print (userdata)
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "Según tus respuestas, los instructores disponibles son:", reply_markup= INSTRUCTORBOARD)
    
    elif query.data == "clases/cursos":
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "¿Qué género quieres aprender?", reply_markup= DANCECOURSEBOARD)
    elif "curso_seleccionado" in query.data:
        userdata["Clases"]=query.data.split("/")[-1] 
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "Según tus respuestas, los cursos disponibles son:", reply_markup= INSTRUCTORBOARD)

    elif "costos/cursos" in query.data:
        await context.bot.send_message(chat_id=update.effective_chat.id, text= PRICECOURSETEXT)
    elif "costos/clases_particulares" in query.data:
        await context.bot.send_message(chat_id=update.effective_chat.id, text= PRICECLASSTEXT)
    elif "costos/promociones" in query.data:
        await context.bot.send_message(chat_id=update.effective_chat.id, text= PROMOTIONTEXT)

    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Parrot says: I cannot handle that action, asshole")
    await context.bot.answer_callback_query(query.id, "feedback message")

callback_handler = CallbackQueryHandler(callback_query_handler)