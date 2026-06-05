<div align="center">

🔍 Job Posting Deception Intelligence Engine

The AI that doesn’t just detect fake jobs— it identifies how a posting may be deceptive.

<br>

🌐 Live Demo →
📄 Full Report →
📊 Dataset →

<br>
</div>

⸻

Executive Summary

Most existing fraud detection systems approach the problem as a basic binary classification problem- labelling postings as either 'real' or 'fake.' But deception isn't binary.

The Job Posting Deception Intelligence Engine extends beyond that approach by introducing a five-archetype deception taxonomy designed to identify how fraudulent or misleading job postings operate.

Built using Python and scikit-learn, the system was trained on 18,238 real-world job postings and combines fraud detection, NLP analysis, company-level risk profiling, and interactive analytics.

The live demo allows users to paste a job description into the prediction engine, receive an instant legitimacy assessment, and explore how deception patterns emerge across 18,238 real-world job postings through an immersive analytics experience.

⸻

Key Results

Metric	Value
ROC-AUC	0.967
F1 Score (Fake Class)	0.934
Average Precision	0.941
Cross-Validation AUC	0.961 ± 0.008
Job Postings Analyzed	18,238
Fraud Cases Identified	866
Companies Profiled	1,254

⸻

The 5 Deception Archetypes

Archetype	Description
🚨 Scam	Identity theft, financial extraction, and payment-related fraud
🎣 Bait & Switch	Misleading compensation structures or role expectations
🧾 Vague Trap	Excessively ambiguous postings with limited accountability
🕳️ Ghost Job	Listings showing little or no hiring intent
⚖️ Discriminatory	Potentially exclusionary hiring requirements

A single posting can belong to multiple archetypes simultaneously.

⸻

Key Findings

* Language-based features outperformed most structured metadata features.
* Scam postings were the easiest deception category to identify.
* Ghost jobs were the most difficult category to detect.
* Fraud patterns were concentrated among specific company profiles rather than being evenly distributed.
* Unusually wide salary ranges appeared more frequently in suspicious postings.
* The deception taxonomy provided additional interpretability beyond simple fraud classification.

⸻

Model Architecture

Raw Job Posting Data
        ↓
Feature Engineering
        ↓
TF-IDF Vectorization
(5,000 Bigram Features)
        ↓
13 Engineered Numeric Features
        ↓
Soft Voting Ensemble
├── Random Forest
├── Gradient Boosting
└── Logistic Regression
        ↓
Multi-Label Deception Classification
        ↓
Dashboard + Company Risk Analysis

⸻

Example Prediction

from deception_engine import predict
result = predict(
    "URGENT! No experience needed. Earn $5000/week. Wire transfer payment. Start today!"
)

Output:

{
    "verdict": "FAKE JOB DETECTED",
    "fake_score": "94.2%",
    "confidence": "HIGH",
    "deception_types": ["scam", "bait_switch"]
}

⸻

Technology Stack

Component	Technology
Language	Python 3.13
Machine Learning	scikit-learn
NLP	TF-IDF Vectorizer
Ensemble Learning	Random Forest, Gradient Boosting, Logistic Regression
Multi-Label Classification	MultiOutputClassifier
Clustering	TruncatedSVD, t-SNE, KMeans
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Seaborn
Deployment	GitHub Pages
Persistence	Joblib

⸻

Project Structure

Job_deception_intelligence/
│
├── data/
├── outputs/
├── deception_engine.py
├── deception_dashboard.py
├── index.html
├── README.md
└── requirements.txt

⸻

Full Report

For methodology, feature engineering, confusion matrices, company-level analysis, dashboard visualizations, and detailed findings, see:

📄 deception_intelligence_report.pdf

⸻

<div align="center">

Built with Python, Scikit-learn, Pandas, Streamlit, and Plotly

</div
