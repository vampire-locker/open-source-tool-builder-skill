# Release Workflow Guidance

Use tag-triggered releases for tools that publish binaries or packaged artifacts.

## Recommended Pattern

```yaml
name: release

on:
  push:
    tags:
      - "v*"

permissions:
  contents: write

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version-file: go.mod
      - run: go test ./...
      - run: |
          mkdir -p dist
          # build commands here
          cd dist
          sha256sum * > checksums.txt
      - uses: softprops/action-gh-release@v2
        with:
          files: dist/*
```

Adapt the toolchain setup and build commands to the chosen stack.

## Artifact Naming

Prefer names users can choose without knowing low-level architecture terms:

- `tool-macos-apple-silicon`
- `tool-macos-intel`
- `tool-linux-x64`
- `tool-windows-x64.exe`

Use engineer terms such as `darwin-arm64` only when the target audience expects them.

## Publishing Flow

1. Ensure `main` is pushed and CI is passing.
2. Create a semantic version tag: `git tag v0.1.0`.
3. Push the tag: `git push origin v0.1.0`.
4. Watch GitHub Actions.
5. Verify the GitHub Release contains expected assets.
6. Update README if install instructions do not match the actual release.

Do not create a new tag until tests and build pass locally unless the user explicitly accepts the risk.
