# Decathlon Turnover Forecasting

![py_version](https://img.shields.io/badge/python-^3.9-blue?style=for-the-badge&logo=python&logoColor=9cf) ![version](https://img.shields.io/badge/version-0.1.0-gree?style=for-the-badge&logo=semver) ![code quality](https://img.shields.io/badge/code_quality-A-51C62B?style=for-the-badge&logo=codeforces&logoColor=9cf)

<!-- TOC depthFrom:1 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Decathlon Turnover Forecasting](#decathlon-turnover-forecasting)
  - [Context](#context)
  - [Get started](#get-started)
    - [Init the project](#init-the-project)
    - [Development workflow](#development-workflow)
    - [Code quality](#code-quality)
    - [Documentation \& versioning](#documentation--versioning)
  - [CI/CD workflow](#cicd-workflow)
  - [Machine Learning](#machine-learning)
    - [Data Exploration](#data-exploration)
    - [Prediction model](#prediction-model)
  - [Notes and future improvements](#notes-and-future-improvements)

<!-- /TOC -->

## Context

In stores many decisions are made by managers at the department level.
In order to help store managers in making mid-term decisions driven by economic data, we want to forecast the turnover for the next 8 weeks at store-department level.

To reach this goal, we use a historical data of 6 years from 2012 to 2017. The historical data concerns 4 departments, each department is made up of a group of stores (see. [Data Exploration](#data-exploration)).

## Get started

### Init the project

A `Makefile` is set up with all the useful commands to use this API.

```text
AVAILABLE COMMANDS
 bake                           Init a poetry env and installing some useful packages (run this first).
                                Install poetry with `pip install poetry`.
 build_docker                   Build a Docker container based on Dockerfile.
 clean                          Delete unwanted files.
 clean_docker                   Stop and delete the container.
 cloc                           Count blank lines, comment lines, and physical lines of source code.
 code_metrics                   Compute various metrics from the source code (code quality).
 coverage                       Run coverage tests.
 dcup                           Build Docker compose.
 devmoji                        Init devmoji (add emojis to commit messages).
                                Install it with `npm install -g devmoji`.
 doc                            Generate MkDocs documentation and serve.
 format                         Format the source code using black.
 format_check                   Check what to change using black.
 isort                          Sort the imports using isort.
 lint                           Lint the source code using Ruff.
 lock                           Generate `poetry.lock` file for dependencies.
 mypy                           Run mypy for data type check
 release                        Update version and quality code rank in Makefile, pyproject.tml 
                                and README files.
 reqs                           Generate a requirements.txt file.
 reqs_dev                       Generate a requirements_dev.txt file.
 run_docker                     Run the built Docker container.
 start                          Start the API locally.
 test                           Run unit tests.
 update_deps                    Update dependencies.
```

First, you need to init the environment by using the command `make bake` which sets up the python virtualenv using poetry, installing required dependencies and init the git repository.

**PS:** To add emojies to git commit messages, use `make devmoji`.

### Development workflow

During the development workflow, you can use these following commands:

- `make start`: to start the API on a defined host and port, then you can access the swagger through <https://{host}:{port}/docs> to test the defined routes.
- `make test`: launch `pytest` with the defined unit tests.
- `make coverage`: check the tests coverage.
- `make build_docker`: build a docker image based on the `Dockerfile` to test the project when contained.
- `make run_docker`: run and access the built container.
- `make clean_docker`: clean and delete the docker image.

To add a new route in the project, simply define it in `decathlon_turnover/routes`. Every route's inputs/outputs are defined in `schemas.py` file for data validation.

A `core/` folder is defined to regroup all the configuration and settings related files. Globa and environment variables and centralized in `settings.py` file for simplicity and better management.

### Code quality

Few commands are defined to ensure a minimum quality code:

- `make format`: the most important command, it formats all the project using `black` and sorting the `import` statements.
- `make format_check`: preview the files and lines to format before formatting.
- `make isort`: sort `import` statements in every python file. this command is also called in `make format`.
- `make mypy`: type check in different functions/classes using `mypy`.
- `make cloc`: count blank lines, comment lines, and physical lines of source code.
- `make code_metrics`: compute various metrics from the source code.
- `make profile`: Code profiling to analyze application performance to ensure it is optimized.

All the packages used for ensuring a quality code are configured in the poetry configuration file, `pyproject.toml`. Every related configuration is defined by its own section.

> **Important:** It's highly recommended to use docstrings in every function/class when possible.

### Documentation & versioning

To keep a good documentation, it's very important to keep this `README` file always updated. You can also use `mkdocs` to generate documentation which could be deployed in `github pages`. `mkdocs` is recommended to use when you working a on big project that requires a very rich documentation where a simple `README` isn't enough.

To use `mkdocs`, you can run the following command `make doc` which build and launch the server for documentation.

Keeping the project's history is also very important to allow future improvements, for that a `CHANGELOG` file is defined listing every release dated and describing what was added, changed, removed... etc. It follows the following format:

```markdown
## [{version}] - yyyy-mm-dd
### { Added | Changed | Removed | Deprecated | Fixed | Security }
- to add
- to add
```

The release version follows the norms of [semantic versioning](https://semver.org/). Given a version number `MAJOR.MINOR.PATCH`, we increment the:

- MAJOR version when you make incompatible API changes,
- MINOR version when you add functionality in a backwards compatible manner.
- PATCH version when you make backwards compatible bug fixes.

**Important:** The version variable must be kept updated in three different files:

- `README` file, where a badge version is used,
- `Makefile`, where the version is used as a variable,
- `pyproject.toml`, a project's version is kept in poetry configuration file.

Some useful functions are used to keep these three files' version updated using `release.py` script, a command is defined using `make release {version} {code quality}`.

The git commit messages are organized by category to simplify the project's history. It follows the following format `<type>[optional scope]: <description>` where the commit type takes the following rules:

```text
- :feat:          feat: a new feature
- :fix:           fix: a bug fix
- :docs:          docs: documentation only changes
- :style:         style: changes that do not affect the meaning of the code
                  (white-space, formatting, missing semi-colons, etc)
- :refactor:      refactor: a code change that neither fixes a bug nor adds a feature
- :perf:          perf: a code change that improves performance
- :test:          test: adding missing or correcting existing tests
- :chore:         chore: changes to the build process or auxiliary tools and
                  libraries such as documentation generation
- :chore-release: chore(release): code deployment or publishing to external repositories
- :chore-deps:    chore(deps): add or delete dependencies
- :build:         build: changes related to build processes
- :ci:            ci: updates to the continuous integration system
- :config:        config: Changing configuration files.
- :security:      security: Fixing security issues.
```

## CI/CD workflow

To allow software shippement quickly and efficiently, we implement a CI/CD workflow using _GitHub Actions_. For the sake of this project, we imagine three environments:

- `Dev`: personal to any developer allowing him to test his changes in an independant environment similar to production environment. The `dev` environment is updated when a PR request is opened following every commit in it.
- `Staging`: a clone of the production environment to simulate the behavior of the application once deployed to end-users allowing the developers to catch bugs early on and resolve them. The `staging` environment is updated in every merge to the `master`/`main` branch.
- `Prod`: finally, once all the new features are tested, they are deployed to the production environment to be consumed by the end-users. The `prod` environment is updated in every git tag to define a release.

The tests integrated in the CI/CD pipeline are:

- Code standards like linting, formatting... etc,
- Unit tests using `pytest`,
- Documentation building using `mkdocs`.

**PS:** The documentation building is optional and could be replaced by simple _.markdown_ or _.org_ files.

## Machine Learning

### Data Exploration

We distinguish three data files:

- `train.csv`: dataset containing stores/departments related features and weekly turnover data for training purpose. The training dataset contains the _turnover_ variable to predict.
- `test.csv`: testing dataset has the same structure as `train.csv` without the turnover variable to predict.
- `bu_feat.csv`: contains more stores' related features like geolocalisation, region, postcode... etc.

The scope of our data concerns **4 departments** and **322 stores**.

To better understand our data, we answer the following questions that we can check the detailled answers in the notebook `notebooks/data_exploration.ipynb`.:

- Which department made the highest turnover in 2016?
  - The department 127 made the highest turnover in 2016
- What are the top 5 week numbers (1 to 53) for department 88 in 2015 in terms of turnover over all stores?
  - Weeks: 27, 37, 36, 38 and 28
- What was the top performer store in 2014?
  - Store 121 was the top performer in 2014
- Based on sales can you guess what kind of sport represents department 73?
  - We notice that the department 73 has higher sales during the summer, which can makes us think that this department is specialized in summer sports
- Based on sales can you guess what kind of sport represents department 117?
  - Same as question above, we notice that the department 117 has higher sales during winter which led us to think that department is specialized in winter's sports like ski for example.
- What other insights can you draw from the data? Provide plots and figures if needed. (Optional)

### Prediction model

To forecast the store's turnover, we used a simple `RandomForestRegressor` with `sklearn` framework and saved it using `pickle` library. The model is saved to `/models` directory to be loaded later by the API.

## Notes and future improvements

This work has be made to show the workflow from scratch to build a forecasting model and deploy it in form of an API to be used by an end-user. Though, a lot of improvements has to be made, we list the most important ones here:

- A simple model is used for turnover forecasting (Random Forest Regressor), while we can use advanced algorithms for time series for example like `ARIMA` or `LSTM`.
- The resulted models are stored inside `/models` directory, which is inconvenient to deploy in servers. A better solution would be using cloud storage like buckets. This solution adds loading time but it's done only once (API startup).
- The unit tests aren't complete. An other approach would be using property based testing to detect edge cases during tests. For this, we use `hypothesis` package inspired by `haskell` testing (functional programming).
- The size of the dataset might be problematic in the future, which makes us think about using other librairies to handle it other than `pandas`, for example `dask` or a more complete solution like `spark`.
- To find the best hyperparameters during our model's training, we might implement `hyperparameters optimization` process. For this, we can use `Ray Tune` which is a mature solution.
- During the training phase, making many experiments is part of the data scientist's daily. Many solutions allow monitoring this process by benchmarking and adding a history list of the experiments, like `MLFlow` and `W&B` (weights and biases).
- Adding interpretability process to better understand the prediction process by the model

We also noticed few details about the dataset itself. The main task is to predict stores' turnover to help managers in the decision making process. Though, all the variables in our dataset describe only the geographical characteristics of the store, which isn't enough to predict the turnover. Some other interesting geographical variables would be:

- Number of inhabitants
- Age groups in region
- Mean salary in region
- ... etc
