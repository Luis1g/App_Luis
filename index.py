import streamlit as st

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Física Master", page_icon="⚛️", layout="wide")

# Título principal y descripción
st.title("⚛️ Física Master: Teoría y Práctica")
st.markdown("""
Bienvenido. Esta aplicación está diseñada para ayudarte a entender conceptos
físicos y practicar con problemas reales.
""")
st.divider() # Una línea divisoria visual

# --- BARRA LATERAL (MENÚ) ---
st.sidebar.header("Navegación")
tema = st.sidebar.radio(
    "Elige un tópico:",
    ["Inicio", "Cinemática (MRU)", "Dinámica (Newton)", "Termodinámica"]
)

# --- CONTENIDO DE LA PÁGINA ---

if tema == "Inicio":
    st.header("👋 ¿Por dónde quieres empezar?")
    st.info("Selecciona un tema en el menú de la izquierda para comenzar a estudiar.")
    # Ejemplo de cómo poner una imagen desde internet
    st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", caption="La física mueve el mundo", width=400)

elif tema == "Cinemática (MRU)":
    st.header("🏃 Movimiento Rectilíneo Uniforme")
    
    col1, col2 = st.columns(2) # Dividimos la pantalla en 2 columnas
    
    with col1:
        st.subheader("Concepto Clave")
        st.write("Un movimiento es rectilíneo uniforme cuando un objeto viaja en una trayectoria recta a una velocidad constante.")
        st.latex(r"v = \frac{d}{t}")
        st.caption("Donde $v$ es velocidad, $d$ es distancia y $t$ es tiempo.")

    with col2:
        st.subheader("📝 Problema Práctico")
        st.write("**Ejercicio:** Un tren viaja a 120 km/h. ¿Cuánto tiempo tarda en recorrer 300 km?")
        
        # Solución interactiva
        if st.button("Mostrar Solución MRU"):
            st.write("Despejamos el tiempo de la fórmula:")
            st.latex(r"t = \frac{d}{v}")
            st.write("Sustituyendo datos:")
            st.code("t = 300 km / 120 km/h = 2.5 horas")
            st.success("Resultado: 2.5 horas")

elif tema == "Dinámica (Newton)":
    st.header("🍎 Leyes de Newton")
    st.warning("Recuerda: La masa siempre debe estar en Kilogramos (kg) para usar Newtons.")
    
    st.subheader("Segunda Ley")
    st.latex(r"F = m \cdot a")
    
    with st.expander("Ver Ejercicio Resuelto: Fuerza"):
        st.write("Calcula la fuerza necesaria para acelerar una masa de 10 kg a 5 m/s².")
        st.latex(r"F = 10 \cdot 5 = 50 N")

# Puedes agregar más 'elif' para más temas...