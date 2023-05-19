# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!--
The rules for this file:
  * entries are sorted newest-first.
  * summarize sets of changes - don't reproduce every git log comment here.
  * don't ever delete anything.
  * keep the format consistent:
    * do not use tabs but use spaces for formatting
    * 79 char width
    * YYYY-MM-DD date format (following ISO 8601)
  * accompany each entry with github issue/PR number (Issue #xyz)
-->

## [Unreleased]

### Authors
<!-- GitHub usernames of contributors to this release -->
- lilyminium
- IAlibay
- fiona-naughton
- ianmkenney

### Added
<!-- New added features -->
- Cookiecutter version dependency (Issue #33, PR #46)
- Configuration files for external hooks (PR #9)
- Overhaul cookiecutter CI (PR #10, #26)
- Overhaul cookie CI (PR #7, #28)
- New packaging standard (PR #6)
- Analysis template (PR #19)


### Fixed
<!-- Bug fixes -->
- Propagate `**kwargs` to `AnalysisBase` (PR #66)
- Remove redundant code of conduct document (Issue #42)
- Generated template shipped with broken CI options (PR #41)
- Added MDA install for CI pylint check (Issue #47, PR #48)
- Removed Python 3.8 from cookiecutter build matrix (Issue #59)

### Changed
<!-- Changes in existing functionality -->
- Update hook scripts to use main branch (PR #5)
- Update code of conduct (PR #4)
- Update cookie contents with basic structure (#8)
- Update cookiecutter options (#2)
- Documentation (PR #25, #30)
- Removed LGTM badge from README (PR #52)


### Deprecated
<!-- Soon-to-be removed features -->

### Removed
<!-- Removed features -->
- Unused files from MolSSI
