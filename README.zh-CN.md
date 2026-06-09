# open-source-tool-builder skill

语言：[English](README.md) | 简体中文

这个仓库包含一个 Codex Skill，用于从零创建可发布的开源工具项目，或把本地原型整理成适合发布到 GitHub 的开源仓库。

## 它能帮助什么

- 根据目标用户和平台进行技术选型
- 设计项目结构和实现流程
- 添加测试、格式化、构建命令和 CI
- 编写对用户友好的 README，包括需要时的中英文文档
- 配置 GitHub Release 自动发布
- 编写安装、卸载和故障排查说明
- 补充平台安全、权限和系统限制说明

## Skill 位置

```text
open-source-tool-builder/
  SKILL.md
  agents/openai.yaml
  references/
```

## 本地安装

把 skill 文件夹复制或软链接到你的 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R open-source-tool-builder ~/.codex/skills/
```

然后开启一个新的 Codex 会话，像这样使用：

```text
Use $open-source-tool-builder to create a new open-source CLI tool project.
```

## 开发

使用 Skill Creator validator 校验 skill 结构：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py open-source-tool-builder
```

具体的 `.system` 路径可能会因你的 Codex 安装方式而不同。

## 许可证

MIT
