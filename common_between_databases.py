#renatafu
#takes inputs mapping-catalog and 3 excel files of pathways returned by ComPath
#outputs pathways common in two or more databases, including relation and databases
import pandas as pd

cat = pd.read_excel(r'/Users/renatafu/Desktop/sci_re/Ovarian_CSCs/Pathways/mapping_catalog_v3.xlsx')

importK = pd.read_excel('/Users/renatafu/Desktop/sci_re/Ovarian_CSCs/Pathways/ComPath/GSE33874_pathways/KEGG33874.xlsx')
KEGG = list(dict.fromkeys(importK["Pathway Name"]))

importR = pd.read_excel("/Users/renatafu/Desktop/sci_re/Ovarian_CSCs/Pathways/ComPath/GSE33874_pathways/Reactome33874.xlsx")
Reactome = list(dict.fromkeys(importR["Pathway Name"]))

importW = pd.read_excel("/Users/renatafu/Desktop/sci_re/Ovarian_CSCs/Pathways/ComPath/GSE33874_pathways/WikiPathways33874.xlsx")
WikiPathways = list(dict.fromkeys(importW["Pathway Name"]))

result = pd.DataFrame(columns=['Pathway 1', 'Database 1', 'Relation', 'Pathway 2', 'Database 2'])

for index, row in cat.iterrows():
    if (row['Database 1']=='KEGG' and row['Pathway 1'] in KEGG and row['Database 2']=='Reactome' and row['Pathway 2'] in Reactome):
        #KR
        result = result.append({'Pathway 1':row['Pathway 1'], 'Database 1':row['Database 1'], 'Relation':row['Relation'], 'Pathway 2':row['Pathway 2'], 'Database 2':row['Database 2']}, ignore_index=True)
    elif (row['Database 1']=='KEGG' and row['Pathway 1'] in KEGG and row['Database 2']=='WikiPathways' and row['Pathway 2'] in WikiPathways):
        #KW
        result = result.append({'Pathway 1':row['Pathway 1'], 'Database 1':row['Database 1'], 'Relation':row['Relation'], 'Pathway 2':row['Pathway 2'], 'Database 2':row['Database 2']}, ignore_index=True)
    elif (row['Database 1']=='Reactome' and row['Pathway 1'] in Reactome and row['Database 2']=='KEGG' and row['Pathway 2'] in KEGG):
        #RK
        result = result.append({'Pathway 1':row['Pathway 1'], 'Database 1':row['Database 1'], 'Relation':row['Relation'], 'Pathway 2':row['Pathway 2'], 'Database 2':row['Database 2']}, ignore_index=True)
    elif (row['Database 1']=='Reactome' and row['Pathway 1'] in Reactome and row['Database 2']=='WikiPathways' and row['Pathway 2'] in WikiPathways):
        #RW
        result = result.append({'Pathway 1':row['Pathway 1'], 'Database 1':row['Database 1'], 'Relation':row['Relation'], 'Pathway 2':row['Pathway 2'], 'Database 2':row['Database 2']}, ignore_index=True)
    elif (row['Database 1']=='WikiPathways' and row['Pathway 1'] in WikiPathways and row['Database 2']=='KEGG' and row['Pathway 2'] in KEGG):
        #WK
        result = result.append({'Pathway 1':row['Pathway 1'], 'Database 1':row['Database 1'], 'Relation':row['Relation'], 'Pathway 2':row['Pathway 2'], 'Database 2':row['Database 2']}, ignore_index=True)
    elif (row['Database 1']=='WikiPathways' and row['Pathway 1'] in WikiPathways and row['Database 2']=='Reactome' and row['Pathway 2'] in Reactome):
        #WR
        result = result.append({'Pathway 1':row['Pathway 1'], 'Database 1':row['Database 1'], 'Relation':row['Relation'], 'Pathway 2':row['Pathway 2'], 'Database 2':row['Database 2']}, ignore_index=True)

#print (result)
result.to_excel(r'/Users/renatafu/Desktop/new.xlsx', index=False)
