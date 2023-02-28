from telegram import InlineKeyboardButton, InlineKeyboardMarkup

KEYBOARD1 = InlineKeyboardMarkup([[InlineKeyboardButton(text="1", callback_data="c1"), InlineKeyboardButton(text="?", callback_data="c111")], [InlineKeyboardButton(text="2", callback_data="c2")]])
FIRSTKEYBOARD = InlineKeyboardMarkup([[InlineKeyboardButton(text="Clases", callback_data="clases"),InlineKeyboardButton(text="Costos", callback_data="costos")]])
CLASSKEYBOARD = InlineKeyboardMarkup([[InlineKeyboardButton(text="Cursos", callback_data="clases/cursos"),InlineKeyboardButton(text="Clases Particulares", callback_data="clases/clases_particulares")]])
COSTKEYBOARD = InlineKeyboardMarkup([[InlineKeyboardButton(text="Cursos", callback_data="costos/cursos"),InlineKeyboardButton(text="Clases Particulares", callback_data="costos/clases_particulares")],[InlineKeyboardButton(text="Promociones", callback_data="costos/promociones")]])
DANCECLASSBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="Bachata", callback_data="clase_seleccionada/bachata"),InlineKeyboardButton(text="Salsa Casino", callback_data="clase_seleccionada/salsa_casino")],
    [InlineKeyboardButton(text="Kizomba", callback_data="clase_seleccionada/kizomba"),InlineKeyboardButton(text="Salsa en Línea", callback_data="clase_seleccionada/salsa_en_linea")],
    [InlineKeyboardButton(text="Merengue", callback_data="clase_seleccionada/merengue"),InlineKeyboardButton(text="Salsa Venezolana", callback_data="clase_seleccionada/salsa_venezolana")],
    [InlineKeyboardButton(text="Bachata Pacheco", callback_data="clase_seleccionada/bachata_pacheco"),InlineKeyboardButton(text="Danza Arabe", callback_data="clase_seleccionada/danza_arabe")],
    [InlineKeyboardButton(text="Break Dance", callback_data="clase_seleccionada/break_dance")]])
DANCECOURSEBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton(text="Bachata", callback_data="curso_seleccionado/bachata"),InlineKeyboardButton(text="Salsa Casino", callback_data="curso_seleccionado/salsa_casino")],
    [InlineKeyboardButton(text="Kizomba", callback_data="curso_seleccionado/kizomba"),InlineKeyboardButton(text="Salsa en Línea", callback_data="curso_seleccionado/salsa_en_linea")],
    [InlineKeyboardButton(text="Merengue", callback_data="curso_seleccionado/merengue"),InlineKeyboardButton(text="Salsa Venezolana", callback_data="curso_seleccionado/salsa_venezolana")],
    [InlineKeyboardButton(text="Bachata Pacheco", callback_data="curso_seleccionado/bachata_pacheco"),InlineKeyboardButton(text="Danza Arabe", callback_data="curso_seleccionado/danza_arabe")],
    [InlineKeyboardButton(text="Break Dance", callback_data="curso_seleccionado/break_dance")]])
GENREINSTRUCTORBOARD = InlineKeyboardMarkup([[InlineKeyboardButton(text="Hombre", callback_data="genero_instructor/hombre"), InlineKeyboardButton(text="Mujer", callback_data="genero_instructor/mujer"), InlineKeyboardButton(text="No importa", callback_data="genero_instructor/no_importa")]])
SITESBOARD = InlineKeyboardMarkup([[InlineKeyboardButton(text="Chacao, Centro Perú", callback_data="sedes/chacao_centro_peru")], [InlineKeyboardButton(text="Chacao, Edificio Hirsch", callback_data="sedes/chacao_edificio_hirsch")],
                                   [InlineKeyboardButton(text="Bellas Artes", callback_data="sedes/bellas_artes")],[InlineKeyboardButton(text="Clases a domicilio", callback_data="sedes/domicilio")]])
INSTRUCTORBOARD = InlineKeyboardMarkup([[InlineKeyboardButton(text="Francis Rodriguez", callback_data="instructor/francis_rodriguez")], [InlineKeyboardButton(text="Luis Fernando Pelaez", callback_data="instructor/luis_fernando_pelaez")],
                                   [InlineKeyboardButton(text="Sander Rodriguez", callback_data="instructor/sander_rodriguez")],[InlineKeyboardButton(text="Carlos Brito", callback_data="instructor/carlos_brito")]])