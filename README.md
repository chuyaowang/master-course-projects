# Course Project Demos

The course projects at the VU/UvA's Master's in Bioinformatics and Systems Biology major more or less allowed for some creativity besides following the guidelines of what to analyze. To prevent plagiarism, the project code repositories are private. Here I will present some noteworthy points that I contributed to the projects.

The page now contains only barebones project information from my CV. Figures and more context will be added.

## Breast Cancer Subtype Classifier

* Project: Built a multi-class classifier to distinguish breast cancer subtypes from array CGH copy number variation data (VU Bioinformatics for Translational Medicine course).
* Feature Selection + XGBoost: Designed a pipeline combining multivariate feature selection (Sparse PLS-DA with tuned sparsity parameters) for high-dimensional genomic data with XGBoost, achieving 87% overall accuracy in nested cross-validation (HER2+ 100%, HR+ 86%, TN 75%).
* Parameter Finetuning: Set up a nested cross validation loop to optimize the parameters for sPLSDA (TBD).
* Model Interpretation: Used SHAP and SPLS-DA loadings to interpret model predictions, identifying chromosomal amplifications linked to HER2+ subtype, including the ERBB2 gene.

* **What I contributed/added:** everything here. Other members of the group explored other directions of feature selection and machine learning.

![sPLS-DA 3D plot and correlation circle](assets/breast%20cancer%20subtypes/splsda_combined.png)

**Figure 1:**
**(A)** sPLS-DA of the features before parameter tuning (column 1), after parameter tuning (column 2), and after feature selection (column 3). The top row shows latent variables 1 and 2; the bottom row shows latent variables 1-3. Parameter tuning let sPLS-DA better separate the groups. Feature selection then removed noisy features, leaving only those that best separated the three groups in sPLS-DA space; these features were used in XGBoost to learn a non-linear decision boundary.
**(B)** Correlation circle plot of the sPLS-DA loadings against the latent variables, using the tuned model and full feature set (Figure 1A, column 2). Longer arrows and arrows closer to an axis indicate a stronger contribution to that latent variable. The chromosomal range `17_35076296_35282086` contributes highly to the second latent variable, which separates the HER2+ subtype from the others. This range contains the ERBB2 gene, a known driver of the HER2+ subtype.

![SHAP value plot](assets/breast%20cancer%20subtypes/shap_value_plot.png)

**Figure 2:** Class-wise SHAP values for the top 15 contributing features in the HER2+ **(A)**, HR+ **(B)**, and Triple Neg **(C)** classification. A higher absolute SHAP value indicates a stronger contribution to the model's prediction for that class. In (A), the chromosomal range `17_35076296_35282086` is the top contributing feature for HER2+ classification, matching the conclusion from Figure 1B via a different feature-importance method.

## Multi-omics Analysis of Bacterial Stress Response

* Project: Integrated transcriptomics and proteomics analysis of cyanobacteria under phosphate limitation, combining wet-lab sample collection with multi-omics data integration (UvA Systems Biology in Practice course).
* Wet-lab Sampling: Harvested cyanobacterial cultures under phosphate-limited and control conditions; prepared cell extracts for RNA and protein extraction.
* Differential Expression Analysis: Analyzed RNA-seq count data using DESeq2 with Benjamini-Hochberg correction, and proteomics data with one-sample T-tests; identified 273 differentially expressed genes and 11 differentially expressed proteins.
* Functional Annotation and Network Analysis: Performed GO enrichment analysis (ShinyGO) and constructed a protein-protein interaction network in Cytoscape, identifying coordinated upregulation of phosphate transporters and downregulation of ribosomal genes.
* Multi-omics Integration: Compared transcriptomic and proteomic log2FC patterns to identify post-transcriptional regulatory mechanisms, and proposed mechanistic hypotheses for observed phenotypes including cell size increase and ploidy reduction.

* **What I contributed/added:** omics data analysis and integration. Generation of mechanistic hypotheses.

![Bacterial ploidy schematic, volcano plots, GO enrichment, and STRING network](assets/bacterial%20ploidy/bacterial_ploidy_combined.png)

**Figure 3:**
**(A)** Extracellular phosphate and light availability influence intracellular phosphate levels and, consequently, ploidy, since DNA synthesis requires phosphate. The bacterial strain used in this project, *Synechocystis* PCC6803, is a polyploid, meaning it has more than two complete sets of chromosomes per cell. Polyploidy affects environmental adaptation and growth and is hypothesized to serve as phosphate storage for the cell.
**(B)** Volcano plots of transcriptomic and proteomic data comparing phosphate-limited to phosphate-replete conditions.
**(C)** GO term enrichment for the up- and down-regulated genes and the up-regulated proteins in the phosphate-limited group relative to the non-limited group. Up-regulated genes are enriched for phosphate transporter-related terms, indicating increased phosphate transporter activity, while down-regulated genes are enriched for ribosome and translation-related terms, suggesting reduced translational activity under phosphate limitation. Up-regulated proteins show the same phosphate transporter enrichment, corroborating the transcriptomic result at the protein level.
**(D)** Protein-protein interaction network of significantly changed genes and proteins, built using the STRING database. Three major clusters emerge: two correspond to the phosphate transporter and ribosomal genes identified by GO analysis, and a third includes genes and proteins involved in cell-cell communication, environmental sensing, and intracellular signaling — most of which were up-regulated under phosphate limitation, suggesting the bacteria became more active in searching their environment for phosphate.

## Single-Cell Gene Expression Dynamics from smFISH

* Project: Quantitative analysis of single-cell gene expression dynamics during carbon-source adaptation in yeast using smFISH time-lapse microscopy data (VU Quantitative Single Cell Biology course).
* Single-Cell Tracking: Developed automated cell segmentation and colony detection pipelines using OpenCV to track individual cells and colonies across time-lapse frames.
* Gene Expression Quantification: Quantified GAL1 mRNA induction dynamics at single-cell resolution, measuring induction delay, fluorescence variability, and daughter-mother fluorescence partitioning across experimental conditions.
* Population Heterogeneity Analysis: Characterized intra- and inter-cellular transcriptional heterogeneity using time-series clustering and Fourier analysis of division cycles, linking colony-level spatial organization to single-cell expression variability.

* **What I contributed/added:** time-series clustering, frequency based analysis of division cycles, and colony-level single cell expression analysis.
