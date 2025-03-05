import streamlit as st
import random
import datetime

# Función para obtener o inicializar el estado de la sesión
def get_state():
    if "last_opened" not in st.session_state:
        st.session_state["last_opened"] = None
    if "opened_today" not in st.session_state:
        st.session_state["opened_today"] = False

# Inicializar el estado de la sesión
get_state()

# Título de la app
st.title("No importa qué tan lejos estemos, estamos bajo el mismo cielo")
st.write("Nunca fui experta en programación, y la creatividad tampoco es mi fuerte, pero gracias a la IA hoy aprendí a hacer nuestra elección de citas virtuales de una forma más… digna de una inge. 💡 Ahora, en lugar de simplemente pensarle en qué hacer diferente, te dejaré dar un click, eligiendo una carta al día con una idea especial para compartir juntas. ¡Espero que te guste tanto como a mí! 💖")
st.write("(La idea es que elijas alguna carta y me digas qué te salió y coordinemos)")
# Lista de citas y sus descripciones
citas = [
    ("🎨 Art Attack", "No le sé al arte, pero ponme un reto y yo te pongo uno a ti y lo hacemos."),
    ("🎬 Noche de películas", "Elije una peli y algo que quieras comer."),
    ("🍽️ Chefsitas", "Vamos a realizar una receta juntas, ¿quieres sal o dulce?"),
    ("🎮 Día de juegos", "Scape room? Cartas? Lo que tú quieras, mi cielo."),
    ("🎶 Musiquita", "Hagamos una playlist juntas y decimos el porqué pusimos la canción."),
    ("🎙️ Exposición super profesional", "Expongamos de algún tema random a la otra.")
]

# Mensajes lindos para los botones
mensajes_botones = [
    "🌸 Que viva el suroccidente Colombiano xd 🌸",
    "💖 Según mi bajo IQ (idk), lo más inteligente que hiciste fue coquetearme 💖",
    "✨ Si yo fuera un personaje de Gumball, cuál sería? ✨",
    "💕 Como le caiste bien a bb Tsuki, me caes bien a mi 💕",
    "🌷 Ojalá ser cobijita de emojis pa estar enrolladita en tus piernas 🌷",
    "💫 Que fueeerte que ande parchando con una IA para que seamos happy a la distancia 💫"
]

# Inicializar el estado si no existe
if "ultima_carta" not in st.session_state:
    st.session_state.ultima_carta = None
if "ultima_fecha" not in st.session_state:
    st.session_state.ultima_fecha = None
if "cartas_disponibles" not in st.session_state:
    st.session_state.cartas_disponibles = list(range(len(citas)))

# Obtener la fecha actual
hoy = datetime.date.today()

# Función para elegir una carta
def elegir_carta(index):
    if st.session_state.ultima_fecha == hoy:
        st.warning("Ya abriste una carta hoy. Espera hasta mañana para abrir otra. 💕")
    else:
        st.session_state.ultima_carta = citas[index][1]
        st.session_state.ultima_fecha = hoy
        st.session_state.cartas_disponibles.remove(index)

# Mostrar los botones con mensajes lindos
for i, mensaje in zip(st.session_state.cartas_disponibles, mensajes_botones):
    if st.button(mensaje):
        elegir_carta(i)

# Mostrar la cita elegida
if st.session_state.ultima_carta:
    st.subheader("💌 Cita revelada 💌")
    st.write(st.session_state.ultima_carta)

# Botón para reiniciar y volver a empezar
if st.button("🔄 Reiniciar"):
    st.session_state.ultima_carta = None
    st.session_state.ultima_fecha = None
    st.session_state.cartas_disponibles = list(range(len(citas)))
    st.success("Se ha reiniciado. ¡Ahora puedes empezar de nuevo! 💖")



#python3.11 -m streamlit run Micielo.py