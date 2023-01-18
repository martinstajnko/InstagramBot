# Instagram Bot, like random post.

## Overview
This is a Python script that automates various actions on Instagram such as liking, commenting, and following/unfollowing users. 
It uses the selenium library to interact with the Instagram website. 
As a project uses webdriver_manager package, you don't need to specifically download a web driver as is descibed in Requirements and Installation.
Each time the script is going to be run web driver is going to be downloaded automatically for you.

## Requirements
* Python 3
* Poetry for packaging and dependency management -> documentation [Poetry](https://python-poetry.org/docs/).
* Selenium
* A web driver for your browser of choice (e.g. ChromeDriver for Google Chrome) - NOT NECESARRY
* Instagram account with username and password

## Installation
1. Clone the repository: ```git clone https://github.com/martinstajnko/InstagramBot```
2. Install the required packages: ```poetry install```
3. Download the web driver for your browser and add it to your PATH - NOT NECESARRY

## Usage
1. Run the script: ```poetry run python main.py```
2. Follow the prompts to perform the desired action (login, contex to like, number of liked posts)

## Note
Please use this script responsibly and in accordance with Instagram's terms of service. 
Misuse of this script may result in your account being flagged or banned.



