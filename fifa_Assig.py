#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns



# In[8]:


df=pd.read_csv('fifa_data.csv')


# In[9]:


df


# In[10]:


print(df.head())
print(df.info())


# In[11]:


print(df['Nationality'].isnull().sum())


# In[12]:


df = df.dropna(subset=['Nationality'])


# In[13]:


player_counts = df['Nationality'].value_counts()


# In[14]:


most_players_country = player_counts.idxmax()
most_players_count = player_counts.max()


# In[15]:


print(f"The country with the most number of players is: {most_players_country} with {most_players_count} players.")


# In[16]:


import matplotlib.pyplot as plt


# In[17]:


df = df.dropna(subset=['Nationality'])


# In[18]:


player_counts = df['Nationality'].value_counts()


# In[19]:


top_5_countries = player_counts.head(5)


# In[20]:


plt.figure(figsize=(10, 6))
top_5_countries.plot(kind='bar', color='skyblue')
plt.title('Top 5 Countries with the Most FIFA Players')
plt.xlabel('Country')
plt.ylabel('Number of Players')
plt.xticks(rotation=45)
plt.show()


# In[21]:


print(df['Wage'].isnull().sum())


# In[22]:


df['Wage'] = df['Wage'].replace({'€': '', 'K': ''}, regex=True).astype(float) * 1000


# In[23]:


highest_salary_player = df.loc[df['Wage'].idxmax()]


# In[24]:


print(f"The player with the highest salary is: {highest_salary_player['Name']} with a salary of €{highest_salary_player['Wage']:.0f}.")


# In[25]:


print(df['Wage'].isnull().sum())


# In[26]:


df['Wage'] = df['Wage'].replace({'€': '', 'K': ''}, regex=True).astype(float) * 1000


# In[27]:


plt.figure(figsize=(10, 6))
plt.hist(df['Wage'], bins=30, color='skyblue', edgecolor='black')
plt.title('Salary Range of FIFA Players')
plt.xlabel('Salary (€)')
plt.ylabel('Number of Players')
plt.grid(True)
plt.show()


# In[41]:


df = pd.read_csv('fifa_data.csv')


print(df.head())
print(df.columns)


# In[42]:


print(f"Missing values in 'Height' column: {df['Height'].isnull().sum()}")


# In[43]:


def height_to_cm(height):
    try:
        feet, inches = height.split("'")
        feet = int(feet)
        inches = int(inches.replace('"', ''))
        return feet * 30.48 + inches * 2.54
    except:
        return None


# In[44]:


df['Height_cm'] = df['Height'].apply(height_to_cm)



# In[45]:


df = df.dropna(subset=['Height_cm'])


# In[46]:


tallest_player = df.loc[df['Height_cm'].idxmax()]


# In[47]:


print(f"The tallest player is: {tallest_player['Name']} with a height of {tallest_player['Height_cm']} cm.")


# In[48]:


df = df.dropna(subset=['Club'])


# In[49]:


club_player_counts = df['Club'].value_counts()


# In[50]:


most_players_club = club_player_counts.idxmax()
num_players = club_player_counts.max()


# In[51]:


print(f"The club with the most number of players is: {most_players_club} with {num_players} players.")


# In[52]:


df = df.dropna(subset=['Preferred Foot'])


# In[53]:


foot_counts = df['Preferred Foot'].value_counts()


# In[54]:


plt.figure(figsize=(8, 6))
foot_counts.plot(kind='bar', color='skyblue')
plt.title('Preferred Foot of FIFA Players')
plt.xlabel('Preferred Foot')
plt.ylabel('Number of Players')
plt.xticks(rotation=0)  
plt.show()


# In[ ]:




