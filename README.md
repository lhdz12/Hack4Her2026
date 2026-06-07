# Gale

**Predicting customer churn before it happens.**

Gale is an AI-powered customer churn prediction platform developed for ARCA Continental. The project combines machine learning, business intelligence, and generative AI to help commercial teams identify at-risk customers, understand the reasons behind their risk, and take proactive retention actions.

---

## Problem

Customer churn is one of the biggest challenges in the beverage distribution industry. With thousands of retail stores across multiple territories, it is difficult to manually identify which customers are likely to stop purchasing.

Our analysis revealed that customer sales often decline dramatically during the months leading up to churn, creating an opportunity to intervene before customers are lost.

The challenge was to transform large volumes of customer, sales, transaction, and equipment data into actionable insights that help sales teams prioritize retention efforts.

---

## Solution

Gale uses a LightGBM machine learning model to predict the probability that a customer will churn.

The platform provides:

* Churn probability predictions for individual customers.
* Business intelligence dashboards and KPIs.
* Identification of customers with sales drops greater than 40%.
* Filtering by Customer ID, territory, business channel, and risk level.
* AI-generated explanations and retention recommendations using Llama 3.2 through Ollama.
* Interactive visualizations for customer risk analysis.

All functionality is delivered through a Streamlit web application designed for business users.

---

## Key Insights

Through exploratory analysis and modeling, we discovered:

* Only **17.95%** of customers churn.
* Customer sales typically decline by nearly **100% during the six months preceding churn**.
* The most critical intervention window occurs approximately **3 to 4 months before churn**.
* Territories such as **Monclova, Reynosa, Guadalajara, and Monterrey** show significant churn activity and should be prioritized for retention efforts.

---

## Machine Learning Model

### Model

* LightGBM Classifier

### Performance

* Accuracy: **98.3%**
* Recall (Churn Class): **81.2%**
* ROC-AUC: **> 0.98**

### Feature Engineering

To improve predictive performance, we engineered behavioral features from historical customer activity, including:

* Short-term sales decline
* Transaction slowdown
* Historical sales trends
* Customer purchasing consistency
* Cooler utilization efficiency
* Store characteristics
* Commercial channel information
* Territory-level indicators

Redundant and highly correlated variables were removed to improve model robustness and generalization.

---

## Explainable AI

Predictions alone are not enough for business decision-making.

To provide actionable insights, Gale integrates **Llama 3.2** running locally through **Ollama**. For each customer, the AI generates:

* Risk summaries
* Possible causes of churn
* Recommended retention actions

This helps sales teams understand not only *who* is at risk, but also *why*.

---

## Application Features

### Dashboard KPIs

* Monthly sales performance
* Churn risk distribution
* High-risk customer counts
* Customers with >40% sales decline

### Advanced Filters

* Customer ID
* Territory
* Commercial channel
* Number of detected risk signals

### Customer-Level Analysis

* Churn probability
* Risk indicators
* AI-generated explanations
* Retention recommendations

---

## Tech Stack

### Data Science & Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* LightGBM

### AI

* Ollama
* Llama 3.2

### Frontend & Visualization

* Streamlit
* Plotly

### Development Tools

* Git
* GitHub

---

## Team

Gale was developed by a multidisciplinary team of four members combining expertise in:

* Machine Learning
* Data Science
* Business Analysis
* Product Development
* Frontend Development

---

## Future Work

Future versions of Gale will include:

* Real-time churn monitoring
* Automated retention alerts
* CRM integration
* Personalized customer retention strategies
* Sales forecasting
* Territory optimization analytics

---

## Impact

By identifying churn months before it occurs and providing actionable explanations, Gale enables ARCA Continental to move from reactive customer management to proactive retention, helping protect revenue and strengthen customer relationships.

---

## License

Developed for hackathon purposes.
