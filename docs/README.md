# My Python lab project

## Part A: Project setup &  Command Descriptions
* **mkdir python_lab**: creates the main root folderfor the projectin your current location.
* **cd python_lab**: Changes the terminal working directory into the newly created project folder.
* **New-Item -ItemType Directory src tests docs**: Creates three separate subdirectories simultaneously to organize source code, tests, and documentation.
* **New-Item -ItemType File ...**: Instantly generates empty placeholder files (main.py, utils.py, config.py) inside the source folder.
* **Get-ChildItem -Recurse**: Recursively displays the entire directory listing showing all nested folders and files.

### Why Separate Code into src, tests, and docs?
Separating project contents into dedicated directories (src, 	ests, and docs) is an industry best practice, even for small projects, because it establishes a clear separation of concerns. The src directory isolates your core application logic, preventing clutter and accidental modification by test or documentation files. The 	ests folder keeps your test suites organized separately from production code, making it easy to run automated checks. Finally, the docs directory centralizes project documentation so that collaborators or users can instantly find setup guides, readmes, and specifications.
