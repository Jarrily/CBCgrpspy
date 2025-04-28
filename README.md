# 📊 Three-line Table Toolkit  
```markdown
Automated comparative analysis tool for group data, supporting intelligent statistical tests for two/multiple groups with standardized output tables.
```
## ⚙️ Installation
```bash
pip install CBCgrpspy 
```

---

## 📖 Parameter Specifications

| Parameter           | Type        | Default   | Description                                                         |
|---------------------|-------------|-----------|---------------------------------------------------------------------|
| `df_path`           | `str`       | **Required** | Data file path (.xlsx/.csv supported)                              |
| `label_series`      | `str`       | "label"   | Target label column name (must specify if no "label" column exists) |
| `skewvaranalysis`   | `list`      | None      | Manually specified categorical variables                           |
| `norm_rd`           | `int`       | 2         | Decimal places for normal distributions (Mean ± SD format)         |
| `sk_rd`             | `int`       | 2         | Decimal places for non-normal distributions (Median (IQR) format)  |
| `cat_rd`            | `int`       | 0         | Decimal places for categorical variable percentages                |
| `pnormtest`         | `float`     | 0.05      | Significance threshold for normality tests                         |
| `phomogeneity`      | `float`     | 0.05      | Significance threshold for homogeneity of variance tests           |
| `extractp`          | `float`     | 0.05      | Threshold for identifying significant variables                    |
| `minfactorlevels`   | `int`       | 10        | Maximum categorical levels (variables exceeding this become continuous) |
| `showstatistic`     | `bool`      | True      | Whether to display statistical values in output                    |

---

## 🚀 Core Features

### 1. Two-Group Comparison (Binary Groups)
- **Use Cases**: Control vs Treatment, Male vs Female, etc.
- **Statistical Methods**:
  - 📌 Continuous variables: Auto-select T-test / Mann-Whitney U test
  - 📌 Categorical variables: Auto-select Chi-square / Fisher's exact test
- **Output**:
  - Standardized comparison table
  - Flagged significant variables (p < extractp)

### 2. Multi-Group Comparison (≥3 Groups)
- **Use Cases**: Age stratification, multiple treatment protocols, etc.
- **Statistical Methods**:
  - 📌 Continuous variables: ANOVA / Kruskal-Wallis test
  - 📌 Categorical variables: Chi-square / Monte Carlo Fisher simulation
- **Output**:
  - Multi-dimensional group comparison summary
  - Subgroup difference indicators

---

## 🎯 Quick Start Example
```python
from CBCgrpspy import dataAnalysis

dataAnalysis(
    df_path="analysis.xlsx",
    label_series="label",
    norm_rd=2,
    sk_rd=2,
    cat_rd=0,
    pnormtest=0.05,
    extractp=0.05,
    phomogeneity=0.05,
    maxfactorlevels=10,
    showstatistic=True
)
```

## 📊 Output Examples

---
### 1. Binary Groups Comparison
| Variables        | Total (n = 196)      | 0 (n = 97)          | 1 (n = 99)          | P-value   | statistic   |
|------------------|----------------------|---------------------|---------------------|-----------|-------------|
| **sex, n (%)**   |                      |                     |                     | **0.027** | **7.220**   |
| &nbsp;&nbsp;central | 56 (29)             | 36 (19)             | 20 (10)             |           |             |
| &nbsp;&nbsp;down    | 66 (34)             | 27 (14)             | 39 (20)             |           |             |
| &nbsp;&nbsp;up      | 74 (38)             | 34 (18)             | 40 (20)             |           |             |
| **location, n (%)** |                      |                     |                     | **0.230** | **1.443**   |
| &nbsp;&nbsp;man     | 119 (61)            | 63 (32)             | 56 (28)             |           |             |
| &nbsp;&nbsp;woman   | 77 (39)             | 34 (18)             | 43 (22)             |           |             |
| **age, Median (IQR)** | 51.45 (24.68, 72.70) | 56.70 (30.40, 79.70) | 48.40 (18.70, 62.85) | 0.055     | 5562.500    |
| **Feature_1, Median (IQR)** | 0.46 (-0.13, 0.76) | -0.13 (-0.69, 0.74) | 0.56 (0.31, 0.79)   | < 1e-03   | 3144.000    |
| **Feature_2, Median (IQR)** | 0.33 (-0.04, 0.80) | -0.05 (-0.68, 0.78) | 0.49 (0.24, 0.81)   | < 1e-03   | 3038.000    |
| **Feature_3, Median (IQR)** | 0.36 (0.01, 0.74) | 0.05 (-0.66, 0.77)  | 0.44 (0.26, 0.69)   | < 1e-03   | 3433.000    |
| **Feature_4, Median (IQR)** | 0.36 (-0.06, 0.80) | -0.07 (-0.72, 0.67) | 0.51 (0.24, 0.84)   | < 1e-03   | 2817.000    |

---
### 2. Multi-Groups Comparison (3 Groups)
| Variables        | Total (n=196)       | 0 (n=58)           | 1 (n=58)           | 2 (n=80)           | p        | statistic   |
|------------------|---------------------|--------------------|--------------------|--------------------|----------|-------------|
| **sex, n (%)**   |                     |                    |                    |                    | **0.01** | **13.228**  |
| &nbsp;&nbsp;central | 56 (29)            | 20 (34)            | 23 (40)            | 13 (16)            |          |             |
| &nbsp;&nbsp;down    | 66 (34)            | 20 (34)            | 12 (21)            | 34 (42)            |          |             |
| &nbsp;&nbsp;up      | 74 (38)            | 18 (31)            | 23 (40)            | 33 (41)            |          |             |
| **location, n (%)** |                     |                    |                    |                    | **0.179**| **3.443**   |
| &nbsp;&nbsp;man     | 119 (61)           | 41 (71)            | 33 (57)            | 45 (56)            |          |             |
| &nbsp;&nbsp;woman   | 77 (39)            | 17 (29)            | 25 (43)            | 35 (44)            |          |             |
| **age, Median (IQR)** | 51.75 (22.60, 70.85) | 51.95 (25.05, 68.80) | 60.10 (30.30, 74.42) | 44.85 (20.75, 65.55) | 0.204    | 3.176       |
| **Feature_1, Median (IQR)** | 0.46 (-0.13, 0.76) | -0.03 (-0.71, 0.75) | 0.27 (-0.34, 0.84) | 0.54 (0.27, 0.76) | 0.014    | 8.548       |
| **Feature_2, Median (IQR)** | 0.33 (-0.04, 0.80) | -0.08 (-0.70, 0.73) | 0.25 (-0.24, 0.82) | 0.48 (0.25, 0.80) | < 0.001  | 14.636      |
| **Feature_3, Median (IQR)** | 0.36 (0.01, 0.74) | -0.07 (-0.75, 0.76) | 0.36 (-0.37, 0.76) | 0.43 (0.27, 0.68) | 0.008    | 9.611       |
| **Feature_4, Median (IQR)** | 0.36 (-0.06, 0.80) | -0.09 (-0.59, 0.62) | 0.36 (-0.26, 0.74) | 0.52 (0.24, 0.84) | < 0.001  | 20.06       |

---

## 📌 Important Notes
1. Ensure the first row contains column headers
2. Convert categorical variables to string type beforehand
3. Recommended for use with Jupyter Notebook for optimal table rendering
4. This package has currently only been tested on **Windows 10/11** systems. Compatibility with macOS and Linux systems has not been verified.
---

## ✉️ Contact
**Package Maintainer**:  
Jarrily9527 (Jinhui Liu)  
📧 Email: [ljh18620847741@gmail.com](mailto:ljh18620847741@gmail.com)

---

> 💡 Pro Tip: Adjust `*_rd` parameters to control decimal precision. Use `showstatistic=False` for simplified outputs.
