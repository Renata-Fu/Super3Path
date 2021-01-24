# README

## Description

## Installation
You can download SuperEnrich by clicking the green Code" button on the webpage, and then selecting "Download ZIP".
To download using bash, simply type `git clone` into terminal and the url which can be found by clicking the "Code" button.

## Requirements
* R 4.0.3 or newer
    * fgsea package
    * BiocParallel package
    * GSA 1.03.1 or newer
    * data.table 1.13.6 or newer
    * ggplot2 3.3.3 or newer
    * writexl 1.3.1 or newer
    * stringr 1.4.0 or newer
* Python 3.8 or newer
    * Pandas

## Usage
On any computer with installed software (e.g. Anaconda) supporting terminal application, change directory to "SuperEnrich".
### module 1: GSEA_3databases.R
This module does gene set enrichment analysis for a gene expression profile.
It uses pathway databases KEGG, Reactome, and WikiPathways (.gmt files provided in software package).
#### user input
* a gene expression profile comparing two conditions with microarray
    * must be a .txt file
    * must contain a column with standard gene names
    * must contain a column with log fold change (logFC)

#### command line
`Rscript GSEA_3databases.R [arg1] [arg2] [arg3]`

`arg1`, `arg2`, and `arg3` are mandatory arguments.
* `arg1`: full path to your input file
* `arg2`: index of the log fold change (logFC) column
* `arg3`: index of the standard gene name column
#### optional command line arguments
Type `plot-all` after `arg3` to plot all pathways. Separate the two arguments with a space.
If this option is chosen, 3 .pdf files containing pathways presented by each database will be outputted. This process may take a few minutes, so please do not click the .pdf files before this message appears in your terminal window: "done."

This Rscript will output three .csv files regardless of whether you choose to plot. These files are inputs for the next script, so please do not delete them.


### module 2: common_pathways.py
This module finds pathways common to 2 or more databases. Pathways have different names in different databases, but may represent the same biological process.

#### command line
`python3 common_pathways.py`

#### optional command line arguments
* This script will automatically output 2 .csv files with pathway relations, if you do not want the output, please add the argument `n`.
* If you changed the name of any input file (.csv files from the last script), please add the full path of the file as an argument. Please enter the paths in the file order: KEGG, Reactome, WikiPathways.
    * If you choose to use these arguments, please enter either `n` or `''` for the last argument.
    * If you did not change the name to the first and/or second file, please enter `''` as a placeholder.
Remember to separate all arguments with spaces.

## Acknowledgements
R. Fu, Y. Bai and Q. -E. Wang, "Computational identification of key pathways and differentially-expressed gene signatures in ovarian cancer stem cells," 2020 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), Seoul, Korea (South), 2020, pp. 1843-1848, doi:10.1109/BIBM49941.2020.9313416.

