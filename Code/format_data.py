# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 11:54:27 2022

@author: wendy
"""

import pandas as pd

default_value = ''

#Total population (millions) & HDI index ################################################################

#------------------------Read data------------------------
start_valid_rows , total_rows  = 5, 195
#Read only valid rows
df = pd.read_csv('Total population (millions).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_tp = pd.DataFrame(columns = ["country", "year","hdi_rank", "total_population_in_millions"])

idx_start_2010 = 6
for idx in df.index:
    country = df['Country'][idx]
    hdi_rank = df['HDI Rank'][idx]
    for year,total_p in (df.iloc[idx, idx_start_2010:]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'hdi_rank': hdi_rank,
            'total_population_in_millions':total_p}
        formated_df_tp = formated_df_tp.append(new_row, ignore_index=True)

print (formated_df_tp)   

#Gross enrolment ratio, pre-primary (% of preschool-age children) #######################################3

#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 192
#Read only valid rows
df = pd.read_csv('Gross enrolment ratio, pre-primary (% of preschool-age children).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_ge = pd.DataFrame(columns = ["country", "year", "gross_enrolment_ratio_pre_primary"])

idx_start_2010, idx_end  = 6 , 16
for idx in df.index:
    country = df['Country'][idx]
    for year,gerpp in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'gross_enrolment_ratio_pre_primary': (default_value if gerpp == '..' else gerpp) }
        formated_df_ge = formated_df_ge.append(new_row, ignore_index=True)

print (formated_df_ge)   


#Gross enrolment ratio, primary (% of primary school-age population) #######################################3

#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 193
#Read only valid rows
df = pd.read_csv('Gross enrolment ratio, primary (% of primary school-age population).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_gep = pd.DataFrame(columns = ["country", "year", "gross_enrolment_ratio_primary"])

idx_start_2010, idx_end  = 6 , 16
for idx in df.index:
    country = df['Country'][idx]
    for year,gerp in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'gross_enrolment_ratio_primary': (default_value if gerp == '..' else gerp) }
        formated_df_gep = formated_df_gep.append(new_row, ignore_index=True)

print (formated_df_gep) 

#Gross enrolment ratio, secondary (% of secondary school-age population) #######################################3

#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 193
#Read only valid rows
df = pd.read_csv('Gross enrolment ratio, secondary (% of secondary school-age population).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_ges = pd.DataFrame(columns = ["country", "year", "gross_enrolment_ratio_secondary"])

idx_start_2010, idx_end  = 6 , 16
for idx in df.index:
    country = df['Country'][idx]
    for year,gers in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'gross_enrolment_ratio_secondary': (default_value if gers == '..' else gers) }
        formated_df_ges = formated_df_ges.append(new_row, ignore_index=True)

print (formated_df_ges) 


#Gross enrolment ratio, tertiary (% of tertiary school-age population) #######################################

#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 191
#Read only valid rows
df = pd.read_csv('Gross enrolment ratio, tertiary (% of tertiary school-age population).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)
print(df)

#---------------------New format data------------------------
formated_df_get = pd.DataFrame(columns = ["country", "year", "gross_enrolment_ratio_tertiary"])

idx_start_2010, idx_end  = 6 , 16
for idx in df.index:
    country = df['Country'][idx]
    for year,gert in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'gross_enrolment_ratio_tertiary': (default_value if gert == '..' else gert) }
        formated_df_get = formated_df_get.append(new_row, ignore_index=True)

print (formated_df_get) 

#Education index #######################################

#------------------------Read data------------------------
start_valid_rows , total_rows  = 5, 189
#Read only valid rows
df = pd.read_csv('Education index.csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_ei = pd.DataFrame(columns = ["country", "year", "education_index"])

idx_start_2010, idx_end  = 22 , 42
for idx in df.index:
    country = df['Country'][idx]
    for year,ei in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'education_index': (default_value if ei == '..' else ei) }
        formated_df_ei = formated_df_ei.append(new_row, ignore_index=True)

print (formated_df_ei) 


#Government expenditure on education (% of GDP) #######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 192
#Read only valid rows
df = pd.read_csv('Government expenditure on education (% of GDP).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_gdp = pd.DataFrame(columns = ["country", "year", "government_expenditure_on_education"])

idx_start_2010, idx_end  = 6 , 16
for idx in df.index:
    country = df['Country'][idx]
    for year,gdp in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'government_expenditure_on_education': (default_value if gdp == '..' else gdp) }
        formated_df_gdp = formated_df_gdp.append(new_row, ignore_index=True)

print (formated_df_gdp) 

#Expected years of schooling (years) #######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 193
#Read only valid rows
df = pd.read_csv('Expected years of schooling (years).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_eyos = pd.DataFrame(columns = ["country", "year", "expected_years_of_school"])

idx_start_2010, idx_end  = 22 , 32
for idx in df.index:
    country = df['Country'][idx]
    for year,eyoe in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'expected_years_of_school': (default_value if eyoe == '..' else eyoe) }
        formated_df_eyos = formated_df_eyos.append(new_row, ignore_index=True)

print (formated_df_eyos) 

#Mean years of schooling (years)#######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 190
#Read only valid rows
df = pd.read_csv('Mean years of schooling (years).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_myos = pd.DataFrame(columns = ["country", "year", "mean_years_of_school"])

idx_start_2010, idx_end  = 22 , 32
for idx in df.index:
    country = df['Country'][idx]
    for year,myos in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'mean_years_of_school': (default_value if myos == '..' else myos) }
        formated_df_myos = formated_df_myos.append(new_row, ignore_index=True)

print (formated_df_myos) 

#Primary school dropout rate (% of primary school cohort)#######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 5, 191
#Read only valid rows
df = pd.read_csv('Primary school dropout rate (% of primary school cohort).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_psdr = pd.DataFrame(columns = ["country", "year", "primary_school_dropout_rate"])

idx_start_2010, idx_end  = 6 , 16
for idx in df.index:
    country = df['Country'][idx]
    for year,psdr in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'primary_school_dropout_rate': (default_value if psdr == '..' else psdr) }
        formated_df_psdr = formated_df_psdr.append(new_row, ignore_index=True)

print (formated_df_psdr) 

#Child labour (% ages 5-17)#######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 190
#Read only valid rows
df = pd.read_csv('Child labour (% ages 5-17).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_pcl = pd.DataFrame(columns = ["country", "year", "porcentage_child_labour"])

idx_start_2010, idx_end  = 2 , 12
for idx in df.index:
    country = df['Country'][idx]
    for year,pcl in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'porcentage_child_labour': (default_value if pcl == '..' else pcl) }
        formated_df_pcl = formated_df_pcl.append(new_row, ignore_index=True)

print (formated_df_pcl) 

#Human Development Index (HDI)#######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 5, 189
#Read only valid rows
df = pd.read_csv('Human Development Index (HDI).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_hdi = pd.DataFrame(columns = ["country", "year", "hdi"])

idx_start_2010, idx_end  = 22 , 32
for idx in df.index:
    country = df['Country'][idx]
    for year,hdi in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'hdi': (default_value if hdi == '..' else hdi) }
        formated_df_hdi = formated_df_hdi.append(new_row, ignore_index=True)

print (formated_df_hdi)

#Population with at least some secondary education (% ages 25 and older)#######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 189
#Read only valid rows
df = pd.read_csv('Population with at least some secondary education (% ages 25 and older).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_pals = pd.DataFrame(columns = ["country", "year", "population_at_least_secundary"])

idx_start_2010, idx_end  = 6, 16
for idx in df.index:
    country = df['Country'][idx]
    for year,pals in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'population_at_least_secundary': (default_value if pals == '..' else pals) }
        formated_df_pals = formated_df_pals.append(new_row, ignore_index=True)

print (formated_df_pals) 

#Population with at least some secondary education, female (% ages 25 and older)#######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 189
#Read only valid rows
df = pd.read_csv('Population with at least some secondary education, female (% ages 25 and older).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_palsf = pd.DataFrame(columns = ["country", "year", "population_at_least_secundary_female"])

idx_start_2010, idx_end  = 6, 16
for idx in df.index:
    country = df['Country'][idx]
    for year, palsf in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'population_at_least_secundary_female': (default_value if palsf == '..' else palsf) }
        formated_df_palsf = formated_df_palsf.append(new_row, ignore_index=True)

print (formated_df_palsf) 

#Population with at least some secondary education, male (% ages 25 and older)#######################################
#------------------------Read data------------------------
start_valid_rows , total_rows  = 6, 189
#Read only valid rows
df = pd.read_csv('Population with at least some secondary education, male (% ages 25 and older).csv', 
                 skiprows = start_valid_rows, nrows = total_rows, encoding='ISO-8859-1')
#Delete invalid colums
df.drop([col for col in df.columns if 'Unnamed' in col], inplace=True, axis=1)
#Replace invalid values
df.fillna(default_value)

#---------------------New format data------------------------
formated_df_palsm = pd.DataFrame(columns = ["country", "year", "population_at_least_secundary_male"])

idx_start_2010, idx_end  = 6, 16
for idx in df.index:
    country = df['Country'][idx]
    for year, palsm in (df.iloc[idx, idx_start_2010:idx_end]).items() :
        new_row = {
            'country': country,
            'year' : year,
            'population_at_least_secundary_male': (default_value if palsm == '..' else palsm) }
        formated_df_palsm = formated_df_palsm.append(new_row, ignore_index=True)

print (formated_df_palsm) 


#Final data ------------------------------------------------------------------------------------------
#df_merge = pd.merge(formated_df_tp, formated_df_ge, how='inner', on=['country','year'])
#df_merge = pd.merge(df_merge, formated_df_gep, how='inner', on=['country','year'])
#df_merge = pd.merge(df_merge, formated_df_ges, how='inner', on=['country','year'])
#df_merge = pd.merge(df_merge, formated_df_get, how='inner', on=['country','year'])
df_merge = pd.merge(formated_df_tp, formated_df_ei, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_gdp, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_eyos, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_myos, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_psdr, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_pcl, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_hdi, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_hdi, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_pals, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_palsf, how='inner', on=['country','year'])
df_merge = pd.merge(df_merge, formated_df_palsm, how='inner', on=['country','year'])
print(df_merge)
df_merge.to_csv(r'proyecto_data.csv', index = False)