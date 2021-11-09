# Python API

Custom take-home project for the Nirvana Health hiring process

## How does it work?

You can find the following folders for the application:

- `/app` folder: It has the business logic for the coalesced API. It implements the strategy design pattern to vary between the strategy used from the coalescing side, while the actual logic for the API can be found at the `coalesced_api.py` file
- `/mocked` folder has the logic for mocking the random APIs which act like data sources for our coalesced API. They can be executed individually but are mostly intended to work with containers (since they use environment variables). They also use SQLite to store the data via filesystem for quicker and easier access and only for testing purposes

## How to execute?

Execute the following commands sequentially:

- `docker-compose up -d --build` from within the `/mocked` folder
- `python coalesced_api.py` inside the `/app` folder
- You can go and check at the <http://localhost:5000> (Coalesced API), <http://localhost:5001> (Fake API-1), <http://localhost:5002> (Fake API-2) and <http://localhost:5003> (Fake API-3) ports

## What would I improve?

- Fix the image build for the mocked API so it actually returns different values from each fake API container
- Use a more robust automated testing workflow and/or stack (give a try to other tools like selenium, json-server, BDD, data seeders and so on)
- Upgrade to newest major Flask version
- Validate user input from the query parameters (don't want to get SQL-injected)

**Thank You! :D**