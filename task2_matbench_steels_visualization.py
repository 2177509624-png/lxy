"""
Task 2: Matbench Steels Dataset Visualization
使用Python包加载matbench_steels数据集，并进行数据可视化
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matbench.bench import MatbenchBenchmark
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def load_matbench_steels():
    """加载matbench_steels数据集"""
    mb = MatbenchBenchmark(autoload=False)
    task = mb.tasks['matbench_steels']
    task.load()
    
    return task

def visualize_steels_data(task):
    """可视化钢铁数据"""
    
    # 获取训练集数据
    train_df = task.train.copy()
    
    print(f"数据集大小: {len(train_df)}")
    print(f"特征列: {train_df.columns.tolist()}")
    print(f"\n数据概览:\n{train_df.head()}")
    print(f"\n数据统计:\n{train_df.describe()}")
    
    # 创建可视化
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Matbench Steels Dataset Visualization', fontsize=16)
    
    # 1. 目标变量分布
    if 'Yield strength (MPa)' in train_df.columns:
        target_col = 'Yield strength (MPa)'
    else:
        target_col = train_df.columns[-1]
    
    axes[0, 0].hist(train_df[target_col], bins=30, color='skyblue', edgecolor='black')
    axes[0, 0].set_title(f'Distribution of {target_col}')
    axes[0, 0].set_xlabel('Value')
    axes[0, 0].set_ylabel('Frequency')
    
    # 2. 数值特征分布
    numeric_cols = train_df.select_dtypes(include=[np.number]).columns
    if len(numeric_cols) > 1:
        for i, col in enumerate(numeric_cols[1:min(5, len(numeric_cols))]):
            if i < 3:
                axes[0, 1].hist(train_df[col], bins=20, alpha=0.6, label=col)
        axes[0, 1].set_title('Numeric Features Distribution')
        axes[0, 1].legend()
        axes[0, 1].set_xlabel('Value')
        axes[0, 1].set_ylabel('Frequency')
    
    # 3. 缺失值统计
    missing_data = train_df.isnull().sum()
    if missing_data.sum() > 0:
        missing_data[missing_data > 0].plot(kind='barh', ax=axes[1, 0], color='coral')
        axes[1, 0].set_title('Missing Values')
        axes[1, 0].set_xlabel('Count')
    else:
        axes[1, 0].text(0.5, 0.5, 'No Missing Values', 
                       horizontalalignment='center', verticalalignment='center',
                       transform=axes[1, 0].transAxes, fontsize=12)
        axes[1, 0].set_title('Missing Values')
    
    # 4. 相关性热力图
    if len(numeric_cols) > 1:
        corr_matrix = train_df[numeric_cols].corr()
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                   ax=axes[1, 1], cbar_kws={'label': 'Correlation'})
        axes[1, 1].set_title('Feature Correlation Heatmap')
    
    plt.tight_layout()
    plt.savefig('matbench_steels_visualization.png', dpi=300, bbox_inches='tight')
    print("\n可视化已保存为 matbench_steels_visualization.png")
    plt.show()
    
    return train_df

def main():
    """主函数"""
    print("=" * 50)
    print("Task 2: Matbench Steels Visualization")
    print("=" * 50)
    
    try:
        # 加载数据
        task = load_matbench_steels()
        
        # 可视化
        visualize_steels_data(task)
        
        print("\n✓ Task 2 完成！")
        
    except Exception as e:
        print(f"错误: {e}")
        print("\n如果是导入错误，请运行: pip install matbench pymatgen")

if __name__ == "__main__":
    main()
