import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Ruleta de Estudiantes", layout="wide")

# Inicializar las variables de estado (como la memoria de la app en la nube)
if "estudiantes" not in st.session_state:
    st.session_state.estudiantes = []
if "elegido" not in st.session_state:
    st.session_state.elegido = ""

st.title("🎡 Sistema de Ruleta Permanente")

# Dividimos la pantalla en 3 columnas en la web
col_lista, col_ruleta, col_registro = st.columns([1, 1.5, 1])

# --- COLUMNA 1: LISTA DE ESTUDIANTES (IZQUIERDA) ---
with col_lista:
    st.header("📝 Estudiantes")
    if st.session_state.estudiantes:
        for est in st.session_state.estudiantes:
            st.write(f"• {est}")
        if st.button("❌ Limpiar Lista"):
            st.session_state.estudiantes = []
            st.session_state.elegido = ""
            st.rerun()
    else:
        st.info("Lista vacía. Esperando registros...")

# --- COLUMNA 2: LA RULETA (CENTRO) ---
with col_ruleta:
    st.header("🔮 El Elegido")
    
    # Marcador de posición para la animación
    placeholder = st.empty()
    
    if st.session_state.elegido:
        placeholder.success(f"🎉 ¡{st.session_state.elegido}! 🎉")
    else:
        placeholder.info("Presiona el botón para sortear")
        
    if st.button("🎰 ¡GIRAR RULETA!", use_container_width=True):
        if len(st.session_state.estudiantes) < 2:
            st.warning("Se necesitan al menos 2 estudiantes para girar.")
        else:
            # Efecto visual de giro
            for _ in range(15):
                temp = random.choice(self.session_state.estudiantes)
                placeholder.warning(f"🎲 {temp} 🎲")
                time.sleep(0.1)
            
            st.session_state.elegido = random.choice(st.session_state.estudiantes)
            st.rerun()

# --- COLUMNA 3: REGISTRO Y QR (DERECHA) ---
with col_registro:
    st.header("📲 Registro")
    
    # Formulario para que se registren (sirve tanto para tu pantalla como para el celular de ellos)
    with st.form("registro_form", clear_on_submit=True):
        nuevo_nombre = st.text_input("Ingresa tu nombre:")
        enviar = st.form_submit_button("¡Unirse al Sorteo!")
        if enviar and nuevo_nombre:
            nombre_limpio = nuevo_nombre.strip()
            if nombre_limpio not in st.session_state.estudiantes:
                st.session_state.estudiantes.append(nombre_limpio)
                st.toast(f"¡{nombre_limpio} añadido!")
                st.rerun()
            else:
                st.error("Ese nombre ya está registrado.")

    st.markdown("---")
    st.subheader("🔗 Código QR para la clase")
    
    # Generador automático de QR nativo usando la URL actual de la app
    try:
        url_actual = "https://ruleta-jstqfmjfad7q2pfsrqxmxx.streamlit.app" # MANTÉN TU LINK REAL AQUÍ
        # Esta es la nueva línea segura:
        qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={url_actual}"
        st.image(qr_url, caption="Escanea para ingresar desde el celular")
    except:
        st.write("El QR se generará al publicar la app.")
