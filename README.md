# Memory Match Game (MmG)

A Python-based memory card game designed as a cognitive exercise tool. This project was created with the intention of providing a fun, accessible mental workout to help elderly individuals keep their minds engaged and active. 

By tracking game statistics over time, this tool allows players, caregivers, or healthcare professionals to monitor cognitive performance and progress.

## 🌟 Features

* **Simple & Accessible Gameplay:** Players match 16 cards consisting of 8 unique pairs. There is no time limit, allowing for a stress-free experience.
* **Clean Main Menu:** Easy navigation with "Start", "Rules", and "Credits" buttons.
* **Performance Tracking:** At the end of the game, players are presented with a detailed breakdown of their performance, including:
  * Date/Time
  * Total time taken
  * Accurate and inaccurate presses
  * Total clicks
* **Data Logging:** Every completed game's statistics are automatically appended to a local `mmgamedata.csv` file. 
* **Progress Review:** The end screen displays the results of the past 5 games, making it easy to track improvement or changes in memory retention.

## 📋 Prerequisites

To run this game, you will need Python installed on your computer along with the `pygame` library.

1. Install Python 3.x from [python.org](https://www.python.org/)
2. Install Pygame via your terminal or command prompt:
   ```bash
   pip install pygame
