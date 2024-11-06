# Cluster-Tracking Approach for Longitudinal Patient Data Analysis

## Purpose of the Repository

> [!NOTE]  
> This repository is a fork from [JudithLamb/Cluster-tracking](https://github.com/JudithLamb/Cluster-tracking). The purpose of this fork was to reorganise the code and give a reproducible development environment for @ReneeLeClech and I to run the code iteratively to get what is going on.

This repository contains the implementation of two novel cluster-tracking approaches for analyzing longitudinal patient data extracted from medico-administrative databases. The primary goals of this research are:

1. To identify clusters of patients at different ages using two clustering strategies:
   a. Markov Cluster algorithm (MCL) applied to patient networks built from raw data
   b. K-means applied directly to raw data
2. To track these clusters over time, defining cluster-trajectories
3. To visualize the results using an R Shiny application

The approaches were initially applied to antithrombotic drug reimbursements data from the Échantillon Généraliste des Bénéficiaires (EGB, a French cohort) between 2008 and 2018 for patients aged 60 to 70 years. Due to privacy concerns, this repository uses a simulated dataset of 5,594 patients with their drug reimbursements, derived from the original raw data.

This work aims to provide researchers and healthcare professionals with tools to better understand patient trajectories and drug usage patterns over time.

## Repository Structure

```{.sh}
.
├── .devcontainer
│   ├── devcontainer.json
│   └── Dockerfile
├── LICENSE
├── README.md
├── data
│   ├── README.md
│   ├── input
│   └── output
├── docs
│   ├── development-environment.md
│   └── methodology.md
├── renv.lock
├── requirements.txt
└── src
    ├── R
    │   ├── app.R
    │   └── functions.R
    └── python
        └── cluster_tracking.py
```

## Methodology

For information about the cluster-tracking approaches and the data analysis process, please see the [Methodology Documentation](docs/methodology.md).

## Development Environment Setup

To run the code in this repository, you'll need to set up a development environment. Please refer to the [Development Environment Setup](docs/development-environment.md) guide for detailed instructions.

##

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
