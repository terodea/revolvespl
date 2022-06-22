# Revolve Solutions Data Test - Starter Project

## Solution:
Main driver code is inside **revolvespl/solution/solution_start.py**
```bash
cd revolvespl/
python3 solution/solution_start.py
```

### Prerequisites
#### Java JDK 8
>
> Go to https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html   
> and under the section "Java SE Development Kit 8u191" (the final digits may vary at the time you're reading this)
> click the `Accept License Agreement` radio button and download the version appropriate to your operating system.

#### Python 3.6.* or later.
> 
> See installation instructions at: https://www.python.org/downloads/
> 
> Check you have python3 installed:
> ```bash
> python3 --version
> ```

#### Preferably an IDE such as Pycharm Community Edition
>
> https://www.jetbrains.com/pycharm/download/


### Dependencies and data

#### Creating a virtual environment
>
> Ensure your pip (package manager) is up to date:
> ```bash
> pip3 install --upgrade pip
> ```
> 
> To check your pip version run:
> ```bash
> pip3 --version
> ```
> 
> Install virtualenv:
> ```bash
> pip3 install virtualenv
> ```
> 
> Create the virtual environment in the root of the cloned project:
> ```bash
> virtualenv -p python3 .venv
> ```

#### Activating the newly created virtual environment
> 
> You always want your virtual environment to be active when working on this project.
> 
> ```bash
> source ./.venv/bin/activate 
> ```

#### Installing Python requirements
>
> This will install some of the packages you might find useful:  
> ```bash
> pip3 install -r ./requirements.txt
> 
> ```

#### Running tests to ensure everything is working correctly
> 
> ```bash
> pytest ./tests
> ```

#### Generating the data
>
> A data generator is included as part of the project in `./input_data_generator/main_data_generator.py`
> This allows you to generate a configurable number of months of data.
> Although the technical test specification mentions 6 months of data, it's best to generate
> less than that initially to help improve the debugging process.

> To run the data generator use:
> ```bash
> python ./input_data_generator/main_data_generator.py
> ```

> This should produce customers, products and transaction data under `./input_data/starter`


#### Getting started
>
> The skeleton of a possible solution is provided in `./solution/solution_start.py`
> You do not have to use this code if you want to approach the problem in a different way.


#### Requirement

>Customer Shopping Patterns
>The task involves developing a data pipeline to complete the user story above using sample data sources that will be provided.
>
>Our client is a major high street retailer that handles millions of transactions each day. Their data science team has reached out to our data engineering team >requesting we pre-process some of the data for them at scale so that they can make better use of it in their downstream algorithms. They would like us to deliver >this data weekly.
>
>The input data sources are comprised of customers (in CSV format), transactions (in JSON Lines format) and products (in CSV format).



#### Acceptance Criteria


>The output json should contain information for every customer and has the following fields:
> customer_id, loyalty_score, product_id, product_category, purchase_count

> The code and design should meet the above requirements, follow best practices and should consider future extension or maintenance by different members of the team
>
> Create a Pull Request with appropriate details.


#### Hints

> Use the solution_start.py file to start with

> Write small functions which do only one thing

> Write test cases for every functions except main

> Add comments, logs, and use typing

> Add appropriate exception handling
