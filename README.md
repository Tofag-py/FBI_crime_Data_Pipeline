DESIGNING AN AUTOMATED DATA PIPELINE FOR CHICAGO CRIME DATA
Objective:
The city of Chicago provides a comprehensive data portal with regularly updated
information on various aspects of the city, including crime data. The objective of this task is
to create a data pipeline that automates the daily update of the local version of the Chicago
crime dataset. This will involve connecting to an API provided by the city, allowing for
seamless data retrieval, cleaning, and feature generation during the import process.
Requirements:
● Data Source: “https://data.cityofchicago.org/resource/ijzp-q8t2.json?”
● Automation: Design a script or program that can be scheduled to run daily, ensuring
the local dataset is automatically updated without manual intervention.
● Data Retrieval: Implement a method to pull the relevant crime data from the API and
import it into a local storage format, such as CSV.
● Parameterization: If applicable, parameterize the script to allow for customization of
API parameters such as date ranges or specific crime types.
● Error Handling: Implement error-handling mechanisms to address potential issues
with API requests, ensuring the stability and reliability of the automated pipeline.
● Cleaning and Feature Generation: During the import process, incorporate data
cleaning and feature generation steps to enhance the dataset&#39;s quality and usability.
● Documentation: Provide clear documentation for the entire pipeline, including
instructions on setting up the automation, retrieving data, and any data
preprocessing steps performed.
Deliverables:
● A script or program capable of automating the daily update of the local Chicago
crime dataset.
● A well-documented guide explaining the setup and usage of the automated pipeline.
● The local version of the Chicago crime dataset and it is regularly updated through the
automated pipeline.