import streamlit as st

# Configuración de la pestaña
st.set_page_config(
    page_title="Piscinas Leah Ibiza | Servicio Premium",
    page_icon="🏊‍♂️",
    layout="centered"
)

# --- DISEÑO DE LUJO (CSS AVANZADO) ---
st.markdown("""
    <style>
    /* Imagen de fondo de piscina que cubre toda la pantalla */
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                    url('https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99?auto=format&fit=crop&q=80&w=2000');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Caja de cristal para el contenido */
    .glass-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        padding: 30px;
        margin-bottom: 20px;
        color: white;
    }

    h1, h2, h3 {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        text-align: center;
    }

    /* Botones Premium */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background: linear-gradient(135deg, #00d4ff 0%, #004a99 100%);
        color: white;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        font-size: 18px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,212,255,0.4);
        color: #ffffff;
    }

    /* Botón de Urgencia */
    .urgent-btn>div>button {
        background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%) !important;
        height: 4.5em !important;
        font-size: 20px !important;
    }

    .service-box {
        background: rgba(0, 0, 0, 0.3);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid #00d4ff;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO DE LA PÁGINA ---

# Espaciado superior
st.markdown("<br><br>", unsafe_allow_html=True)

with st.container():
    st.markdown("""
        <div class="glass-card">
            <h1>PISCINAS LEAH IBIZA</h1>
            <p style='text-align: center; font-size: 1.3em; font-weight: bold; color: #00d4ff;'>
                Mantenimiento de Excelencia & Servicio Técnico Especializado
            </p>
            <p style='text-align: center; font-style: italic;'>
                Expertos en el cuidado de aguas cristalinas en toda la isla de Ibiza.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Sección de Servicios Detallada
with st.container():
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.subheader("Nuestros Servicios Profesionales")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class='service-box'>
                <strong>💎 Mantenimiento Integral</strong><br>
                Limpieza profunda, control químico y supervisión técnica constante.
            </div>
            <div class='service-box'>
                <strong>🌊 Tratamiento de Sal e Hidrólisis</strong><br>
                Especialistas en sistemas modernos para el máximo confort.
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div class='service-box'>
                <strong>🔧 Servicio Técnico Oficial</strong><br>
                Reparación de maquinaria, bombas y localización de fugas.
            </div>
            <div class='service-box'>
                <strong>✨ Iluminación y Reformas</strong><br>
                Actualización de focos LED y mejoras estéticas.
            </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Botones de Contacto
st.markdown("<h3 style='color: white;'>¿Hablamos de su piscina?</h3>", unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    if st.button("💬 WhatsApp Directo"):
        st.components.v1.html("<script>window.open('https://wa.me/34661764402?text=Hola,%20solicito%20información%20profesional')</script>")
with c2:
    if st.button("✉️ Correo Electrónico"):
        st.components.v1.html("<script>window.location.href='mailto:piscinasleah@gmail.com'</script>")

# Botón de Urgencia Destacado
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="urgent-btn">', unsafe_allow_html=True)
if st.button("🚨 AVISO DE AVERÍA URGENTE 24H"):
    st.components.v1.html("<script>window.open('https://wa.me/34661764402?text=URGENTE:%20Avería%20en%20piscina')</script>")
st.markdown('</div>', unsafe_allow_html=True)

# Pie de página
st.markdown("""
    <br><br>
    <div style='text-align: center; color: rgba(255,255,255,0.7); font-size: 0.9em; padding: 20px;'>
        © 2026 Piscinas Leah Ibiza | Calidad y Compromiso.<br>
        📍 Servicio en toda la isla.
    </div>
""", unsafe_allow_html=True)
