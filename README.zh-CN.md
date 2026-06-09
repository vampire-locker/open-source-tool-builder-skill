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

## 安装

### 使用 Codex 安装

让 Codex 从 GitHub 安装这个 skill：

```text
Use $skill-installer to install the skill at path `open-source-tool-builder` from git@github.com:vampire-locker/open-source-tool-builder-skill.git
```

安装完成后，重启 Codex，让新 skill 被发现。

### 手动安装

克隆仓库，并把 skill 文件夹复制到你的 Codex skills 目录：

```bash
git clone git@github.com:vampire-locker/open-source-tool-builder-skill.git
cd open-source-tool-builder-skill
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
