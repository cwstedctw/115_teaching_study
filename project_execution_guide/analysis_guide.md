# 研究計畫執行指南 | Research Project Execution Guide

## 📋 專案概述 | Project Overview

本指南說明「AI鷹架漸退式程式設計教學」研究計畫的資料收集與分析流程，協助執行量化與質性資料分析。

---

## 🗂️ 資料收集清單 | Data Collection Checklist

### 1. 量化資料 (Quantitative Data)

#### Python程式設計能力測驗
- **前測**: 第2週
- **後測**: 第17週
- **檔案格式**: CSV
- **欄位**: `student_id`, `pretest_score`, `posttest_score`

#### AI依賴與SRL量表
- **施測時間**: 第6週、第12週、第17週
- **檔案格式**: CSV
- **欄位**: `student_id`, `week`, `ai_dependency_score`, `srl_score`, `q1`, `q2`, ..., `q35`

#### AI互動紀錄
- **收集時間**: 全學期每週
- **檔案格式**: CSV
- **欄位**: `student_id`, `week`, `problem_type`, `tried_before_ai`, `ai_prompt`, `adoption_decision`, `modification_notes`

#### PBL專題評量
- **評量時間**: 第12週(期中)、第18週(期末)
- **檔案格式**: CSV
- **欄位**: `student_id`, `code_correctness`, `problem_analysis`, `interface_design`, `creativity`, `reflection`

---

### 2. 質性資料 (Qualitative Data)

#### 學習反思報告
- **提交時間**: 第6、10、14、18週
- **檔案格式**: TXT 或 DOCX
- **命名規則**: `reflection_week{week}_student{id}.txt`

#### 焦點團體訪談
- **時間**: 第12週，2場
- **檔案格式**: TXT (逐字稿)
- **命名規則**: `interview_group{1或2}.txt`

---

## 🐍 Python分析流程 | Python Analysis Workflow

### 快速開始 | Quick Start

**一鍵產出所有核心圖表**（推薦）：
```bash
cd project_execution_guide/scripts
pip install -r requirements.txt
python quick_analysis.py
```

產出 4 張圖表 + 統計摘要文字，詳見 `scripts/README.md`

---

### 環境設置 | Environment Setup

```bash
# 安裝必要套件
pip install pandas numpy scipy matplotlib seaborn scikit-learn
```

### 研究問題一：Python程式設計能力分析

**測試方法**: Paired t-test

```python
import pandas as pd
from scipy import stats
import numpy as np

# 讀取資料
df = pd.read_csv('python_test_scores.csv')

# 計算前後測差異
pre_scores = df['pretest_score']
post_scores = df['posttest_score']

# Paired t-test
t_stat, p_value = stats.ttest_rel(post_scores, pre_scores)

# Cohen's d效果量
mean_diff = np.mean(post_scores - pre_scores)
std_diff = np.std(post_scores - pre_scores, ddof=1)
cohens_d = mean_diff / std_diff

print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_value:.3f}")
print(f"Cohen's d: {cohens_d:.3f}")
```

**結果解讀**:
- p < 0.05: 顯著提升
- Cohen's d > 0.5: 中等效果
- Cohen's d > 0.8: 大效果

---

### 研究問題二：AI依賴與SRL能力轉變

**測試方法**: Friedman test

```python
import pandas as pd
from scipy import stats

# 讀取資料
df = pd.read_csv('survey_data.csv')

# 整理三時點資料
week6 = df[df['week'] == 6]['ai_dependency_score'].values
week12 = df[df['week'] == 12]['ai_dependency_score'].values
week17 = df[df['week'] == 17]['ai_dependency_score'].values

# Friedman test
stat, p_value = stats.friedmanchisquare(week6, week12, week17)

print(f"Friedman statistic: {stat:.3f}")
print(f"p-value: {p_value:.3f}")
```

**同樣方式分析**: `srl_score`

---

### 研究問題三：AI互動行為分析

**分析方法**: 行為類型統計與時間序列趨勢

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取資料
df = pd.read_csv('ai_interaction_log.csv')

# 統計各週「先嘗試後求助」比例
tried_before_ratio = df.groupby('week')['tried_before_ai'].mean()

# 繪製趨勢圖
plt.figure(figsize=(10, 6))
plt.plot(tried_before_ratio.index, tried_before_ratio.values, marker='o')
plt.xlabel('Week')
plt.ylabel('Ratio of Try-Before-AI')
plt.title('Student Self-Attempt Behavior Trend')
plt.grid(True)
plt.savefig('ai_behavior_trend.png')
plt.show()

# 行為類型分布
behavior_dist = df['problem_type'].value_counts()
print(behavior_dist)
```

---

### 研究問題四：質性資料分析

**方法**: Thematic Analysis (主題分析法)

#### 步驟1: 準備文本資料

```python
import pandas as pd
import glob

# 讀取所有反思報告
reflection_files = glob.glob('reflections/*.txt')
reflections = []

for file in reflection_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        student_id = file.split('student')[1].split('.')[0]
        week = file.split('week')[1].split('_')[0]
        reflections.append({
            'student_id': student_id,
            'week': week,
            'content': content
        })

df_reflections = pd.DataFrame(reflections)
```

#### 步驟2: 編碼與分類

```python
# 手動編碼範例 (需兩位編碼者獨立進行)
# 建議主題類別:
# - AI_dependency (AI依賴)
# - self_regulation (自我調節)
# - learning_strategy (學習策略)
# - problem_solving (問題解決)
# - attitude_change (態度轉變)

df_reflections['theme'] = ''  # 手動標記主題

# 統計主題分布
theme_counts = df_reflections['theme'].value_counts()
print(theme_counts)
```

#### 步驟3: 雙人編碼一致性檢查

```python
from sklearn.metrics import cohen_kappa_score

# 假設兩位編碼者的結果
coder1_labels = [...]  # 編碼者1的標記
coder2_labels = [...]  # 編碼者2的標記

# Cohen's Kappa
kappa = cohen_kappa_score(coder1_labels, coder2_labels)
print(f"Inter-rater reliability (Kappa): {kappa:.3f}")
```

---

## 📊 資料整合 | Data Integration (Triangulation)

```python
import pandas as pd

# 讀取各類資料
python_scores = pd.read_csv('python_test_scores.csv')
survey_data = pd.read_csv('survey_data.csv')
ai_logs = pd.read_csv('ai_interaction_log.csv')

# 整合資料
merged_data = python_scores.merge(survey_data, on='student_id')
merged_data = merged_data.merge(ai_logs, on='student_id')

# 相關性分析
correlation = merged_data[['posttest_score', 'srl_score', 'tried_before_ai']].corr()
print(correlation)

# 視覺化
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Data Triangulation: Correlation Matrix')
plt.savefig('triangulation_heatmap.png')
plt.show()
```

---

## 📁 建議資料夾結構 | Recommended Folder Structure

```
project_data/
├── raw_data/
│   ├── python_test_scores.csv
│   ├── survey_data.csv
│   ├── ai_interaction_log.csv
│   ├── pbl_evaluation.csv
│   └── reflections/
│       ├── reflection_week6_student001.txt
│       └── ...
├── processed_data/
│   ├── cleaned_survey.csv
│   └── coded_reflections.csv
├── analysis_scripts/
│   ├── rq1_python_ability.py
│   ├── rq2_srl_change.py
│   ├── rq3_ai_behavior.py
│   └── rq4_qualitative.py
└── results/
    ├── figures/
    ├── tables/
    └── analysis_report.md
```

---

## ✅ 執行檢查表 | Execution Checklist

### 資料收集階段
- [ ] 第2週: 收集Python前測
- [ ] 第6週: 收集第一次量表、反思報告(1)
- [ ] 第10週: 收集反思報告(2)
- [ ] 第12週: 收集第二次量表、焦點團體訪談、期中專題
- [ ] 第14週: 收集反思報告(3)
- [ ] 第17週: 收集Python後測、第三次量表
- [ ] 第18週: 收集期末專題、反思報告(4)
- [ ] 全學期: 每週收集AI互動紀錄

### 資料分析階段
- [ ] 資料清理與格式標準化
- [ ] 執行研究問題一分析 (paired t-test, Cohen's d)
- [ ] 執行研究問題二分析 (Friedman test)
- [ ] 執行研究問題三分析 (行為統計、趨勢圖)
- [ ] 執行研究問題四分析 (主題編碼、雙人編碼一致性)
- [ ] 資料三角檢證與整合
- [ ] 生成圖表與結果報告

---

## 🔧 常見問題 | Troubleshooting

### Q1: 資料格式不一致怎麼辦?
```python
# 統一日期格式
df['week'] = pd.to_numeric(df['week'])

# 處理缺失值
df.fillna(0, inplace=True)
```

### Q2: 樣本數不足時?
- 使用非參數檢定 (如Friedman test已是非參數)
- 報告實際樣本數與效果量

### Q3: 質性編碼意見不一致?
- 討論差異並達成共識
- 建立明確的編碼手冊 (codebook)

---

## 📚 參考資源 | References

- **Pandas文件**: https://pandas.pydata.org/docs/
- **SciPy統計**: https://docs.scipy.org/doc/scipy/reference/stats.html
- **Matplotlib繪圖**: https://matplotlib.org/stable/tutorials/index.html
- **主題分析法**: Braun & Clarke (2006) 論文

---

**注意**: 本指南僅供執行參考，實際分析需依資料特性調整。
