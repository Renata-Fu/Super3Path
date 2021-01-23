#GSEA
#input: gene expression files(gene name and logfc)
#output: GSEA from KEGG, Reactome, and WikiPathways
#load packages
library(fgsea)
library(GSA)
library(data.table)
library(ggplot2)
library(BiocParallel)
library("writexl")
register(SerialParam())
library(stringr)

#setting command line arguments
args <- commandArgs(trailingOnly = TRUE)

#------------------------------------------------------------------------------

#LOADING TXT EXPRESSION FILE FOR RANKS(stats)
#load dataset
setwd("/Users/renatafu/Desktop")
data <- read.table(args[1], sep='\t', header = TRUE, skipNul = TRUE)

#ranking
ranks <- data[[as.numeric(args[2])]]
names(ranks) <- data[[as.numeric(args[3])]]
print (head(ranks))

#------------------------------------------------------------------------------

#LOADING GMT FILES FOR PATHS(pathways)
#KEGG
KEGG <- GSA.read.gmt("c2.cp.kegg.v7.2.symbols.gmt")
Kpaths <- KEGG$genesets
names(Kpaths) <- KEGG$geneset.names

#Reactome
Reactome <- GSA.read.gmt("c2.cp.reactome.v7.2.symbols.gmt")
Rpaths <- Reactome$genesets
names(Rpaths) <- Reactome$geneset.names

#WikiPathways
WikiPathways <- GSA.read.gmt("c2.cp.wikipathways.v7.2.symbols.gmt")
Wpaths <- WikiPathways$genesets
names(Wpaths) <- WikiPathways$geneset.names

#------------------------------------------------------------------------------

#FGSEA
KEGGRes <- fgsea(pathways = Kpaths, stats = ranks, 
                 minSize = 2, maxSize = 500)
ReactomeRes <- fgsea(Rpaths, ranks, 
                     minSize=2, maxSize = 500)
WikiPathwaysRes <- fgsea(Wpaths, ranks, 
                         minSize=2, maxSize = 500)

#------------------------------------------------------------------------------

#EXPORT TO CSV
exportK <- subset(KEGGRes, select = -c(leadingEdge))
write.csv(exportK, "/Users/renatafu/Desktop/KEGG_results.csv", row.names = FALSE)
exportR <- subset(ReactomeRes, select = -c(leadingEdge))
write.csv(exportR, "/Users/renatafu/Desktop/Reactome_results.csv", row.names = FALSE)
exportW <- subset(WikiPathwaysRes, select = -c(leadingEdge))
write.csv(exportW, "/Users/renatafu/Desktop/WikiPathways_results.csv", row.names = FALSE)

#------------------------------------------------------------------------------

#GRAPH
if (length(args)>3 && all.equal(args[4], 'plot-all')) {
  pdf(file = "KEGG_plots.pdf")
  for (x in KEGGRes$pathway) {
    name <- gsub('_', ' ', x)
    name <- str_to_title(name)
    name <- gsub('Kegg', 'KEGG', name)
    print(plotEnrichment(Kpaths[[x]], ranks) + labs(title=name))
  }
  dev.off()
  
  pdf(file = "Reactome_plots.pdf")
  for (x in ReactomeRes$pathway) {
    name <- gsub('_', ' ', x)
    name <- str_to_title(name)
    print(plotEnrichment(Rpaths[[x]], ranks) + labs(title=name))
  }
  dev.off()
  
  pdf(file = "WikiPathways_plots.pdf")
  for (x in WikiPathwaysRes$pathway) {
    name <- gsub('_', ' ', x)
    name <- str_to_title(name)
    name <- gsub('Wp ', 'WikiPathways ', name)
    print(plotEnrichment(Wpaths[[x]], ranks) + labs(title=name))
  }
  dev.off()
}

print('done.')
