''' Script para as ontologias '''

from owlready2 import *

onto = get_ontology('http://prototipo/dsi.owl')

with onto:

    # Classes principais
    class usuario(Thing): pass
    class assunto(Thing): pass
    class idioma(Thing): pass

    # Propriedades de objeto
    class temInteresse(ObjectProperty):
        domain = [usuario]
        range = [assunto]

    class falaIdioma(ObjectProperty):
        domain = [usuario]
        range = [assunto]

    # Propriedade dos dados
    class rotuloPT(DataProperty):
        domain = [usuario]
        range = [idioma]

    class rotuloEN(DataProperty):
        domain = [usuario]
        range = [idioma]

# Idiomas

pt = idioma('portugues')
en = idioma('ingles')

# Assuntos

data_mining = assunto('data_mining')
data_mining.rotuloPT('mineração de dados')
data_mining.rotuloPT('mineracao de dados')
data_mining.rotuloEN('data mining')

sem_web = assunto('semantic_web')
sem_web.rotuloPT('web semantica')
sem_web.rotuloEN('semantic web')

big_data = assunto('big_data')
big_data.rotuloPT('grandes dados')
big_data.rotuloEN('big data')

info_sci = assunto('information_science')
info_sci.rotuloPT('ciência da informação')
info_sci.rotuloPT('ciencia da informacao')
info_sci.rotuloEN('information science')

# Usuários

pesquisador = usuario('Pesquisador Teste')
pesquisador.temInteresse = [data_mining, sem_web, big_data, info_sci]
pesquisador.falaIdioma = [pt, en]

onto.save(file="perfis.rdf", format="rdfxml")

# Leitura (o que seu programa já faz)
onto2 = get_ontology("file://perfis.rdf").load()
p = onto2.Pesquisador_2
print([a.rotuloPT for a in p.temInteresse])