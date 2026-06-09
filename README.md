# open-source-tool-builder skill

Language: English | [简体中文](README.zh-CN.md)

This repository contains a Codex Skill for creating publishable open-source tool projects from scratch or upgrading local prototypes into GitHub-ready repositories.

## What It Helps With

- Technology selection for the target users and platform
- Project structure and implementation workflow
- Tests, formatting, build commands, and CI
- User-friendly README files, including bilingual docs when needed
- GitHub Release automation
- Installation, uninstall, and troubleshooting docs
- Platform security and permission notes

## Skill Location

```text
open-source-tool-builder/
  SKILL.md
  agents/openai.yaml
  references/
```

## Install

### Install With Codex

Ask Codex to install this skill from GitHub:

```text
Use $skill-installer to install the skill at path `open-source-tool-builder` from git@github.com:vampire-locker/open-source-tool-builder-skill.git
```

Restart Codex after installation so the new skill is discovered.

### Install Manually

Clone the repository and copy the skill folder into your Codex skills directory:

```bash
git clone git@github.com:vampire-locker/open-source-tool-builder-skill.git
cd open-source-tool-builder-skill
mkdir -p ~/.codex/skills
cp -R open-source-tool-builder ~/.codex/skills/
```

Then start a new Codex session and ask for tasks such as:

```text
Use $open-source-tool-builder to create a new open-source CLI tool project.
```

## Development

Validate the skill structure with the Skill Creator validator:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py open-source-tool-builder
```

The exact `.system` path may differ depending on your Codex installation.

## License

MIT
