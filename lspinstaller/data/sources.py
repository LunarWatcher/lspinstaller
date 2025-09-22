from dataclasses import dataclass
from enum import Enum

"""
# Syntax
## Root
```
"package name": { data object }
```

The package name is also used for folders in some cases, so make sure the
package name is plain text!

## Data objects

Data objects can have the following main keys:

* github
* npm
* binary
    * The binary spec describes a binary file. Its exact meaning depends on the
      main provider
    * Must be included when using any of  these providers: "github".

### `github`

The github object contains the following keys:
* `fragment`: must be in the format `user/repo`

In addition, the separate `binary` object must be specified.

### `npm`

The npm object contains the following keys:
* `package`: the package name as it's used on npm

### `binary`

The binary object contains the following keys:
* `pattern`: required when using `github` or another provider that finds
  multiple files. Otherwise optional. Mutually exclusive with `url`
* `url`: required when the object is used with a source that's only used for
  the version. See kotlin-lsp for an example. Mutually exclusive with `pattern`
* `link`: describes which files to symlink to the special bin directory.
  Syntax: `"file name in lsp/bin": "filename relative to download root"`
* `archive`: the archive type. Required. Accepted values: "zip".
* `is_nested`: whether or not the archive is nested. Required if `archive` is
  set

The binary object is special, and will never be executed standalone. It exists
to consume data from other providers to actually do the install.

## Special values

In some strings, there are special values. These are in the format `${key}`,
and the currently recognised values are:

* `os`: One of the literals `windows` or `linux`
* `version`: the version as determined by a provider. Note that for versions
  including the `v` prefix, the `v` is stripped and must be included literally
  in the resulting string.

"""
sources = {
    "clangd": {
        "github": {
            "fragment": "clangd/clangd",
        },
        "binary": {
            "pattern": "clangd-${os}-${version}.zip",
            "link": {
                "clangd": "bin/clangd"
            },
            "archive": "zip",
            "is_nested": True
        }
    },
    "tsserver": {
        "npm": {
            "package": "typescript-language-server"
        }
    },
    "pyright": {
        "npm": {
            "package": "pyright"
        }
    },
    "kotlin-lsp": {
        "github": {
            "fragment": "Kotlin/kotlin-lsp"
        },
        "binary": {
            "url": "https://download-cdn.jetbrains.com/kotlin-lsp/${version}/kotlin-${version}.zip",
            "link": {
                "kotlin-lsp": "kotlin-lsp.sh"
            },
            "archive": "zip",
            "is_nested": False
        },
        "version_parser": lambda raw : raw[raw.index("v") + 1:]
    }
}
