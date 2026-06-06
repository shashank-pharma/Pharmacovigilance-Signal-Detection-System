# Pharmacovigilance-Signal-Detection-System


A Python-based Pharmacovigilance (PV) Signal Detection tool designed to identify potential safety signals from Adverse Drug Reaction (ADR) reports using industry-recognized disproportionality methods such as **PRR (Proportional Reporting Ratio)** and **ROR (Reporting Odds Ratio)**.

## Project Overview

Pharmacovigilance plays a critical role in monitoring the safety of medicines after they reach the market. This project automates basic signal detection calculations and generates structured safety reports for drugs and their associated adverse drug reactions.

The system:

* Calculates Proportional Reporting Ratio (PRR)
* Calculates Reporting Odds Ratio (ROR)
* Applies WHO-UMC signal detection criteria
* Generates signal reports
* Logs activities and errors
* Saves reports to a text file for future review

---

## Features

### Signal Detection Metrics

#### 1. Proportional Reporting Ratio (PRR)

PRR compares the frequency of a specific ADR for a drug against the frequency of that ADR in the overall database.

Formula:

PRR = (Drug ADR Reports / Total Drug Reports) ÷ (All ADR Reports / Total Reports)

---

#### 2. Reporting Odds Ratio (ROR)

ROR measures the association between a drug and a specific adverse event.

Formula:

ROR = (a × d) / (b × c)

Where:

* a = Drug reports with ADR
* b = Drug reports without ADR
* c = Other reports with ADR
* d = Other reports without ADR

---

### WHO-UMC Signal Detection Criteria

A signal is considered detected when:

* PRR ≥ 2.0
* ADR Cases ≥ 3

---

## Project Structure

```text
├── pv_signal_detector.py
├── pv_signal_report.txt
├── pv_signal_log.txt
└── README.md
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Custom Exceptions
* File Handling
* Logging Module
* Pharmacovigilance Concepts

---

## Example Output

```text
============================================================
PHARMACOVIGILANCE SIGNAL ANALYSIS
============================================================

Drug         : Metformin
ADR          : Lactic Acidosis
Cases        : 45
PRR          : 10.417
ROR          : 13.296
Signal       : SIGNAL DETECTED
Criteria     : PRR ≥ 2.0 + Cases ≥ 3 (WHO-UMC)
```

---

## Sample Drugs Included

* Metformin → Lactic Acidosis
* Aspirin → GI Bleeding
* Atorvastatin → Myopathy
* Paracetamol → Hepatotoxicity
* Insulin → Hypoglycemia

---

## Error Handling

The project includes a custom exception:

```python
class InsufficientDataError(Exception):
    pass
```

This exception is raised when:

* Total reports are zero
* Required values are missing
* ADR case count is below WHO threshold

---

## Logging

All important activities are logged using Python's logging module.

Example:

```text
INFO - Signal Report Generated for Metformin and Lactic Acidosis
ERROR - WHO THRESHOLD LIMIT IS (3)
```

Logs are automatically stored in:

```text
pv_signal_log.txt
```

---

## Learning Outcomes

Through this project, I practiced:

* Pharmacovigilance signal detection concepts
* PRR and ROR calculations
* Object-Oriented Programming
* Custom Exception Handling
* Logging and File Handling
* Python Project Structuring
* Real-world healthcare data analysis concepts

---

## Future Improvements

* CSV/Excel data import
* Graphical dashboard
* Confidence Interval calculations
* Bayesian Signal Detection Models
* Regulatory Reporting Integration
* Database Connectivity (MySQL/PostgreSQL)

---

## Author

**Shashank Limje**

B.Pharm Graduate | Pharmacovigilance | Regulatory Affairs | Python Programming | Healthcare Analytics

---

### Disclaimer

This project is developed for educational and learning purposes only. It does not replace validated pharmacovigilance systems used by regulatory authorities or pharmaceutical companies.
