import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Business Plan - Société IT",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .section-header {
        font-size: 1.8rem;
        color: #2e86ab;
        border-bottom: 2px solid #2e86ab;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #2e86ab;
        margin: 0.5rem 0;
    }
    .positive {
        color: #00a86b;
        font-weight: bold;
    }
    .negative {
        color: #ff6b6b;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Titre principal
st.markdown('<h1 class="main-header">💻 Business Plan - Société de Services Informatiques</h1>', unsafe_allow_html=True)

# Sidebar pour la navigation
st.sidebar.title("📊 Navigation")
section = st.sidebar.radio("Sélectionnez une section:", [
    "📋 Présentation du Projet",
    "💰 Hypothèses Commerciales", 
    "💻 Investissements IT",
    "📈 Chiffre d'Affaires",
    "👥 Charges de Personnel",
    "🏢 Frais Fixes",
    "📊 Compte de Résultat",
    "💵 Plan de Trésorerie",
    "📉 Analyse des Ratios"
])

# Données de base
@st.cache_data
def load_data():
    # Hypothèses commerciales
    hypotheses = pd.DataFrame({
        'Service': ['Développement sur mesure', 'Maintenance évolutive', 'Infogérance', 
                   'Conseil transformation', 'Formation technique', 'Audit cybersécurité'],
        'Prix_HT': [130, 95, 1800, 200, 120, 2500],
        'Cout_Revient': [45, 28, 520, 65, 32, 700],
        'Marge': [65.4, 70.5, 71.1, 67.5, 73.3, 72.0],
        'Delai_Client': [60, 30, 30, 60, 30, 45],
        'Delai_Fournisseur': [30, 30, 30, 30, 0, 30]
    })
    
    # Investissements année 1
    investissements = pd.DataFrame({
        'Type': ['Corporels', 'Corporels', 'Corporels', 'Corporels', 'Corporels',
                'Incorporels', 'Incorporels', 'Incorporels', 'Incorporels',
                'Financiers', 'Financiers'],
        'Poste': ['Serveurs infrastructure', 'Postes développement', 'Équipements réseau',
                 'Mobilier ergonomique', 'Sécurité physique', 'Licences logicielles',
                 'Développement CRM', 'Brevets/Propriété IP', 'Site web/SEO',
                 'Dépôt garantie', 'Caution bancaire'],
        'Montant_HT': [25000, 14000, 7500, 9000, 3500, 12000, 15000, 8000, 5000, 6000, 4000],
        'TVA': [20, 20, 20, 20, 20, 20, 20, 0, 20, 0, 0],
        'Mois': ['Janvier', 'Janvier', 'Janvier', 'Janvier', 'Mars', 'Janvier', 'Janvier', 'Janvier', 'Janvier', 'Janvier', 'Janvier']
    })
    
    # Chiffre d'affaires détaillé
    mois = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
            'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    
    ca_data = {
        'Mois': mois,
        'Développement': [8000, 12000, 16000, 20000, 24000, 24000, 26000, 22000, 28000, 30000, 30000, 32000],
        'Maintenance': [2000, 3000, 4000, 5000, 6000, 6000, 6500, 5500, 7000, 7500, 7500, 8000],
        'Infogérance': [3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600, 3600],
        'Conseil': [3000, 4000, 5000, 6000, 7000, 7000, 7500, 6500, 8000, 8500, 8500, 9000],
        'Formation': [1200, 1800, 2400, 3000, 3600, 3600, 3600, 2400, 3600, 3600, 3600, 3600],
        'Cybersécurité': [1000, 1500, 2000, 2500, 2500, 2500, 2500, 2000, 2500, 2500, 2500, 2500]
    }
    
    ca_df = pd.DataFrame(ca_data)
    
    # CORRECTION : Calculer le total uniquement sur les colonnes numériques
    colonnes_numeriques = ['Développement', 'Maintenance', 'Infogérance', 'Conseil', 'Formation', 'Cybersécurité']
    ca_df['Total'] = ca_df[colonnes_numeriques].sum(axis=1)
    
    return hypotheses, investissements, ca_df

hypotheses, investissements, ca_df = load_data()

# Section 1: Présentation du Projet
if section == "📋 Présentation du Projet":
    st.markdown('<h2 class="section-header">🎯 Présentation du Projet IT</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📋 Description de l'Entreprise")
        st.write("""
        **Société de Services en Ingénierie Informatique (ESN)** spécialisée dans :
        - 🚀 Développement d'applications sur mesure
        - 🔧 Maintenance et infogérance
        - 💡 Conseil en transformation digitale  
        - 🎓 Formation technique
        - 🛡️ Audit et conseil en cybersécurité
        """)
        
        st.subheader("🎯 Objectifs Stratégiques")
        st.write("""
        - Atteindre le seuil de rentabilité en 30 mois
        - Développer un portefeuille clients diversifié
        - Maintenir une marge brute de 70%
        - Croître progressivement le chiffre d'affaires
        """)
    
    with col2:
        st.subheader("📊 Métriques Clés")
        
        ca_an1 = ca_df['Total'].sum()
        
        metrics_data = {
            "Chiffre d'affaires année 1": f"{ca_an1:,.0f} €",
            "Investissements initiaux": "109 000 €", 
            "Effectif année 1": "7 personnes",
            "Marge brute cible": "70%",
            "Point mort": "Juillet 2024",
            "Rentabilité année 3": "264 €"
        }
        
        for metric, value in metrics_data.items():
            st.metric(metric, value)

# Section 2: Hypothèses Commerciales
elif section == "💰 Hypothèses Commerciales":
    st.markdown('<h2 class="section-header">💰 Hypothèses Commerciales</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 Services & Tarifs", "⏱️ Délais de Paiement", "📈 Paramètres Financiers"])
    
    with tab1:
        st.subheader("Services et Structure de Coûts")
        
        # Afficher le tableau des hypothèses
        st.dataframe(hypotheses, use_container_width=True)
        
        # Graphique des marges
        fig_marges = px.bar(
            hypotheses, 
            x='Service', 
            y='Marge',
            title="📊 Marges Brutes par Service",
            color='Marge',
            color_continuous_scale='Viridis'
        )
        fig_marges.update_layout(yaxis_title="Marge (%)")
        st.plotly_chart(fig_marges, use_container_width=True)
    
    with tab2:
        st.subheader("⏱️ Délais de Paiement")
        
        fig_delais = go.Figure()
        
        fig_delais.add_trace(go.Bar(
            name='Délai Client (jours)',
            x=hypotheses['Service'],
            y=hypotheses['Delai_Client'],
            marker_color='#ff7f0e'
        ))
        
        fig_delais.add_trace(go.Bar(
            name='Délai Fournisseur (jours)', 
            x=hypotheses['Service'],
            y=hypotheses['Delai_Fournisseur'],
            marker_color='#1f77b4'
        ))
        
        fig_delais.update_layout(
            title="Délais de Paiement Clients vs Fournisseurs",
            barmode='group'
        )
        
        st.plotly_chart(fig_delais, use_container_width=True)
        
        st.info("💡 **Analyse**: Les délais clients plus longs (45-60 jours) créent un besoin en fonds de roulement important.")
    
    with tab3:
        st.subheader("📈 Paramètres Financiers")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Taux IS", "25%")
            st.metric("TVA moyenne", "20%")
        
        with col2:
            st.metric("Croissance année 2", "+40%")
            st.metric("Croissance année 3", "+25%")
        
        with col3:
            st.metric("Taux charges sociales", "45%")
            st.metric("Coefficient moyen", "3.3")

# Section 3: Investissements IT
elif section == "💻 Investissements IT":
    st.markdown('<h2 class="section-header">💻 Investissements Informatiques</h2>', unsafe_allow_html=True)
    
    # Résumé des investissements
    total_invest = investissements['Montant_HT'].sum()
    total_tva = (investissements['Montant_HT'] * investissements['TVA'] / 100).sum()
    total_ttc = total_invest + total_tva
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Investissements HT", f"{total_invest:,.0f} €")
    col2.metric("TVA", f"{total_tva:,.0f} €") 
    col3.metric("Total TTC", f"{total_ttc:,.0f} €")
    col4.metric("Répartition mensuelle", "Échelonnée")
    
    tab1, tab2, tab3 = st.tabs(["📋 Détail des Investissements", "📊 Répartition par Type", "🗓️ Calendrier de Déploiement"])
    
    with tab1:
        st.subheader("Détail des Investissements Année 1")
        
        # Ajouter colonne TTC
        investissements['Montant_TTC'] = investissements['Montant_HT'] * (1 + investissements['TVA']/100)
        st.dataframe(investissements, use_container_width=True)
    
    with tab2:
        st.subheader("Répartition des Investissements")
        
        # Par type
        invest_par_type = investissements.groupby('Type')['Montant_HT'].sum().reset_index()
        fig_type = px.pie(
            invest_par_type, 
            values='Montant_HT', 
            names='Type',
            title="Répartition des Investissements par Type"
        )
        st.plotly_chart(fig_type, use_container_width=True)
        
        # Par poste (top 10)
        fig_poste = px.bar(
            investissements.nlargest(10, 'Montant_HT'),
            x='Poste',
            y='Montant_HT',
            title="Top 10 des Postes d'Investissement"
        )
        st.plotly_chart(fig_poste, use_container_width=True)
    
    with tab3:
        st.subheader("Calendrier de Déploiement")
        
        invest_mensuel = investissements.groupby('Mois')['Montant_HT'].sum().reindex(
            ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'], 
            fill_value=0
        )
        
        fig_calendrier = px.bar(
            x=invest_mensuel.index,
            y=invest_mensuel.values,
            title="Investissements par Mois",
            labels={'x': 'Mois', 'y': 'Montant HT (€)'}
        )
        st.plotly_chart(fig_calendrier, use_container_width=True)

# Section 4: Chiffre d'Affaires
elif section == "📈 Chiffre d'Affaires":
    st.markdown('<h2 class="section-header">📈 Chiffre d\'Affaires Prévisionnel</h2>', unsafe_allow_html=True)
    
    # Métriques CA
    ca_an1 = ca_df['Total'].sum()
    ca_an2 = 735980  # Données année 2
    ca_an3 = 921850  # Données année 3
    
    col1, col2, col3 = st.columns(3)
    col1.metric("CA Année 1", f"{ca_an1:,.0f} €")
    col2.metric("CA Année 2", f"{ca_an2:,.0f} €", f"+{(ca_an2-ca_an1)/ca_an1*100:.1f}%")
    col3.metric("CA Année 3", f"{ca_an3:,.0f} €", f"+{(ca_an3-ca_an2)/ca_an2*100:.1f}%")
    
    tab1, tab2, tab3 = st.tabs(["📊 Évolution Mensuelle", "🔍 Analyse par Service", "📈 Projection 3 Ans"])
    
    with tab1:
        st.subheader("Évolution Mensuelle du Chiffre d'Affaires")
        
        fig_ca_mensuel = go.Figure()
        
        services = ['Développement', 'Maintenance', 'Infogérance', 'Conseil', 'Formation', 'Cybersécurité']
        for service in services:
            fig_ca_mensuel.add_trace(go.Scatter(
                x=ca_df['Mois'],
                y=ca_df[service],
                name=service,
                stackgroup='one'
            ))
        
        fig_ca_mensuel.update_layout(
            title="Évolution du CA par Service - Année 1",
            yaxis_title="Chiffre d'Affaires (€)",
            xaxis_title="Mois"
        )
        
        st.plotly_chart(fig_ca_mensuel, use_container_width=True)
        
        # Tableau détaillé
        st.subheader("Détail Mensuel")
        st.dataframe(ca_df, use_container_width=True)
    
    with tab2:
        st.subheader("Répartition par Service")
        
        # CA total par service
        services = ['Développement', 'Maintenance', 'Infogérance', 'Conseil', 'Formation', 'Cybersécurité']
        ca_par_service = ca_df[services].sum()
        
        fig_repartition = px.pie(
            values=ca_par_service.values,
            names=ca_par_service.index,
            title="Répartition du CA par Service - Année 1"
        )
        st.plotly_chart(fig_repartition, use_container_width=True)
        
        # Performance relative
        st.subheader("Performance des Services")
        performance_df = pd.DataFrame({
            'Service': ca_par_service.index,
            'CA_Total': ca_par_service.values,
            'Part_Marche': (ca_par_service.values / ca_par_service.sum() * 100).round(1)
        })
        
        st.dataframe(performance_df, use_container_width=True)
    
    with tab3:
        st.subheader("Projection sur 3 Ans")
        
        annees = ['2024', '2025', '2026']
        ca_total = [ca_an1, ca_an2, ca_an3]
        
        fig_projection = px.line(
            x=annees, 
            y=ca_total,
            title="Projection du Chiffre d'Affaires sur 3 Ans",
            markers=True
        )
        fig_projection.update_layout(
            yaxis_title="Chiffre d'Affaires (€)",
            xaxis_title="Année"
        )
        fig_projection.add_annotation(
            x='2024', y=ca_an1,
            text=f"{ca_an1:,.0f} €",
            showarrow=True,
            arrowhead=1
        )
        
        st.plotly_chart(fig_projection, use_container_width=True)

# Section 5: Charges de Personnel
elif section == "👥 Charges de Personnel":
    st.markdown('<h2 class="section-header">👥 Charges de Personnel</h2>', unsafe_allow_html=True)
    
    # Données personnel
    personnel_data = pd.DataFrame({
        'Poste': ['Directeur technique', 'Développeur senior', 'Développeur junior', 
                 'Commercial IT', 'Admin/Comptable'],
        'Effectif': [1, 2, 2, 1, 1],
        'Salaire_Brut_Mensuel': [5500, 4500, 3200, 4000, 2500],
        'Salaire_Brut_Annuel': [66000, 108000, 76800, 48000, 30000]
    })
    
    personnel_data['Charges_Sociales'] = personnel_data['Salaire_Brut_Annuel'] * 0.45
    personnel_data['Total_Charges'] = personnel_data['Salaire_Brut_Annuel'] + personnel_data['Charges_Sociales']
    
    total_masse_salariale = personnel_data['Salaire_Brut_Annuel'].sum()
    total_charges = personnel_data['Total_Charges'].sum()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Effectif total", "7 personnes")
    col2.metric("Masse salariale brute", f"{total_masse_salariale:,.0f} €")
    col3.metric("Total charges personnel", f"{total_charges:,.0f} €")
    
    tab1, tab2 = st.tabs(["📋 Détail des Postes", "📊 Répartition des Coûts"])
    
    with tab1:
        st.subheader("Détail des Postes et Rémunérations")
        st.dataframe(personnel_data, use_container_width=True)
        
        # Graphique des salaires
        fig_salaires = px.bar(
            personnel_data,
            x='Poste',
            y='Salaire_Brut_Mensuel',
            title="Salaires Bruts Mensuels par Poste",
            color='Salaire_Brut_Mensuel',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_salaires, use_container_width=True)
    
    with tab2:
        st.subheader("Répartition des Coûts de Personnel")
        
        fig_repartition_couts = px.pie(
            personnel_data,
            values='Total_Charges',
            names='Poste',
            title="Répartition des Coûts de Personnel par Poste"
        )
        st.plotly_chart(fig_repartition_couts, use_container_width=True)
        
        # Évolution sur 3 ans
        evolution_personnel = pd.DataFrame({
            'Année': [2024, 2025, 2026],
            'Effectif': [7, 8, 9],
            'Masse_Salariale': [328800, 408240, 478920],
            'Total_Charges': [476760, 565240, 658920]
        })
        
        fig_evolution = px.line(
            evolution_personnel,
            x='Année',
            y=['Masse_Salariale', 'Total_Charges'],
            title="Évolution des Charges de Personnel sur 3 Ans",
            markers=True
        )
        st.plotly_chart(fig_evolution, use_container_width=True)

# Section 6: Frais Fixes
elif section == "🏢 Frais Fixes":
    st.markdown('<h2 class="section-header">🏢 Frais Fixes et Frais Généraux</h2>', unsafe_allow_html=True)
    
    # Données frais fixes
    frais_fixes = pd.DataFrame({
        'Poste': ['Loyer bureau', 'Cloud (AWS/Azure)', 'Licences SaaS', 'Télécom fibre',
                 'Électricité/Clim', 'Maintenance', 'Certifications', 'Événements/Conf.',
                 'Marketing digital', 'Sécurité IT', 'Assurances', 'Frais bancaires'],
        'Mensuel_HT': [1800, 1500, 950, 350, 280, 400, 300, 600, 450, 500, 250, 150],
        'Annuel_HT': [21600, 18000, 11400, 4200, 3360, 4800, 3600, 7200, 5400, 6000, 3000, 1800],
        'TVA': [20, 20, 20, 20, 20, 20, 0, 20, 20, 20, 0, 0]
    })
    
    total_frais_ht = frais_fixes['Annuel_HT'].sum()
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Frais Fixes HT", f"{total_frais_ht:,.0f} €")
    col2.metric("Moyenne Mensuelle", f"{total_frais_ht/12:,.0f} €")
    col3.metric("% du CA année 1", f"{(total_frais_ht/525700*100):.1f}%")
    
    tab1, tab2 = st.tabs(["📋 Détail des Frais", "📊 Structure des Coûts"])
    
    with tab1:
        st.subheader("Détail des Frais Fixes Annuels")
        
        frais_fixes['Annuel_TTC'] = frais_fixes['Annuel_HT'] * (1 + frais_fixes['TVA']/100)
        st.dataframe(frais_fixes, use_container_width=True)
        
        # Graphique des frais fixes
        fig_frais = px.bar(
            frais_fixes.nlargest(10, 'Annuel_HT'),
            x='Poste',
            y='Annuel_HT',
            title="Top 10 des Frais Fixes (HT)",
            color='Annuel_HT',
            color_continuous_scale='Reds'
        )
        st.plotly_chart(fig_frais, use_container_width=True)
    
    with tab2:
        st.subheader("Structure des Coûts")
        
        fig_structure = px.pie(
            frais_fixes,
            values='Annuel_HT',
            names='Poste',
            title="Répartition des Frais Fixes"
        )
        st.plotly_chart(fig_structure, use_container_width=True)
        
        # Comparaison avec standards du secteur
        st.subheader("Benchmark Sectoriel")
        
        benchmark_data = pd.DataFrame({
            'Poste': ['Personnel', 'Frais généraux', 'R&D', 'Marketing', 'Autres'],
            'Notre_Structure': [62.5, 17.2, 8.5, 7.3, 4.5],
            'Moyenne_Secteur': [58.0, 19.0, 10.0, 8.0, 5.0]
        })
        
        fig_benchmark = go.Figure()
        fig_benchmark.add_trace(go.Bar(name='Notre Structure', x=benchmark_data['Poste'], y=benchmark_data['Notre_Structure']))
        fig_benchmark.add_trace(go.Bar(name='Moyenne Secteur', x=benchmark_data['Poste'], y=benchmark_data['Moyenne_Secteur']))
        fig_benchmark.update_layout(title="Structure des Coûts vs Benchmark Sectoriel (%)", barmode='group')
        
        st.plotly_chart(fig_benchmark, use_container_width=True)

# Section 7: Compte de Résultat
elif section == "📊 Compte de Résultat":
    st.markdown('<h2 class="section-header">📊 Compte de Résultat Prévisionnel</h2>', unsafe_allow_html=True)
    
    # Données compte de résultat
    resultat_data = pd.DataFrame({
        'Poste': ['Chiffre d\'affaires', 'Coût des services vendus', 'Marge commerciale',
                 'Charges de personnel', 'Frais fixes', 'Dotations amortissements',
                 'Résultat exploitation', 'Charges financières', 'Résultat avant IS',
                 'IS (25%)', 'Résultat net'],
        '2024': [525700, 157710, 367990, 328800, 90360, 36300, -87470, -4000, -91470, 0, -91470],
        '2025': [735980, 220794, 515186, 408240, 101203, 48400, -42657, -3200, -45857, 0, -45857],
        '2026': [921850, 276555, 645295, 478920, 111323, 52300, 2752, -2400, 352, 88, 264]
    })
    
    # Métriques clés
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Résultat 2024", f"{resultat_data.loc[10, '2024']:,.0f} €")
    col2.metric("Résultat 2025", f"{resultat_data.loc[10, '2025']:,.0f} €")
    col3.metric("Résultat 2026", f"{resultat_data.loc[10, '2026']:,.0f} €", f"+{resultat_data.loc[10, '2026'] - resultat_data.loc[10, '2025']:,.0f} €")
    col4.metric("Point de rentabilité", "Août 2024")
    
    tab1, tab2, tab3 = st.tabs(["📋 Compte de Résultat Détaillé", "📈 Évolution sur 3 Ans", "🎯 Seuil de Rentabilité"])
    
    with tab1:
        st.subheader("Compte de Résultat Détaillé")
        
        # Formatage pour affichage
        resultat_display = resultat_data.copy()
        for col in ['2024', '2025', '2026']:
            resultat_display[col] = resultat_display[col].apply(lambda x: f"{x:,.0f} €" if pd.notnull(x) else "")
        
        st.dataframe(resultat_display, use_container_width=True)
        
        # Graphique des résultats
        resultat_graph_data = resultat_data.iloc[[6, 8, 10]].copy()  # Résultat exploitation, avant IS, net
        resultat_graph_data = resultat_graph_data.melt(id_vars=['Poste'], var_name='Année', value_name='Montant')
        
        fig_resultat = px.line(
            resultat_graph_data,
            x='Poste',
            y='Montant',
            color='Année',
            title="Évolution des Résultats (€)",
            markers=True
        )
        st.plotly_chart(fig_resultat, use_container_width=True)
    
    with tab2:
        st.subheader("Évolution des Principaux Postes")
        
        postes_a_afficher = ['Chiffre d\'affaires', 'Marge commerciale', 'Charges de personnel', 'Résultat net']
        data_evolution = resultat_data[resultat_data['Poste'].isin(postes_a_afficher)]
        data_evolution = data_evolution.melt(id_vars=['Poste'], var_name='Année', value_name='Montant')
        
        fig_evolution = px.line(
            data_evolution,
            x='Poste',
            y='Montant',
            color='Année',
            title="Évolution des Principaux Postes sur 3 Ans",
            markers=True
        )
        st.plotly_chart(fig_evolution, use_container_width=True)
        
        # Analyse de la marge
        st.subheader("Analyse de la Rentabilité")
        marge_data = pd.DataFrame({
            'Année': [2024, 2025, 2026],
            'Marge_Brute': [70.0, 70.0, 70.0],
            'Marge_Exploitation': [-16.6, -5.8, 0.3],
            'Marge_Net': [-17.4, -6.2, 0.03]
        })
        
        fig_marges = px.line(
            marge_data,
            x='Année',
            y=['Marge_Brute', 'Marge_Exploitation', 'Marge_Net'],
            title="Évolution des Marges (%)",
            markers=True
        )
        st.plotly_chart(fig_marges, use_container_width=True)
    
    with tab3:
        st.subheader("🎯 Analyse du Seuil de Rentabilité")
        
        # Calcul du point mort
        charges_fixes = 90360 + 328800  # Frais fixes + Personnel
        marge_brute = 0.70  # 70%
        
        ca_point_mort = charges_fixes / marge_brute
        
        st.metric("Chiffre d'affaires au point mort", f"{ca_point_mort:,.0f} €")
        st.metric("Mois d'atteinte du point mort", "Juillet 2024")
        
        # Graphique du point mort
        ca_cumul = ca_df['Total'].cumsum()
        charges_cumul = [charges_fixes/12 * i for i in range(1, 13)]
        
        fig_point_mort = go.Figure()
        fig_point_mort.add_trace(go.Scatter(x=ca_df['Mois'], y=ca_cumul, name='CA Cumulé', line=dict(color='green')))
        fig_point_mort.add_trace(go.Scatter(x=ca_df['Mois'], y=charges_cumul, name='Charges Cumulées', line=dict(color='red')))
        fig_point_mort.add_trace(go.Scatter(x=ca_df['Mois'], y=ca_cumul - charges_cumul, name='Résultat Cumulé', line=dict(color='blue')))
        
        fig_point_mort.update_layout(
            title="Analyse du Point Mort",
            yaxis_title="Montant Cumulé (€)",
            xaxis_title="Mois"
        )
        
        st.plotly_chart(fig_point_mort, use_container_width=True)

# Section 8: Plan de Trésorerie
elif section == "💵 Plan de Trésorerie":
    st.markdown('<h2 class="section-header">💵 Plan de Trésorerie</h2>', unsafe_allow_html=True)
    
    # Données trésorerie
    treso_data = pd.DataFrame({
        'Mois': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 
                'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'],
        'Encaissements': [300000, 0, 18800, 25900, 33000, 40100, 49700, 42000, 52700, 55700, 55700, 58700],
        'Décaissements': [193200, 52500, 45300, 43100, 42900, 42700, 44200, 38200, 45200, 47200, 47200, 47200],
        'Solde_Mois': [106800, -52500, -26500, -17200, -9900, -2600, 5500, 3800, 7500, 8500, 8500, 11500],
        'Solde_Cumulé': [106800, 54300, 27800, 10600, 700, -1900, 3600, 7400, 14900, 23400, 31900, 43400]
    })
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Trésorerie fin année 1", f"{treso_data['Solde_Cumulé'].iloc[-1]:,.0f} €")
    col2.metric("Mois le plus difficile", "Juin")
    col3.metric("Besoin max de trésorerie", "1 900 €")
    
    tab1, tab2, tab3 = st.tabs(["📊 Flux de Trésorerie", "📈 Évolution du Solde", "🔄 Analyse du BFR"])
    
    with tab1:
        st.subheader("Flux de Trésorerie Mensuels")
        
        fig_treso = go.Figure()
        fig_treso.add_trace(go.Bar(name='Encaissements', x=treso_data['Mois'], y=treso_data['Encaissements'], marker_color='green'))
        fig_treso.add_trace(go.Bar(name='Décaissements', x=treso_data['Mois'], y=treso_data['Décaissements'], marker_color='red'))
        fig_treso.add_trace(go.Scatter(name='Solde Mensuel', x=treso_data['Mois'], y=treso_data['Solde_Mois'], mode='lines+markers', line=dict(color='blue')))
        
        fig_treso.update_layout(
            title="Flux de Trésorerie Mensuels",
            barmode='group',
            yaxis_title="Montant (€)"
        )
        
        st.plotly_chart(fig_treso, use_container_width=True)
        
        # Tableau détaillé
        st.dataframe(treso_data, use_container_width=True)
    
    with tab2:
        st.subheader("Évolution de la Trésorerie")
        
        fig_solde = px.area(
            treso_data,
            x='Mois',
            y='Solde_Cumulé',
            title="Évolution de la Trésorerie Cumulée",
            markers=True
        )
        fig_solde.add_hline(y=0, line_dash="dash", line_color="red", annotation_text="Seuil de trésorerie positive")
        
        st.plotly_chart(fig_solde, use_container_width=True)
        
        # Analyse des points critiques
        st.subheader("Points Critiques de Trésorerie")
        
        points_critiques = treso_data[treso_data['Solde_Cumulé'] < 50000].nlargest(3, 'Solde_Cumulé')
        if not points_critiques.empty:
            st.warning(f"🚨 **Point le plus critique**: {points_critiques.iloc[0]['Mois']} avec {points_critiques.iloc[0]['Solde_Cumulé']:,.0f} €")
        
        st.success(f"✅ **Point mort franchi**: Juillet avec trésorerie positive durable")
    
    with tab3:
        st.subheader("Analyse du Besoin en Fonds de Roulement (BFR)")
        
        bfr_data = pd.DataFrame({
            'Année': [2024, 2025, 2026],
            'BFR': [86640, 98200, 107500],
            'Variation_BFR': [86640, 11560, 9300],
            'CA': [525700, 735980, 921850],
            'BFR_CA': [16.5, 13.3, 11.7]
        })
        
        col1, col2, col3 = st.columns(3)
        col1.metric("BFR année 1", f"{bfr_data.loc[0, 'BFR']:,.0f} €")
        col2.metric("BFR/CA année 1", f"{bfr_data.loc[0, 'BFR_CA']}%")
        col3.metric("Variation BFR année 2", f"{bfr_data.loc[1, 'Variation_BFR']:,.0f} €")
        
        # CORRECTION : Utiliser go.Figure() au lieu de px.line() pour secondary_y
        fig_bfr = go.Figure()
        
        # Ajouter BFR (axe Y principal)
        fig_bfr.add_trace(go.Scatter(
            x=bfr_data['Année'],
            y=bfr_data['BFR'],
            name='BFR (€)',
            line=dict(color='blue', width=3),
            yaxis='y1'
        ))
        
        # Ajouter BFR/CA (axe Y secondaire)
        fig_bfr.add_trace(go.Scatter(
            x=bfr_data['Année'],
            y=bfr_data['BFR_CA'],
            name='BFR/CA (%)',
            line=dict(color='red', width=3, dash='dash'),
            yaxis='y2'
        ))
        
        fig_bfr.update_layout(
            title="Évolution du BFR",
            xaxis=dict(title='Année'),
            yaxis=dict(
                title='BFR (€)',
                titlefont=dict(color='blue'),
                tickfont=dict(color='blue')
            ),
            yaxis2=dict(
                title='BFR/CA (%)',
                titlefont=dict(color='red'),
                tickfont=dict(color='red'),
                overlaying='y',
                side='right'
            ),
            legend=dict(x=0, y=1.1, orientation='h')
        )
        
        st.plotly_chart(fig_bfr, use_container_width=True)
        
        st.info("""
        💡 **Analyse BFR**: 
        - BFR important dû aux délais clients longs (60 jours)
        - Amélioration progressive du ratio BFR/CA
        - Besoin de financement initial important pour couvrir le BFR
        """)

# Section 9: Analyse des Ratios
elif section == "📉 Analyse des Ratios":
    st.markdown('<h2 class="section-header">📉 Analyse des Ratios Financiers</h2>', unsafe_allow_html=True)
    
    # Données ratios
    ratios_data = pd.DataFrame({
        'Ratio': [
            'Marge brute', 'Charges personnel/CA', 'Frais généraux/CA', 
            'BFR/CA', 'Rentabilité nette', 'Délai de rentabilité',
            'Productivité par salarié', 'Rotation du BFR'
        ],
        'Notre_Valeur': [70.0, 62.5, 17.2, 16.5, 0.03, 30, 75100, 6.1],
        'Norme_Secteur_Min': [65, 55, 15, 15, 5, 24, 70000, 5.0],
        'Norme_Secteur_Max': [80, 70, 25, 30, 15, 36, 90000, 8.0],
        'Unité': ['%', '%', '%', '%', '%', 'mois', '€/salarié', 'fois']
    })
    
    # Calcul de la performance relative
    ratios_data['Performance'] = np.where(
        ratios_data['Ratio'].isin(['Charges personnel/CA', 'Frais généraux/CA', 'BFR/CA', 'Délai de rentabilité']),
        (ratios_data['Norme_Secteur_Min'] / ratios_data['Notre_Valeur']).clip(0, 2),
        (ratios_data['Notre_Valeur'] / ratios_data['Norme_Secteur_Max']).clip(0, 2)
    )
    
    ratios_data['Statut'] = np.where(
        ratios_data['Performance'] >= 0.8, '✅ Bon',
        np.where(ratios_data['Performance'] >= 0.6, '⚠️ Correct', '❌ À améliorer')
    )
    
    tab1, tab2, tab3 = st.tabs(["📊 Tableau des Ratios", "📈 Analyse Comparative", "🎯 Recommandations"])
    
    with tab1:
        st.subheader("Ratios Financiers Clés")
        
        # Formatage pour affichage
        ratios_display = ratios_data.copy()
        ratios_display['Valeur_Affichée'] = ratios_display.apply(
            lambda x: f"{x['Notre_Valeur']} {x['Unité']}", axis=1
        )
        ratios_display['Fourchette_Secteur'] = ratios_display.apply(
            lambda x: f"{x['Norme_Secteur_Min']}-{x['Norme_Secteur_Max']} {x['Unité']}", axis=1
        )
        
        display_cols = ['Ratio', 'Valeur_Affichée', 'Fourchette_Secteur', 'Statut']
        st.dataframe(ratios_display[display_cols], use_container_width=True)
        
        # Graphique radar des ratios
        categories = ratios_data['Ratio'].tolist()
        our_values = ratios_data['Notre_Valeur'].tolist()
        sector_min = ratios_data['Norme_Secteur_Min'].tolist()
        sector_max = ratios_data['Norme_Secteur_Max'].tolist()
        
        fig_radar = go.Figure()
        
        fig_radar.add_trace(go.Scatterpolar(
            r=our_values,
            theta=categories,
            fill='toself',
            name='Notre performance',
            line_color='blue'
        ))
        
        fig_radar.add_trace(go.Scatterpolar(
            r=sector_max,
            theta=categories,
            fill='toself',
            name='Max secteur',
            line_color='lightgray'
        ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, max(sector_max + our_values) * 1.1]
                )),
            showlegend=True,
            title="Analyse Comparative des Ratios"
        )
        
        st.plotly_chart(fig_radar, use_container_width=True)
    
    with tab2:
        st.subheader("Analyse Comparative Détailée")
        
        for _, ratio in ratios_data.iterrows():
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                
                with col1:
                    st.write(f"**{ratio['Ratio']}**")
                
                with col2:
                    st.write(f"{ratio['Notre_Valeur']} {ratio['Unité']}")
                
                with col3:
                    st.write(f"{ratio['Norme_Secteur_Min']}-{ratio['Norme_Secteur_Max']} {ratio['Unité']}")
                
                with col4:
                    if ratio['Statut'] == '✅ Bon':
                        st.success(ratio['Statut'])
                    elif ratio['Statut'] == '⚠️ Correct':
                        st.warning(ratio['Statut'])
                    else:
                        st.error(ratio['Statut'])
                
                # Barre de progression
                valeur_norm = (ratio['Notre_Valeur'] - ratio['Norme_Secteur_Min']) / (ratio['Norme_Secteur_Max'] - ratio['Norme_Secteur_Min'])
                st.progress(float(min(max(valeur_norm, 0), 1)))
                
                st.markdown("---")
    
    with tab3:
        st.subheader("🎯 Recommandations Stratégiques")
        
        recommendations = {
            'Marge brute': "✅ Excellente marge - Maintenir la stratégie de pricing",
            'Charges personnel/CA': "⚠️ Optimiser la productivité - Automatiser les processus",
            'Frais généraux/CA': "✅ Bon contrôle - Poursuivre la rigueur managériale", 
            'BFR/CA': "⚠️ Négocier les délais clients - Facturation anticipée",
            'Rentabilité nette': "❌ Amélioration nécessaire - Focus sur la croissance du CA",
            'Délai de rentabilité': "⚠️ Dans la norme - Accélérer si possible",
            'Productivité par salarié': "✅ Bon niveau - Former et outiller l'équipe",
            'Rotation du BFR': "✅ Efficace - Maintenir la gestion rigoureuse"
        }
        
        for ratio, recommandation in recommendations.items():
            with st.expander(f"{ratio} - {recommandation.split(' - ')[0]}"):
                st.write(recommandation)
                
                if ratio == 'Rentabilité nette':
                    st.write("""
                    **Actions concrètes**:
                    - Accélérer l'acquisition clients
                    - Développer les services à forte marge  
                    - Optimiser les coûts fixes
                    - Réduire le délai de facturation
                    """)
                elif ratio == 'Charges personnel/CA':
                    st.write("""
                    **Actions concrètes**:
                    - Mettre en place des outils de productivité
                    - Former aux bonnes pratiques
                    - Automatiser les tâches répétitives
                    - Réviser l'organisation du travail
                    """)

# Footer
st.markdown("---")
st.markdown(
    "📊 *Application développée pour l'étude de cas Business Plan Société IT* • "
    "📧 *Contact: contact@societe-it.com* • "
    "📅 *Dernière mise à jour: {}*".format(datetime.now().strftime("%d/%m/%Y"))
)