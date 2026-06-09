---
name: open-source-tool-builder
description: Create or upgrade publishable open-source tool projects from scratch, including technical selection, project structure, implementation, tests, README in one or more languages, CI, release automation, installation and uninstall flows, security and platform-permission notes, Git initialization, GitHub remote setup, and first release guidance. Use when Codex is asked to create a CLI, desktop, web, automation, developer, or utility tool intended for public GitHub release; when converting a local script/prototype into an open-source project; or when improving an existing tool repository for real users.
---

# Open Source Tool Builder

## Objective

Build open-source tool projects that are usable by real users, maintainable by developers, and ready for GitHub publication. Optimize for a complete project, not just working code.

Use this skill as the main workflow for new tool repositories or for turning prototypes into polished open-source projects.

## Core Workflow

1. Inspect the current directory and existing files before making changes.
2. Clarify only missing information that blocks safe execution, such as the real GitHub repository URL, package name, target platform, or distribution channel.
3. If the user asks to create a new tool but does not specify the tool's purpose or core functionality, ask for clarification before implementing. You may suggest 2-3 concrete project ideas, but do not choose and create one without user confirmation unless the user explicitly asks you to decide.
4. Choose the smallest suitable technology stack for the target users and platform. Explain the choice briefly, then implement.
5. Create or adapt the project structure.
6. Implement the core functionality with conservative dependencies.
7. Add focused tests for parsing, generation, command construction, configuration, and platform-specific behavior.
8. Add user-facing documentation and developer documentation.
9. Add CI and, when distribution requires artifacts, tag-triggered release automation.
10. Run formatting, tests, and build commands. Fix failures.
11. Initialize Git only when appropriate, then commit, configure remotes, push, and create a version tag when the user has provided or approved the destination repository.
12. Summarize what was delivered, how to install and use it, verification results, and the next release process.

## Technology Selection

Prefer the technology that minimizes user installation friction while fitting the tool domain.

Use these defaults unless the repository context points elsewhere:

- **Single-binary CLI or system utility**: Go or Rust. Prefer Go when standard-library implementation is enough and fast delivery matters.
- **Node ecosystem developer tool**: TypeScript when npm distribution is the natural user path.
- **Python data/automation tool**: Python when users already operate in Python or package scripting matters more than single-binary distribution.
- **Frontend/web app**: Follow the existing frontend stack, or use a minimal Vite/React/TypeScript setup when starting fresh.
- **Desktop app**: Choose the smallest platform-appropriate framework; avoid heavy desktop stacks for a simple CLI need.

Before selecting a stack, weigh: target user runtime burden, distribution model, testing, long-term maintenance, platform APIs, dependency risk, and community expectations for the tool type.

## Documentation Requirements

Create documentation for first-time users, not only for the author.

Use `README.md` as the primary language. Add `README.zh-CN.md` when Chinese users are part of the target audience or the user asks for bilingual docs. Put language-switch links near the top of both files.

README content should include, as applicable:

- What the tool does
- Who it is for
- What problem it solves
- Requirements
- Recommended install path first
- Alternative install paths only when they actually work
- Quick start
- Common commands
- Configuration
- Uninstall or cleanup
- Troubleshooting
- Security, permission, signing, sandbox, path, credential, or privacy notes
- Build from source
- Test and development workflow
- Release process
- License

Do not leave outward-facing placeholders, fake owner or repository names, fake package names, fake taps, or commands that are not yet valid. If a real value is missing, ask the user or move it to a pre-release checklist.

## Release Automation

When the project distributes binaries or packaged artifacts, add a GitHub Actions release workflow triggered by semantic version tags such as `v0.1.0`.

The workflow should usually:

1. Check out the repository.
2. Install the required language/toolchain.
3. Run tests.
4. Build target artifacts.
5. Name artifacts for normal users, not only engineers.
6. Generate checksums when useful.
7. Create a GitHub Release and upload artifacts.

Do not document Homebrew, npm, pip, Docker, winget, or other package-manager install commands as available until they are actually published and tested.

For detailed release patterns, read `references/release-workflow.md`.

## Safety And Platform Fit

Identify platform and security constraints early. Do not bypass security prompts silently.

Common cases:

- macOS downloaded binaries may need a quarantine note or signing/notarization explanation.
- macOS automation, accessibility, launchd, login items, keychain, and app-control permissions need explicit user-facing explanations.
- Tools that operate on repositories should avoid trusting broad folders such as `~/Downloads` by default.
- Credentials should be read from standard secret stores or environment variables; never commit secrets.
- Network access, file writes outside the workspace, destructive commands, and background tasks need clear user consent.

For detailed guidance, read `references/security-and-permissions.md`.

## GitHub Publication

When the user provides a GitHub repository URL:

1. Update module/package/import paths and README links.
2. Initialize Git if needed.
3. Set the default branch, usually `main`.
4. Add a remote named `origin`.
5. Commit the complete project.
6. Push `main`.
7. Create the first version tag only after tests pass and the user wants a release.
8. Push the tag and confirm that the release workflow is expected to run.

If API or SSH checks are blocked by sandboxing or rate limits, report what was verified locally and what the user should inspect in GitHub Actions/Releases.

## Validation Checklist

Before final response, verify:

- Formatting ran.
- Tests ran.
- Build ran when applicable.
- README commands match actual files and release artifacts.
- Public docs contain no fake placeholders.
- `.gitignore` excludes local build outputs and OS junk.
- Release workflow artifact names are understandable.
- Worktree status is clean after commits, unless the user asked not to commit.

Use `references/project-checklist.md` for a fuller checklist when the project is broad.
