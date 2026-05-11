import streamlit as st

# Configuración de lujo para Ibiza
st.set_page_config(
    page_title="Piscinas Leah Ibiza | Servicio Premium",
    page_icon="🏊‍♂️",
    layout="centered"
)

# --- ESTILO DE ALTO NIVEL (CSS) ---
st.markdown("""
    <style>
    /* Imagen de fondo: Piscina infinita de lujo */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.6)), 
                    url('https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Contenedor efecto cristal */
    .glass-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 35px;
        color: white;
        text-align: center;
    }

    /* Tarjetas de servicios técnicos */
    .service-box {
        background: rgba(0, 0, 0, 0.4);
        padding: 15px;
        border-radius: 12px;
        border-left: 5px solid #00d4ff;
        margin-bottom: 15px;
        text-align: left;
    }

    /* Botones de contacto */
    .btn-contact {
        display: inline-block;
        width: 100%;
        padding: 15px;
        margin: 10px 0;
        border-radius: 50px;
        font-weight: bold;
        text-decoration: none;
        color: white;
        text-align: center;
        font-size: 18px;
        transition: 0.3s;
    }
    
    .whatsapp-btn { background: linear-gradient(135deg, #25D366 0%, #128C7E 100%); }
    .email-btn { background: linear-gradient(135deg, #00d4ff 0%, #004a99 100%); }
    .urgent-btn { 
        background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%); 
        font-size: 20px;
        padding: 20px;
    }

    h1 { text-shadow: 3px 3px 6px rgba(0,0,0,0.8); font-size: 3em; }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO DE LA WEB ---

st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown("<h1>PISCINAS LEAH IBIZA</h1>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 1.4em; color: #00d4ff; font-weight: bold;'>Mantenimiento de Excelencia & Servicio Técnico Especializado</p>", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<div style='font-size: 1.1em; line-height: 1.6;'>
Especialistas en la gestión integral de instalaciones acuáticas de alto nivel en Ibiza. 
Combinamos tecnología de vanguardia con un servicio técnico riguroso.
</div>
""", unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# BLOQUES TÉCNICOS
col1, col2 = st.columns(2)
with col1:
    st.markdown("<div class='service-box'><strong>💎 Mantenimiento Preventivo</strong><br>Control químico automatizado y gestión de filtración.</div>", unsafe_allow_html=True)
    st.markdown("<div class='service-box'><strong>🧪 Tratamiento Avanzado</strong><br>Expertos en electrólisis salina e hidrólisis.</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='service-box'><strong>🔧 Ingeniería de Reparación</strong><br>Localización de fugas y sustitución de bombas.</div>", unsafe_allow_html=True)
    st.markdown("<div class='service-box'><strong>💡 Optimización Energética</strong><br>Iluminación LED y domótica para piscinas.</div>", unsafe_allow_html=True)

st.write("---")

# BOTONES FUNCIONALES
st.subheader("Contacto Directo")

# WhatsApp funciona con tu número 661764402
st.markdown('<a href="https://wa.me/34661764402?text=Hola%20Piscinas%20Leah,%20deseo%20solicitar%20presupuesto" class="btn-contact whatsapp-btn">💬 Contactar por WhatsApp</a>', unsafe_allow_html=True)

# Email
st.markdown('<a href="mailto:piscinasleah@gmail.com" class="btn-contact email-btn">✉️ Enviar Correo Electrónico</a>', unsafe_allow_html=True)

st.write("<br>", unsafe_allow_html=True)

# BOTÓN URGENCIA
st.markdown('<a href="https://wa.me/34661764402?text=URGENTE:%20Aviso%20de%20avería" class="btn-contact urgent-btn">🚨 ASISTENCIA TÉCNICA URGENTE 24H</a>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: white; padding: 20px;'>© 2024 Piscinas Leah Ibiza | Servicio Oficial</p>", unsafe_allow_html=True)
