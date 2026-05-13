import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title("📊 Dashboard")
st.markdown("---")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Receita Total", "R$ 128.500", "+12.5%")
with col2:
    st.metric("Usuários Ativos", "1.482", "+8.3%")
with col3:
    st.metric("Taxa de Conversão", "3.24%", "-0.5%")
with col4:
    st.metric("Ticket Médio", "R$ 287", "+5.1%")

st.markdown("---")

chart_data = pd.DataFrame(
    np.random.randn(30, 3),
    columns=["Vendas", "Visitas", "Conversões"],
    index=pd.date_range(
        start=datetime(2026, 4, 1), periods=30, freq="D"
    ).strftime("%d/%m"),
)

st.subheader("Desempenho Diário")
st.line_chart(chart_data)

st.markdown("---")

col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Distribuição por Categoria")
    categories = pd.DataFrame(
        {
            "Categoria": ["Produto A", "Produto B", "Produto C", "Produto D"],
            "Valor": [45, 30, 15, 10],
        }
    )
    st.bar_chart(categories.set_index("Categoria"))

with col_b:
    st.subheader("Últimas Transações")
    transactions = pd.DataFrame(
        {
            "Data": pd.date_range(end=datetime.today(), periods=5, freq="h").strftime(
                "%H:%M"
            ),
            "Cliente": [f"Cliente {i}" for i in range(1, 6)],
            "Valor": np.random.randint(50, 500, 5),
        }
    )
    st.dataframe(transactions, hide_index=True, use_container_width=True)
