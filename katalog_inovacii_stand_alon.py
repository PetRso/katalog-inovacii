import streamlit as st
import streamlit.components.v1 as components
from streamlit.components.v1 import html

st.set_page_config(page_title="Katalóg výsledkov experimentálneho vzdelávania a inovácií", page_icon=":spiral_note_pad:")
st.logo("logo-minedu-sk.svg", link='https://www.minedu.sk/katalog-vysledkov-experimentalneho-overovania-a-inovacii-vo-vychove-a-vzdelavani/')

def obsah_katalogu():
    st.subheader('Katalóg výsledkov experimentálneho overovania a inovácií vo výchove a vzdelávaní', divider=True)

    # Search
    query = st.sidebar.text_input('Vyhľadávanie', '', key=1)

    # Selectbox
    druhy_inovacii = ['-', 'Výchovno-vzdelávacie programy',
                      'Formy, metódy a prostriedky výchovy a vzdelávania',
                      'Formy a spôsoby hodnotenia detí a žiakov', 'Koncepcie inkluzívneho vzdelávania',
                      'Formy riadenia škôl a školských zariadení', 'Preventívne a rozvojové programy']

    stupne_vzdelania = ['-', 'Predprimárne', 'Základné vzdelanie', 'Stredné vzdelanie', 'Vyššie odborné vzdelanie']

    s_zameranie = st.sidebar.selectbox('Obsahové zameranie inovácie', ['-'], index=0)
    s_druh = st.sidebar.selectbox('Druh inovácie', druhy_inovacii, index=0)
    s_skupina = st.sidebar.selectbox('Stupeň vzdelania', stupne_vzdelania, index=0)

    if 'Základné vzdelanie' in s_skupina:
        s_cyklus = st.sidebar.multiselect('Cyklus', ['1.','2.','3.'], default=['1.','2.','3.'], placeholder='Vyber možnosť')

    # Results
    st.info('Katalóg je aktuálne prázdny. Tešíme sa na vaše žiadosti o pridanie inovácie do katalógu.')

    # H1: Názov inovácie + (názov subjektu)
    # H2: Popis inovácie
    # H2: Obsahové zameranie inovácie
    # H2: Spôsob použitia inovácie
    # H2: Vymedzenie skupiny žiakov
    # H2: Aplikačná prax(ak je)

    # Title
    st.page_link(label="Nová žiadosť", page=page2,
                    help='Formulár žiadosti o zápis inovácie do katalógu výsledkov experimentálneho overovania a inovácií vo výchove a vzdelávaní',
                    icon=":material/add:",
                    use_container_width=True)

def nova_ziadost():
    # iframe_src = "https://www.cognitoforms.com/M%C5%A0VVa%C5%A0SR1/%C5%BDiados%C5%A5OZ%C3%A1pisInov%C3%A1cieVoV%C3%BDchoveAVzdel%C3%A1van%C3%ADDoKatal%C3%B3guV%C3%BDsledkovExperiment%C3%A1lnehoOverovaniaAInov%C3%A1ci%C3%AD"
    # st.components.v1.iframe(iframe_src, height=1200, scrolling=True)
    with open("ziadost_cognito_idsk2.html") as f:
        html(f.read(), height=1200, scrolling=True)

page1 = st.Page(obsah_katalogu, title="Zoznam inovácií", icon=":material/view_list:")
page2 = st.Page(nova_ziadost, title="Nová žiadosť", icon=":material/add:")
pages = [page1, page2]

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css('style.css')

pg = st.navigation(pages)
pg.run()

st.sidebar.caption("Aplikácia je beta verzia. V budúcnosti bude migrovaná do pripravovaného IS Systém na podporu reformy kurikula.")