# Changelog

Only maintained as of v0.2.0

## [v0.2.0] (unreleased)

### Added

* Added pip support (venv-based installation)
* Added new LSP servers:
    * [`ty`](https://docs.astral.sh/ty/installation)
* Added support for updating

### Changed

* Logging is now based on Loguru rather than print statements
* Internal: sources are now properly type-checked and type-defined rather than being raw, untyped dicts

### Fixed

* Kotlin-lsp quietly changed their download URL. This has been corrected, so it can be downloaded again
* Patterns can now be full URLs rather than just asset patterns
    * This was required for the kotlin-lsp fix, which also split the filenames into OS-specific versions. Thanks, JetBrains


[v0.2.0]: https://github.com/LunarWatcher/lspinstaller/compare/v0.1.0...v0.2.0
