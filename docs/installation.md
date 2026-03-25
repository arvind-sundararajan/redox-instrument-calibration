# Installation
## Prerequisites
Before installing the Oxidation-Reduction Potential Instrument Calibration Engine, ensure you have the following prerequisites installed:

* **Python 3.9**
* **PostgreSQL 13.4**
* **Docker**

## Installation Steps
To install the engine, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/redox-instrument-calibration.git`
2. Navigate to the repository directory: `cd redox-instrument-calibration`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. Build the Docker image: `docker build -t redox-instrument-calibration .`
7. Run the Docker container: `docker run -p 8080:8080 redox-instrument-calibration`
