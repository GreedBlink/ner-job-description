# Final project 


## Introduction

A NER model to extract skills (hard and soft) for job description fields.

## Data 

For this project, job advertisements in the technology sector were collected between two sites Remotar and Catho. For each ad, we have the title, description and where it was collected from.

![sample of a job object](public/job_sample.png)

In addition to job postings, two taxonomies were created, one for hard-skills and one for soft-skills.

![sample of taxonomies](public/tax_sample.png)


## What's in this repository?

```
├── README.md
├── public
│   ├── job_sample.png
│   └── tax_sample.png
└── src
    ├── experiment
    │   ├── __init__.py
    │   ├── tests.ipynb
    │   └── utils
    │       ├── __init__.py
    │       └── utils.py
    ├── scrap
    │   ├── README.md
    │   ├── output
    │   │   ├── catho_jobs.json
    │   │   └── remotar_jobs.json
    │   ├── remotar.csv
    │   ├── remotar.json
    │   ├── scrap
    │   │   ├── __init__.py
    │   │   ├── items.py
    │   │   ├── middlewares.py
    │   │   ├── pipelines.py
    │   │   ├── settings.py
    │   │   └── spiders
    │   │       ├── __init__.py
    │   │       ├── catho_job_spider.py
    │   │       └── remotar_spyder.py
    │   └── scrapy.cfg
    └── taxonomies
        ├── README.md
        ├── main.py
        └── utils
            ├── __init__.py
            ├── model_utils.py
            └── utils.py

```

## Requirements