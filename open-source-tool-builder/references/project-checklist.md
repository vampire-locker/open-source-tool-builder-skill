# Project Checklist

Use this checklist for open-source tool repositories.

## Discovery

- Inspect current files before editing.
- Identify whether this is a new project, prototype cleanup, or existing repo upgrade.
- Identify target users, target platforms, distribution channel, and non-goals.
- Ask for real repository/package names when public docs or package metadata need them.

## Repository Contents

- Core implementation lives in a conventional structure for the selected stack.
- Tests cover core behavior and platform-sensitive command generation.
- `README.md` is accurate for real users.
- `README.zh-CN.md` exists when bilingual docs are required.
- Language-switch links work.
- `LICENSE` exists, default MIT unless the user chooses otherwise.
- `.gitignore` excludes build artifacts, dependency caches, OS files, and local secrets.
- Makefile or equivalent task runner provides common commands.
- CI runs tests on push and pull request.
- Release workflow exists when users need downloadable artifacts.

## Documentation Quality

- Recommended installation path appears first.
- Source build instructions are separate from ordinary user install steps.
- Package-manager commands are shown only if the package is actually published.
- Artifact names map to user language such as `macos-apple-silicon`, not only `darwin-arm64`, when ordinary users download them.
- Security prompts and platform permissions are explained where users encounter them.
- No author-local paths or template placeholders remain.

## Final Verification

- Run formatter.
- Run tests.
- Run build.
- Run CLI help or smoke test when possible.
- Review generated release artifacts locally when possible.
- Confirm Git status before final response.
