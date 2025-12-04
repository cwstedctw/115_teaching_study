# 研究表單與範本說明 | Forms and Templates Documentation

本資料夾包含研究計畫執行所需的所有表單、量表與範本。

---

## 📋 表單清單 | Form List

### 1. 量化資料收集表單

#### 1.1 Python能力測驗
- **檔案**: `python_test_template.csv`
- **用途**: 記錄前測與後測成績
- **欄位**: 學生ID、測驗類型、日期、各題分數、總分
- **施測時間**: 第2週（前測）、第17週（後測）

#### 1.2 AI依賴與SRL量表
- **檔案**: `ai_dependency_srl_survey_template.csv`
- **用途**: 收集學生AI使用態度與自我調節學習能力
- **欄位**: 學生ID、日期、週次、題目編號、回應分數
- **題目數量**: 35題（AI依賴12題 + SRL能力23題）
- **計分方式**: Likert 5點量表（1=非常不同意，5=非常同意）
- **施測時間**: 第6、12、17週

#### 1.3 AI互動紀錄
- **檔案**: `ai_interaction_log_template.csv`
- **用途**: 記錄學生與AI工具的互動過程
- **欄位**: 
  - 問題類型（debugging/design/optimization/application）
  - 先嘗試步驟
  - AI工具與提示
  - 採納決定與理由
  - 驗證方式與結果
- **提交頻率**: 每週3-5筆

#### 1.4 PBL專題評量
- **檔案**: `pbl_project_evaluation_template.csv`
- **用途**: 評量期中與期末專題
- **評量向度**:
  - 程式碼正確性（30%）
  - 問題分析深度（25%）
  - 介面設計（20%）
  - 創意應用（15%）
  - 學習反思（10%）
- **評量時間**: 第12週（期中）、第18週（期末）

#### 1.5 介入忠誠度檢核表
- **檔案**: `intervention_fidelity_checklist.csv`
- **用途**: 確保三階段教學設計的執行一致性
- **記錄內容**: 
  - 提示模板使用率
  - 教學步驟完成情況
  - 各週教學活動
- **填寫者**: 教師/助教

---

### 2. 質性資料收集表單

#### 2.1 學習反思報告範本
- **檔案**: `learning_reflection_template.md`
- **用途**: 引導學生撰寫學習反思
- **內容架構**:
  1. 學習內容回顧
  2. AI工具使用經驗
  3. 學習策略與自我調節
  4. 對AI輔助學習的反思
  5. 學習成果自我評估
  6. 下階段學習目標
  7. 其他想法或建議
- **提交時間**: 第6、10、14、18週
- **建議字數**: 500-1000字

#### 2.2 焦點團體訪談指引
- **檔案**: `focus_group_interview_guide.md`
- **用途**: 提供訪談主持人使用的半結構式訪談指引
- **訪談主題**:
  1. 學習經驗與感受（15分鐘）
  2. AI工具使用經驗（20分鐘）
  3. 學習策略與自我調節（15分鐘）
  4. 對三階段教學的看法（10分鐘）
- **訪談時間**: 第12週
- **參與人數**: 每場6-8人，共2場

---

### 3. 學術誠信與倫理表單

#### 3.1 AI使用揭露與學術誠信聲明表
- **檔案**: `academic_integrity_disclosure_template.md`
- **用途**: 專題繳交時揭露AI使用情況
- **內容包含**:
  - AI工具使用揭露
  - 程式碼原創性聲明
  - 理解與掌握程度自評
  - 可重現性說明（測試證據）
  - 學習反思
  - 學術誠信聲明
- **提交時間**: 期中與期末專題繳交時

#### 3.2 研究參與知情同意書
- **檔案**: `informed_consent_template.md`
- **用途**: 開學第一週取得學生研究參與同意
- **內容說明**:
  - 研究目的與內容
  - 參與方式與權益
  - 可能風險與效益
  - 資料保密與使用
  - 自願參與與退出權利
- **發放時間**: 第1週

---

## 🔄 資料收集時程表 | Data Collection Timeline

| 週次 | 階段 | 收集項目 | 表單 |
|------|------|---------|------|
| 1 | - | 知情同意書 | informed_consent |
| 2 | 引導期 | Python前測 | python_test_template |
| 6 | 引導期末 | 第一次量表、反思報告(1) | survey_template, reflection_template |
| 10 | 轉換期 | 反思報告(2) | reflection_template |
| 12 | 轉換期末 | 第二次量表、訪談、期中專題 | survey_template, interview_guide, pbl_evaluation + integrity_disclosure |
| 14 | 自主期 | 反思報告(3) | reflection_template |
| 17 | 自主期末 | Python後測、第三次量表 | python_test_template, survey_template |
| 18 | 自主期末 | 期末專題、反思報告(4) | pbl_evaluation + integrity_disclosure, reflection_template |
| 全學期 | - | AI互動紀錄（每週） | ai_interaction_log |
| 全學期 | - |介入忠誠度檢核（每週） | intervention_fidelity_checklist |

---

## 💾 資料管理建議 | Data Management Guidelines

### 檔案命名規範

**學生資料**:
- Python測驗: `python_test_{pretest/posttest}_{date}.csv`
- 量表: `survey_week{6/12/17}_{date}.csv`
- AI紀錄: `ai_log_week{week}_{date}.csv`
- 反思: `reflection_week{6/10/14/18}_student{ID}.md`
- 專題評量: `pbl_{midterm/final}_evaluation_{date}.csv`

**教師資料**:
- 介入檢核: `fidelity_check_week{week}_{date}.csv`
- 訪談紀錄: `interview_group{1/2}_{date}.txt`

### 資料儲存結構

```
research_data/
├── 01_informed_consent/
│   └── consent_forms_2025.pdf
├── 02_quantitative/
│   ├── python_tests/
│   ├── surveys/
│   ├── ai_logs/
│   └── pbl_evaluations/
├── 03_qualitative/
│   ├── reflections/
│   └── interviews/
├── 04_fidelity_checks/
└── 05_processed/
    └── cleaned_data/
```

### 資料保護措施

1. **去識別化**: 使用學生代碼（S001, S002...）取代真實姓名
2. **加密儲存**: 敏感資料使用密碼保護
3. **備份**: 定期備份至安全雲端空間
4. **存取控制**: 僅研究團隊成員可存取

---

## 📊 資料處理流程 | Data Processing Workflow

### 步驟1: 資料收集
使用上述表單收集原始資料

### 步驟2: 資料檢查
- 檢查缺失值
- 檢查異常值
- 確認資料格式一致

### 步驟3: 資料清理
```python
import pandas as pd

# 讀取資料
df = pd.read_csv('raw_data.csv')

# 處理缺失值
df.fillna(method='ffill', inplace=True)

# 標準化格式
df['week'] = df['week'].astype(int)

# 去識別化
df['student_id'] = df['student_id'].apply(lambda x: f"S{x:03d}")

# 儲存清理後資料
df.to_csv('cleaned_data.csv', index=False)
```

### 步驟4: 資料分析
參考 `analysis_guide.md` 執行統計分析

### 步驟5: 結果報告
整理分析結果，產生圖表與報告

---

## ⚠️ 注意事項 | Important Notes

### 填寫指引
1. **即時記錄**: AI互動紀錄應在使用AI後立即填寫，避免遺忘
2. **誠實填寫**: 所有資料強調誠實填寫，無對錯之分
3. **完整性**: 確保必填欄位都有填寫
4. **一致性**: 學生ID等關鍵欄位保持一致

### 倫理考量
- 學生有權拒絕參與研究
- 不參與研究不影響課程成績
- 所有資料保密處理
- 學生可隨時退出研究

### 品質控管
- 雙人編碼質性資料以確保一致性
- 定期檢查資料收集完整性
- 記錄介入忠誠度確保教學一致性

---

## 📧 問題與支援 | Support

如有表單使用問題，請聯絡：

**研究主持人**: ___________  
**Email**: ___________  
**Office**: ___________

---

**版本**: v1.0  
**更新日期**: 2025-11-29
