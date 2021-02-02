r = getOption("repos")
r["CRAN"] = "http://cran.us.r-project.org"
options(repos = r)

if (!requireNamespace("BiocManager", quietly = TRUE)) {
  install.packages("BiocManager")
} else {
  update.packages("BiocManager")
}

if (!requireNamespace("fgsea", quietly = TRUE))
  BiocManager::install("fgsea")
if (!requireNamespace("BiocParallel", quietly = TRUE))
  BiocManager::install("BiocParallel")
if (!requireNamespace("ggplot2", quietly = TRUE))
  BiocManager::install("ggplot2")

if (!requireNamespace("GSA", quietly = TRUE)) {
  install.packages("GSA")
} else {
  update.packages("GSA")
}

if (!requireNamespace("data.table", quietly = TRUE)) {
  install.packages("data.table")
} else {
  update.packages("data.table")
}

if (!requireNamespace("writexl", quietly = TRUE)) {
  install.packages("writexl")
} else {
  update.packages("writexl")
}

if (!requireNamespace("stringr", quietly = TRUE)) {
  install.packages("stringr")
} else {
  update.packages("stringr")
}
