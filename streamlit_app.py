import streamlit as st

# Configuración de página con SEO para Ibiza
st.set_page_config(
    page_title="Piscinas Leah Ibiza | Mantenimiento y Servicio Técnico",
    page_icon="🏊‍♂️",
    layout="centered"
)

# ESTILO CSS AVANZADO (Basado en nuestro documento)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #004a99;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #003366;
        border: 1px solid #00d4ff;
    }
    .urgent-button>div>button {
        background-color: #ff4b4b !important;
        font-size: 20px !important;
        height: 4em !important;
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }
    .service-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f8fbff;
        border-left: 5px solid #004a99;
        margin-bottom: 10px;
    }
    h1 { color: #003366; font-family: 'Helvetica'; }
    .location { color: #00a8e8; font-weight: bold; font-size: 1.2em; }
    </style>
    """, unsafe_allow_html=True)

# CABECERA
st.image("https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&q=80&w=1000", caption="Servicio Profesional en toda la Isla")

st.title("PISCINAS LEAH IBIZA")
st.markdown("<p class='location'>📍 Servicio Técnico Oficial en Ibiza</p>", unsafe_allow_html=True)

st.write("""
**Piscinas Leah** es sinónimo de tranquilidad. Nos encargamos de que su piscina esté siempre en perfectas condiciones, combinando maquinaria de última generación con un trato cercano y profesional.
""")

st.write("---")

# SECCIÓN DE SERVICIOS (Lo que faltaba)
st.subheader("🛠️ Nuestros Servicios Especializados")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""<div class='service-card'>
    <strong>🏊 Mantenimiento Integral</strong><br>
    Limpieza, control de PH y cloro, y puesta a punto estacional.
    </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class='service-card'>
    <strong>🧪 Tratamiento de Agua</strong><br>
    Sistemas de salinidad, hidrólisis y análisis químico avanzado.
    </div>""", unsafe_allow_html=True)

with col_b:
    st.markdown("""<div class='service-card'>
    <strong>⚙️ Servicio Técnico</strong><br>
    Reparación de bombas, filtros y fugas estructurales.
    </div>""", unsafe_allow_html=True)
    
    st.markdown("""<div class='service-card'>
    <strong>💡 Iluminación y Domótica</strong><br>
    Instalación de focos LED y control remoto de su piscina.
    </div>""", unsafe_allow_html=True)

st.write("---")

# CONTACTO Y ACCIÓN
st.subheader("¿Necesita ayuda con su piscina?")

c1, c2 = st.columns(2)
with c1:
    if st.button("💬 Contactar por WhatsApp"):
        js = "window.open('https://wa.me/34661764402?text=Hola,%20solicito%20información%20sobre%20sus%20servicios')"
        st.components.v1.html(f"<script>{js}</script>")

with c2:
    if st.button("✉️ Enviar Correo"):
        js = "window.location.href = 'mailto:piscinasleah@gmail.com'"
        st.components.v1.html(f"<script>{js}</script>")

# BOTÓN DE URGENCIA
st.markdown('<div class="urgent-button">', unsafe_allow_html=True)
if st.button("🚨 AVISO DE AVERÍA URGENTE"):
    js = "window.open('https://wa.me/34661764402?text=URGENTE:%20Tengo%20una%20avería%20en%20mi%20piscina')"
    st.components.v1.html(f"<script>{js}</script>")
st.markdown('</div>', unsafe_allow_html=True)

# PIE DE PÁGINA
st.write("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 0.8em;'>
    <p>Piscinas Leah Ibiza - Especialistas en el cuidado del agua.<br>
    © 2024 Servicio Técnico Autorizado.</p>
</div>
""", unsafe_allow_html=True)
