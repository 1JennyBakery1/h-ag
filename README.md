# Hello Agents - 智能体教程（离线版）

> 本项目是从 [DataWhale Hello Agents](https://datawhalechina.github.io/hello-agents/) 教程网站爬取的离线版本，保留完整的页面样式和交互体验。

## 简介

Hello Agents 是由 DataWhale 开源的智能体（Agent）入门教程，涵盖从基础概念到实战项目的完整学习路径。本仓库提供该教程的离线版本，无需联网即可在本地浏览器中阅读。

## 使用方式

直接用浏览器打开首页即可开始阅读：

```
datawhalechina/hello-agents/zh/index.html
```

> **注意**：请保持 `_next/` 目录与 `datawhalechina/` 目录的相对位置不变，否则页面资源无法正确加载。

## 章节目录

### 基础篇

| 序号 | 章节 | 文件 |
|:----:|------|------|
| 1 | 概览 | [1-overview.html](datawhalechina/hello-agents/zh/1-overview.html) |
| 2 | 快速开始 | [2-quick-start.html](datawhalechina/hello-agents/zh/2-quick-start.html) |
| 3 | 最新更新 | [3-latest-updates.html](datawhalechina/hello-agents/zh/3-latest-updates.html) |
| 4 | 问题与反馈 | [4-issues-and-feedbacks.html](datawhalechina/hello-agents/zh/4-issues-and-feedbacks.html) |
| 5 | 关于贡献者 | [5-about-contributors.html](datawhalechina/hello-agents/zh/5-about-contributors.html) |

### 入门篇

| 序号 | 章节 | 文件 |
|:----:|------|------|
| 6 | 架构概览 | [6-architecture-overview.html](datawhalechina/hello-agents/zh/6-architecture-overview.html) |
| 7 | Agent 概念与发展史 | [7-agent-concepts-and-history.html](datawhalechina/hello-agents/zh/7-agent-concepts-and-history.html) |
| 8 | LLM 基础回顾 | [8-llm-fundamentals-refresher.html](datawhalechina/hello-agents/zh/8-llm-fundamentals-refresher.html) |
| 9 | ReAct 模式实现 | [9-react-pattern-implementation.html](datawhalechina/hello-agents/zh/9-react-pattern-implementation.html) |
| 10 | 规划、求解与反思 | [10-plan-and-solve-and-reflection.html](datawhalechina/hello-agents/zh/10-plan-and-solve-and-reflection.html) |

### 进阶篇

| 序号 | 章节 | 文件 |
|:----:|------|------|
| 11 | 低代码平台 (Coze/Dify/n8n) | [11-low-code-platforms-coze-dify-n8n.html](datawhalechina/hello-agents/zh/11-low-code-platforms-coze-dify-n8n.html) |
| 12 | 主流框架 (AutoGen/LangGraph) | [12-mainstream-frameworks-autogen-langgraph.html](datawhalechina/hello-agents/zh/12-mainstream-frameworks-autogen-langgraph.html) |
| 13 | 框架核心架构 | [13-framework-core-architecture.html](datawhalechina/hello-agents/zh/13-framework-core-architecture.html) |
| 14 | SimpleAgent 与工具注册 | [14-simpleagent-and-tool-registry.html](datawhalechina/hello-agents/zh/14-simpleagent-and-tool-registry.html) |
| 15 | ReActAgent 自定义实现 | [15-reactagent-custom-implementation.html](datawhalechina/hello-agents/zh/15-reactagent-custom-implementation.html) |

### 高级篇

| 序号 | 章节 | 文件 |
|:----:|------|------|
| 16 | 记忆系统（工作/情景/语义） | [16-memory-system-working-episodic-semantic.html](datawhalechina/hello-agents/zh/16-memory-system-working-episodic-semantic.html) |
| 17 | RAG 流水线与检索 | [17-rag-pipeline-and-retrieval.html](datawhalechina/hello-agents/zh/17-rag-pipeline-and-retrieval.html) |
| 18 | 上下文工程与 ContextBuilder | [18-context-engineering-with-contextbuilder.html](datawhalechina/hello-agents/zh/18-context-engineering-with-contextbuilder.html) |
| 19 | Agent 协议 (MCP/A2A/ANP) | [19-agent-protocols-mcp-a2a-anp.html](datawhalechina/hello-agents/zh/19-agent-protocols-mcp-a2a-anp.html) |
| 20 | Agentic RL 训练流水线 (SFT→GRPO) | [20-agentic-rl-sft-to-grpo-pipeline.html](datawhalechina/hello-agents/zh/20-agentic-rl-sft-to-grpo-pipeline.html) |
| 21 | Agent 性能评估 | [21-agent-performance-evaluation.html](datawhalechina/hello-agents/zh/21-agent-performance-evaluation.html) |

### 实战篇

| 序号 | 章节 | 文件 |
|:----:|------|------|
| 22 | 智慧旅行助手 | [22-intelligent-travel-assistant.html](datawhalechina/hello-agents/zh/22-intelligent-travel-assistant.html) |
| 23 | DeepResearch Agent | [23-deepresearch-agent.html](datawhalechina/hello-agents/zh/23-deepresearch-agent.html) |
| 24 | 赛博小镇模拟 | [24-cyber-town-simulation.html](datawhalechina/hello-agents/zh/24-cyber-town-simulation.html) |

## 目录结构

```
h-ag/
├── _next/                              # Next.js 静态资源 (JS/CSS/字体)
│   ├── static/chunks/                  # JavaScript 模块
│   ├── static/css/                     # 样式表
│   └── static/media/                   # 字体文件
├── datawhalechina/hello-agents/zh/     # 教程页面（中文）
│   ├── index.html                      # 首页/导航页
│   ├── 1-overview.html ~ 24-*.html     # 各章节内容页
│   ├── icon.png                        # 网站图标
│   └── apple-icon.png                  # Apple 设备图标
├── .gitignore                          # Git 忽略规则
└── README.md                           # 本说明文件
```

## 来源

- **原站地址**: https://datawhalechina.github.io/hello-agents/
- **开源组织**: [DataWhale China](https://github.com/datawhalechina)

## 许可

本项目内容遵循 DataWhale Hello Agents 原项目的开源协议。
