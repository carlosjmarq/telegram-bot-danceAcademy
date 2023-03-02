from telegram import Update
from telegram.ext import ContextTypes, CallbackQueryHandler
from constants.inline_keyboards import CLASSKEYBOARD, COSTKEYBOARD, DANCECLASSBOARD, DANCECOURSEBOARD, GENREINSTRUCTORBOARD, SITESBOARD, INSTRUCTORBOARD
from constants.text import SELECTCLASSTEXT, PRICECOURSETEXT, PRICECLASSTEXT, PROMOTIONTEXT
from db.config import start_db
from utils.inline_keyboards_funtions import create_inline_keyboard
from utils.email_functions import send_message, start_smtp_server

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
        con, cur = start_db()
        dance_res = cur.execute("SELECT id FROM generos_baile WHERE nombre LIKE '{}';".format(userdata["Clases"]))
        dance_data = dance_res.fetchone()
        instructor_dance_res = cur.execute("SELECT instructores_id FROM instructores_generos_baile WHERE generos_baile_id = {};".format(dance_data[0]))
        instructor_dance_data = instructor_dance_res.fetchall()
        instructores = []
        for row in instructor_dance_data:
            res = cur.execute("SELECT nombre, genre FROM instructores WHERE id = {};".format(row[0]))
            instructor = res.fetchone()
            if userdata["genero_de_instructor"] and userdata["genero_de_instructor"].upper() != instructor[1].upper():
                continue
            instructores.append(instructor)
        instructores_data = [{"text": instructor[0], "callback_data": "contactar/{}".format(instructor[0])} for instructor in instructores]
        instructores_keyboard = create_inline_keyboard(instructores_data)

        await context.bot.send_message(chat_id=update.effective_chat.id, text= "Según tus respuestas, los instructores disponibles son:", reply_markup=instructores_keyboard)
        con.close()
    
    elif "contactar" in query.data:
        nombre_instructor = query.data.split("/")[-1]
        con, cur = start_db()
        intructor_res = cur.execute("SELECT nombre, email FROM instructores WHERE nombre = '{}';".format(nombre_instructor))
        intructor_data = intructor_res.fetchone()
        email_data = {"subject": "Reserva de clase particular", "email": intructor_data[1], "content": "Se te ha reservado particular una clase de {} para {}.".format(userdata["Clases"], update.effective_chat.full_name)}

        server = start_smtp_server()

        # send_message(server, email_data)
        # server.quit()
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "Se ha enviado un correo al instructor: \n\n\n {}".format(email_data["content"]))
        con.close()


    elif query.data == "clases/cursos":
        await context.bot.send_message(chat_id=update.effective_chat.id, text= "¿Qué género quieres aprender?", reply_markup= DANCECOURSEBOARD)
    elif "curso_seleccionado" in query.data:
        userdata["Clases"] = query.data.split("/")[-1] 

        con, cur = start_db()

        dance_res = cur.execute("SELECT id, nombre FROM generos_baile WHERE nombre LIKE '{}';".format(userdata["Clases"]))
        dance_data = dance_res.fetchone()

        class_res = cur.execute("SELECT id, instructor_id, sede_id, horario FROM clases WHERE genero_id = {};".format(dance_data[0]))

        class_data = class_res.fetchall()
        if not class_data:
            await context.bot.send_message(chat_id=update.effective_chat.id, text= "En estos momentos no tenemos cursos de {} disponibles".format(userdata["Clases"]))
            return
        
        class_options = []
        for clase in class_data:
            instructor_res = cur.execute("SELECT nombre FROM instructores WHERE id = {};".format(clase[1]))
            instructor_data = instructor_res.fetchone()
            sede_res = cur.execute("SELECT nombre FROM sedes WHERE id = {};".format(clase[2]))
            sede_data = sede_res.fetchone()
            class_options.append({
                "text": "{} en {}. Dictado por: {}".format(clase[3], sede_data[0], instructor_data[0]),
                "callback_data": "inscribir/{}".format(clase[0])
            })

        clases_keyboard = create_inline_keyboard(class_options)

        await context.bot.send_message(chat_id=update.effective_chat.id, text= "Según tus respuestas, los cursos disponibles son:", reply_markup= clases_keyboard)
        con.close()

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