# Simyan

[![PyPI - Python](https://img.shields.io/pypi/pyversions/Simyan.svg?logo=Python&label=Python-Versions&style=flat-square)](https://pypi.python.org/pypi/Simyan/)
[![PyPI - Version](https://img.shields.io/pypi/v/Simyan.svg?logo=PyPI&label=Version&style=flat-square)](https://pypi.python.org/pypi/Simyan/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/Simyan.svg?logo=PyPI&label=Downloads&style=flat-square)](https://pypi.python.org/pypi/Simyan/)
[![PyPI - License](https://img.shields.io/pypi/l/Simyan.svg?logo=PyPI&label=License&style=flat-square)](https://opensource.org/licenses/MIT)

[![Github - Contributors](https://img.shields.io/github/contributors/Buried-In-Code/Simyan.svg?logo=Github&label=Contributors&style=flat-square)](https://github.com/Buried-In-Code/Simyan/graphs/contributors)
[![Github Action - Code Analysis](https://img.shields.io/github/workflow/status/Buried-In-Code/Simyan/Code-Analysis?logo=Github-Actions&label=Code-Analysis&style=flat-square)](https://github.com/Buried-In-Code/Simyan/actions/workflows/code-analysis.yml)
[![Github Action - Code Formatting](https://img.shields.io/github/workflow/status/Buried-In-Code/Simyan/Code-Formatting?logo=Github-Actions&label=Code-Formatting&style=flat-square)](https://github.com/Buried-In-Code/Simyan/actions/workflows/code-formatting.yml)


A [Python](https://www.python.org/) wrapper for the [Comicvine](https://comicvine.gamespot.com/api/) API.

## Installation

### PyPI
```bash
$ pip install Simyan
```

## Example Usage
```python
from Simyan import api
# Your config/secrets
from config import comicvine_api_key

session = api(api_key=comicvine_api_key)

# Search for Publisher
results = session.publisher_list(params={'name': 'DC Comics'})
for publisher in results:
    print(f"{publisher.id} | {publisher.name} - {publisher.site_url}")

# Get details for a Volume
result = session.volume(_id=26266)
print(result.summary)
```

*There is a cache option to limit required calls to API*
```python
from Simyan import api, SqliteCache
# Your config/secrets
from config import comicvine_api_key

session = api(api_key=comicvine_api_key, cache=SqliteCache())

# Get details for an Issue
result = session.issue(_id=189810)
print(f"{result.volume.name} #{result.issue_number}")
print(result.description)
```

## Socials

Big thanks to [Mokkari](https://github.com/bpepple/mokkari) for the inspiration and template for this project.

[![Social - Discord](https://img.shields.io/discord/618581423070117932.svg?logo=Discord&label=The-DEV-Environment&style=flat-square&colorB=7289da)](https://discord.gg/nqGMeGg)