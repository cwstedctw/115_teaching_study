"""
一鍵產出研究問題核心圖表與報告數據
Generate core figures and summary stats for all research questions

使用方式 | Usage:
    python quick_analysis.py

輸出 | Output:
    - results/figures/ 目錄下產生 4 張圖
    - results/summary_stats.txt 文字統計摘要
"""

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# 設定中文字型與視覺風格
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang TC']
plt.rcParams['axes.unicode_minus'] = False
sns.set_style("whitegrid")
sns.set_palette("husl")

# 建立輸出目錄
OUTPUT_DIR = Path("results/figures")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def load_data():
    """載入所有資料檔案"""
    python_scores = pd.read_csv("project_data/raw_data/python_test_scores.csv")
    survey = pd.read_csv("project_data/raw_data/survey_data.csv")
    ai_logs = pd.read_csv("project_data/raw_data/ai_interaction_log.csv")
    return python_scores, survey, ai_logs

def add_phase_labels(df, week_col='week'):
    """依週次標註階段 (引導/轉換/自主)"""
    def get_phase(week):
        if week <= 6:
            return '引導期'
        elif week <= 12:
            return '轉換期'
        else:
            return '自主期'
    df['phase'] = df[week_col].apply(get_phase)
    return df

def rq1_python_ability(python_scores):
    """
    研究問題一：Python程式設計能力分析
    paired t-test + Cohen's d + boxplot
    """
    print("\n" + "="*60)
    print("研究問題一：Python程式設計能力")
    print("="*60)
    
    pre = python_scores['pretest_score']
    post = python_scores['posttest_score']
    
    # Paired t-test
    t_stat, p_value = stats.ttest_rel(post, pre)
    
    # Cohen's d (using difference scores)
    diff = post - pre
    cohens_d = np.mean(diff) / np.std(diff, ddof=1)
    
    print(f"\n前測平均: {pre.mean():.2f} (SD={pre.std():.2f})")
    print(f"後測平均: {post.mean():.2f} (SD={post.std():.2f})")
    print(f"paired t-test: t({len(pre)-1}) = {t_stat:.3f}, p = {p_value:.4f}")
    print(f"Cohen's d: {cohens_d:.3f}")
    
    if p_value < 0.05:
        print("✓ 達顯著差異 (p < .05)")
    else:
        print("✗ 未達顯著差異")
    
    # 視覺化
    fig, ax = plt.subplots(figsize=(8, 6))
    data_to_plot = pd.DataFrame({
        '前測': pre,
        '後測': post
    })
    data_melted = data_to_plot.melt(var_name='測驗', value_name='分數')
    
    sns.boxplot(data=data_melted, x='測驗', y='分數', ax=ax)
    sns.stripplot(data=data_melted, x='測驗', y='分數', 
                  color='black', alpha=0.3, size=3, ax=ax)
    
    ax.set_title(f'Python能力前後測比較\nt({len(pre)-1})={t_stat:.2f}, p={p_value:.3f}, d={cohens_d:.2f}',
                 fontsize=14, fontweight='bold')
    ax.set_ylabel('測驗分數', fontsize=12)
    ax.set_xlabel('', fontsize=12)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "rq1_python_ability.png", dpi=300, bbox_inches='tight')
    print(f"\n圖表已儲存: {OUTPUT_DIR / 'rq1_python_ability.png'}")
    plt.close()

def rq2_srl_ai_trends(survey):
    """
    研究問題二：AI依賴與SRL能力轉變
    Friedman test + line plot for 3 time points
    """
    print("\n" + "="*60)
    print("研究問題二：AI依賴與SRL能力轉變")
    print("="*60)
    
    # 計算各構念總分 (假設欄位為 ai_dependency_score, srl_score)
    week6 = survey[survey['week'] == 6]
    week12 = survey[survey['week'] == 12]
    week17 = survey[survey['week'] == 17]
    
    # AI依賴分析
    ai_w6 = week6.groupby('student_id')['ai_dependency_score'].mean()
    ai_w12 = week12.groupby('student_id')['ai_dependency_score'].mean()
    ai_w17 = week17.groupby('student_id')['ai_dependency_score'].mean()
    
    # 對齊學生ID
    common_students = set(ai_w6.index) & set(ai_w12.index) & set(ai_w17.index)
    ai_w6 = ai_w6[list(common_students)].values
    ai_w12 = ai_w12[list(common_students)].values
    ai_w17 = ai_w17[list(common_students)].values
    
    stat_ai, p_ai = stats.friedmanchisquare(ai_w6, ai_w12, ai_w17)
    
    print(f"\nAI依賴程度:")
    print(f"  第6週平均: {ai_w6.mean():.2f} (SD={ai_w6.std():.2f})")
    print(f"  第12週平均: {ai_w12.mean():.2f} (SD={ai_w12.std():.2f})")
    print(f"  第17週平均: {ai_w17.mean():.2f} (SD={ai_w17.std():.2f})")
    print(f"  Friedman test: χ²(2) = {stat_ai:.3f}, p = {p_ai:.4f}")
    
    # SRL能力分析
    srl_w6 = week6.groupby('student_id')['srl_score'].mean()
    srl_w12 = week12.groupby('student_id')['srl_score'].mean()
    srl_w17 = week17.groupby('student_id')['srl_score'].mean()
    
    srl_w6 = srl_w6[list(common_students)].values
    srl_w12 = srl_w12[list(common_students)].values
    srl_w17 = srl_w17[list(common_students)].values
    
    stat_srl, p_srl = stats.friedmanchisquare(srl_w6, srl_w12, srl_w17)
    
    print(f"\nSRL能力:")
    print(f"  第6週平均: {srl_w6.mean():.2f} (SD={srl_w6.std():.2f})")
    print(f"  第12週平均: {srl_w12.mean():.2f} (SD={srl_w12.std():.2f})")
    print(f"  第17週平均: {srl_w17.mean():.2f} (SD={srl_w17.std():.2f})")
    print(f"  Friedman test: χ²(2) = {stat_srl:.3f}, p = {p_srl:.4f}")
    
    # 視覺化
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    weeks = [6, 12, 17]
    ai_means = [ai_w6.mean(), ai_w12.mean(), ai_w17.mean()]
    srl_means = [srl_w6.mean(), srl_w12.mean(), srl_w17.mean()]
    
    # AI依賴趨勢
    ax1.plot(weeks, ai_means, marker='o', linewidth=2, markersize=8, label='AI依賴')
    ax1.fill_between(weeks, ai_means, alpha=0.3)
    ax1.set_title(f'AI依賴程度變化\nFriedman χ²(2)={stat_ai:.2f}, p={p_ai:.3f}',
                  fontsize=12, fontweight='bold')
    ax1.set_xlabel('週次', fontsize=11)
    ax1.set_ylabel('平均分數', fontsize=11)
    ax1.set_xticks(weeks)
    ax1.grid(True, alpha=0.3)
    
    # SRL能力趨勢
    ax2.plot(weeks, srl_means, marker='s', linewidth=2, markersize=8, 
             color='green', label='SRL能力')
    ax2.fill_between(weeks, srl_means, alpha=0.3, color='green')
    ax2.set_title(f'SRL能力變化\nFriedman χ²(2)={stat_srl:.2f}, p={p_srl:.3f}',
                  fontsize=12, fontweight='bold')
    ax2.set_xlabel('週次', fontsize=11)
    ax2.set_ylabel('平均分數', fontsize=11)
    ax2.set_xticks(weeks)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "rq2_srl_ai_trends.png", dpi=300, bbox_inches='tight')
    print(f"\n圖表已儲存: {OUTPUT_DIR / 'rq2_srl_ai_trends.png'}")
    plt.close()

def rq3_ai_behavior(ai_logs):
    """
    研究問題三：AI互動行為分析
    Try-before-AI ratio by phase + problem type distribution
    """
    print("\n" + "="*60)
    print("研究問題三：AI互動行為分析")
    print("="*60)
    
    # 加入階段標籤
    ai_logs = add_phase_labels(ai_logs, week_col='week')
    
    # Try-Before-AI 比例依階段統計
    phase_order = ['引導期', '轉換期', '自主期']
    try_ratio = ai_logs.groupby('phase')['tried_before_ai'].apply(
        lambda x: (x == 'yes').sum() / len(x) * 100
    )
    try_ratio = try_ratio.reindex(phase_order)
    
    print("\n「先嘗試後求助」比例:")
    for phase in phase_order:
        print(f"  {phase}: {try_ratio[phase]:.1f}%")
    
    delta_transition = try_ratio['轉換期'] - try_ratio['引導期']
    delta_autonomous = try_ratio['自主期'] - try_ratio['轉換期']
    print(f"\n轉換期相較引導期變化: {delta_transition:+.1f}%")
    print(f"自主期相較轉換期變化: {delta_autonomous:+.1f}%")
    
    # 問題類型分布
    problem_dist = ai_logs['problem_type'].value_counts()
    print(f"\n問題類型分布:")
    for ptype, count in problem_dist.items():
        pct = count / len(ai_logs) * 100
        print(f"  {ptype}: {count} 次 ({pct:.1f}%)")
    
    # 視覺化
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Try-Before-AI柱狀圖
    bars = ax1.bar(phase_order, try_ratio.values, color=['#3498db', '#2ecc71', '#e74c3c'])
    ax1.set_title('各階段「先嘗試後求助」比例', fontsize=12, fontweight='bold')
    ax1.set_ylabel('比例 (%)', fontsize=11)
    ax1.set_ylim(0, 100)
    
    for bar in bars:
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.1f}%', ha='center', va='bottom', fontsize=10)
    
    # 問題類型圓餅圖
    ax2.pie(problem_dist.values, labels=problem_dist.index, autopct='%1.1f%%',
            startangle=90, textprops={'fontsize': 10})
    ax2.set_title('問題類型分布', fontsize=12, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "rq3_ai_behavior.png", dpi=300, bbox_inches='tight')
    print(f"\n圖表已儲存: {OUTPUT_DIR / 'rq3_ai_behavior.png'}")
    plt.close()

def triangulation_heatmap(python_scores, survey, ai_logs):
    """
    資料整合：相關性熱圖
    posttest_score vs srl_score vs tried_before_ai ratio
    """
    print("\n" + "="*60)
    print("資料整合：相關性分析")
    print("="*60)
    
    # 合併資料
    # 後測分數
    post_scores = python_scores[['student_id', 'posttest_score']]
    
    # 第17週SRL分數
    srl_final = survey[survey['week'] == 17].groupby('student_id')['srl_score'].mean().reset_index()
    
    # Try-Before-AI比例（全學期）
    try_ratio = ai_logs.groupby('student_id')['tried_before_ai'].apply(
        lambda x: (x == 'yes').sum() / len(x)
    ).reset_index()
    try_ratio.columns = ['student_id', 'try_before_ai_ratio']
    
    # 合併
    merged = post_scores.merge(srl_final, on='student_id', how='inner')
    merged = merged.merge(try_ratio, on='student_id', how='inner')
    
    # 計算相關性
    corr_matrix = merged[['posttest_score', 'srl_score', 'try_before_ai_ratio']].corr()
    
    print("\n相關性矩陣:")
    print(corr_matrix.round(3))
    
    # 視覺化
    fig, ax = plt.subplots(figsize=(8, 6))
    
    sns.heatmap(corr_matrix, annot=True, fmt='.3f', cmap='coolwarm', 
                center=0, vmin=-1, vmax=1, square=True, ax=ax,
                xticklabels=['後測成績', 'SRL能力', 'Try-Before-AI比例'],
                yticklabels=['後測成績', 'SRL能力', 'Try-Before-AI比例'])
    
    ax.set_title('資料整合：相關性熱圖', fontsize=14, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "triangulation_heatmap.png", dpi=300, bbox_inches='tight')
    print(f"\n圖表已儲存: {OUTPUT_DIR / 'triangulation_heatmap.png'}")
    plt.close()

def save_summary(python_scores, survey, ai_logs):
    """儲存文字統計摘要"""
    output_path = Path("results/summary_stats.txt")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*60 + "\n")
        f.write("研究計畫核心統計摘要\n")
        f.write("="*60 + "\n\n")
        
        # RQ1
        pre = python_scores['pretest_score']
        post = python_scores['posttest_score']
        t_stat, p_value = stats.ttest_rel(post, pre)
        diff = post - pre
        cohens_d = np.mean(diff) / np.std(diff, ddof=1)
        
        f.write("研究問題一：Python程式設計能力\n")
        f.write(f"  paired t-test: t({len(pre)-1}) = {t_stat:.3f}, p = {p_value:.4f}\n")
        f.write(f"  Cohen's d: {cohens_d:.3f}\n")
        f.write(f"  前測M={pre.mean():.2f}, 後測M={post.mean():.2f}\n\n")
        
        # RQ2
        week6 = survey[survey['week'] == 6]
        week12 = survey[survey['week'] == 12]
        week17 = survey[survey['week'] == 17]
        
        ai_w6 = week6.groupby('student_id')['ai_dependency_score'].mean().values
        ai_w12 = week12.groupby('student_id')['ai_dependency_score'].mean().values
        ai_w17 = week17.groupby('student_id')['ai_dependency_score'].mean().values
        
        stat_ai, p_ai = stats.friedmanchisquare(ai_w6, ai_w12, ai_w17)
        
        f.write("研究問題二：AI依賴與SRL能力轉變\n")
        f.write(f"  AI依賴 Friedman test: χ²(2) = {stat_ai:.3f}, p = {p_ai:.4f}\n")
        f.write(f"  第6週M={ai_w6.mean():.2f}, 第12週M={ai_w12.mean():.2f}, 第17週M={ai_w17.mean():.2f}\n\n")
        
        # RQ3
        ai_logs = add_phase_labels(ai_logs, week_col='week')
        phase_order = ['引導期', '轉換期', '自主期']
        try_ratio = ai_logs.groupby('phase')['tried_before_ai'].apply(
            lambda x: (x == 'yes').sum() / len(x) * 100
        ).reindex(phase_order)
        
        f.write("研究問題三：AI互動行為\n")
        f.write(f"  引導期Try-Before-AI: {try_ratio['引導期']:.1f}%\n")
        f.write(f"  轉換期Try-Before-AI: {try_ratio['轉換期']:.1f}%\n")
        f.write(f"  自主期Try-Before-AI: {try_ratio['自主期']:.1f}%\n")
    
    print(f"\n統計摘要已儲存: {output_path}")

def main():
    """主程式：執行所有分析"""
    print("\n" + "="*60)
    print("開始執行研究計畫資料分析")
    print("="*60)
    
    # 載入資料
    print("\n載入資料檔案...")
    python_scores, survey, ai_logs = load_data()
    print(f"✓ Python測驗: {len(python_scores)} 筆")
    print(f"✓ 問卷資料: {len(survey)} 筆")
    print(f"✓ AI紀錄: {len(ai_logs)} 筆")
    
    # 執行四個研究問題分析
    rq1_python_ability(python_scores)
    rq2_srl_ai_trends(survey)
    rq3_ai_behavior(ai_logs)
    triangulation_heatmap(python_scores, survey, ai_logs)
    
    # 儲存統計摘要
    save_summary(python_scores, survey, ai_logs)
    
    print("\n" + "="*60)
    print("✓ 分析完成！")
    print(f"✓ 4張圖表已儲存至: {OUTPUT_DIR}/")
    print("✓ 統計摘要已儲存至: results/summary_stats.txt")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
