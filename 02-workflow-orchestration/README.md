<div>
<img src="https://github.com/mage-ai/assets/blob/main/mascots/mascots-shorter.jpeg?raw=true">
</div>

## Data Engineering Zoomcamp - Week 2

Welcome to DE Zoomcamp with Mage!

Mage is an open-source, hybrid framework for transforming and integrating data. ✨

Workflow orchestration is the process of dependency management through automation. An orchestration tool, such as Mage, Apache Airflow, Prefect and Luigi, manages and controls the movement, transformation and integration of data across various systems, applications and databases. We delved deeper into the use of Mage to automate our data workflow.

Mage is an open-source pipeline tool for orchestrating, transforming and integrating data. It handles the entire Extract, Transform, and Load (ETL) process using Python and SQL. Matt Palmer incredibly introduced the key magical concepts of Mage (on an early Monday morning 😂) using a hands-on approach by creating different pipelines for extracting, transforming and loading data into and out of PostgreSQL database, Google Cloud Storage buckets, and BigQuery data warehouse.

🔍 Project Overview:

- Extracted data from DataTalkClub GitHub repository using Mage data loader.

- Transformed the extracted data to standardize the column names and clean the data using Python.

- Queried the data for meaningful insights using Python.

- Loaded the transformed data into Google Cloud Storage bucket as partitioned files.

- Created a schedule for the pipeline to automatically run daily.

💡 Skills learnt:

- Creating data pipelines (DAGs).

- Extracting and loading data from Google Cloud Storage and BigQuery warehouse.

- Loading and extracting data from databases using pipelines.

- Running and creating resources on Virtual Machines.

🛠 Tools and languages used:

- Mage

- PostgreSQL

- Python

- Docker

- Terraform

- Google Cloud Platform (Google Cloud Services, BigQuery, VM Instances)

💻 Challenges faced:

Running data pipelines locally on a low-powered laptop led to the pipelines taking too long to execute and sometimes not executing at all (which is expected when dealing with a lot of data).

- I had to use a Google virtual machine instance with 4 vCPU and 16 GB memory to run Mage on the VM using Docker, and connect to it using ssh.

## Assistance

1. [Mage Docs](https://docs.mage.ai/introduction/overview): a good place to understand Mage functionality or concepts.
2. [Mage Slack](https://www.mage.ai/chat): a good place to ask questions or get help from the Mage team.
3. [DTC Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/week_2_workflow_orchestration): a good place to get help from the community on course-specific inquireies.
4. [Mage GitHub](https://github.com/mage-ai/mage-ai): a good place to open issues or feature requests.
