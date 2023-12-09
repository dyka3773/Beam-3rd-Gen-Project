<!-- omit in toc -->
# Project DROPSTAR

Hello 👋, we are BEAM 3rd Gen, one of BEAM’s teams, that consist of students from various fields of study, who share their love for space missions.
Our team was created in August 2020.
We are currently working on our main project, DROPSTAR, which is a microgravity experiment that will be launched in a sounding rocket in 2024.
This project is part of the REXUS/BEXUS programme, an educational competition organized by ESA, DLR, SNSA, SSC, ZARM and EUROLAUNCH.

For more details visit [the wiki page](https://github.com/dyka3773/Beam-3rd-Gen-Project/wiki)

This is the repository of our project, where we will upload all the files that we will use for our experiment.

<!-- omit in toc -->
## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#usage)
  - [Ground Station](#ground-station)
  - [Rocket](#rocket)
  - [SED Stuff](#sed-stuff)
- [Contributing](#contributing)
- [License](#license)
- [Contributors](#contributors)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

This project is written in Python 3.10, so you will need to install it on your computer.
You can download it from [here](https://www.python.org/downloads/).

Each folder has its own requirements.txt file, so you will need to install the required packages for each folder.
You can do this by running the following command in the terminal:

```
pip install -r requirements.txt
```
> Note: It is strongly recommended to use a virtual environment for each folder, so that you don't have any conflicts between the packages.


## Usage

For now, the folders that have useful files are the following:
- [Ground Station](./Ground%20Station/)
- [Rocket](./Rocket/)
- [SED Stuff](./SED%20Stuff/)

And only the `Ground Station` folder has code in it.

### Ground Station

The Ground Station folder contains the code that will be used to communicate with the experiment and to receive and display the data that will be sent.

A Flask server will be used to display the data on a webpage.
In order to run the server, you will first have to change the directory to the `Ground Station` folder and then run the following command in the terminal:

```
run_server.bat
```

This will run a server in the background, so you can access it by going to `localhost:8000` in your browser or (in other machines in your network) to your machine's IP address, followed by `:8000`.


### Rocket

This folder is used to store the code that will be used in the rocket.

> This section will be updated when we have implemented more functionalities.


### SED Stuff

This folder is used to store the files that are needed for the SED (Student Experiment Documentation) that we have to write for the REXUS/BEXUS programme.
They are usually images, diagrams, etc.


## Contributing

If you want to contribute to this project, you can do so by creating a pull request.


## License

This project is Unlicensed but some of the information and ideas that are used in it are licensed by ESA, DLR, SNSA, SSC, ZARM and EUROLAUNCH.
Please contact us if you want to use any of the information or ideas that are used in this project.


## Contributors

- Iraklis Konsoulas - [dyka3773](https://github.com/dyka3773)
- Katerina Zachari - [sugarstreet](https://github.com/sugarstreet)
- Chrysa Episkopou - [xrysanthemo](https://github.com/xrysanthemo)
- Alexis Pakas - [Alex-Pak](https://github.com/Alex-Pak)
- Maria Afentouli - [afentoulimaria](https://github.com/afentoulimaria)
- Ilias Myserlis - [Louismys](https://github.com/Louismys)