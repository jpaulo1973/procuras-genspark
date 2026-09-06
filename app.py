from datetime import datetime
import streamlit as st

st.set_page_config(page_title="Procuras - Gerador Genspark", layout="wide")

st.title("🏡 Procuras — Gerador de Prompts Imobiliários")
st.subheader("Crie prompts avançados para pesquisa exaustiva no Genspark")

# --- FORMULÁRIO DE ENTRADA ---
with st.form("client_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**1. Identificação e Orçamento**")
        nome_cliente = st.text_input("Nome do Cliente", value="Luís Cortes")
        finalidade = st.selectbox(
            "Finalidade", ["Habitação Própria Permanente (HPP)", "Investimento"]
        )
        orcamento_max = st.number_input(
            "Orçamento Máximo (€)", value=550000, step=10000
        )
        tipologia_min = st.selectbox(
            "Tipologia Mínima", ["T1", "T2", "T3", "T4"], index=1
        )

    with col2:
        st.markdown("**2. Localização e Estado**")
        concelhos = st.text_input(
            "Concelhos (separados por vírgula)", value="Alcochete, Montijo"
        )
        estado_imovel = st.multiselect(
            "Estado do Imóvel",
            ["Novo", "Semi-novo", "Usado em bom estado", "Para obras"],
            default=["Novo", "Semi-novo"],
        )
        idade_pref = st.text_input("Preferência de Idade", value="2 a 3 anos")

    with col3:
        st.markdown("**3. Requisitos Obrigatórios**")
        espaco_exterior = st.text_input(
            "Espaço Exterior",
            value="Varanda, terraço ou espaço exterior com dimensão real",
        )
        estacionamento = st.selectbox(
            "Estacionamento",
            [
                "Obrigatório (Garagem fechada ou privativo)",
                "Opcional",
                "Não necessário",
            ],
        )
        data_pesquisa = st.text_input(
            "Data da Pesquisa", value=datetime.now().strftime("%d de %B de %Y")
        )

    submitted = st.form_submit_button("🔥 Gerar Prompt para Genspark")

# --- GERAÇÃO DO PROMPT ---
if submitted:
    prompt_gerado = f"""Atua como um investigador imobiliário especializado no mercado residencial português, com foco nos concelhos de {concelhos}.
Preciso de realizar uma pesquisa exaustiva de imóveis atualmente disponíveis para compra para o cliente {nome_cliente}.

PERFIL DO CLIENTE
Finalidade: {finalidade}.
Localização: exclusivamente nos concelhos de {concelhos}.
Tipologia mínima: {tipologia_min}.
Preferência: Tipologia superior caso apresente boa relação qualidade/preço.
Estado: {', '.join(estado_imovel)}.
Preferência de idade: aproximadamente {idade_pref}.
Imóveis usados com mais idade podem ser considerados apenas quando estejam em excelente estado de conservação, tenham características claramente superiores e mantenham elevada adequação ao perfil.
O imóvel deve estar em bom ou excelente estado de conservação e pronto a habitar, sem necessidade evidente de obras.
Orçamento máximo: €{orcamento_max:,.2f}.
Varanda ou espaço exterior: {espaco_exterior}.
Estacionamento: {estacionamento}.
Áreas: privilegiar imóveis com boas áreas interiores, boa distribuição e espaços funcionais.
Valorizar especialmente: qualidade construtiva, luminosidade, exposição solar, dimensão e qualidade do espaço exterior, estacionamento, arrumação, eficiência energética, qualidade das zonas comuns, localização e relação qualidade/preço.

ÁREA GEOGRÁFICA
Pesquisar todo o território dos seguintes concelhos: {concelhos}.
Pesquisar também as diferentes freguesias e localidades pertencentes a estes concelhos. Não incluir imóveis localizados fora destes concelhos.

FONTES A PESQUISAR
Realizar pesquisa ampla em: Idealista, Imovirtual, Casa Sapo, SUPERCASA, OLX Imóveis, sites de agências imobiliárias e promotores locais.

CRITÉRIOS DE EXCLUSÃO
Excluir: imóveis acima de €{orcamento_max:,.2f}, abaixo de {tipologia_min}, que necessitem de obras, sem estacionamento, sem espaço exterior relevante, destinados a arrendamento/AL ou com informação insuficiente.

DADOS A APRESENTAR
Para cada imóvel: Ranking (0-100), Preço, Localidade, Freguesia, Tipologia, Área bruta/útil, Área exterior, Estacionamento, Ano de construção, Piso, Elevador, Exposição solar, Estado, Eficiência energética, Pontos fortes/fracos, Preço/m², Link direto, Fonte e Data de verificação.

SHORTLIST FINAL
Apresentar: TOP 10 Melhores Oportunidades, TOP 5 Qualidade/Preço, TOP 5 Opções HPP, TOP 5 Espaço Exterior, TOP 5 Tipologias Superiores, Oportunidades Prioritárias e Imóveis a Evitar.

ANÁLISE COMPARATIVA DO MERCADO E CONCLUSÃO
Analisar a oferta entre as zonas pesquisadas (preço/m², oferta disponível, variação de preços) e terminar com a seleção dos 5 MELHORES IMÓVEIS para apresentar ao cliente, justificando a escolha para visita.
Data da pesquisa: {data_pesquisa}."""

    st.success("Prompt gerado com sucesso!")
    st.text_area("Copia o texto abaixo e cola no Genspark:", prompt_gerado, height=450)
