# open-source-tool-builder skill

语言：简体中文 | [English](README.en.md)

这个仓库包含一个 Codex Skill，用于从零创建可发布的开源工具项目、把本地原型整理成适合发布到 GitHub 的开源仓库，或检查并改进现有开源工具项目的发布就绪度。

## 它能帮助什么

- 根据目标用户和平台进行技术选型
- 设计项目结构和实现流程
- 添加测试、格式化、构建命令和 CI
- 编写对用户友好的 README，默认以简体中文为主，需要时补充英文版
- 配置 GitHub Release 自动发布
- 编写安装、卸载和故障排查说明
- 补充平台安全、权限和系统限制说明
- 检查现有开源工具仓库的文档、发布、测试和维护完整性

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
安装这个 skill：git@github.com:vampire-locker/open-source-tool-builder-skill.git
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
使用 $open-source-tool-builder 创建一个新的开源 CLI 工具项目。
```

也可以用于检查现有项目：

```text
使用 $open-source-tool-builder 检查这个开源工具仓库的发布就绪度，并指出需要补齐的内容。
```

## 开发

使用本仓库校验脚本检查 skill 结构：

```bash
python3 scripts/validate_skill.py
```

也可以使用 Skill Creator validator：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py open-source-tool-builder
```

具体的 `.system` 路径可能会因你的 Codex 安装方式而不同。

## 许可证

MIT
