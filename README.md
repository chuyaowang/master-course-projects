# Course Project Demos

The course projects at the VU/UvA's Master's in Bioinformatics and Systems Biology major more or less allowed for some creativity besides following the guidelines of what to analyze. To prevent plagiarism, the project code repositories are private. Here I will present some noteworthy points that I contributed to the projects.

The page now contains only barebones project information from my CV. Figures and more context will be added.

## Breast Cancer Subtype Classifier

* Project: Built a multi-class classifier to distinguish breast cancer subtypes from array CGH copy number variation data (VU Bioinformatics for Translational Medicine course).
* Feature Selection + XGBoost: Designed a pipeline combining multivariate feature selection (Sparse PLS-DA with tuned sparsity parameters) for high-dimensional genomic data with XGBoost, achieving 87% overall accuracy in nested cross-validation (HER2+ 100%, HR+ 86%, TN 75%).
* Parameter Finetuning: Set up a nested cross validation loop to optimize the parameters for sPLSDA (TBD).
* Model Interpretation: Used SHAP and SPLS-DA loadings to interpret model predictions, identifying chromosomal amplifications linked to HER2+ subtype, including the ERBB2 gene.

* **What I contributed/added:** everything here. Other members of the group explored other directions of feature selection and machine learning.

## Multi-omics Analysis of Bacterial Stress Response

* Project: Integrated transcriptomics and proteomics analysis of cyanobacteria under phosphate limitation, combining wet-lab sample collection with multi-omics data integration (UvA Systems Biology in Practice course).
* Wet-lab Sampling: Harvested cyanobacterial cultures under phosphate-limited and control conditions; prepared cell extracts for RNA and protein extraction.
* Differential Expression Analysis: Analyzed RNA-seq count data using DESeq2 with Benjamini-Hochberg correction, and proteomics data with one-sample T-tests; identified 273 differentially expressed genes and 11 differentially expressed proteins.
* Functional Annotation and Network Analysis: Performed GO enrichment analysis (ShinyGO) and constructed a protein-protein interaction network in Cytoscape, identifying coordinated upregulation of phosphate transporters and downregulation of ribosomal genes.
* Multi-omics Integration: Compared transcriptomic and proteomic log2FC patterns to identify post-transcriptional regulatory mechanisms, and proposed mechanistic hypotheses for observed phenotypes including cell size increase and ploidy reduction.

* **What I contributed/added:** omics data analysis and integration. Generation of mechanistic hypotheses.

## Single-Cell Gene Expression Dynamics from smFISH

* Project: Quantitative analysis of single-cell gene expression dynamics during carbon-source adaptation in yeast using smFISH time-lapse microscopy data (VU Quantitative Single Cell Biology course).
* Single-Cell Tracking: Developed automated cell segmentation and colony detection pipelines using OpenCV to track individual cells and colonies across time-lapse frames.
* Gene Expression Quantification: Quantified GAL1 mRNA induction dynamics at single-cell resolution, measuring induction delay, fluorescence variability, and daughter-mother fluorescence partitioning across experimental conditions.
* Population Heterogeneity Analysis: Characterized intra- and inter-cellular transcriptional heterogeneity using time-series clustering and Fourier analysis of division cycles, linking colony-level spatial organization to single-cell expression variability.

* **What I contributed/added:** time-series clustering, frequency based analysis of division cycles, and colony-level single cell expression analysis.
