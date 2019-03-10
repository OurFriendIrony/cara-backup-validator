| **License** | **Build** | **Coverage** |
|---|---|---|
| [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0) | [![Build Status](https://travis-ci.org/OurFriendIrony/cara-backup-validator.png)](https://travis-ci.org/OurFriendIrony/cara-backup-validator) | [![codecov](https://codecov.io/gh/OurFriendIrony/cara-backup-validator/branch/master/graph/badge.svg)](https://codecov.io/gh/OurFriendIrony/cara-backup-validator) |
  
## Purpose
- Parse CaraNetworks ROBOCOPY backup reports
- Identify reports that highlight backup failures
- Display to user
- Allow user to select report

## Directions for use  
### Windows
* Copy the following to the backup reports directory
* * `src\`
* * `_run.bat`
* Execute the `_run.bat` file.
* Follow instructions
  
## Prereqs  
`pip install -r requirements.txt`  
  
## Executing Tests  
`coverage run -m pytest -v`  
  
