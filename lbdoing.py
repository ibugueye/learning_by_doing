import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta

# Configuration de la page
st.set_page_config(
    page_title="Système Learning by Doing",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .department-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
    }
    .scenario-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border: 1px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

# Header principal
st.markdown('<h1 class="main-header">🎯 Système Learning by Doing</h1>', unsafe_allow_html=True)
st.markdown("### Plateforme Collaborative Inter-Départements")

# Sidebar pour la navigation
# Ajoutez cette nouvelle section dans votre code existant

# Mettre à jour la sidebar pour inclure les nouveaux cas




st.sidebar.title("📚 Navigation")
section = st.sidebar.radio(
    "Choisissez une section:",
    ["🏠 Accueil", "📊 Départements", "🔄 Interactions", "🍽️ Scénario Restaurant", "🚀 Business Plan IT", 
     "📈 Tableaux de Bord", "🎯 Évaluation", "💻 Cas IT & Dual", "🎓 Centre Formation"]
)
# Section Accueil
if section == "🏠 Accueil":
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("🌟 Présentation du Système")
        st.markdown("""
        ### Le Concept Learning by Doing
        
        Notre système transforme l'apprentissage théorique en expérience pratique grâce à :
        
        - **🎯 Projets réels** dans un environnement d'entreprise simulée
        - **🤝 Collaboration obligatoire** entre tous les départements
        - **📊 Outils professionnels** et indicateurs de performance
        - **🔄 Boucle d'amélioration continue** avec rétroaction
        
        ### L'Entreprise Virtuelle Collaborative
        
        Les apprenants sont répartis en 4 départements spécialisés qui doivent collaborer
        pour faire prospérer des entreprises virtuelles à travers des scénarios réalistes.
        """)
    
    with col2:
        st.image("https://cdn.pixabay.com/photo/2017/08/01/00/38/man-2562325_1280.jpg", 
                caption="Collaboration d'équipe", use_container_width=True)
    
    # Métriques globales
    st.subheader("📈 Métriques du Système")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Départements", "4", "Spécialisés")
    with col2:
        st.metric("Projets Actifs", "12", "+3 cette semaine")
    with col3:
        st.metric("Taux de Collaboration", "87%", "4% ↑")
    with col4:
        st.metric("Satisfaction", "4.5/5", "0.2 ↑")

# Section Départements
elif section == "📊 Départements":
    st.header("🏢 Les 4 Départements Spécialisés")
    
    tab1, tab2, tab3, tab4 = st.tabs(["💰 Comptabilité", "📢 Marketing", "🎯 Contrôle de Gestion", "💻 Informatique"])
    
    with tab1:
        st.markdown('<div class="department-card">', unsafe_allow_html=True)
        st.subheader("💰 Département Comptabilité & Finance")
        st.markdown("""
        ### 🎯 Missions Principales
        - Gestion de la trésorerie et comptabilité générale
        - Établissement des budgets prévisionnels
        - Analyse des coûts et calcul de rentabilité
        - Gestion de la paie et des déclarations fiscales
        
        ### 🛠️ Outils & Applications
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Tableau de Bord Financier** (Streamlit)
            - **Calculateur de Coûts** 
            - **Simulateur de Rentabilité**
            - **Gestionnaire de Trésorerie**
            """)
        
        with col2:
            # Exemple de graphique financier
            data = {
                'Mois': ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun'],
                'CA': [25000, 32000, 28000, 35000, 40000, 45000],
                'Charges': [18000, 22000, 20000, 25000, 28000, 30000]
            }
            df = pd.DataFrame(data)
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Chiffre d\'Affaires', x=df['Mois'], y=df['CA']))
            fig.add_trace(go.Bar(name='Charges', x=df['Mois'], y=df['Charges']))
            fig.update_layout(title='Évolution CA vs Charges', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div class="department-card">', unsafe_allow_html=True)
        st.subheader("📢 Département Marketing & Ventes")
        st.markdown("""
        ### 🎯 Missions Principales
        - Études de marché et analyse de la concurrence
        - Stratégie de marque et positionnement
        - Campagnes marketing digital et traditionnel
        - Relation client et fidélisation
        
        ### 🛠️ Outils & Applications
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Analyseur de Marché**
            - **Planificateur de Campagnes**
            - **Calculateur de ROI Marketing**
            - **Tableau de Bord Social Media**
            """)
        
        with col2:
            # Métriques marketing
            st.metric("ROI Campagnes", "245%", "15%")
            st.metric("Taux Conversion", "3.2%", "0.4%")
            st.metric("Coût Acquisition Client", "45€", "-5€")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab3:
        st.markdown('<div class="department-card">', unsafe_allow_html=True)
        st.subheader("🎯 Département Contrôle de Gestion")
        st.markdown("""
        ### 🎯 Missions Principales
        - Définition et suivi des KPI
        - Analyse des écarts budget/réel
        - Tableaux de bord de performance
        - Optimisation des processus
        
        ### 🛠️ Outils & Applications
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Tableau de Bord Global**
            - **Analyseur d'Écarts**
            - **Calculateur de KPI**
            - **Optimisateur de Processus**
            """)
        
        with col2:
            # KPI dashboard
            kpi_data = {
                'KPI': ['Marge Brute', 'Rotation Stock', 'Productivité', 'Satisfaction Client'],
                'Valeur': [72, 15, 85, 4.5],
                'Cible': [70, 12, 80, 4.3]
            }
            kpi_df = pd.DataFrame(kpi_data)
            st.dataframe(kpi_df, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab4:
        st.markdown('<div class="department-card">', unsafe_allow_html=True)
        st.subheader("💻 Département Informatique")
        st.markdown("""
        ### 🎯 Missions Principales
        - Développement d'applications métier
        - Gestion de l'infrastructure IT
        - Automatisation des processus
        - Support technique et formation
        
        ### 🛠️ Outils & Applications
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            - **Développement d'Applications**
            - **Gestionnaire de Projets IT**
            - **Outil d'Automatisation**
            - **Portail de Support**
            """)
        
        with col2:
            # Projets IT
            projets = {
                'Projet': ['Site Web', 'App Mobile', 'CRM', 'BI'],
                'Avancement': [90, 75, 60, 45],
                'Priorité': ['Haute', 'Haute', 'Moyenne', 'Basse']
            }
            projets_df = pd.DataFrame(projets)
            fig = px.bar(projets_df, x='Projet', y='Avancement', color='Priorité',
                        title='Avancement des Projets IT')
            st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

# Section Interactions
elif section == "🔄 Interactions":
    st.header("🤝 Interactions entre Départements")
    
    st.markdown("""
    ### Le Système de Collaboration
    
    Chaque projet nécessite la collaboration d'au moins 2 départements.
    Voici les interactions types :
    """)
    
    # Graphique des interactions
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("📋 Exemples d'Interactions")
        
        interactions = [
            {"Départements": "Marketing + Comptabilité", "Projet": "Fixation des prix", "Livrable": "Grille tarifaire optimisée"},
            {"Départements": "Comptabilité + Contrôle", "Projet": "Analyse de rentabilité", "Livrable": "Rapport d'écarts"},
            {"Départements": "Marketing + Informatique", "Projet": "Site e-commerce", "Livrable": "Plateforme de vente"},
            {"Départements": "Tous départements", "Projet": "Business Plan", "Livrable": "Plan stratégique complet"}
        ]
        
        for interaction in interactions:
            with st.expander(f"🔗 {interaction['Départements']} - {interaction['Projet']}"):
                st.write(f"**Livrable:** {interaction['Livrable']}")
                st.write("**Points de collaboration:**")
                st.write("- Réunions de coordination hebdomadaires")
                st.write("- Partage de données en temps réel")
                st.write("- Validation croisée des décisions")
    
    with col2:
        st.subheader("📊 Flux de Données")
        
        # Diagramme simplifié des flux
        flux_data = {
            'Source': ['Marketing', 'Marketing', 'Comptabilité', 'Comptabilité', 'Informatique'],
            'Destination': ['Comptabilité', 'Informatique', 'Contrôle', 'Informatique', 'Tous'],
            'Données': ['Données marché', 'Besoins fonctionnels', 'Données financières', 'Transactions', 'Applications']
        }
        flux_df = pd.DataFrame(flux_data)
        st.dataframe(flux_df, use_container_width=True)
        
        st.metric("Interactions/jour", "47", "12% ↑")
        st.metric("Projets transverses", "8", "2 nouveaux")

# Section Scénario Restaurant
elif section == "🍽️ Scénario Restaurant":
    st.header("🍽️ Scénario Complet: Restaurant 'La Table Collaborative'")
    
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Présentation", "💰 Comptabilité", "📢 Marketing", "🎯 Contrôle", "💻 Informatique"])
    
    with tab1:
        st.subheader("🎯 Présentation du Scénario")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            ### Contexte
            **Restaurant 'La Table Collaborative'**
            - Cuisine bistronomique
            - 40 couverts
            - Quartier mixte bureaux/résidentiel
            - CA cible : 430 000€/an
            
            ### Objectifs Pédagogiques
            - Comprendre l'interdépendance des fonctions
            - Maîtriser les outils de gestion
            - Développer l'esprit d'équipe
            - Prendre des décisions data-driven
            """)
        
        with col2:
            # Chiffres clés
            st.subheader("📊 Chiffres Clés")
            indicateurs = {
                'Investissement initial': '100 000€',
                'Charges fixes/mois': '16 858€',
                'Seuil rentabilité': '23 414€ CA/mois',
                'Panier moyen visé': '22€',
                'Couverts/jour objectif': '75'
            }
            
            for indicateur, valeur in indicateurs.items():
                st.write(f"**{indicateur}:** {valeur}")
    
    with tab2:
        st.subheader("💰 Application Comptabilité")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Calculateur de Coûts")
            
            # Inputs pour le calcul de coûts
            prix_vente = st.number_input("Prix de vente (€)", min_value=5.0, max_value=50.0, value=16.5, step=0.5)
            cout_matiere = st.number_input("Coût matières (€)", min_value=1.0, max_value=20.0, value=4.2, step=0.1)
            cout_main_oeuvre = st.number_input("Coût main d'œuvre (€)", min_value=1.0, max_value=10.0, value=2.5, step=0.1)
            cout_autres = st.number_input("Autres coûts (€)", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
            
            if st.button("Calculer la Rentabilité"):
                cout_total = cout_matiere + cout_main_oeuvre + cout_autres
                marge = prix_vente - cout_total
                taux_marge = (marge / prix_vente) * 100
                
                st.success(f"""
                **Résultat:**
                - Marge brute: {marge:.2f}€
                - Taux de marge: {taux_marge:.1f}%
                - Coût total: {cout_total:.2f}€
                """)
        
        with col2:
            st.markdown("### Simulateur de Trésorerie")
            
            ca_mensuel = st.number_input("CA Mensuel (€)", min_value=10000, max_value=100000, value=35000)
            charges_mensuelles = st.number_input("Charges Mensuelles (€)", min_value=5000, max_value=50000, value=16858)
            
            resultat = ca_mensuel - charges_mensuelles
            trésorerie = resultat * 12  # Simplification
            
            fig = go.Figure(go.Indicator(
                mode = "gauge+number+delta",
                value = resultat,
                domain = {'x': [0, 1], 'y': [0, 1]},
                title = {'text': "Résultat Mensuel"},
                delta = {'reference': 0},
                gauge = {
                    'axis': {'range': [-10000, 20000]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [-10000, 0], 'color': "red"},
                        {'range': [0, 10000], 'color': "yellow"},
                        {'range': [10000, 20000], 'color': "green"}]
                }
            ))
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("📢 Application Marketing")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Calculateur de ROI Marketing")
            
            budget_campagne = st.number_input("Budget campagne (€)", min_value=500, max_value=10000, value=2000)
            nouveaux_clients = st.number_input("Nombre nouveaux clients", min_value=10, max_value=500, value=80)
            panier_moyen = st.number_input("Panier moyen (€)", min_value=10, max_value=50, value=22)
            taux_fidelisation = st.slider("Taux de fidélisation (%)", 0, 100, 30)
            
            if st.button("Calculer ROI"):
                ca_genere = nouveaux_clients * panier_moyen * (1 + taux_fidelisation/100)
                roi = ((ca_genere - budget_campagne) / budget_campagne) * 100
                
                st.metric("ROI Campagne", f"{roi:.1f}%")
                st.metric("CA Généré", f"{ca_genere:.0f}€")
        
        with col2:
            st.markdown("### Analyse de Marché")
            
            segments = ['Jeunes actifs', 'Familles', 'Seniors', 'Professionnels']
            parts_marche = [35, 25, 20, 20]
            
            fig = px.pie(values=parts_marche, names=segments, title="Répartition Clientèle")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        st.subheader("🎯 Application Contrôle de Gestion")
        
        st.markdown("### Tableau de Bord des KPI")
        
        # KPI dynamiques
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            marge_brute = st.slider("Marge brute (%)", 50, 90, 72)
            st.metric("Marge Brute", f"{marge_brute}%", "2%")
        
        with col2:
            rotation_stock = st.slider("Rotation stock (jours)", 5, 30, 15)
            st.metric("Rotation Stock", f"{rotation_stock}j", "-2j")
        
        with col3:
            productivite = st.slider("Productivité (%)", 50, 100, 85)
            st.metric("Productivité", f"{productivite}%", "5%")
        
        with col4:
            satisfaction = st.slider("Satisfaction client (/5)", 3.0, 5.0, 4.5)
            st.metric("Satisfaction", f"{satisfaction}/5", "0.2")
        
        # Graphique de performance
        kpis = ['Marge', 'Rotation', 'Productivité', 'Satisfaction']
        valeurs = [marge_brute, rotation_stock, productivite, satisfaction * 20]  # Normalisé
        cibles = [70, 12, 80, 86]  # 4.3/5 = 86%
        
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(
            r=valeurs,
            theta=kpis,
            fill='toself',
            name='Performance Réelle'
        ))
        fig.add_trace(go.Scatterpolar(
            r=cibles,
            theta=kpis,
            fill='toself',
            name='Objectifs'
        ))
        fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.subheader("💻 Application Informatique")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### Gestion des Projets IT")
            
            projets = {
                'Projet': ['Site Web', 'App Mobile', 'Système Résa', 'Tableau Bord'],
                'Équipe': ['2 dev', '3 dev', '1 dev', '1 dev + 1 data'],
                'Budget': [8000, 12000, 5000, 6000],
                'Délai (semaines)': [6, 8, 4, 5]
            }
            
            projets_df = pd.DataFrame(projets)
            st.dataframe(projets_df, use_container_width=True)
        
        with col2:
            st.markdown("### Calculateur de Rentabilité IT")
            
            investissement = st.number_input("Investissement IT (€)", min_value=1000, max_value=50000, value=15000)
            gain_temps = st.number_input("Gain temps (h/semaine)", min_value=5, max_value=40, value=20)
            cout_horaire = st.number_input("Coût horaire moyen (€)", min_value=15, max_value=50, value=25)
            
            if st.button("Calculer Rentabilité IT"):
                gain_annuel = gain_temps * cout_horaire * 52
                roi_annuel = (gain_annuel - investissement) / investissement * 100
                amortissement = investissement / gain_annuel * 12
                
                st.metric("Gain Annuel", f"{gain_annuel:.0f}€")
                st.metric("ROI Annuel", f"{roi_annuel:.1f}%")
                st.metric("Amortissement", f"{amortissement:.1f} mois")

# Section Tableaux de Bord
elif section == "📈 Tableaux de Bord":
    st.header("📈 Tableaux de Bord Interactifs")
    
    tab1, tab2, tab3 = st.tabs(["📊 Performance Globale", "🔗 Collaboration", "🎯 Projets"])
    
    with tab1:
        st.subheader("Tableau de Bord de Performance")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Graphique d'évolution du CA
            mois = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun']
            ca_reel = [25000, 32000, 28000, 35000, 40000, 45000]
            ca_objectif = [30000, 32000, 34000, 36000, 38000, 40000]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=mois, y=ca_reel, mode='lines+markers', name='CA Réel'))
            fig.add_trace(go.Scatter(x=mois, y=ca_objectif, mode='lines+markers', name='Objectif'))
            fig.update_layout(title='Évolution du Chiffre d\'Affaires')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Graphique de répartition des coûts
            categories = ['Personnel', 'Matières', 'Loyer', 'Marketing', 'Autres']
            valeurs = [10800, 12040, 3000, 1600, 1500]
            
            fig = px.pie(values=valeurs, names=categories, title="Répartition des Charges Mensuelles")
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Tableau de Bord Collaboration")
        
        # Matrice des interactions
        st.markdown("### Matrice des Interactions Départementales")
        
        data = {
            'Département': ['Marketing', 'Comptabilité', 'Contrôle', 'Informatique'],
            'Marketing': [0, 15, 8, 12],
            'Comptabilité': [15, 0, 20, 10],
            'Contrôle': [8, 20, 0, 15],
            'Informatique': [12, 10, 15, 0]
        }
        
        df = pd.DataFrame(data).set_index('Département')
        st.dataframe(df, use_container_width=True)
        
        st.metric("Taux de Collaboration Global", "87%", "4% ↑")
        st.metric("Projets Transverses Actifs", "8", "+2")

# Section Évaluation
elif section == "🎯 Évaluation":
    st.header("🎯 Système d'Évaluation")
    
    st.markdown("""
    ### Grille d'Évaluation Complète
    
    L'évaluation se fait sur 4 axes principaux :
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 📊 Performance Individuelle (40%)
        - Maîtrise des concepts métier
        - Qualité du travail produit
        - Respect des délais
        - Capacité d'analyse
        
        #### 🤝 Collaboration (30%)
        - Participation active aux réunions
        - Qualité des échanges
        - Respect des engagements
        - Contribution au collectif
        """)
    
    with col2:
        st.markdown("""
        #### 💡 Innovation (20%)
        - Proposition d'idées nouvelles
        - Amélioration des processus
        - Résolution créative de problèmes
        - Adaptation au changement
        
        #### 📈 Résultats (10%)
        - Atteinte des objectifs
        - Impact sur la performance globale
        - Qualité des livrables
        - Satisfaction client
        """)
    
    # Calculateur de note
    st.subheader("🔢 Calculateur de Note Finale")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        perf_indiv = st.slider("Performance Individuelle", 0, 20, 16)
    with col2:
        collaboration = st.slider("Collaboration", 0, 20, 15)
    with col3:
        innovation = st.slider("Innovation", 0, 20, 14)
    with col4:
        resultats = st.slider("Résultats", 0, 20, 17)
    
    note_finale = (perf_indiv * 0.4 + collaboration * 0.3 + innovation * 0.2 + resultats * 0.1)
    
    st.success(f"### Note Finale: {note_finale:.1f}/20")
    
    if note_finale >= 16:
        st.balloons()
        st.success("🌟 Excellence - Félicitations !")
    elif note_finale >= 14:
        st.success("✅ Très bon travail - Continue comme ça !")
    elif note_finale >= 12:
        st.info("📈 Bon potentiel - Quelques améliorations possibles")
    else:
        st.warning("📝 Besoin de progression - Plan d'action nécessaire")

elif section == "💻 Cas IT & Dual":
    
    st.header("💻 Études de Cas IT & Modèle Dual")
    
    tab1, tab2, tab3 = st.tabs(["🏢 Société de Services IT", "🔄 Modèle Dual IT/Restaurant", "📊 Comparatif Stratégique"])
    
    with tab1:
        st.subheader("🏢 Société de Services IT - Étude de Cas Complète")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 📋 Présentation du Cas
            **Création d'une société de services informatiques spécialisée** :
            - Développement d'applications sur mesure
            - Maintenance et infogérance
            - Conseil en transformation digitale
            - Solutions cloud et mobiles
            
            ### 🎯 Chiffres Clés du Business Plan
            """)
            
            # Métriques IT
            kpi_it = {
                'Indicateur': ['Investissement initial', 'CA Année 1', 'CA Année 2', 'CA Année 3', 
                              'Marge brute cible', 'Effectif année 1', 'Seuil rentabilité'],
                'Valeur': ['145,000€', '600,000€', '900,000€', '1,200,000€', '73%', '6 personnes', 'Mois 18']
            }
            st.dataframe(pd.DataFrame(kpi_it), use_container_width=True)
            
            st.markdown("""
            ### 🚀 Stratégie de Croissance
            - **Mois 1-6** : Acquisition premiers clients, développement IP
            - **Mois 7-12** : Scaling équipe, diversification services
            - **Année 2** : Internationalisation, produits propriétaires
            - **Année 3** : Leadership régional, levée de croissance
            """)
        
        with col2:
            # Graphique croissance CA IT
            annees = ['Année 1', 'Année 2', 'Année 3']
            ca_it = [600000, 900000, 1200000]
            fig = px.bar(x=annees, y=ca_it, title="Croissance CA Société IT",
                        labels={'x': 'Années', 'y': 'Chiffre d\'Affaires (€)'})
            fig.update_traces(marker_color='#00CC96')
            st.plotly_chart(fig, use_container_width=True)
            
            # Répartition du CA par service
            services = ['Développement', 'Maintenance', 'Conseil', 'Infogérance']
            repartition = [50, 30, 15, 5]
            fig = px.pie(values=repartition, names=services, 
                        title="Répartition CA par Service")
            st.plotly_chart(fig, use_container_width=True)
        
        # Calculateur de rentabilité IT
        st.markdown("### 🧮 Calculateur de Rentabilité IT")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            tjm_moyen = st.number_input("TJM Moyen (€)", min_value=300, max_value=1000, value=450)
            jours_factures = st.number_input("Jours facturés/mois", min_value=10, max_value=22, value=18)
        
        with col2:
            cout_operatif = st.number_input("Coût opératif/mois (€)", min_value=5000, max_value=30000, value=18500)
            marge_cible = st.slider("Marge cible (%)", 10, 50, 30)
        
        with col3:
            if st.button("📊 Calculer Rentabilité IT"):
                ca_mensuel = tjm_moyen * jours_factures
                resultat = ca_mensuel - cout_operatif
                marge_reelle = (resultat / ca_mensuel) * 100
                
                st.metric("CA Mensuel", f"{ca_mensuel:,.0f}€")
                st.metric("Résultat Mensuel", f"{resultat:,.0f}€")
                st.metric("Marge Réelle", f"{marge_reelle:.1f}%")
                
                if marge_reelle >= marge_cible:
                    st.success("🎯 Objectif de marge atteint !")
                else:
                    st.warning("⚠️ Marge inférieure à l'objectif")
    
    with tab2:
        st.subheader("🔄 Modèle Dual IT/Restaurant - Synergies Stratégiques")
        
        st.markdown("""
        ### 💡 Concept Innovant : Deux Activités, Une Synergie
        
        **Combinaison d'un restaurant traditionnel et d'une société de services IT** :
        - Mutualisation des compétences et ressources
        - Cycles de trésorerie complémentaires
        - Innovation croisée et partage de clients
        - Optimisation fiscale et financière
        """)
        
        # Tableau comparatif des deux activités
        st.markdown("### 📊 Comparatif des Deux Activités")
        
        comparatif_data = {
            'Aspect': ['Investissement initial', 'CA Année 1', 'Marge brute', 'BFR', 
                      'Cycle trésorerie', 'Croissance année 2', 'Rentabilité'],
            'Restaurant': ['241,675€', '1,170,000€', '71.2%', '+6,506€', 'Court', '+36%', 'Mois 8'],
            'Société IT': ['145,000€', '600,000€', '73.0%', '-34,500€', 'Long', '+50%', 'Mois 18'],
            'Synergie': ['-15% coûts', '+15% CA', '+2% points', '-28,000€', 'Équilibré', '+43%', 'Mois 6']
        }
        
        st.dataframe(pd.DataFrame(comparatif_data), use_container_width=True)
        
        # Graphique des synergies
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution du CA dual
            annees = ['Année 1', 'Année 2', 'Année 3']
            ca_resto = [1170000, 1595000, 1661000]
            ca_it = [600000, 900000, 1200000]
            ca_total = [1770000, 2495000, 2861000]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=annees, y=ca_resto, mode='lines+markers', 
                                   name='Restaurant', line=dict(color='#FFA15A')))
            fig.add_trace(go.Scatter(x=annees, y=ca_it, mode='lines+markers', 
                                   name='Société IT', line=dict(color='#00CC96')))
            fig.add_trace(go.Scatter(x=annees, y=ca_total, mode='lines+markers', 
                                   name='Total Dual', line=dict(color='#636EFA')))
            fig.update_layout(title='Évolution du CA Modèle Dual', height=400)
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Répartition du bénéfice
            st.markdown("### 📈 Répartition du Résultat")
            
            resultats = {
                'Activité': ['Restaurant seul', 'IT seul', 'Modèle Dual'],
                'Résultat Année 1': ['328,125€', '-32,580€', '499,581€'],
                'Résultat Année 2': ['505,962€', '75,420€', '758,905€'],
                'Croissance': ['+54%', 'N/A', '+52%']
            }
            
            st.dataframe(pd.DataFrame(resultats), use_container_width=True)
        
        # Calculateur de synergie duale
        st.markdown("### 🧮 Calculateur de Synergies Duales")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            ca_resto = st.number_input("CA Restaurant (k€)", min_value=100, max_value=2000, value=1170)
            ca_it = st.number_input("CA Société IT (k€)", min_value=100, max_value=1500, value=600)
        
        with col2:
            economies_mutualisation = st.slider("Économies mutualisation (%)", 5, 25, 15)
            conversion_croisee = st.slider("Conversion clients croisés (%)", 5, 30, 15)
        
        with col3:
            if st.button("🎯 Calculer Synergies"):
                ca_total = ca_resto + ca_it
                economies = (ca_total * economies_mutualisation / 100) / 10  # Conversion en k€
                ca_additionnel = (ca_resto * conversion_croisee / 1000) + (ca_it * conversion_croisee / 1000)
                ca_synergie = ca_total + ca_additionnel
                
                st.metric("CA Total Initial", f"{ca_total:,.0f} k€")
                st.metric("Économies Mutualisation", f"{economies:,.0f} k€")
                st.metric("CA Additionnel Croisé", f"{ca_additionnel:,.0f} k€")
                st.metric("CA avec Synergies", f"{ca_synergie:,.0f} k€")
                
                st.success(f"🚀 Gain de synergies : {((ca_synergie - ca_total) / ca_total * 100):.1f}%")
    
    with tab3:
        st.subheader("📊 Analyse Stratégique Comparative")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### ⚖️ Avantages du Modèle Dual")
            
            avantages = [
                "🛡️ **Risque diversifié** : Deux activités indépendantes",
                "💸 **Trésorerie optimisée** : BFR restaurant compense BFR IT",
                "🤝 **Synergies clients** : Base de données partagée",
                "🔄 **Innovation croisée** : Solutions IT testées en interne",
                "💰 **Optimisation fiscale** : Report de déficits possible",
                "🎯 **Résilience** : Moins sensible aux cycles économiques"
            ]
            
            for avantage in avantages:
                st.markdown(f"- {avantage}")
            
            st.markdown("### 📋 Défis à Maîtriser")
            
            defis = [
                "🎯 **Double expertise** nécessaire",
                "⚖️ **Répartition du temps** de direction",
                "📊 **Système de reporting** complexe",
                "👥 **Culture d'entreprise** duale à créer"
            ]
            
            for defi in defis:
                st.markdown(f"- {defi}")
        
        with col2:
            st.markdown("### 📈 Indicateurs de Performance Clés")
            
            # Radar chart des performances
            categories = ['Rentabilité', 'Croissance', 'Résilience', 'Innovation', 'Synergies']
            
            modele_resto = [7, 6, 5, 4, 3]
            modele_it = [5, 9, 4, 8, 3]
            modele_dual = [8, 8, 9, 7, 9]
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=modele_resto,
                theta=categories,
                fill='toself',
                name='Restaurant seul'
            ))
            fig.add_trace(go.Scatterpolar(
                r=modele_it,
                theta=categories,
                fill='toself',
                name='IT seul'
            ))
            fig.add_trace(go.Scatterpolar(
                r=modele_dual,
                theta=categories,
                fill='toself',
                name='Modèle Dual'
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 10]
                    )),
                showlegend=True,
                title="Comparaison des Modèles d'Affaires"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Recommandations stratégiques
        st.markdown("### 🎯 Recommandations Stratégiques")
        
        recommandations = {
            'Phase': ['Lancement (Mois 1-6)', 'Croissance (Mois 7-18)', 'Maturité (Mois 19+)'],
            'Actions Restaurant': [
                'Focus expérience client et qualité',
                'Digitalisation avec solutions internes',
                'Réplication du concept'
            ],
            'Actions IT': [
                'Développement solutions propriétaires',
                'Acquisition clients externes',
                'Internationalisation'
            ],
            'Actions Duales': [
                'Mise en place synergies opérationnelles',
                'Marketing croisé et CRM unifié',
                'Levée de croissance et scaling'
            ]
        }
        
        st.dataframe(pd.DataFrame(recommandations), use_container_width=True)
        
        # Calculateur d'investissement dual
        st.markdown("### 💰 Calculateur d'Investissement Dual")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            invest_resto = st.number_input("Invest. Restaurant (k€)", min_value=100, max_value=500, value=242)
            invest_it = st.number_input("Invest. IT (k€)", min_value=50, max_value=300, value=145)
        
        with col2:
            economies_duales = st.slider("Économies duales (%)", 5, 20, 15)
            levée_capital = st.number_input("Levée capital (k€)", min_value=0, max_value=500, value=200)
        
        with col3:
            if st.button("📊 Calculer Investissement"):
                invest_total = invest_resto + invest_it
                economies = invest_total * economies_duales / 100
                invest_net = invest_total - economies + levée_capital
                
                st.metric("Investissement Brut", f"{invest_total:,.0f} k€")
                st.metric("Économies Duales", f"{economies:,.0f} k€")
                st.metric("Levée Capital", f"{levée_capital:,.0f} k€")
                st.metric("Investissement Net", f"{invest_net:,.0f} k€")
                
                st.info(f"💡 L'effet de levier dual réduit l'investissement de {economies_duales}%")
 
elif section == "🚀 Business Plan IT":
    st.header("🚀 Business Plan Complet - Société de Services IT")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📋 Executive Summary", "💰 Investissements", "📈 Chiffre d'Affaires", 
                                                  "👥 Ressources Humaines", "📊 Compte de Résultat", "🎯 Analyse Stratégique"])
    
    with tab1:
        st.subheader("📋 Executive Summary - Société 'TechSolutions'")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 🎯 Présentation de l'Opportunité
            
            **Création d'une société de services informatiques B2B spécialisée dans :**
            - 🖥️ **Développement d'applications sur mesure**
            - ☁️ **Solutions cloud et infrastructure**
            - 📱 **Applications mobiles enterprise**
            - 🔧 **Maintenance et infogérance**
            
            ### 📊 Chiffres Clés du Business Plan
            """)
            
            # Métriques principales
            metrics_data = {
                'Indicateur': ['Investissement initial', 'CA Année 1', 'CA Année 3', 'Résultat Année 3', 
                              'Effectif final', 'Seuil rentabilité', 'ROI projet'],
                'Valeur': ['145,000€', '600,000€', '1,200,000€', '120,000€', '12 personnes', 'Mois 18', '82%']
            }
            st.dataframe(pd.DataFrame(metrics_data), use_container_width=True)
            
            st.markdown("""
            ### 🚀 Proposition de Valeur Unique
            
            **Différenciation stratégique :**
            - 🎯 **Expertise sectorielle** : solutions adaptées par métier
            - 🔄 **Modèle agile** : développement itératif et collaboratif
            - 💰 **Pricing flexible** : forfaits, régie, forfait + régie
            - 🌐 **Approche cloud-native** : solutions modernes et scalables
            """)
        
        with col2:
            # Graphique vision stratégique
            st.markdown("### 📈 Vision de Croissance")
            
            annees = ['Lancement', 'Année 1', 'Année 2', 'Année 3']
            ca_vision = [0, 600, 900, 1200]  # en k€
            effectif = [0, 6, 9, 12]
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=annees, y=ca_vision, mode='lines+markers', 
                                   name='CA (k€)', line=dict(color='#00CC96')))
            fig.add_trace(go.Scatter(x=annees, y=effectif, mode='lines+markers', 
                                   name='Effectif', line=dict(color='#636EFA'), yaxis='y2'))
            
            fig.update_layout(
                title='Projection Croissance CA et Effectif',
                yaxis=dict(title='CA (k€)'),
                yaxis2=dict(title='Effectif', overlaying='y', side='right')
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Quick metrics
            st.metric("💰 Marge Brute Cible", "73%", "3% vs marché")
            st.metric("🚀 Croissance Annuelle", "40%", "2x marché")
            st.metric("🎯 Taux Rétention Clients", "85%", "5% objectif")
     
    with tab2:
        st.subheader("💰 Plan d'Investissement IT Détaillé")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🖥️ Investissements Corporels")


            # CORRIGÉ : 6 éléments dans chaque colonne
            invest_corporels = {
                'Équipement': ['Serveurs...', 'Postes...', 'Équipements...', 'Périphériques', 'Salle serveur', 'Matériel télécom'],
                'Montant HT': [25000, 15000, 8000, 5000, 12000, 3000],  # 6 éléments
                'Calendrier': ['Mois 1', 'Mois 1-2', 'Mois 1', 'Mois 2', 'Mois 1', 'Mois 1']  # 6 éléments
            }
            
            
            df_corporels = pd.DataFrame(invest_corporels)
            df_corporels['Total'] = df_corporels['Montant HT'].sum()
            st.dataframe(df_corporels, use_container_width=True)
            
            total_corporels = df_corporels['Montant HT'].sum()
            st.metric("💰 Total Investissements Corporels", f"{total_corporels:,}€")
        
        with col2:
            st.markdown("### 💡 Investissements Incorporels")
            
            invest_incorporels = {
                'Actif': ['Licences logicielles', 'Développement IP', 'Brevet solution', 
                         'Marque déposée', 'Site web corporate', 'Base de données'],
                'Montant HT': [12000, 30000, 25000, 5000, 8000, 2000],
                'Amortissement': ['3 ans', '5 ans', '10 ans', '5 ans', '3 ans', '3 ans']
            }
            
            df_incorporels = pd.DataFrame(invest_incorporels)
            df_incorporels['Total'] = df_incorporels['Montant HT'].sum()
            st.dataframe(df_incorporels, use_container_width=True)
            
            total_incorporels = df_incorporels['Montant HT'].sum()
            st.metric("💡 Total Investissements Incorporels", f"{total_incorporels:,}€")
        
        # Calculateur d'investissement personnalisé
        st.markdown("### 🧮 Calculateur d'Investissement Personnalisé")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            nb_developers = st.slider("Nombre de développeurs", 1, 10, 3)
            nb_serveurs = st.slider("Serveurs nécessaires", 1, 5, 2)
        
        with col2:
            besoin_licences = st.selectbox("Pack licences", ['Basique', 'Standard', 'Premium'], index=1)
            developpement_ip = st.checkbox("Développement propriétaire", value=True)
        
        with col3:
            if st.button("📊 Calculer Investissement"):
                # Calculs basés sur les sélections
                cout_workstations = nb_developers * 5000
                cout_serveurs = nb_serveurs * 12500
                
                if besoin_licences == 'Basique':
                    cout_licences = 5000
                elif besoin_licences == 'Standard':
                    cout_licences = 12000
                else:
                    cout_licences = 25000
                
                cout_ip = 30000 if developpement_ip else 0
                
                invest_total = cout_workstations + cout_serveurs + cout_licences + cout_ip
                
                st.success(f"**💰 Investissement total estimé : {invest_total:,}€**")
                
                # Détail du calcul
                detail = {
                    'Poste': ['Postes de travail', 'Serveurs', 'Licences', 'Développement IP'],
                    'Montant': [cout_workstations, cout_serveurs, cout_licences, cout_ip]
                }
                st.dataframe(pd.DataFrame(detail), use_container_width=True)
    
    with tab3:
        st.subheader("📈 Prévisionnel Chiffre d'Affaires Détaillé")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💼 Structure du CA par Service")
            
            # CA par service et par année
            ca_services = {
                'Service': ['Développement sur mesure', 'Maintenance évolutive', 'Conseil stratégique', 
                           'Infogérance', 'Formation', 'Produits propriétaires'],
                'Année 1': [300000, 180000, 80000, 20000, 15000, 5000],
                'Année 2': [450000, 270000, 120000, 35000, 25000, 0],
                'Année 3': [600000, 360000, 150000, 50000, 30000, 10000]
            }
            
            df_ca = pd.DataFrame(ca_services)
            st.dataframe(df_ca, use_container_width=True)
            
            # Graphique évolution CA
            fig = px.bar(df_ca.melt(id_vars=['Service'], var_name='Année', value_name='CA'), 
                        x='Année', y='CA', color='Service', 
                        title='Évolution du CA par Service')
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 📊 Analyse de la Rentabilité par Service")
            
            # Marges par service
            marges_data = {
                'Service': ['Développement', 'Maintenance', 'Conseil', 'Infogérance', 'Formation'],
                'Marge Brute': [70.6, 77.8, 75.0, 73.3, 80.0],
                'Coût Direct': [25, 10, 30, 400, 15],  # €/h ou €/mois
                'Prix Vente': [85, 45, 120, 1500, 75]  # €/h ou €/mois
            }
            
            df_marges = pd.DataFrame(marges_data)
            st.dataframe(df_marges, use_container_width=True)
            
            # Calculateur de CA personnalisé
            st.markdown("### 🧮 Simulateur de CA Personnalisé")
            
            jours_dev = st.slider("Jours développement/mois", 10, 22, 16)
            clients_maintenance = st.slider("Clients maintenance", 5, 50, 15)
            jours_conseil = st.slider("Jours conseil/mois", 5, 15, 8)
            
            if st.button("📈 Calculer CA Potentiel"):
                ca_dev = jours_dev * 85 * 12
                ca_maint = clients_maintenance * 45 * 12
                ca_conseil = jours_conseil * 120 * 12
                ca_total = ca_dev + ca_maint + ca_conseil
                
                st.metric("💼 CA Développement", f"{ca_dev:,}€")
                st.metric("🔧 CA Maintenance", f"{ca_maint:,}€")
                st.metric("🎯 CA Conseil", f"{ca_conseil:,}€")
                st.metric("🚀 CA Total Annuel", f"{ca_total:,}€")
    
    with tab4:
        st.subheader("👥 Plan de Recrutement et Masse Salariale")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📋 Structure d'Équipe par Année")
            
            equipe_data = {
                'Poste': ['Développeur Senior', 'Développeur Junior', 'Tech Lead', 
                         'Commercial IT', 'Chef de Projet', 'Admin Système'],
                'Année 1': [2, 1, 0, 1, 1, 1],
                'Année 2': [3, 2, 1, 1, 2, 1],
                'Année 3': [4, 3, 1, 2, 2, 1]
            }
            
            df_equipe = pd.DataFrame(equipe_data)
            st.dataframe(df_equipe, use_container_width=True)
            
            # Graphique évolution effectif
            effectif_total = df_equipe[['Année 1', 'Année 2', 'Année 3']].sum()
            fig = px.line(x=effectif_total.index, y=effectif_total.values, 
                         title='Évolution des Effectifs', markers=True)
            fig.update_layout(yaxis_title="Nombre de collaborateurs")
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            st.markdown("### 💰 Structure des Rémunérations")
            
            salaires_data = {
                'Poste': ['Développeur Senior', 'Développeur Junior', 'Tech Lead', 
                         'Commercial IT', 'Chef de Projet', 'Admin Système'],
                'Salaire Brut': [4500, 3200, 5500, 3500, 5200, 3800],
                'Charges Patronales': [2025, 1440, 2475, 1575, 2340, 1710],
                'Coût Total': [6525, 4640, 7975, 5075, 7540, 5510]
            }
            
            df_salaires = pd.DataFrame(salaires_data)
            st.dataframe(df_salaires, use_container_width=True)
            
            # Calculateur de masse salariale
            st.markdown("### 🧮 Calculateur de Masse Salariale")
            
            col_a, col_b = st.columns(2)
            with col_a:
                nb_seniors = st.number_input("Dev Seniors", 0, 10, 2)
                nb_juniors = st.number_input("Dev Juniors", 0, 10, 1)
            with col_b:
                nb_techlead = st.number_input("Tech Leads", 0, 5, 0)
                nb_commerciaux = st.number_input("Commerciaux", 0, 5, 1)
            
            if st.button("💰 Calculer Masse Salariale"):
                cout_seniors = nb_seniors * 6525
                cout_juniors = nb_juniors * 4640
                cout_techlead = nb_techlead * 7975
                cout_commerciaux = nb_commerciaux * 5075
                
                masse_annuelle = (cout_seniors + cout_juniors + cout_techlead + cout_commerciaux) * 12
                
                st.metric("💵 Masse Salariale Annuelle", f"{masse_annuelle:,}€")
                st.info(f"📊 Représente {masse_annuelle/600000*100:.1f}% du CA année 1")
    
    with tab5:
        st.subheader("📊 Compte de Résultat Prévisionnel Détaillé")
        
        # Données du compte de résultat sur 3 ans
        resultat_data = {
            'Poste': ['Chiffre d\'Affaires HT', 'Coûts directs', 'MARGE BRUTE', 
                     'Charges personnel', 'Charges externes', 'Charges locatives',
                     'Dotations amortissements', 'EBE (Excédent Brut d\'Exploitation)',
                     'Charges financières', 'Résultat avant impôt', 'Impôt sur les sociétés',
                     'RESULTAT NET'],
            'Année 1': [600000, -162000, 438000, -247200, -58200, -18000,
                       -14059, 118541, -2839, 115702, -39704, 75998],
            'Année 2': [900000, -243000, 657000, -296640, -64020, -19800,
                       -16326, 260214, -2473, 257741, -85914, 171827],
            'Année 3': [1200000, -324000, 876000, -346080, -69840, -21600,
                       -19092, 420388, -2085, 418303, -139434, 278869]
        }
        
        df_resultat = pd.DataFrame(resultat_data)
        st.dataframe(df_resultat, use_container_width=True)
        
        # Analyse des ratios
        col1, col2, col3 = st.columns(3)
        
        with col1:
            marge_brute_1 = (resultat_data['Année 1'][2] / resultat_data['Année 1'][0]) * 100
            st.metric("📈 Marge Brute Année 1", f"{marge_brute_1:.1f}%")
        
        with col2:
            taux_croissance = ((resultat_data['Année 3'][0] - resultat_data['Année 1'][0]) / resultat_data['Année 1'][0]) * 100
            st.metric("🚀 Taux Croissance CA", f"{taux_croissance:.1f}%")
        
        with col3:
            renta_nette_3 = (resultat_data['Année 3'][11] / resultat_data['Année 3'][0]) * 100
            st.metric("💰 Rentabilité Nette Année 3", f"{renta_nette_3:.1f}%")
        
        # Graphiques d'analyse
        col1, col2 = st.columns(2)
        
        with col1:
            # Évolution de la rentabilité
            annees = ['Année 1', 'Année 2', 'Année 3']
            marges_brutes = [marge_brute_1, 73.0, 73.0]  # Simplifié
            resultats_nets = [12.7, 19.1, 23.2]  # En % du CA
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=annees, y=marges_brutes, mode='lines+markers', 
                                   name='Marge Brute (%)'))
            fig.add_trace(go.Scatter(x=annees, y=resultats_nets, mode='lines+markers', 
                                   name='Résultat Net (%)', yaxis='y2'))
            
            fig.update_layout(
                title='Évolution de la Rentabilité',
                yaxis=dict(title='Marge Brute (%)'),
                yaxis2=dict(title='Résultat Net (%)', overlaying='y', side='right')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Répartition des charges année 3
            charges_an3 = {
                'Type': ['Coûts directs', 'Personnel', 'Charges externes', 'Locatif', 'Amortissements'],
                'Montant': [324000, 346080, 69840, 21600, 19092]
            }
            
            fig = px.pie(charges_an3, values='Montant', names='Type', 
                        title='Répartition des Charges - Année 3')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab6:
        st.subheader("🎯 Analyse Stratégique et Plan d'Action")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📋 Analyse SWOT")
            
            swot_data = {
                'Forces': [
                    '🎯 Expertise technique pointue',
                    '💼 Équipe pluridisciplinaire',
                    '🚀 Méthodologie agile éprouvée',
                    '💰 Modèle économique scalable'
                ],
                'Faiblesses': [
                    '📛 Marque non connue au démarrage',
                    '👥 Effectif limité initialement',
                    '💸 Trésorerie de départ serrée',
                    '🌐 Réseau commercial à construire'
                ],
                'Opportunités': [
                    '📈 Digitalisation accélérée des entreprises',
                    '☁️ Migration massive vers le cloud',
                    '🎯 Spécialisation sur niches porteuses',
                    '🤝 Partenariats stratégiques possibles'
                ],
                'Menaces': [
                    '⚔️ Concurrence agressive des grands groupes',
                    '💸 Pression sur les prix',
                    '🔧 Évolution rapide des technologies',
                    '🌍 Conjoncture économique volatile'
                ]
            }
            
            for categorie, elements in swot_data.items():
                with st.expander(f"**{categorie}**"):
                    for element in elements:
                        st.write(f"- {element}")
        
        with col2:
            st.markdown("### 🗓️ Feuille de Route Opérationnelle")
            
            roadmap_data = {
                'Période': ['Mois 1-3', 'Mois 4-6', 'Mois 7-12', 'Année 2', 'Année 3'],
                'Objectifs Clés': [
                    'Installation, recrutement, premiers clients',
                    'Développement IP, processus qualité',
                    'Atteinte seuil rentabilité, scaling',
                    'Internationalisation, produits propriétaires',
                    'Leadership régional, levée croissance'
                ],
                'KPI à Suivre': [
                    '3 clients, 50k€ CA, équipe complète',
                    'Process qualité, 1 produit IP, 150k€ CA',
                    'Rentabilité, 5 clients récurrents',
                    '20% CA international, 2 produits',
                    '15% parts marché régional, 1.2M€ CA'
                ]
            }
            
            df_roadmap = pd.DataFrame(roadmap_data)
            st.dataframe(df_roadmap, use_container_width=True)
            
            # Calculateur de seuil de rentabilité
            st.markdown("### 🧮 Calculateur de Seuil de Rentabilité")
            
            charges_fixes = st.number_input("Charges fixes annuelles (€)", 100000, 500000, 247200)
            taux_marge = st.slider("Taux de marge brute (%)", 50, 90, 73)
            
            if st.button("🎯 Calculer Seuil"):
                seuil = charges_fixes / (taux_marge / 100)
                st.success(f"**💡 Seuil de rentabilité : {seuil:,.0f}€ de CA**")
                st.info(f"📅 Soit {seuil/12:,.0f}€ par mois")


# Nouvelle section Centre de Formation
elif section == "🎓 Centre Formation":
    st.header("🎓 Centre de Formation Multidisciplinaire 'SkillHub Academy'")
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🏫 Présentation", "📊 Gestion & Contrôle", "💻 Informatique & Data", 
                                                  "🏨 Hôtellerie", "📈 Business Plan", "🤝 Synergies"])
    
    with tab1:
        st.subheader("🏫 Présentation du Centre de Formation Multidisciplinaire")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 🎯 Concept Innovant
            
            **SkillHub Academy - Premier centre de formation intégrant 4 domaines d'excellence :**
            
            #### 📊 Management & Contrôle de Gestion
            - Formation des managers et contrôleurs de gestion
            - Certifications professionnelles reconnues
            - Conseil en optimisation organisationnelle
            
            #### 💻 Informatique & Data Science
            - Développement full-stack et DevOps
            - Data analyse, machine learning, IA
            - Cybersécurité et cloud computing
            
            #### 🏨 Hôtellerie & Tourisme
            - Management hôtelier et restauration
            - Service client d'excellence
            - Événementiel et tourisme durable
            
            #### 🎓 Pédagogie Innovante
            - Learning by doing avec cas réels
            - Plateforme collaborative inter-filières
            - Certification des compétences transverses
            """)
        
        with col2:
            st.image("https://cdn.pixabay.com/photo/2016/11/14/04/36/boy-1822559_1280.jpg", 
                    caption="Formation collaborative", use_container_width=True)
            
            # Chiffres clés
            st.metric("🏫 Campus", "1 site principal + 2 antennes")
            st.metric("🎓 Formations", "15 programmes certifiants")
            st.metric("👨‍🏫 Formateurs", "35 experts métiers")
            st.metric("📈 Taux insertion", "87% à 6 mois")
        
        # Vision stratégique
        st.markdown("### 🚀 Vision Stratégique 2024-2027")
        
        vision_data = {
            'Année': ['2024', '2025', '2026', '2027'],
            'Effectif Formés': [1200, 1800, 2500, 3200],
            'CA (k€)': [1800, 2600, 3500, 4500],
            'Taux Satisfaction': [88, 90, 92, 94],
            'Nouvelles Formations': [3, 4, 5, 6]
        }
        
        df_vision = pd.DataFrame(vision_data)
        st.dataframe(df_vision, use_container_width=True)
    
    with tab2:
        st.subheader("📊 Département Gestion & Contrôle de Gestion")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🎯 Offre de Formation Management")
            
            formations_gestion = {
                'Programme': ['MBA Management Général', 'Certification Contrôleur de Gestion', 
                             'Formation Analyste Financier', 'Executive Leadership',
                             'Gestion de Projet Agile', 'Transformation Digitale des RH'],
                'Durée': ['12 mois', '6 mois', '4 mois', '3 mois', '2 mois', '3 mois'],
                'Prix (€)': [12500, 6800, 4200, 3500, 2800, 3200],
                'Participants/an': [45, 60, 80, 35, 120, 75]
            }
            
            df_gestion = pd.DataFrame(formations_gestion)
            st.dataframe(df_gestion, use_container_width=True)
            
            # Calculateur de rentabilité formation
            st.markdown("### 🧮 Calculateur de Rentabilité Formation")
            
            prix_formation = st.number_input("Prix de la formation (€)", 1000, 20000, 6800)
            cout_pedagogique = st.number_input("Coût pédagogique (€)", 500, 10000, 3200)
            participants = st.slider("Nombre de participants", 10, 100, 25)
            frais_fixes = st.number_input("Frais fixes (€)", 1000, 5000, 2000)
            
            if st.button("📊 Calculer Rentabilité"):
                ca = prix_formation * participants
                cout_total = (cout_pedagogique * participants) + frais_fixes
                marge = ca - cout_total
                taux_marge = (marge / ca) * 100
                
                st.metric("💵 Chiffre d'Affaires", f"{ca:,}€")
                st.metric("💰 Coût Total", f"{cout_total:,}€")
                st.metric("📈 Marge", f"{marge:,}€")
                st.metric("🎯 Taux de Marge", f"{taux_marge:.1f}%")
        
        with col2:
            st.markdown("### 📈 Tableau de Bord Pédagogique")
            
            # KPI pédagogiques
            kpi_data = {
                'Indicateur': ['Taux de réussite', 'Satisfaction apprenants', 
                              "Taux d'abandon", 'Insertion professionnelle',
                              'Taux de recommandation'],
                'Valeur': ['92%', '4.7/5', '8%', '87%', '94%'],
                'Objectif': ['90%', '4.5/5', '10%', '85%', '90%']
            }
            
            st.dataframe(pd.DataFrame(kpi_data), use_container_width=True)
            
            # Graphique performance formations
            formations = ['MBA', 'Contrôle Gestion', 'Analyste Financier', 'Leadership']
            satisfaction = [4.6, 4.8, 4.7, 4.9]
            insertion = [85, 90, 88, 92]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Satisfaction (/5)', x=formations, y=satisfaction))
            fig.add_trace(go.Bar(name='Insertion (%)', x=formations, y=[x/20 for x in insertion]))
            fig.update_layout(title='Performance des Formations Management', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.subheader("💻 Département Informatique & Data Science")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🖥️ Offre de Formation Tech & Data")
            
            formations_tech = {
                'Domaine': ['Développement Full-Stack', 'Data Science & IA', 
                           'Cloud & DevOps', 'Cybersécurité',
                           'Data Analyse Business', 'Machine Learning'],
                'Niveau': ['Bac+3 à Bac+5', 'Bac+5', 'Bac+3 à Bac+5', 
                          'Bac+3 à Bac+5', 'Bac+2 à Bac+4', 'Bac+5'],
                'Durée': ['9 mois', '6 mois', '4 mois', '5 mois', '3 mois', '6 mois'],
                'Prix (€)': [7500, 8200, 5800, 6900, 4200, 7800],
                'Laboratoires': ['2 salles équipées', '1 lab IA', '1 cloud privé', 
                               '1 cyber-range', '1 salle data', '1 lab ML']
            }
            
            df_tech = pd.DataFrame(formations_tech)
            st.dataframe(df_tech, use_container_width=True)
            
            # Calculateur infrastructure tech
            st.markdown("### 🛠️ Calculateur d'Infrastructure Technologique")
            
            nb_salles = st.slider("Nombre de salles informatiques", 1, 10, 5)
            nb_postes = st.number_input("Postes par salle", 10, 30, 20)
            cloud_usage = st.selectbox("Usage cloud", ['Faible', 'Moyen', 'Intensif'])
            
            if st.button("💰 Calculer Investissement Tech"):
                cout_salle = nb_salles * 25000
                cout_postes = nb_salles * nb_postes * 1500
                
                if cloud_usage == 'Faible':
                    cout_cloud = 500
                elif cloud_usage == 'Moyen':
                    cout_cloud = 1200
                else:
                    cout_cloud = 2500
                
                invest_total = cout_salle + cout_postes + (cout_cloud * 12)
                
                st.metric("💻 Investissement Infrastructure", f"{invest_total:,}€")
                st.metric("🖥️ Postes disponibles", f"{nb_salles * nb_postes}")
                st.metric("☁️ Coût Cloud Annuel", f"{cout_cloud * 12:,}€")
        
        with col2:
            st.markdown("### 📊 Analytics des Compétences Tech")
            
            # Demande marché des compétences
            competences_data = {
                'Compétence': ['Python', 'SQL', 'Machine Learning', 'Cloud AWS', 
                              'Power BI', 'Cybersécurité', 'DevOps'],
                'Demande (%)': [95, 88, 82, 78, 85, 90, 75],
                'Salaire Moyen (k€)': [45, 42, 55, 52, 40, 58, 50]
            }
            
            df_competences = pd.DataFrame(competences_data)
            st.dataframe(df_competences, use_container_width=True)
            
            # Graphique demande compétences
            fig = px.bar(df_competences, x='Compétence', y='Demande (%)',
                        title='Demande Marché des Compétences Tech')
            st.plotly_chart(fig, use_container_width=True)
            
            # Simulateur de parcours data
            st.markdown("### 🎯 Simulateur de Parcours Data Scientist")
            
            competences_acquises = st.multiselect(
                "Compétences actuelles",
                ['Python', 'SQL', 'Statistiques', 'Machine Learning', 'Visualisation', 'Big Data']
            )
            
            if st.button("📈 Analyser Parcours"):
                competences_manquantes = ['Python', 'SQL', 'Machine Learning', 'Big Data']
                competences_restantes = [c for c in competences_manquantes if c not in competences_acquises]
                
                if competences_restantes:
                    st.warning(f"📚 Compétences à acquérir : {', '.join(competences_restantes)}")
                    duree_estimee = len(competences_restantes) * 1.5  # mois par compétence
                    st.info(f"⏱️ Durée estimée : {duree_estimee} mois")
                else:
                    st.success("🎉 Toutes les compétences de base sont acquises !")
    
    with tab4:
        st.subheader("🏨 Département Hôtellerie & Tourisme")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🍽️ Offre de Formation Hôtellerie")
            
            formations_hotel = {
                'Programme': ['Bachelor Management Hôtelier', 'MBA Hospitality', 
                             'Formation Sommelier', 'Certification Chef de Cuisine',
                             'Management Événementiel', 'Tourisme Durable'],
                'Spécialité': ['Gestion hôtelière', 'Stratégie', 'Œnologie', 
                              'Culinaire', 'Événements', 'Tourisme'],
                'Durée': ['3 ans', '18 mois', '6 mois', '8 mois', '4 mois', '5 mois'],
                'Prix (€)': [8900, 12500, 4500, 6200, 3800, 4100],
                'Partenariats': ['10 hôtels 4*', '20 groupes', '15 domaines', 
                               '8 restaurants', '12 agencies', '10 écolabels']
            }
            
            df_hotel = pd.DataFrame(formations_hotel)
            st.dataframe(df_hotel, use_container_width=True)
            
            # Calculateur de coût formation pratique
            st.markdown("### 🧮 Calculateur de Coût Formation Pratique")
            
            nb_stagiaires = st.slider("Nombre de stagiaires", 10, 50, 25)
            duree_stage = st.number_input("Durée stage (semaines)", 4, 24, 12)
            type_formation = st.selectbox("Type formation", ['Cuisine', 'Service', 'Réception', 'Management'])
            
            if st.button("🍳 Calculer Coût Formation"):
                if type_formation == 'Cuisine':
                    cout_matiere = nb_stagiaires * duree_stage * 150
                    cout_encadrement = nb_stagiaires * duree_stage * 200
                elif type_formation == 'Service':
                    cout_matiere = nb_stagiaires * duree_stage * 80
                    cout_encadrement = nb_stagiaires * duree_stage * 180
                else:
                    cout_matiere = nb_stagiaires * duree_stage * 50
                    cout_encadrement = nb_stagiaires * duree_stage * 220
                
                cout_total = cout_matiere + cout_encadrement
                
                st.metric("🥬 Coût Matières Premières", f"{cout_matiere:,}€")
                st.metric("👨‍🏫 Coût Encadrement", f"{cout_encadrement:,}€")
                st.metric("💰 Coût Total Formation", f"{cout_total:,}€")
        
        with col2:
            st.markdown("### 🏨 Infrastructure Hôtelière Pédagogique")
            
            infrastructure_data = {
                'Équipement': ['Laboratoire cuisine', 'Salle restaurant pédagogique', 
                              'Laboratoire bar', 'Salle réception',
                              'Chambres pédagogiques', 'Salle événementielle'],
                'Capacité': ['24 stagiaires', '40 couverts', '20 stagiaires', 
                           '30 stagiaires', '8 chambres', '100 personnes'],
                'Investissement': [120000, 80000, 45000, 35000, 60000, 90000]
            }
            
            df_infra = pd.DataFrame(infrastructure_data)
            st.dataframe(df_infra, use_container_width=True)
            
            # Métriques secteur hôtelier
            st.metric("🏨 Taux d'occupation moyen", "72%", "5%")
            st.metric("⭐ Satisfaction client", "4.8/5", "0.2")
            st.metric("👥 Taux de fidélisation", "65%", "8%")
            
            # Graphique débouchés hôtellerie
            metiers = ['Réceptionniste', 'Chef de cuisine', 'Serveur', 'Manager', 'Sommelier']
            salaires = [28, 45, 26, 38, 35]
            demande = [85, 78, 92, 82, 65]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Salaire (k€)', x=metiers, y=salaires))
            fig.add_trace(go.Bar(name='Demande (%)', x=metiers, y=demande))
            fig.update_layout(title='Débouchés Métiers Hôtellerie', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab5:
        st.subheader("📈 Business Plan du Centre de Formation")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💰 Prévisionnel Financier sur 3 Ans")
            
            business_plan = {
                'Poste': ['Chiffre d\'Affaires', 'Charges Personnels', 'Charges Pédagogiques',
                         'Charges Infrastructure', 'Charges Marketing', 'EBE', 'Résultat Net'],
                'Année 1': [1800000, 850000, 320000, 280000, 150000, 200000, 140000],
                'Année 2': [2600000, 1100000, 450000, 320000, 180000, 550000, 385000],
                'Année 3': [3500000, 1350000, 580000, 350000, 220000, 1000000, 700000]
            }
            
            df_business = pd.DataFrame(business_plan)
            st.dataframe(df_business, use_container_width=True)
            
            # Calculateur de seuil de rentabilité
            st.markdown("### 🎯 Calculateur de Seuil de Rentabilité")
            
            charges_fixes = st.number_input("Charges fixes annuelles (k€)", 500, 2000, 800)
            prix_moyen = st.number_input("Prix moyen formation (€)", 2000, 10000, 4500)
            cout_variable = st.number_input("Coût variable par formation (€)", 500, 3000, 1200)
            
            if st.button("📊 Calculer Seuil"):
                marge_unitaire = prix_moyen - cout_variable
                seuil_participants = (charges_fixes * 1000) / marge_unitaire
                seuil_formations = seuil_participants / 25  # 25 participants par formation en moyenne
                
                st.metric("👥 Participants nécessaires", f"{seuil_participants:.0f}")
                st.metric("🎓 Formations nécessaires", f"{seuil_formations:.1f}")
                st.metric("💰 CA seuil", f"{(seuil_participants * prix_moyen)/1000:.0f} k€")
        
        with col2:
            st.markdown("### 📊 Répartition du CA par Département")
            
            # CA par département
            departements = ['Management', 'Informatique', 'Hôtellerie', 'Formations sur mesure']
            ca_an1 = [720, 540, 360, 180]  # en k€
            ca_an2 = [1040, 780, 520, 260]
            ca_an3 = [1400, 1050, 700, 350]
            
            fig = go.Figure()
            fig.add_trace(go.Bar(name='Année 1', x=departements, y=ca_an1))
            fig.add_trace(go.Bar(name='Année 2', x=departements, y=ca_an2))
            fig.add_trace(go.Bar(name='Année 3', x=departements, y=ca_an3))
            fig.update_layout(title='Évolution du CA par Département (k€)', barmode='group')
            st.plotly_chart(fig, use_container_width=True)
            
            # Investissements initiaux
            st.markdown("### 🏗️ Plan d'Investissement Initial")
            
            investissements = {
                'Poste': ['Immobilier & Rénovation', 'Équipements pédagogiques', 
                         'Infrastructure IT', 'Développement pédagogique',
                         'Marketing lancement', 'Fonds de roulement'],
                'Montant (k€)': [800, 350, 200, 150, 100, 200],
                'Calendrier': ['Mois 1-3', 'Mois 2-4', 'Mois 1-2', 'Mois 1-6', 'Mois 1-3', 'Mois 1']
            }
            
            df_invest = pd.DataFrame(investissements)
            st.dataframe(df_invest, use_container_width=True)
            
            total_invest = sum(investissements['Montant (k€)'])
            st.metric("💰 Investissement Total", f"{total_invest:,} k€")
    
    with tab6:
        st.subheader("🤝 Synergies Multidisciplinaires")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 🔗 Interactions entre Départements")
            
            synergies_data = {
                'Interaction': ['Data analyse pour gestion hôtelière', 
                               'Management pour projets tech',
                               'Tech pour optimisation processus',
                               'Hôtellerie pour soft skills',
                               'Formations croisées',
                               'Projets clients communs'],
                'Bénéfice': ['+15% efficacité', '+20% productivité', '+25% automation',
                            '+30% satisfaction', '+40% compétences', '+35% CA'],
                'Départements': ['Data + Hôtellerie', 'Management + Tech', 'Tech + Management',
                               'Hôtellerie + Tous', 'Tous départements', 'Tous départements']
            }
            
            df_synergies = pd.DataFrame(synergies_data)
            st.dataframe(df_synergies, use_container_width=True)
            
            # Calculateur de synergies
            st.markdown("### 🧮 Calculateur d'Impact des Synergies")
            
            ca_initial = st.number_input("CA initial estimé (k€)", 1000, 5000, 1800)
            taux_synergie = st.slider("Taux de synergie (%)", 5, 30, 15)
            
            if st.button("🚀 Calculer Impact Synergies"):
                ca_avec_synergies = ca_initial * (1 + taux_synergie/100)
                gain_synergies = ca_avec_synergies - ca_initial
                
                st.metric("💰 CA Initial", f"{ca_initial:,} k€")
                st.metric("📈 CA avec Synergies", f"{ca_avec_synergies:,} k€")
                st.metric("🎯 Gain Synergies", f"{gain_synergies:,} k€")
        
        with col2:
            st.markdown("### 🌟 Avantages Compétitifs du Modèle Intégré")
            
            avantages = [
                "🎯 **Formation 360°** : Compétences techniques ET managériales",
                "🤝 **Réseau intégré** : Alumni communs aux 3 filières",
                "💡 **Innovation pédagogique** : Cas réels inter-filières",
                "🏆 **Reconnaissance employeurs** : Profils polyvalents",
                "📊 **Data-driven** : Analytics des compétences recherchées",
                "🌍 **Approche globale** : Du technique au stratégique"
            ]
            
            for avantage in avantages:
                st.markdown(f"- {avantage}")
            
            st.markdown("### 📋 Projets Collaboratifs")
            
            projets_data = {
                'Projet': ['Outil de gestion hôtelière', 'Plateforme analytics formation',
                          'Application mobile événementielle', 'Système de recommandation carrières'],
                'Porteur': ['Tech + Hôtellerie', 'Data + Management', 
                           'Tech + Hôtellerie', 'Data + Management'],
                'Impact': ['Optimisation 25%', 'Décision +30%', 'Satisfaction +40%', 'Insertion +20%']
            }
            
            df_projets = pd.DataFrame(projets_data)
            st.dataframe(df_projets, use_container_width=True)
            
            # ROI formation
            st.metric("📊 ROI Formation Management", "245%", "15%")
            st.metric("💻 ROI Formation Tech", "280%", "20%")
            st.metric("🏨 ROI Formation Hôtellerie", "210%", "12%")

 
 
# Footer (existant)
st.markdown("---")
st.markdown(
    "**Xataxeli Système Learning by Doing** - Plateforme pédagogique collaborative • "
    "Designed by  **Amiharbi Eyeug** • "
    "Développé par Amiharby pour la formation inter-départements • "
    "© 2025 Xataxeli Corporation. Tous droits réservés."
)

 