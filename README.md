# README
This pipeline does gene set enrichment analysis for an input dataset using three pathway databases –– KEGG[1], Reactome[2], and WikiPathways[3], and it identifies pathways that are presented by multiple databases.

## About Super3Path
Gene set enrichment analysis (GSEA) is a common method in computational biology. GSEA identifies enriched pathways in certain cell populations or under certain conditions, and it is important to our understanding of many illnesses, as well as how to treat them. While there are many pathway databases that can be used in GSEA, most studies fail to analyze results from multiple pathway databases because 1) the process is tedious 2) it is hard to categorize pathways based on the databases since different databases often name one biological pathway differently.

Super3Path streamlines the process of using three databases for GSEA, and shows users pathways presented by multiple databases, so that users do not have to sort through everything themselves.

## Requirements
* [R 4.0.3 or newer](https://www.r-project.org/)
    * R packages will be automatically installed by the first module (download_packages.R)
* [Python 3.8 or newer](https://www.python.org/downloads/)
    * Pandas ([installation guide here](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html))

## Installation
* Users can download Super3Path by clicking the green "Code" button on the webpage, and then selecting "Download ZIP".
* To download using bash, simply type `git clone` into terminal followed by the url, which can be found by clicking the "Code" button.

## Usage
The package must be run on the command line on Unix/Linux, or any platform supporting terminal (e.g. Mac terminal, [Windows terminal](https://www.microsoft.com/en-us/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab)). 
1. Download Super3Path (with the required versions of R and Python installed)
2. Change directory to "Super3Path"
3. Run the modules as instructed below

-------------------------------

### module 1 (download_packages.R)
This module downloads necessary R packages for the next module. If a package is already installed, it will be updated.
#### command line
`Rscript download_packages.R`

-------------------------------

### module 2 (GSEA_3databases.R)
This module does gene set enrichment analysis for a gene expression profile.
It uses pathway databases KEGG, Reactome, and WikiPathways (.gmt files provided in the input_files folder in Super3Path).

This module uses the fgsea package. [4]
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
#### optional command line argument
Type `plot-all` after `arg3` to plot all pathways. Separate the two arguments with a space. If this option is chosen, three .pdf files containing pathways presented by each database will be outputted. This process may take a long time depending on the speed of your device, so please do not try to open the .pdf files before this message appears in your terminal window: "done."

This R script will output three .csv files regardless of whether you choose to plot the pathways or not. These files are inputs for the next script, so please do not delete them. It is also suggested that you not change the names or location of these files, as it may complicate the next command.

-------------------------------

### module 3 (common_pathways.py)
This module finds pathways common to 2 or more databases. Pathways may have different names in different databases, but may represent the same biological process.

This module utilizes Compath's mapping catalog [5]. A slightly modified version of this catalog can be found in the input_files folder.
#### command line
`python3 common_pathways.py`
#### optional command line arguments
* If you changed the name of any input file (.csv files from the last script), please add the full path of the file as an argument. Please enter the paths in the file order: KEGG, Reactome, WikiPathways.
    * If you did not change the name to the first and/or second file, please enter `''` as a placeholder.
Remember to separate all arguments with spaces.

This Python script will output a file called common_pathways.csv. It is a collection of pathways that are presented by two or three databases. "Equivalent" relations indicate that the pathways are identical between two databases, and "Part Of" relations indicate that the pathway on the left is a part of the pathway on the right. normalized enrichment scores (NES) are shown for each pathway.

## Test Datasets
This package includes two test samples in the [test_examples](https://github.com/Renata-Fu/Super3Path/tree/master/samples) folder. The tests were done using public datasets from the Gene Expression Omnibus, GSE104975 [6] and GSE156435[7].

## License
Distributed under the MIT License. See [LICENSE](https://github.com/Renata-Fu/Super3Path/blob/master/LICENSE) for more information.

## Contact
Renata Fu - renatafu2333@gmail.com
Yongsheng Bai - yongshengbaicool@gmail.com

Project link: https://github.com/Renata-Fu/Super3Path

## Citations
1. Kanehisa, M., Furumichi, M., Sato, Y., Ishiguro-Watanabe, M., & Tanabe, M. (2020). KEGG: Integrating viruses and cellular organisms. Nucleic Acids Research, 49(D1). https://doi.org/10.1093/nar/gkaa970
2. Jassal, B., Matthews, L., Viteri, G., Gong, C., Lorente, P., Fabregat, A., . . . D’Eustachio, P. (2019). The reactome pathway knowledgebase. Nucleic Acids Research. https://doi.org/10.1093/nar/gkz1031
3. Martens, M., Ammar, A., Riutta, A., Waagmeester, A., Slenter, D., Hanspers, K., . . . Kutmon, M. (2020). WikiPathways: Connecting communities. Nucleic Acids Research, 49(D1). https://doi.org/10.1093/nar/gkaa1024
4. Korotkevich, G., Sukhov, V., Budin, N., Shpak, B., Artyomov, M. N., & Sergushichev, A. (2016). Fast gene set enrichment analysis. doi:10.1101/060012
5. Domingo-Fernández, D., Hoyt, C. T., Bobis-Álvarez, C., Marín-Llaó, J., & Hofmann-Apitius, M. (2018). ComPath: An ecosystem for exploring, analyzing, and curating mappings across pathway databases. Nature. https://doi.org/10.1101/353235
6. Maitra Majee, S., Sharma, E., Singh, B., & Khurana, J. P. (2020). Drought-induced protein (Di19-3) plays a role in auxin signaling by interacting with IAA14 in Arabidopsis. Plant direct, 4(6), e00234. https://doi.org/10.1002/pld3.234
7. Cui, J., Song, Y., Han, X., Hu, J., Chen, Y., Chen, X., Xu, X., Xing, Y., Lu, H., & Cai, L. (2020). Targeting 14-3-3ζ Overcomes Resistance to Epidermal Growth Factor Receptor-Tyrosine Kinase Inhibitors in Lung Adenocarcinoma via BMP2/Smad/ID1 Signaling. Frontiers in oncology, 10, 542007. https://doi.org/10.3389/fonc.2020.542007
8. R. Fu, Y. Bai and Q. -E. Wang, "Computational identification of key pathways and differentially-expressed gene signatures in ovarian cancer stem cells," 2020 IEEE International Conference on Bioinformatics and Biomedicine (BIBM), Seoul, Korea (South), 2020, pp. 1843-1848, https://doi.org/10.1109/BIBM49941.2020.9313416
