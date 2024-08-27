import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Katalóg výsledkov experimentálneho vzdelávania a inovácií", page_icon=":spiral_note_pad:")
st.logo("logo-minedu-sk.svg", link='https://www.minedu.sk/katalog-vysledkov-experimentalneho-overovania-a-inovacii-vo-vychove-a-vzdelavani/')

def obsah_katalogu():
    st.subheader('Katalóg výsledkov experimentálneho overovania a inovácií vo výchove a vzdelávaní', divider=True)

    # Search
    query = st.sidebar.text_input('Vyhľadávanie', '', key=1)

    # Selectbox
    druhy_inovacii = ['Všetky', 'Výchovno-vzdelávacie programy',
                      'Formy, metódy a prostriedky výchovy a vzdelávania',
                      'Formy a spôsoby hodnotenia detí a žiakov', 'Koncepcie inkluzívneho vzdelávania',
                      'Formy riadenia škôl a školských zariadení', 'Preventívne a rozvojové programy']

    stupne_vzdelania = ['Všetky', 'Predprimárne', 'Základné vzdelanie', 'Stredné vzdelanie', 'Vyššie odborné vzdelanie']

    s_zameranie = st.sidebar.selectbox('Obsahové zameranie inovácie', ['Všetky'], index=0)
    s_druh = st.sidebar.selectbox('Druh inovácie', druhy_inovacii, index=0)
    s_skupina = st.sidebar.selectbox('Stupeň vzdelania', stupne_vzdelania, index=0)

    # Results
    st.info('Katalóg je aktuálne prázdny. Tešíme sa na vaše žiadosti o pridanie inovácie do katalógu.')

    # Title
    st.page_link(label="Nová žiadosť", page=page2,
                    help='Formulár žiadosti o zápis inovácie do katalógu výsledkov experimentálneho overovania a inovácií vo výchove a vzdelávaní',
                    icon=":material/add:",
                    use_container_width=True)

def nova_ziadost():
    iframe_src = "https://www.cognitoforms.com/m%C5%A1vva%C5%A1sr1/%C5%BEiados%C5%A5oz%C3%A1pisinov%C3%A1cievov%C3%BDchoveavzdel%C3%A1van%C3%ADdokatal%C3%B3guv%C3%BDsledkovexperiment%C3%A1lnehooverovaniaainov%C3%A1ci%C3%AD1"
    st.components.v1.iframe(iframe_src, height=1000, scrolling=True)

page1 = st.Page(obsah_katalogu, title="Zoznam inovácií", icon=":material/view_list:")
page2 = st.Page(nova_ziadost, title="Nová žiadosť", icon=":material/add:")
pages = [page1, page2]

pg = st.navigation(pages)
pg.run()

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

