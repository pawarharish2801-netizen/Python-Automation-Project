# 🛡️ Hari's Data Shield System

An intelligent, automated file backup tool built in Python. It monitors a source directory, backs up only new or modified files, and creates timestamped ZIP archives — all on a customizable schedule.

---

## ✨ Features

- 🔁 **Scheduled Backups** — Automatically runs at a custom time interval (in minutes)
- 🔍 **Smart File Detection** — Uses MD5 hashing to copy only new or changed files
- 📦 **ZIP Archiving** — Creates a timestamped `.zip` archive after every backup
- 🖥️ **CLI Interface** — Simple command-line usage with color-coded output
- ⚡ **Lightweight** — No database, no heavy dependencies — pure Python

---

## 📁 Project Structure

```
HarishDataShield/
│
├── HarishDataShield.py   # Main script
└── README.md             # Documentation
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have Python 3.x installed, then install the required packages:

```bash
pip install schedule colorama
```

### Clone the Repository

```bash
git clone https://github.com/your-username/HarishDataShield.git
cd HarishDataShield
```

---

## 🛠️ Usage

```bash
python HarishDataShield.py <TimeInterval> <SourceDirectory>
```

| Argument | Description |
|---|---|
| `TimeInterval` | How often to run the backup (in **minutes**) |
| `SourceDirectory` | Path to the folder you want to back up |

### Example

```bash
python HarishDataShield.py 10 MyProjectFolder
```

This will back up `MyProjectFolder` every **10 minutes**.

---

## 📋 Command Line Options

| Flag | Description |
|---|---|
| `--h` or `--H` | Show help — what the script does |
| `--u` or `--U` | Show usage instructions |

```bash
python HarishDataShield.py --h
python HarishDataShield.py --u
```

---

## ⚙️ How It Works

1. **Scan** the source directory recursively
2. **Compare** each file with its backup copy using MD5 hash
3. **Copy** only files that are new or have been modified
4. **Create** a `.zip` archive of the entire backup folder with a timestamp
5. **Repeat** based on the scheduled interval

### Output Example

```
------------------------------------------------------------
----------------- Hari's Data Shield System --------------
------------------------------------------------------------
Success :  Data Shield System Started Successfully ....
Time Interval in Minutes :  10
Press Ctrl + C to stop the execution : (For Windows)
Press Ctrl + Z to stop the execution : (For Linux/macOS)

Creating the backup folder for backup process...
Success :  Backup Process Started Successfully at : Fri Dec 12 10:00:00 2025
************************************************************
Backup completed succesfully
Files copied :  5
Zip file gets created with name :  HarisDataShieldBackup_2025-1212_10-00-00.zip
************************************************************
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `schedule` | Periodic task scheduling |
| `colorama` | Colored terminal output |
| `hashlib` | MD5 file integrity check (built-in) |
| `zipfile` | ZIP archive creation (built-in) |
| `shutil` | File copying (built-in) |
| `os` | Directory traversal (built-in) |

---

## 👨‍💻 Author

**Harish Mahendra Pawar**
📅 December 2025

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> ⭐ If you found this useful, consider giving the repo a star!
