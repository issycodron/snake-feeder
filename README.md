# snake-feeder

# 🐍 Meeko's Feeding Tracker

A Raspberry Pi-powered feeding tracker for my western hognose snake, Meeko.

Meeko feeds every 5-6 days. I kept forgetting when he last ate. The obvious solution was to build a Python-powered tracking system with a colour-changing LED, a small display, and eventually a web dashboard — rather than, say, writing it on a Post-it note.

---

## What It Does

- Logs feeding dates to a local JSON file
- Calculates how many days since the last feeding
- Generates a continuous urgency score (0.0 = just fed, 1.0 = feed today, >1.0 = overdue)
- Returns human-readable status messages ("Last fed 3 days ago. Next feed in 2 days.")
- Will drive a colour-changing RGB LED (green → amber → red) on a Raspberry Pi Zero 2W

---

## Planned Features

- [ ] RGB LED urgency indicator (green → red)
- [ ] Physical button to log a feeding
- [ ] Small OLED display showing feeding status
- [ ] Raspberry Pi Zero 2W deployment
- [ ] Flask web dashboard for logging and history
- [ ] SQLite database for long-term feeding records
- [ ] Weight tracking and shed cycle logging

---

## Project Structure

```
snake-feeder/
├── data/
│   └── snake_state.json      # stores the last feeding date
├── src/
│   ├── main.py               # runs the programme
│   ├── feeder.py             # core logic and calculations
│   └── display.py            # output and display functions
├── requirements.txt
└── README.md
```

---

## Getting Started

%### Prerequisites
%- Python 3.12+
%- Git

### Installation

Clone the repository:
```bash
git clone https://github.com/issycodron/snake-feeder.git
cd snake-feeder
```

Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Tracker

```bash
python src/main.py
```

---

## Background

This project started as a practical problem — keeping track of Meeko's feeding schedule — but has become a deliberate effort to develop software development skills beyond academic Python.

During my astrophysics PhD I used Python daily for data analysis, interferometry pipelines, and Bayesian inference. This project is bridging that experience toward software development more broadly: proper project structure, version control, hardware abstraction, and eventually a full web application.

The hardware (Raspberry Pi Zero 2W, RGB LED, OLED display, tactile button) is on its way. In the meantime the software is being developed and tested as a simulation on a laptop, with hardware calls mocked until the physical components arrive.

---

## Author

Issy — astrophysicist, snake owner, and now, tinkerer

[GitHub](https://github.com/issycodron)