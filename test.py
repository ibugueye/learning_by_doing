 # Ajouter cette nouvelle section dans votre application

# Mettre à jour la sidebar
st.sidebar.title("📚 Navigation")
section = st.sidebar.radio(
    "Choisissez une section:",
    ["🏠 Accueil", "📊 Départements", "🔄 Interactions", "🍽️ Scénario Restaurant", 
     "📈 Tableaux de Bord", "🎯 Évaluation", "💻 Cas IT & Dual", "🚀 Business Plan IT",
     "🎓 Centre Formation"]
)

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
                              'Taux d'abandon', 'Insertion professionnelle',
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
    "**Système Learning by Doing** - Plateforme pédagogique collaborative • "
    "Développé pour la formation inter-départements • "
    "© 2024"
)