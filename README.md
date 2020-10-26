Assignment # 4.5
>> Django-4.5 ETL to Django Fixture
Objective
The goal is to obtain and share data. Test ability to import data into your Django Application constitutes a key and vital skill.

Below is a basic library/program that reads an extract of the T-100 Domestic Market Tables from the U.S. Department of Transportation - Bureau of Transportation Statistics (BTS) . The data can be downloaded as a CSV file from the BTS website.

Converted this data to a [Django Serialization format] for further processing and to provide initial data for models.

This code uses the following elements:

CSV for CSV file reading and writing
JSON for JSON encoding and decoding

The option used for loading data in Django APP:

Consuming some serialization of objects/data - Django Fixtures

CBV 
Views attempted - list view and detail view using Django Class-Based Views.

Data used was from United States Department of Transportation - Bureau of Transportation Statistics - the Air Carriers : T-100 Domestic Market (U.S. Carriers) Tables

Steps:
Reviewed the Air Carriers : T-100 Domestic Market (U.S. Carriers).

Developed appropriate Django Models.

Created new project and virtual environment 

Created an ETL Process to Transform the CSV data downloaded from the Air Carriers “ T-100 Domestic Market (U.S. Carriers) Tables” into importable serializations using Django Fixtures.

Create a “fixtures” folder so that Django can auto-load ETL data.

Developed Queries using Django  web application framework to access data and data enquiries.

Utilized the ListView and DetailView CBVs to present the results of various queries of the Air Carriers : T-100 Domestic Market (U.S. Carriers) data.

Attempted 3-4 queries using Django ORM provisions for querying. 

