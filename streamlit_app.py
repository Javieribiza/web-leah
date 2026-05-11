import streamlit as st

# Configuración de la pestaña del navegador
st.set_page_config(page_title="Piscinas Leah Ibiza", page_icon="🏊‍♂️")

# Estilo personalizado
st.markdown("""
    <style>
    .main { background-color: #f0f7ff; }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #004a99;
        color: white;
        font-weight: bold;
        border: none;
        font-size: 18px;
    }
    .urgent-button>div>button { background-color: #d9534f !important; }
    h1 { color: #003366; text-align: center; }
    h3 { color: #0056b3; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# Imagen de cabecera
st.image("https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&q=80&w=1000", use_container_width=True)

# Títulos
st.title("PISCINAS LEAH")
st.subheader("Mantenimiento · Averías · Servicio Técnico")
st.write("<p style='text-align: center; font-weight: bold;'>📍 IBIZA</p>", unsafe_allow_html=True)

st.write("---")

# Botones de Acción
col1, col2 = st.columns(2)
with col1:
    if st.button("💬 WhatsApp"):
        js = "window.open('https://wa.me/34661764402?text=Hola%20Piscinas%20Leah,%20necesito%20información')"
        st.components.v1.html(f"<script>{js}</script>")

with col2:
    if st.button("✉️ Email"):
        js = "window.location.href = 'mailto:piscinasleah@gmail.com'"
        st.components.v1.html(f"<script>{js}</script>")

# Botón de Urgencia
st.markdown('<div class="urgent-button">', unsafe_allow_html=True)
if st.button("🚨 AVISO DE AVERÍA URGENTE"):
    js = "window.open('https://wa.me/34661764402?text=URGENTE:%20Tengo%20una%20avería')"
    st.components.v1.html(f"<script>{js}</script>")
st.markdown('</div>', unsafe_allow_html=True)

st.write("---")
st.markdown("<p style='text-align: center;'>© 2026 Piscinas Leah Ibiza</p>", unsafe_allow_html=True)
