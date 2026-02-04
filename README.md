# ZoteRofi!


This is a small utility that uses the BetterBibtex zotero plugin to query and show citations in Rofi.

## Setup

First, clone this repo:
```bash
git clone https://github.com/indukurimkv/ZoteRofi.git
```

The project was tested on python 3.14.2, but other versions should work fine.
I recommend using a virtual environment and installing the required packages there:

```bash
# Make sure you are in the root of the repo
mkdir venv; python -m venv .
```

**Activate the virtual environment** (this will differ based on OS).

Now **install the dependencies**:

```bash
# Again, run this from the repo root
pip install -r ./requirements.txt
```

Now the project should be setup!

To run this, just use the path for the python interpreter of the virtual environment and pass in the script!

On linux, this would be something like `/absolute/path/to/repo/venv/bin/python /absolute/path/to/repo/zoterofi.py`

Just bind the command to run the script to a keyboard shortcut of your choosing, and you're set!

Note: For convenience, a bash script is included that will use the appropriate interpreter and call the script. This should make it easier to bind as a shortcut. Unfortunately, this is currently bash-specific
