import streamlit as st
import matplotlib.pyplot as plt # Importa Matplotlib para gráficas
import numpy as np # Importa NumPy para cálculos numéricos

# ... el resto de tu código de configuración de página y estilos ...

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Física Master", page_icon="E=MC", layout="wide")

# Título principal y descripción
st.title(" Física Master: Teoría y Práctica")
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
    st.header("Hola, ¿Por dónde quieres empezar?")
    st.info("Selecciona un tema en el menú de la izquierda para comenzar a estudiar.")
    # Ponemos una imagen desde internet
    st.image("https://images.unsplash.com/photo-1635070041078-e363dbe005cb", caption="La física mueve el mundo", width=400)

elif tema == "Cinemática (MRU)":
    st.header(" Movimiento Rectilíneo Uniforme")
    tab_cin1, tab_cin2 = st.tabs(["Teoría", "Calculadora de distancia"])
    with tab_cin1:
        
        col1, col2 = st.columns(2) # Dividimos la pantalla en 2 columnas
        
        with col1:
            st.subheader("Concepto Clave")
            st.write("Un movimiento es rectilíneo uniforme cuando un objeto viaja en una trayectoria recta a una velocidad constante.")
            st.latex(r"v = \frac{d}{t}")
            st.caption("Donde $v$ es velocidad, $d$ es distancia y $t$ es tiempo.")

        with col2:
            st.subheader(" Problema Práctico")
            st.write("**Ejercicio:** Un tren viaja a 120 km/h. ¿Cuánto tiempo tarda en recorrer 300 km?")
            
            # Solución interactiva
            if st.button("Mostrar Solución MRU"):
                st.write("Despejamos el tiempo de la fórmula:")
                st.latex(r"t = \frac{d}{v}")
                st.write("Sustituyendo datos:")
                st.code("t = 300 km / 120 km/h = 2.5 horas")
                st.success("Resultado: 2.5 horas")
            # ... (tu código anterior de configuración y la barra lateral) ...
        with col1:
            st.divider() # Otra línea para separar visualmente
            st.header("Tiro Parabólico (Básico)")
            
            st.write("Explora la trayectoria de un proyectil.")
            
            # Inputs para los parámetros del tiro
            velocidad_inicial = st.slider("Velocidad Inicial (m/s)", 0, 100, 30)
            angulo_grados = st.slider("Ángulo de Lanzamiento (grados)", 0, 90, 45)
            
            # Convertir el ángulo a radianes para los cálculos
            angulo_radianes = np.deg2rad(angulo_grados)
            
            # Gravedad (constante)
            g = 9.81 # m/s²
            
            # Cálculo del tiempo de vuelo máximo
            tiempo_vuelo = (2 * velocidad_inicial * np.sin(angulo_radianes)) / g
            
            # Generar puntos para la trayectoria
            t = np.linspace(0, tiempo_vuelo, 100) # 100 puntos de tiempo desde 0 hasta el tiempo de vuelo
            
            x = velocidad_inicial * np.cos(angulo_radianes) * t
            y = (velocidad_inicial * np.sin(angulo_radianes) * t) - (0.5 * g * t**2)
            
            # Crear la figura y los ejes de Matplotlib
            fig, ax = plt.subplots(figsize=(10, 5)) # Tamaño de la gráfica
            ax.plot(x, y, label="Trayectoria del Proyectil", color='blue')
            ax.set_xlabel("Distancia Horizontal (metros)")
            ax.set_ylabel("Altura (metros)")
            ax.set_title(f"Trayectoria de Proyectil (v₀={velocidad_inicial} m/s, θ={angulo_grados}°)")
            ax.grid(True)
            ax.set_ylim(bottom=0) # Asegurar que el eje Y no muestre valores negativos
            ax.legend()
            
            # Mostrar la gráfica en Streamlit
            st.pyplot(fig)
            
            st.markdown(f"""
            **Detalles del tiro:**
            * Tiempo de vuelo: `{tiempo_vuelo:.2f}` segundos
            * Alcance máximo: `{x.max():.2f}` metros
            * Altura máxima: `{y.max():.2f}` metros
            """)

# ... (el resto de tus elif para Dinámica, Termodinámica, etc.) ...
    with tab_cin2:
        st.subheader(" Calculadora de d = v t")
        st.write("Cambia los valores para calcular la distancia resultante.")
        
        # Columnas para poner los inputs lado a lado
        col_a, col_b = st.columns(2)
        
        with col_a:
            velocidad = st.number_input("Velocidad (m/s)", min_value=0.0, value=10.0, step=0.1)
        
        with col_b:
            tiempo = st.number_input("Tiempo (s)", value=5.0, step=0.1)
            
        # Cálculo automático
        distancia = velocidad * tiempo
        
        st.divider()
        st.metric(label="distancia total recorrida (d)", value=f"{distancia:.2f} m")
        

elif tema == "Dinámica (Newton)":
    st.header(" Leyes de Newton")
    
    # Pestañas para organizar mejor la teoría de la práctica
    tab1, tab2 = st.tabs(["Teoría", "Calculadora de Fuerza"])
    
    with tab1:
        st.subheader("Segunda Ley")
        st.write("La aceleración de un objeto es directamente proporcional a la fuerza neta que actúa sobre él e inversamente proporcional a su masa.")
        st.latex(r"\vec{F} = m \cdot \vec{a}")
        st.info("Esta ley explica qué sucede cuando una fuerza actúa sobre un cuerpo.")
        
    with tab2:
        st.subheader(" Calculadora de F = m·a")
        st.write("Cambia los valores para calcular la fuerza resultante.")
        
        # Columnas para poner los inputs lado a lado
        col_a, col_b = st.columns(2)
        
        with col_a:
            masa = st.number_input("Masa (kg)", min_value=0.0, value=10.0, step=0.1)
        
        with col_b:
            aceleracion = st.number_input("Aceleración (m/s²)", value=5.0, step=0.1)
            
        # Cálculo automático
        fuerza = masa * aceleracion
        
        st.divider()
        st.metric(label="Fuerza Resultante (N)", value=f"{fuerza:.2f} N")
        