# 一鍵分析腳本 | Quick Analysis Script

自動產出研究計畫的四個核心圖表與統計摘要。

## 🚀 快速開始

### 1. 安裝套件

```bash
cd project_execution_guide/scripts
pip install -r requirements.txt
```

### 2. 準備資料

確保以下資料檔案已就緒：

```
project_data/
├── raw_data/
│   ├── python_test_scores.csv       # 前後測成績
│   ├── survey_data.csv              # 三時點量表
│   └── ai_interaction_log.csv       # AI互動紀錄
```

### 3. 執行分析

```bash
python quick_analysis.py
```

## 📊 產出結果

### 四張核心圖表

1. **rq1_python_ability.png**
   - 前後測箱型圖 + paired t-test + Cohen's d

2. **rq2_srl_ai_trends.png**
   - AI依賴與SRL能力三時點折線圖 + Friedman test

3. **rq3_ai_behavior.png**
   - Try-Before-AI比例柱狀圖（依階段）
   - 問題類型圓餅圖

4. **triangulation_heatmap.png**
   - 相關性熱圖（後測、SRL、Try-Before-AI）

### 統計摘要文字

**results/summary_stats.txt** 包含：
- 所有檢定結果（t值、p值、效果量）
- 描述統計（平均數、標準差）
- 階段變化百分比

## 🎯 對應研究問題

| 圖表 | 研究問題 | 分析方法 |
|------|---------|---------|
| 圖1 | Python能力提升 | paired t-test, Cohen's d |
| 圖2 | AI依賴/SRL轉變 | Friedman test |
| 圖3 | AI互動行為 | 描述統計、階段比較 |
| 圖4 | 資料整合 | Pearson相關性 |

## 📝 報告用語範例

### 研究問題一
> Python能力paired t-test顯示前後測有顯著差異（t(49)=5.23, p<.001），效果量d=0.74屬中等偏大效果。

### 研究問題二
> AI依賴Friedman test顯示三時點有顯著趨勢變化（χ²(2)=12.45, p=.002），由引導期M=3.8降至自主期M=2.9。

### 研究問題三
> 「先嘗試後求助」比例在轉換期較引導期提升15.3%，常見問題類型為debugging (42%)與design (35%)。

### 資料整合
> 相關性分析顯示後測成績與SRL能力呈中度正相關（r=.52, p<.01），與Try-Before-AI比例呈低度正相關（r=.28, p<.05）。

## 🔧 客製化調整

### 修改圖表樣式

編輯 `quick_analysis.py` 中的：
```python
sns.set_style("whitegrid")  # 可改為 "darkgrid", "white", "ticks"
sns.set_palette("husl")     # 可改為 "Set2", "Pastel1"
```

### 調整輸出解析度

```python
plt.savefig(..., dpi=300)  # 可改為 150, 600
```

### 更改中文字型

```python
plt.rcParams['font.sans-serif'] = ['你的字型名稱']
```

## ⚠️ 注意事項

1. **資料格式**：確保CSV檔案欄位名稱與範本一致
2. **缺失值**：腳本會自動過濾不完整資料
3. **樣本數**：三時點分析僅計算完整填答者
4. **階段劃分**：Week 1-6引導、7-12轉換、13-18自主

## 💡 疑難排解

### 找不到資料檔案
```bash
# 檢查資料路徑是否正確
ls project_data/raw_data/
```

### 中文顯示方塊
```bash
# macOS
brew install font-dejavu

# 或在程式中改用英文標籤
```

### 記憶體不足
```python
# 分批讀取大檔案
df = pd.read_csv('file.csv', chunksize=1000)
```

## 📚 延伸功能

可參考 `analysis_guide.md` 進行：
- 質性資料主題編碼
- 進階統計分析（ANOVA、迴歸）
- 互動式視覺化（Plotly）

---

**版本**: v1.0  
**更新**: 2025-12-02
