import pandas as pd
import sys

#preset command line arguments
if len(sys.argv)<=1: #no inputs
    x = "KEGG_results.csv"
    y = "Reactome_results.csv"
    z = "WikiPathways_results.csv"
elif len(sys.argv)<=2: #one input
    x = sys.argv[1]
    y = "Reactome_results.csv"
    z = "WikiPathways_results.csv"
elif len(sys.argv)<=3: #two inputs
    x = sys.argv[1]
    y = sys.argv[2]
    z = "WikiPathways_results.csv"
else: #three inputs
    x = sys.argv[1]
    y = sys.argv[2]
    z = sys.argv[3]

#import data
map_cat = pd.read_csv(r'./input_files/mapping_catalog.csv') #mapping catalog, name format to be changed
map_cat_export = map_cat.copy(deep=True) #mapping catalog, name format kept
importK = pd.read_csv(x, usecols=('pathway', 'NES'))
KEGG = dict(importK.values) #KEGG dict (pathway:NES)
importR = pd.read_csv(y, usecols=('pathway', 'NES'))
Reactome = dict(importR.values) #Reactome dict (pathway:NES)
importW = pd.read_csv(z, usecols=('pathway', 'NES'))
WikiPathways = dict(importW.values) #WikiPathways dict (pathway:NES)

#change pathway name format for map_cat so it matches with pathway lists
def standard_name(x):
    x = x.upper() #uppercase everything
    x = x.replace(' ', '_') #change spaces, dashes into underscore
    x = x.replace('-', '_')
    x = x.replace(',', '') #delete parentheses, commas, single quotation marks
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

#create empty dataframe for exporting result
result = pd.DataFrame(columns=['Pathway 1', 'NES 1', 'Database 1', 'Relation', 'Pathway 2', 'NES 2', 'Database 2'])
#add to results
line = 0 #keeps track of line number for map_cat_export
for index, row in map_cat.iterrows():
    mapping = list(map_cat_export.loc[line])
    x = row['Pathway 1']
    y = row['Pathway 2']
    #KEGG and Reactome
    if (row['Database 1']=='KEGG' and x in KEGG and
       row['Database 2']=='Reactome' and y in Reactome):
       result = result.append({'Pathway 1':mapping[0], 'Pathway 2':mapping[3],
                               'NES 1':KEGG[x], 'NES 2':Reactome[y], 'Relation':row['Relation'],
                               'Database 1':row['Database 1'], 'Database 2':row['Database 2'],
                               }, ignore_index=True)
    #KEGG and WikiPathways
    elif (row['Database 1']=='KEGG' and x in KEGG and
          row['Database 2']=='WikiPathways' and y in WikiPathways):
       result = result.append({'Pathway 1':mapping[0], 'Pathway 2':mapping[3],
                               'NES 1':KEGG[x], 'NES 2':WikiPathways[y], 'Relation':row['Relation'],
                               'Database 1':row['Database 1'], 'Database 2':row['Database 2'],
                               }, ignore_index=True)
    #Reactome and KEGG
    if (row['Database 1']=='Reactome' and x in Reactome and
       row['Database 2']=='KEGG' and y in KEGG):
       result = result.append({'Pathway 1':mapping[0], 'Pathway 2':mapping[3],
                               'NES 1':Reactome[x], 'NES 2':KEGG[y], 'Relation':row['Relation'],
                               'Database 1':row['Database 1'], 'Database 2':row['Database 2'],
                               }, ignore_index=True)
    #Reactome and WikiPathways
    elif (row['Database 1']=='Reactome' and x in Reactome and
          row['Database 2']=='WikiPathways' and y in WikiPathways):
       result = result.append({'Pathway 1':mapping[0], 'Pathway 2':mapping[3],
                               'NES 1':Reactome[x], 'NES 2':WikiPathways[y], 'Relation':row['Relation'],
                               'Database 1':row['Database 1'], 'Database 2':row['Database 2'],
                               }, ignore_index=True)
    #WikiPathways and KEGG
    if (row['Database 1']=='WikiPathways' and x in WikiPathways and
       row['Database 2']=='KEGG' and y in KEGG):
       result = result.append({'Pathway 1':mapping[0], 'Pathway 2':mapping[3],
                               'NES 1':WikiPathways[x], 'NES 2':KEGG[y], 'Relation':row['Relation'],
                               'Database 1':row['Database 1'], 'Database 2':row['Database 2'],
                               }, ignore_index=True)
    #WikiPathways and Reactome
    if (row['Database 1']=='WikiPathways' and x in WikiPathways and
       row['Database 2']=='Reactome' and y in Reactome):
       result = result.append({'Pathway 1':mapping[0], 'Pathway 2':mapping[3],
                               'NES 1':WikiPathways[x], 'NES 2':Reactome[y], 'Relation':row['Relation'],
                               'Database 1':row['Database 1'], 'Database 2':row['Database 2'],
                               }, ignore_index=True)
    line+=1

#output result csv
result.to_csv('common_pathways.csv', index=False)
