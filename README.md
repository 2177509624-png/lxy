# 📁 Python 项目完整代码集合

## ✅ 已完成的所有文件列表

本仓库包含以下Python项目：

### 📚 材料科学作业 (5个任务)

#### Task 1: PubChem API 分子数据下载
- **文件**: `task1_pubchem_downloader.py`
- **功能**: 
  - 批量下载分子数据（阿司匹林、咖啡因、葡萄糖等）
  - 支持多种搜索方式（名称、SMILES、InChI）
  - 提取关键分子性质（分子量、密度、LogP等）
  - 保存为JSON和CSV格式

#### Task 2: Matbench 钢铁数据集可视化
- **文件**: `task2_matbench_steels_visualization.py`
- **功能**:
  - 加载matbench_steels数据集
  - 目标变量分布直方图
  - 数值特征分布对比
  - 缺失值统计
  - 相关性热力图
  - 生成高分辨率可视化图片

#### Task 3: COD数据库查询下载
- **文件**: `task3_cod_database_downloader.py`
- **功能**:
  - **方式1**: REST API查询（Si、O元素结构）
  - **方式2**: MySQL SQL查询（包含3个查询条件）
  - 下载CIF晶体结构文件（最多100个）
  - 保存元数据JSON

**SQL查询示例**:
```sql
SELECT cod_id, formula, year, authors, title 
FROM cod_structures
WHERE (formula LIKE '%Si%' OR formula LIKE '%O%')
AND year >= 2010
AND formula_mass > 0
ORDER BY year DESC
LIMIT 100;
```

#### Task 4: 材料数据下载
- **文件**: `task4_materials_data_downloader.py`
- **功能**:
  - **方法1**: Materials Project API（需要API密钥）
  - **方法2**: OQMD API（开源，无需认证）
  - 查询Si-O系统材料
  - 提取能带间隙、密度、晶体学信息
  - 保存为JSON和CSV

#### Task 5: 材料数据库调研报告
- **文件**: `task5_research_report.py`
- **功能**:
  - 调研7个主要材料数据库
  - 生成详细调研报告
  - 数据库对比分析
  - 应用领域推荐
  - 生成使用指南

**调研的数据库**:
1. PubChem - 化学分子数据库
2. Materials Project - 材料计算数据库
3. COD - 晶体学开放数据库
4. OQMD - 量子材料数据库
5. ICSD - 无机晶体结构数据库
6. MPDS - 材料数据科学平台
7. AFlow - 材料发现自动工作流

---

### 🎭 额外项目

#### Random Joke Generator - 随机笑话生成器
- **文件**: `random_joke_generator.py`
- **功能**:
  - 集成3个外部API
  - 获取随机笑话
  - 笑话历史管理
  - 统计分析
  - 保存到JSON文件

**集成的API**:
1. Official Joke API - 英文笑话（开始&结尾形式）
2. Dad Jokes API (icanhazdadjoke.com) - 爸爸笑话
3. Chuck Norris Jokes API - 查克·诺里斯笑话

**使用方式**:
```bash
# Demo 模式
python random_joke_generator.py demo

# 交互模式
python random_joke_generator.py
```

**交互菜单选项**:
1. 获取随机笑话（任意来源）
2. 从特定来源获取笑话
3. 获取多个笑话
4. 查看历史
5. 查看统计
6. 保存到文件
7. 退出

---

## 📋 快速开始

### 安装依赖
```bash
pip install requests pandas matplotlib seaborn numpy
pip install matbench pymatgen  # 用于Task 2
pip install pymysql           # 用于Task 3 (可选)
```

### 运行示例

**Task 1 - PubChem下载**:
```bash
python task1_pubchem_downloader.py
```
输出: `pubchem_molecules.json`, `pubchem_molecules.csv`

**Task 2 - 数据可视化**:
```bash
python task2_matbench_steels_visualization.py
```
输出: `matbench_steels_visualization.png`

**Task 3 - COD查询**:
```bash
python task3_cod_database_downloader.py
```
输出: `cod_data/` 目录, `cod_data/metadata.json`

**Task 4 - 材料数据**:
```bash
python task4_materials_data_downloader.py
```
输出: `materials_data/`, `oqmd_data/` 目录

**Task 5 - 调研报告**:
```bash
python task5_research_report.py
```
输出: `材料数据库调研报告.txt`, `materials_databases_info.json`

**笑话生成器 - Demo模式**:
```bash
python random_joke_generator.py demo
```

**笑话生成器 - 交互模式**:
```bash
python random_joke_generator.py
```

---

## 📊 文件统计

| 文件名 | 行数 | 功能 | 状态 |
|--------|------|------|------|
| task1_pubchem_downloader.py | ~140 | PubChem API下载 | ✅ |
| task2_matbench_steels_visualization.py | ~107 | 数据可视化 | ✅ |
| task3_cod_database_downloader.py | ~250 | COD查询&下载 | ✅ |
| task4_materials_data_downloader.py | ~250 | Materials Project/OQMD | ✅ |
| task5_research_report.py | ~475 | 数据库调研 | ✅ |
| random_joke_generator.py | ~350 | 笑话生成器 | ✅ |

---

## 🔗 外部API文档

- **PubChem**: https://pubchem.ncbi.nlm.nih.gov/docs/pug-rest
- **Materials Project**: https://materialsproject.org/docs/
- **COD**: http://www.crystallography.net/cod/
- **OQMD**: http://oqmd.org/
- **Official Joke API**: https://official-joke-api.appspot.com/
- **Dad Jokes**: https://icanhazdadjoke.com/
- **Chuck Norris**: https://api.chucknorris.io/

---

## 📝 作业提交清单

对于材料科学作业，请准备以下内容：

```
学号_班级.zip
├── task1_pubchem_downloader.py
├── task2_matbench_steels_visualization.py
├── task3_cod_database_downloader.py
├── task4_materials_data_downloader.py
├── task5_research_report.py
├── 生成的数据文件 (JSON, CSV, CIF等)
├── 生成的报告文件 (TXT)
└── README.md (本文件)
```

**提交邮箱**: ghaiyan@ustb.edu.cn

---

## 💡 使用提示

1. **API密钥**: Materials Project需要申请API密钥（免费注册）
2. **网络连接**: 所有脚本需要网络连接才能调用外部API
3. **超时设置**: 部分API响应可能较慢，请耐心等待
4. **错误处理**: 所有脚本都包含错误处理，失败时会输出提示

---

## ✨ 特色功能

✅ 完整的错误处理  
✅ 详细的代码注释  
✅ 友好的用户界面  
✅ 数据持久化  
✅ 统计分析  
✅ 可视化输出  

---

**创建时间**: 2026-06-09  
**所有代码已测试** ✓
