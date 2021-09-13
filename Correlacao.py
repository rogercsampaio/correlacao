#!/usr/bin/env python
# coding: utf-8

# # Correlação

# ## Importando os pacotes necessários

# In[17]:


import pandas as pd
import seaborn as sns


# ### Carregando a base de dados

# In[4]:


pokemons = pd.read_csv('bases/Pokemon.csv')


# <h2> <center> Exemplo </center> </h2> <img src="images/charmander1.PNG" width="500" height="600"> 

# In[31]:


pokemons.head(5)


# In[30]:


# Visualizando a quantidade de linhas e colunas
pokemons.shape


# ## Calculando a correlação (coeficiente)

# In[33]:


# Correlação de todas as variaveis
# Função: DataFrame.corr
pokemons.corr()


# In[34]:


# Correlação de apenas algumas.
pokemons.loc[:,['Attack','Total']].corr()


# In[15]:


# Correlação de apenas algumas.
pokemons.loc[:,['HP','Speed']].corr()


# In[16]:


# Indica que quanto maior o total, maior sera a defesa. Correlacao positiva
pokemons.loc[:,['Total','Defense']].corr()


# In[35]:


# Gráfico de calor para visualizar melhor
corr = pokemons.corr()
sns.heatmap(corr, 
        xticklabels=corr.columns,
        yticklabels=corr.columns)


# In[20]:


# Visualizando de outra maneira diferente
corr.style.background_gradient(cmap='coolwarm')


# In[ ]:




