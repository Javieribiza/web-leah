import streamlit as st

# Configuración premium
st.set_page_config(
    page_title="Piscinas Leah Ibiza | Luxury Pool Services",
    page_icon="🏊‍♂️",
    layout="centered"
)

# --- DISEÑO DE ALTO NIVEL (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.5)), 
                    url('https://r.jina.ai/i/9f9e31d457634f1a8c3d8d64115e348f'); /* Tu imagen de la villa */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .glass-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        border-radius: 25px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 40px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    .service-card {
        background: rgba(0, 0, 0, 0.4);
        padding: 20px;
        border-radius: 15px;
        border-left: 4px solid #00d4ff;
        margin-bottom: 15px;
        text-align: left;
    }

    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3.5em;
        background: linear-gradient(135deg, #00d4ff 0%, #004a99 100%);
        color: white;
        font-weight: bold;
        border: none;
        font-size: 18px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.4);
    }

    .urgent-btn>div>button {
        background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%) !important;
    }
    
    h1 { font-size: 3em; text-shadow: 3px 3px 6px rgba(0,0,0,0.9); }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUCTURA DE LA WEB ---

st.markdown('<div class="glass-container">', unsafe_allow_html=True)
st.markdown("<h1>PISCINAS LEAH IBIZA</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.5em; color: #00d4ff;'>Mantenimiento de Excelencia & Servicio Técnico Especializado</p>", unsafe_allow_html=True)
st.write("---")

st.markdown("""
<div style='font-size: 1.1em; line-height: 1.6;'>
Especialistas en la gestión integral de instalaciones acuáticas de alto nivel. 
Combinamos tecnología de vanguardia con un servicio técnico riguroso para garantizar 
la perfección en cada gota de agua.
</div>
""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# SERVICIOS TÉCNICOS
col1, col2 = st.columns(2)
with col1:
    st.markdown("""<div class='service-card'><strong>💎 Mantenimiento Preventivo</strong><br>Control químico automatizado, limpieza de fondos y gestión de filtración.</div>""", unsafe_allow_html=True)
    st.markdown("""<div class='service-card'><strong>🧪 Tratamiento Avanzado</strong><br>Expertos en electrólisis salina, hidrólisis y desinfección UV.</div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class='service-card'><strong>🔧 Ingeniería de Reparación</strong><br>Localización de fugas estructurales y sustitución de bombas de alta eficiencia.</div>""", unsafe_allow_html=True)
    st.markdown("""<div class='service-card'><strong>💡 Optimización Energética</strong><br>Instalación de iluminación LED subacuática y sistemas de domótica.</div>""", unsafe_allow_html=True)

st.write("---")

# BOTONES (Ahora con el número 661 76 44 02 funcionando)
st.subheader("Contacto Directo")
c1, c2 = st.columns(2)

with c1:
    # Botón WhatsApp
    st.markdown(f'<a href="https://wa.me/34661764402?text=Hola%20Piscinas%20Leah,%20deseo%20solicitar%20un%20presupuesto%20profesional" target="_blank"><button style="width:100%; border-radius:50px; height:3.5em; background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); color:white; font-weight:bold; border:none; cursor:pointer;">💬 WhatsApp</button></a>', unsafe_allow_html=True)

with c2:
    # Botón Email
    st.markdown(f'<a href="mailto:piscinasleah@gmail.com"><button style="width:100%; border-radius:50px; height:3.5em; background: linear-gradient(135deg, #00d4ff 0%, #004a99 100%); color:white; font-weight:bold; border:none; cursor:pointer;">✉️ Email</button></a>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# BOTÓN URGENTE
st.markdown(f'<div class="urgent-btn"><a href="https://wa.me/34661764402?text=URGENTE:%20Aviso%20de%20avería" target="_blank"><button style="width:100%; border-radius:12px; height:4.5em; background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%); color:white; font-weight:bold; border:none; font-size:20px; cursor:pointer;">🚨 ASISTENCIA TÉCNICA URGENTE</button></a></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white; padding-top: 20px;'>© 2024 Piscinas Leah Ibiza | Servicio Oficial 24h</p>", unsafe_allow_html=True)
