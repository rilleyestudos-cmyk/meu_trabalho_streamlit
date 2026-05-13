import streamlit as st

st.set_page_config(
    page_title="Meu Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
    .landing-title {
        font-size: 48px;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 16px;
    }
    .landing-title span {
        background: linear-gradient(135deg, #6C63FF, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .landing-subtitle {
        font-size: 18px;
        color: #a0a0b8;
        line-height: 1.7;
        margin-bottom: 32px;
        max-width: 520px;
    }
    .badge {
        display: inline-block;
        padding: 6px 16px;
        border-radius: 20px;
        background: rgba(108,99,255,.15);
        color: #a78bfa;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 20px;
    }
    .feature-card {
        background: rgba(255,255,255,.03);
        border: 1px solid rgba(255,255,255,.06);
        border-radius: 14px;
        padding: 28px;
        transition: all .2s;
        text-align: center;
    }
    .feature-card:hover {
        border-color: rgba(108,99,255,.3);
        transform: translateY(-4px);
    }
    .feature-icon { font-size: 28px; margin-bottom: 16px; }
    .feature-card h3 { font-size: 18px; font-weight: 600; margin-bottom: 8px; }
    .feature-card p { font-size: 14px; color: #a0a0b8; line-height: 1.6; }
    .mockup {
        background: linear-gradient(145deg, #1a1a2e, #16213e);
        border-radius: 16px;
        padding: 24px;
        border: 1px solid rgba(255,255,255,.06);
        box-shadow: 0 20px 60px rgba(0,0,0,.5);
    }
    .mockup-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
    }
    .mockup-grid .card {
        background: rgba(255,255,255,.04);
        border-radius: 10px;
        padding: 16px;
    }
    .mockup-grid .card .m-value { font-size: 22px; font-weight: 700; }
    .mockup-grid .card .m-label { font-size: 12px; color: #a0a0b8; margin-top: 4px; }
    .mockup-grid .card .m-bar {
        height: 4px;
        border-radius: 4px;
        margin-top: 10px;
        background: linear-gradient(90deg, #6C63FF, transparent);
    }
    .footer-text {
        text-align: center;
        padding: 32px 0;
        color: #666;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1])

with col_left:
    st.markdown('<div class="badge">📈 Dashboard Interativo</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="landing-title">Seus dados em <span>tempo real</span></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="landing-subtitle">Dashboard completo com métricas de desempenho, gráficos dinâmicos e análises inteligentes para suas decisões de negócio.</div>',
        unsafe_allow_html=True,
    )
    if st.button("🚀 Acessar Dashboard", type="primary", use_container_width=True):
        st.switch_page("pages/dashboard")

with col_right:
    st.markdown("""
    <div class="mockup">
        <div class="mockup-grid">
            <div class="card">
                <div class="m-value">R$ 128.5K</div>
                <div class="m-label">Receita Total</div>
                <div class="m-bar" style="width:80%"></div>
            </div>
            <div class="card">
                <div class="m-value">1.482</div>
                <div class="m-label">Usuários Ativos</div>
                <div class="m-bar" style="width:60%"></div>
            </div>
            <div class="card">
                <div class="m-value">3.24%</div>
                <div class="m-label">Taxa Conversão</div>
                <div class="m-bar" style="width:40%"></div>
            </div>
            <div class="card">
                <div class="m-value">R$ 287</div>
                <div class="m-label">Ticket Médio</div>
                <div class="m-bar" style="width:70%"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("## Recursos do Dashboard")
cols = st.columns(3)

features = [
    ("📊", "Gráficos Dinâmicos", "Visualize vendas, visitas e conversões com gráficos interativos."),
    ("📈", "Métricas em Destaque", "Acompanhe receita total, usuários ativos e ticket médio."),
    ("📋", "Transações Recentes", "Acompanhe as últimas transações com detalhes de cliente e valor."),
    ("🎨", "Design Moderno", "Interface limpa e responsiva com tema personalizado."),
    ("☁️", "100% Online", "Hospedado no Streamlit Cloud com deploy automático via GitHub."),
    ("📱", "Responsivo", "Acesse de qualquer dispositivo com layout adaptável."),
]

for i, (icon, title, desc) in enumerate(features):
    with cols[i % 3]:
        st.markdown(
            f'<div class="feature-card">'
            f'<div class="feature-icon">{icon}</div>'
            f"<h3>{title}</h3>"
            f"<p>{desc}</p>"
            f"</div>",
            unsafe_allow_html=True,
        )

st.markdown("---")

st.markdown("## Pronto para explorar?")
st.markdown("Acesse o dashboard e veja seus dados em ação.")
if st.button("🚀 Acessar Dashboard Agora", type="primary"):
    st.switch_page("pages/dashboard")

st.markdown('<div class="footer-text">© 2026 Meu Dashboard. Feito com Streamlit.</div>', unsafe_allow_html=True)
