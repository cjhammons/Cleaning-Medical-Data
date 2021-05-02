# Extract the continuous variables
X = medical_dropped[['Population', 'Children', 'Age', 
                 'Income', 'Doc_visits', 'Full_meals_eaten', 
                 'Initial_days', 'Total_charge', 'Additional_charges',
                 'Item1', 'Item2', 'Item3', 
                 'Item4', 'Item5', 'Item6',
                 'Item7', 'Item8']]

pca = PCA(n_components=X.shape[1])
pca.fit(norm)
medical_pca = pd.DataFrame(pca.transform(norm), columns=['PC1','PC2','PC3',
                                                         'PC4','PC5','PC6',
                                                         'PC7','PC8','PC9',
                                                        'PC10', 'PC11', 'PC12',
                                                        'PC13', 'PC14', 'PC15', 
                                                        'PC16', 'PC17'])

loadings = pd.DataFrame(pca.components_.T, 
                        columns=['PC1','PC2','PC3',
                                'PC4','PC5','PC6',
                                'PC7','PC8','PC9',
                                'PC10', 'PC11', 'PC12',
                                'PC13', 'PC14', 'PC15', 
                                'PC16', 'PC17'],
                        index=norm.columns)
loadings