# LNKiller

LNKiller is a Python program for generating malicious Windows shortcut files (.lnk) that can be used for red teaming purposes. It uses powershell to download the payload and 

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [License](#license)

## Description

LNKiller generates malicious Windows shortcut files (.lnk) that can be used to execute arbitrary commands on a target system when opened by the user.

## Features

- Generate malicious .lnk files with customized parameters
- (Rudimentary) Payload encryption
- Option to specify icon (with most standard icons dumped in the icons folder)

## Usage

To use LNKiller, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Jumpy22/LNKiller.git
   ```

2. Navigate to the cloned directory:
   ```bash
   cd LNKiller
   ```

3. Run the program:
   ```bash
   python LNKiller.py
   ```

4. Generate and upload payload

   ![Generate Payload GUI](https://i.imgur.com/6jOBqd7.png)

6. Generate LNK

  ![Generate lnk GUI](https://i.imgur.com/ZuYtlX0.png)

7. Give me money
  - $NoTagNoLife (Cashapp)
  - (I'll update with crypto when I got my Ledger) 

## Installation

LNKiller requires Python 3 and the `tkinter`, `pywin32`, `base64`, and `string` modules. You can install the dependencies using pip:

```bash
pip install tk pywin32 base64 string
```

Once the dependencies are installed, you can run the program as described in the [Usage](#usage) section.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
