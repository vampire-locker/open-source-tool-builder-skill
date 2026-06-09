# Security And Permissions Guidance

Use this reference when a tool touches system features, background tasks, network, credentials, or local files.

## Principles

- Prefer least privilege.
- Ask before destructive or broad actions.
- Do not silently bypass OS security mechanisms.
- Explain prompts users will see before or near the command that triggers them.
- Avoid broad default working directories such as `~/Downloads`, `~/Desktop`, or home root.
- Keep secrets out of files, logs, release artifacts, and README examples.

## macOS Examples

- Downloaded unsigned binaries may trigger Gatekeeper. Document quarantine handling or signing/notarization status.
- `launchd` is appropriate for user-level scheduled jobs. Provide install, status, and uninstall commands.
- AppleScript/JXA control of apps can trigger Automation permission prompts. Prefer non-automation alternatives when possible.
- Accessibility, Screen Recording, Keychain, Login Items, and network permissions need explicit user-facing notes.

## Repository Trust

If a downstream tool asks users to trust a directory, do not auto-trust it. Tell users to choose a narrow, intentional project/work directory and trust it once if appropriate.

## Release Integrity

Generate checksums for downloadable binaries when practical. Explain optional verification only if it is useful for the target audience.
