# 研究計畫改進總覽 | Project Improvements Summary

**更新日期**: 2025-12-02

---

## ✅ 已完成改進項目

### 1. 簡化資料分析方法（`sections/research_plan.tex`）

#### 修改內容
- **AI依賴與SRL分析**：明確指出「計算各構念總分以簡化分析」，避免逐題分析的複雜度
- **AI互動行為**：聚焦「先嘗試後求助」比例作為核心指標，依三階段（引導/轉換/自主）統計，取代複雜的時間序列
- **質性分析**：明確三主題（自我調節、AI依賴、學習策略），要求報告編碼一致性（Cohen's Kappa或文字說明）
- **資料整合**：改用「以圖表呈現量化趨勢並搭配質性引文」取代 "joint display" 術語
- **短版量表**：明確三時點皆用短版（16-20題），施測時間15分鐘內

#### 效益
- ✅ 減少統計複雜度，易於Python實作
- ✅ 降低學生填答負擔，提升完測率
- ✅ 報告更聚焦，符合25頁限制
- ✅ 用詞更清晰，IT背景易理解

---

### 2. 新增一鍵分析腳本（`project_execution_guide/scripts/`）

#### 核心功能
**quick_analysis.py** 自動產出：
1. **圖1**: Python能力前後測箱型圖 + paired t-test + Cohen's d
2. **圖2**: AI依賴與SRL三時點折線圖 + Friedman test
3. **圖3**: Try-Before-AI比例柱狀圖（依階段）+ 問題類型圓餅圖
4. **圖4**: 相關性熱圖（後測成績、SRL、Try-Before-AI）
5. **文字摘要**: 所有統計結果（t值、p值、效果量、描述統計）

#### 使用方式
```bash
cd project_execution_guide/scripts
pip install -r requirements.txt
python quick_analysis.py
```

#### 效益
- ✅ 一鍵產出4圖1表，節省分析時間
- ✅ 程式碼清晰註解，易於理解與修改
- ✅ 自動產生報告用語範例
- ✅ 確保分析可重現性

---

### 3. 完整表單與範本（`project_execution_guide/forms/`）

#### 已建立檔案（共10個）

**量化資料**:
1. `python_test_template.csv` - 前後測成績
2. `ai_dependency_srl_survey_template.csv` - 三時點量表（含35題完整版）
3. `ai_interaction_log_template.csv` - AI互動紀錄
4. `pbl_project_evaluation_template.csv` - 專題評量
5. `intervention_fidelity_checklist.csv` - 介入忠誠度檢核

**質性資料**:
6. `learning_reflection_template.md` - 學習反思報告範本
7. `focus_group_interview_guide.md` - 焦點團體訪談指引

**倫理與誠信**:
8. `academic_integrity_disclosure_template.md` - AI使用揭露表
9. `informed_consent_template.md` - 知情同意書

**說明文件**:
10. `README.md` - 表單使用說明與資料管理指引

#### 效益
- ✅ 所有表單標準化，確保資料格式一致
- ✅ 範例資料協助理解填寫方式
- ✅ 完整收集時程表，不遺漏任何步驟

---

## 📊 改進成效總結

### 分析複雜度降低
| 項目 | 改進前 | 改進後 |
|------|--------|--------|
| 量表題數 | 35題全程 | 16-20題短版 |
| 施測時間 | 20-25分鐘 | 15分鐘 |
| 統計指標 | 多維度分析 | 3核心指標 |
| 視覺化圖表 | 6-8張 | 4張核心圖 |
| 質性主題 | 開放編碼 | 聚焦3主題 |

### Python可操作性提升
| 功能 | 工具/套件 | 實作難度 |
|------|----------|---------|
| paired t-test | `scipy.stats.ttest_rel` | ⭐ 簡單 |
| Friedman test | `scipy.stats.friedmanchisquare` | ⭐ 簡單 |
| Cohen's d | `numpy` 計算 | ⭐ 簡單 |
| 階段標註 | `pandas` apply | ⭐⭐ 中等 |
| 視覺化 | `seaborn`, `matplotlib` | ⭐⭐ 中等 |
| 編碼一致性 | `sklearn.metrics.cohen_kappa_score` | ⭐⭐ 中等 |

### 頁數控制
- 資料分析方法段落：**精簡約200字**
- 移除冗餘術語與說明，保留核心方法
- 報告範本：**每個研究問題1-2句話即可**

---

## 🎯 核心改進原則

### 1. 聚焦高影響指標
- ❌ 移除：Kendall's W、逐題分析、週週趨勢線
- ✅ 保留：paired t-test、Friedman test、Try-Before-AI比例

### 2. Python友善設計
- 統一CSV格式與欄位名稱
- 階段自動標註（week → phase）
- 一鍵腳本產出所有結果

### 3. 報告簡潔化
- 用詞直白（圖表搭配引文 vs. joint display）
- 統計範本化（t(df)=…, p=…, d=…）
- 限制視覺化數量（4圖即可說明完整故事）

---

## 📁 專案檔案結構

```
115_teaching_study/
├── sections/
│   ├── research_plan.tex           ✅ 已簡化
│   └── teaching_design.tex         ⚪ 保持原樣
├── project_execution_guide/        ✅ 新增
│   ├── analysis_guide.md           ✅ 更新（加入快速腳本說明）
│   ├── forms/                      ✅ 10個表單範本
│   │   ├── python_test_template.csv
│   │   ├── ai_dependency_srl_survey_template.csv
│   │   ├── ai_interaction_log_template.csv
│   │   ├── pbl_project_evaluation_template.csv
│   │   ├── intervention_fidelity_checklist.csv
│   │   ├── learning_reflection_template.md
│   │   ├── focus_group_interview_guide.md
│   │   ├── academic_integrity_disclosure_template.md
│   │   ├── informed_consent_template.md
│   │   └── README.md
│   └── scripts/                    ✅ 新增
│       ├── quick_analysis.py       ✅ 一鍵分析
│       ├── requirements.txt        ✅ 套件清單
│       └── README.md               ✅ 使用說明
```

---

## 🚀 下一步建議

### 立即可做
1. ✅ 使用 `quick_analysis.py` 測試範例資料
2. ✅ 依需求調整圖表樣式（顏色、字型）
3. ✅ 準備質性編碼手冊（codebook）定義三主題

### 學期執行時
1. 第1週：發放知情同意書
2. 第2週：前測 + 開始收集AI互動紀錄
3. 第6/12/17週：三時點量表施測
4. 期中/期末：專題評量 + AI使用揭露表
5. 學期末：執行 `quick_analysis.py` 產出初步結果

### 論文撰寫時
1. 複製 `summary_stats.txt` 內容到結果章節
2. 插入4張圖表並簡述發現
3. 質性引文選擇6-8句對應三主題
4. 限制與討論：單組設計、短版量表、IT背景母群

---

## 💬 常見問題 FAQ

### Q1: 為什麼改用短版量表？
**A**: 降低學生負擔、提升完測率、簡化分析；35題全版可附錄供參考但不分析。

### Q2: Try-Before-AI如何定義？
**A**: AI互動紀錄中 `tried_before_ai` 欄位標示 yes/no，學生自陳是否先自己嘗試。

### Q3: 質性分析如何確保一致性？
**A**: 雙人編碼30%樣本，計算Cohen's Kappa（可用 `sklearn.metrics.cohen_kappa_score`），報告數值或文字說明。

### Q4: 資料缺失怎麼辦？
**A**: 腳本自動過濾不完整資料；三時點分析僅納入完整填答者；說明實際樣本數。

### Q5: 可以加入其他分析嗎？
**A**: 可以！參考 `analysis_guide.md` 的詳細範例，或修改 `quick_analysis.py` 加入新功能。

---

## 📧 支援資源

- **分析指南**: `project_execution_guide/analysis_guide.md`
- **表單說明**: `project_execution_guide/forms/README.md`
- **腳本使用**: `project_execution_guide/scripts/README.md`
- **原始計畫**: `sections/research_plan.tex`

---

**本次改進讓研究計畫更簡潔、更實用、更易於執行！** 🎉
