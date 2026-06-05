<div align="center">

<h1 style="color: #A259FF; font-weight: bold; font-size: 2.2em; border-bottom: none; margin-bottom: 0px; padding-bottom: 0px;">🔮 Job Posting Deception Intelligence Engine</h1>
<p style="color: #EC4899; font-style: italic; font-size: 1.2em; margin-top: 5px; margin-bottom: 25px;">Multi-Label AI Classification System</p>

![Python](https://img.shields.io/badge/Python-1E1035?style=for-the-badge&logo=python&logoColor=A259FF) ![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1E1035?style=for-the-badge&logo=scikit-learn&logoColor=EC4899) ![Streamlit](https://img.shields.io/badge/Streamlit-1E1035?style=for-the-badge&logo=streamlit&logoColor=C084FC)

---

📥 **[Download Deception Intelligence Report (PDF)](./Deception_report.pdf)**

</div>

---

# 🎯 Executive Summary

**Most existing fraud detection systems approach the problem as a basic binary classification problem—labelling postings as either 'real' or 'fake.' But deception isn't binary.**

The Job Posting Deception Intelligence Engine extends beyond that approach by introducing a **five-archetype deception taxonomy** designed to identify exactly *how* fraudulent or misleading job postings operate. Built using Python and scikit-learn, the system was trained on 18,238 real-world job postings and combines fraud detection, NLP analysis, company-level risk profiling, and interactive analytics.

The live dashboard application allows users to paste any job description into the prediction engine, receive an instant legitimacy assessment, and explore how deception patterns emerge across 18,238 real-world job postings through an immersive analytics experience.

---

# 📊 Key Metrics

| Metric | Value |
| :--- | :--- |
| **ROC-AUC** | `0.967` |
| **F1 Score (Fake Class)** | `0.934` |
| **Average Precision** | `0.941` |
| **Cross-Validation AUC** | `0.961 ± 0.008` |
| **Job Postings Analyzed** | `18,238` |
| **Fraud Cases Identified** | `866` |
| **Companies Profiled** | `1,254` |

---

# 🏷️ The 5 Deception Archetypes

| Archetype | Behavioral Indication |
| :--- | :--- |
| 🚨 **Scam** | Identity theft, financial extraction, and payment-related fraud |
| 🎣 **Bait & Switch** | Misleading compensation structures or role expectations |
| 🧾 **Vague Trap** | Excessively ambiguous postings with limited accountability |
| 🕳️ **Ghost Job** | Listings showing little or no hiring intent |
| ⚖️ **Discriminatory** | Potentially exclusionary hiring requirements |

> 💡 *A single posting can belong to multiple archetypes simultaneously.*

---

# 💡 Key Findings

* Language-based features outperformed most structured metadata features.
* Scam postings were the easiest deception category to identify.
* Ghost jobs were the most difficult category to detect.
* Fraud patterns were concentrated among specific company profiles rather than being evenly distributed.
* Unusually wide salary ranges appeared more frequently in suspicious postings.
* The deception taxonomy provided additional interpretability beyond simple fraud classification.

---

# 🛠️ Model Architecture

```text
Raw Job Posting Data
        ↓
Feature Engineering
        ↓
TF-IDF Vectorization (5,000 Bigram Features) + 13 Engineered Numeric Features
        ↓
Soft Voting Ensemble (Random Forest + Gradient Boosting + Logistic Regression)
        ↓
Multi-Label Deception Classification
        ↓
Dashboard + Company Risk Analysis

<div align="center">


Built with Python, Scikit-learn, Pandas, Streamlit, and Plotly


</div
