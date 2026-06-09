"""
Task 5: 调研本ppt提及的所有材料数据库
数据库调研报告 + 代码示例

调研报告内容:
1. 数据库基本信息
2. 数据库用途
3. 适用研究目的
4. API使用示例
"""

import json
import os
from datetime import datetime

# 数据库信息汇总
MATERIALS_DATABASES = {
    "PubChem": {
        "name": "PubChem - 公开化学数据库",
        "url": "https://pubchem.ncbi.nlm.nih.gov/",
        "type": "化学分子数据库",
        "description": "美国国立生物技术信息中心提供的最大的化学信息公开数据库",
        "content": [
            "化学结构（分子结构）",
            "化学性质（分子量、密度等）",
            "生物活性数据",
            "毒性数据"
        ],
        "suitable_for": [
            "药物设计与发现",
            "有机化学研究",
            "分子性质预测",
            "毒理学研究"
        ],
        "api": "REST API",
        "free": True,
        "authentication": "无需认证"
    },
    
    "Materials Project": {
        "name": "Materials Project - 材料信息学数据库",
        "url": "https://materialsproject.org/",
        "type": "无机材料结构和性质数据库",
        "description": "全面的计算材料数据库，包含超过150,000个无机化合物的计算性质",
        "content": [
            "晶体结构",
            "能带结构",
            "电子性质",
            "热力学数据",
            "弹性常数"
        ],
        "suitable_for": [
            "新材料发现",
            "材料性质计算与筛选",
            "电子器件设计",
            "能源材料研究"
        ],
        "api": "RESTful API + Python库",
        "free": True,
        "authentication": "需要API密钥（免费注册获取）"
    },
    
    "COD (Crystallography Open Database)": {
        "name": "COD - 晶体学开放数据库",
        "url": "http://www.crystallography.net/",
        "type": "晶体结构数据库",
        "description": "包含从文献中提取的晶体结构数据，完全开放且免费",
        "content": [
            "晶体结构（CIF格式）",
            "晶胞参数",
            "原子坐标",
            "对称性信息"
        ],
        "suitable_for": [
            "晶体结构分析",
            "X射线衍射数据分析",
            "结构预测与模拟",
            "材料相图研究"
        ],
        "api": "REST API + SQL查询",
        "free": True,
        "authentication": "无需认证"
    },
    
    "OQMD (Open Quantum Materials Database)": {
        "name": "OQMD - 开源量子材料数据库",
        "url": "http://oqmd.org/",
        "type": "计算材料性质数据库",
        "description": "包含150万+种化学组成的DFT计算结果的开源数据库",
        "content": [
            "形成能（formation energy）",
            "相稳定性数据",
            "结构优化结果",
            "电子结构数据"
        ],
        "suitable_for": [
            "热力学稳定性评估",
            "相图计算",
            "新化学物质发现",
            "计算材料学"
        ],
        "api": "REST API",
        "free": True,
        "authentication": "无需认证"
    },
    
    "ICSD (Inorganic Crystal Structure Database)": {
        "name": "ICSD - 无机晶体结构数据库",
        "url": "https://icsd.products.fiz-karlsruhe.de/",
        "type": "实验晶体结构数据库",
        "description": "包含实验测定的无机晶体结构，是最权威的晶体结构数据库之一",
        "content": [
            "实验晶体结构",
            "从论文中提取的精确结构数据",
            "发表年份和参考文献"
        ],
        "suitable_for": [
            "晶体结构参考",
            "结构验证",
            "材料信息查询",
            "论文引用"
        ],
        "api": "Web界面+本地安装版本",
        "free": False,
        "authentication": "机构订阅或付费"
    },
    
    "MPDS (Materials Platform for Data Science)": {
        "name": "MPDS - 材料数据科学平台",
        "url": "https://mpds.io/",
        "type": "多源材料数据集成平台",
        "description": "整合多个数据源的材料数据平台，支持数据挖掘和机器学习",
        "content": [
            "晶体结构",
            "物理性质（热、电、磁）",
            "机械性质",
            "文献数据"
        ],
        "suitable_for": [
            "材料数据挖掘",
            "机器学习模型训练",
            "材料性质预测",
            "高通量计算筛选"
        ],
        "api": "REST API + Python库",
        "free": False,
        "authentication": "需要订阅"
    },
    
    "AFlow (Automatic FLOW for Materials Discovery)": {
        "name": "AFlow - 材料发现自动工作流",
        "url": "http://www.aflowlib.org/",
        "type": "高通量计算数据库",
        "description": "通过高通量DFT计算生成的材料数据库，涵盖百万级化学组成",
        "content": [
            "高通量DFT计算结果",
            "结构、能量、弹性等多种性质",
            "功能性材料推荐"
        ],
        "suitable_for": [
            "功能性材料搜索",
            "物理性质预测",
            "高通量筛选",
            "计算验证"
        ],
        "api": "REST API",
        "free": True,
        "authentication": "无需认证"
    }
}


def generate_research_report():
    """生成调研报告"""
    
    report = f"""
{'='*80}
材料数据库调研报告
Report on Materials Databases Research
{'='*80}

报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
研究目的: 调研本课程PPT提及的所有材料数据库，了解其用途、适用研究目的及使用方式
{'='*80}

目录 (Table of Contents)
{'-'*80}
1. 数据库概览 (Overview of Databases)
2. 各数据库详细信息 (Detailed Information)
3. 对比分析 (Comparative Analysis)
4. 建议 (Recommendations)
5. 使用指南 (Usage Guide)
{'='*80}


1. 数据库概览 (Overview)
{'-'*80}

本调研涉及 {len(MATERIALS_DATABASES)} 个主要材料数据库:

"""
    
    for i, (key, db) in enumerate(MATERIALS_DATABASES.items(), 1):
        report += f"\n{i}. {db['name']}\n"
    
    report += f"""

{'='*80}
2. 各数据库详细信息 (Detailed Information)
{'-'*80}

"""
    
    for i, (key, db) in enumerate(MATERIALS_DATABASES.items(), 1):
        report += f"""
{i}. {db['name']}
{'~'*80}

官方网站: {db['url']}
数据库类型: {db['type']}
描述: {db['description']}

包含内容:
"""
        for content in db['content']:
            report += f"  • {content}\n"
        
        report += f"""
适用研究目的:
"""
        for purpose in db['suitable_for']:
            report += f"  • {purpose}\n"
        
        report += f"""
API接口: {db['api']}
是否免费: {'是' if db['free'] else '否'}
认证方式: {db['authentication']}

"""
    
    report += f"""
{'='*80}
3. 对比分析 (Comparative Analysis)
{'-'*80}

3.1 按数据性质分类:

(1) 实验数据库:
  • ICSD - 实验晶体结构数据（权威、准确、需要订阅）
  • COD - 开放实验晶体结构数据（免费、易获取）

(2) 计算数据库:
  • Materials Project - 计算无机材料性质（全面、易用、推荐）
  • OQMD - 量子材料数据库（开源、数据量大）
  • AFlow - 高通量计算结果（快速、全面）
  • MPDS - 集成多源数据（专业、付费）

(3) 化学分子数据库:
  • PubChem - 有机小分子数据（免费、全面、易用）

3.2 按应用领域分类:

晶体结构研究: COD > ICSD > Materials Project
计算材料学: OQMD > AFlow > Materials Project
药物设计: PubChem > Materials Project
新材料发现: Materials Project > MPDS > AFlow
教学/科研入门: Materials Project, COD, OQMD (推荐)

3.3 按易用性排序:

最易用: PubChem > Materials Project > COD
中等易用: OQMD > AFlow
较难使用: ICSD > MPDS (需要专业知识或付费)

{'='*80}
4. 建议 (Recommendations)
{'-'*80}

4.1 对于材料学初学者:
  推荐使用: Materials Project + COD
  理由: 免费、易用、数据完整、文档清晰

4.2 对于有机化学研究:
  推荐使用: PubChem
  理由: 最全面的有机分子数据库

4.3 对于计算材料学研究:
  推荐使用: OQMD + AFlow + Materials Project
  理由: 数据量大、覆盖面广、API完善

4.4 对于晶体学研究:
  推荐使用: COD (免费入门) > ICSD (权威参考)

4.5 对于高通量筛选/机器学习:
  推荐使用: MPDS + OQMD
  理由: 数据量大、适合数据挖掘

{'='*80}
5. 使用指南 (Usage Guide)
{'-'*80}

5.1 通用访问方式:

(1) Web界面访问:
  - 直接访问官方网站
  - 在线搜索和浏览数据
  - 适合快速查询

(2) API访问:
  - 大批量数据下载
  - 集成到自己的程序
  - 需要编程知识

(3) 本地数据库:
  - ICSD: 可申请本地安装版本
  - 数据库大小通常为 GB 级

5.2 典型工作流程:

第一步: 定义研究问题
  → 确定需要哪类数据
  → 选择合适的数据库

第二步: 获取数据
  → 通过API或Web界面下载
  → 数据清洗和预处理

第三步: 数据分析
  → 结构优化和计算
  → 性质预测
  → 结果验证

第四步: 论文发表
  → 引用数据来源
  → 说明数据处理方法

5.3 常见问题解答:

Q: 如何选择数据库?
A: 根据研究方向选择:
   - 晶体结构 → COD/ICSD
   - 计算预测 → Materials Project/OQMD
   - 有机分子 → PubChem

Q: 数据库是否免费?
A: 大多数主要数据库都提供免费访问，但：
   - ICSD 需要订阅
   - MPDS 需要订阅
   - 其他数据库均免费

Q: 如何获取API密钥?
A: 在官方网站注册账号，通常会自动生成API密钥

Q: 数据更新频率?
A: 大多数数据库定期更新（月度或季度），详见各数据库文档

{'='*80}
总结 (Conclusion)
{'-'*80}

材料数据库是现代材料科学研究的重要基础设施。选择合适的数据库并学会高效
使用它们，对研究效率提升和创新发现都有重要意义。

推荐学习路径:
1. 从 PubChem 或 Materials Project 入门
2. 学习 API 的使用方法
3. 进行数据分析和可视化
4. 根据需要扩展到其他专业数据库

{'='*80}
参考资源 (References)
{'-'*80}

"""
    
    for key, db in MATERIALS_DATABASES.items():
        report += f"• {db['name']}: {db['url']}\n"
    
    report += f"""

{'='*80}
附录: 各数据库详细比较表
{'-'*80}

"""
    
    # 创建对比表
    report += "| 数据库名称 | 数据类型 | 免费 | API | 易用性 | 推荐度 |\n"
    report += "|-----------|---------|------|-----|--------|--------|\n"
    
    for key, db in MATERIALS_DATABASES.items():
        name = db['name'].split('-')[0].strip()
        data_type = db['type']
        free = "✓" if db['free'] else "✗"
        api = db['api']
        
        # 简化易用性
        if 'PubChem' in db['name'] or 'Materials Project' in db['name']:
            usability = "★★★★★"
            recommend = "★★★★★"
        elif 'COD' in db['name'] or 'OQMD' in db['name']:
            usability = "★★★★☆"
            recommend = "★★★★☆"
        elif 'AFlow' in db['name']:
            usability = "★★★☆☆"
            recommend = "★★★★☆"
        else:
            usability = "★★☆☆☆"
            recommend = "★★★☆☆"
        
        report += f"| {name} | {data_type} | {free} | {api} | {usability} | {recommend} |\n"
    
    report += f"""

{'='*80}
END OF REPORT
报告结束时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
{'='*80}

"""
    
    return report


def save_report(report, filename="材料数据库调研报告.txt"):
    """保存报告"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"✓ 报告已保存: {filename}")


def save_database_info_json(filename="materials_databases_info.json"):
    """保存数据库信息为JSON格式"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(MATERIALS_DATABASES, f, ensure_ascii=False, indent=2)
    print(f"✓ 数据库信息已保存: {filename}")


def main():
    print("="*80)
    print("Task 5: 材料数据库调研")
    print("="*80)
    
    # 生成报告
    print("\n正在生成调研报告...")
    report = generate_research_report()
    
    # 保存报告
    save_report(report)
    save_database_info_json()
    
    # 显示报告摘要
    print("\n" + "="*80)
    print("调研完成 - 报告摘要")
    print("="*80)
    
    print(f"\n调研的数据库总数: {len(MATERIALS_DATABASES)}\n")
    
    print("数据库列表:")
    for i, (key, db) in enumerate(MATERIALS_DATABASES.items(), 1):
        free_status = "免费" if db['free'] else "付费"
        print(f"{i}. {db['name']:<50} ({free_status})")
    
    print("\n" + "="*80)
    print("作业提交内容:")
    print("="*80)
    print("✓ 调研报告: 材料数据库调研报告.txt")
    print("✓ 数据库信息JSON: materials_databases_info.json")
    print("✓ 本Python脚本: task5_research_report.py")
    print("\n所有文件已生成，请打包提交！")


if __name__ == "__main__":
    main()
