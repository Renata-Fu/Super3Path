import pandas as pd
import sys

#preset command line arguments
if len(sys.argv)<=1: #inputs
    x = "KEGG_results.csv"
    y = "Reactome_results.csv"
    z = "WikiPathways_results.csv"
elif len(sys.argv)<=2:
    x = sys.argv[1]
    y = "Reactome_results.csv"
    z = "WikiPathways_results.csv"
elif len(sys.argv)<=3:
    x = sys.argv[1]
    y = sys.argv[2]
    z = "WikiPathways_results.csv"
else:
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]

#import data
map_cat = pd.read_csv(r'./input_files/mapping_catalog.csv') #mapping catalog
map_cat_export = map_cat.copy(deep=True) #mapping catalog
importK = pd.read_csv(x)
KEGG = list(dict.fromkeys(importK["pathway"])) #KEGG
importR = pd.read_csv(y)
Reactome = list(dict.fromkeys(importR["pathway"])) #Reactome
importW = pd.read_csv(y)
WikiPathways = list(dict.fromkeys(importW["pathway"])) #WikiPathways

#change pathway name format for map_cat so it matches with import files
def standard_name(x):
    x = x.upper() #uppercase everything
    x = x.replace(' ', '_') #change [spaces, dashes] into underscore
    x = x.replace('-', '_')
    x = x.replace(',', '') #delete [parentheses, commas, single quotation marks]
    x = x.replace('\'', '')
    x = x.replace('(', '')
    x = x.replace(')', '')
    x = x.replace('WIKIPATHWAYS', 'WP')
    return x
i = 0
for index, row in map_cat.iterrows(): #change name and append prefix based on database
    prefices = ['KEGG', 'Reactome', 'WikiPathways']
    for x in prefices:
        if row['Database 1']==x:
            row['Pathway 1'] = x + '_' + row['Pathway 1']
            row['Pathway 1'] = standard_name(row['Pathway 1'])
        elif row['Database 2']==x:
            row['Pathway 2'] = x + '_' + row['Pathway 2']
            row['Pathway 2'] = standard_name(row['Pathway 2'])
    i+=1

#sort pathways based on normalized enrichment scores
#KEGG
KEGG_pos = []
KEGG_neg = []
for index, row in importK.iterrows():
    if row['NES'] >= 0:
        KEGG_pos.append(row['pathway']) #building positive KEGG pathways list
    else:
        KEGG_neg.append(row['pathway']) #building negative KEGG pathways list
#Reactome
Reactome_pos = []
Reactome_neg = []
for index, row in importR.iterrows():
    if row['NES'] >= 0:
        Reactome_pos.append(row['pathway']) #building positive Reactome pathways list
    else:
        Reactome_neg.append(row['pathway']) #building negative Reactome pathways list
#WikiPathways
WikiPathways_pos = []
WikiPathways_neg = []
for index, row in importW.iterrows():
    if row['NES'] >= 0:
        WikiPathways_pos.append(row['pathway']) #building positive WikiPathways pathways list
    else:
        WikiPathways_neg.append(row['pathway']) #building positive WikiPathways pathways list

#create empty dataframe for exporting result
result_pos = pd.DataFrame(columns=['Pathway 1', 'Database 1', 'Relation', 'Pathway 2', 'Database 2'])
result_neg = pd.DataFrame(columns=['Pathway 1', 'Database 1', 'Relation', 'Pathway 2', 'Database 2'])

#add to positive results
line = 0
for index, row in map_cat.iterrows():
    mapping = list(map_cat_export.loc[line])
    if (#KEGG & Reactome
        (row['Database 1']=='KEGG' and row['Pathway 1'] in KEGG_pos and
         row['Database 2']=='Reactome' and row['Pathway 2'] in Reactome_pos) or
        #KEGG & WikiPathways
        (row['Database 1']=='KEGG' and row['Pathway 1'] in KEGG_pos and
         row['Database 2']=='WikiPathways' and row['Pathway 2'] in WikiPathways_pos) or
        #Reactome & KEGG
        (row['Database 1']=='Reactome' and row['Pathway 1'] in Reactome_pos and
         row['Database 2']=='KEGG' and row['Pathway 2'] in KEGG_pos) or
        #Reactome & WikiPathways
        (row['Database 1']=='Reactome' and row['Pathway 1'] in Reactome_pos and
         row['Database 2']=='WikiPathways' and row['Pathway 2'] in WikiPathways_pos) or
        #WikiPathways & KEGG
        (row['Database 1']=='WikiPathways' and row['Pathway 1'] in WikiPathways_pos and
         row['Database 2']=='KEGG' and row['Pathway 2'] in KEGG_pos) or
        #WikiPathways & Reactome
        (row['Database 1']=='WikiPathways' and row['Pathway 1'] in WikiPathways_pos and
         row['Database 2']=='Reactome' and row['Pathway 2'] in Reactome_pos)):
        #if satisfy any of the above, add a row to the result DataFrame
        append_row = pd.Series(mapping, index=result_pos.columns)
        result_pos = result_pos.append(append_row, ignore_index=True)
    line+=1

#add to negative results
line = 0
for index, row in map_cat.iterrows():
    mapping = list(map_cat_export.loc[line])
    if (#KEGG & Reactome
        (row['Database 1']=='KEGG' and row['Pathway 1'] in KEGG_neg and
         row['Database 2']=='Reactome' and row['Pathway 2'] in Reactome_neg) or
        #KEGG & WikiPathways
        (row['Database 1']=='KEGG' and row['Pathway 1'] in KEGG_neg and
         row['Database 2']=='WikiPathways' and row['Pathway 2'] in WikiPathways_neg) or
        #Reactome & KEGG
        (row['Database 1']=='Reactome' and row['Pathway 1'] in Reactome_neg and
         row['Database 2']=='KEGG' and row['Pathway 2'] in KEGG_neg) or
        #Reactome & WikiPathways
        (row['Database 1']=='Reactome' and row['Pathway 1'] in Reactome_neg and
         row['Database 2']=='WikiPathways' and row['Pathway 2'] in WikiPathways_neg) or
        #WikiPathways & KEGG
        (row['Database 1']=='WikiPathways' and row['Pathway 1'] in WikiPathways_neg and
         row['Database 2']=='KEGG' and row['Pathway 2'] in KEGG_neg) or
        #WikiPathways & Reactome
        (row['Database 1']=='WikiPathways' and row['Pathway 1'] in WikiPathways_neg and
         row['Database 2']=='Reactome' and row['Pathway 2'] in Reactome_neg)):
        #if satisfy any of the above, add a row to the result DataFrame
        append_row = pd.Series(mapping, index=result_pos.columns)
        result_neg = result_neg.append(append_row, ignore_index=True)
    line+=1

#output result csv
result_pos.to_csv('upregulated_common_pathways.csv', index=False)
result_neg.to_csv('downregulated_common_pathways.csv', index=False)
