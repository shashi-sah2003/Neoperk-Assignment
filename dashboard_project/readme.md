Dashboard Project

- Project Overview
This project is a Django web application that allows users to select a country (USA or India) and view a dashboard with charts and details of drivers from the selected country. The dashboard includes a pie chart showing the average earnings per month by car type and a line chart showing the ages of the drivers. Additionally, detailed information about each driver is displayed.

Technologies Used
- Django
- HTML/CSS
- JavaScript
- Chart.js
- Requests

Flow of the Project
- Landing Page:

- View: landing_page
- Template: landing_page.html
This is the homepage of the application where users can start their journey.

Select Country Page:

- View: select_country
- Template: select_country.html
Users are presented with a dropdown to select a country (USA or India) and a submit button.

Dashboard Page:

- View: dashboard
- Template: dashboard.html
Upon selecting a country, users are redirected to the dashboard page.
This page fetches driver data from an external API based on the selected country and displays it using charts and detailed sections.

Detailed Explanation

Views
- landing_page:

Renders the landing page (landing_page.html).

- select_country:

Renders the country selection page (select_country.html).
Provides a dropdown with options for USA and India.

- dashboard:

Fetches driver data from an external API based on the selected country.
Prepares data for the pie chart and line chart.
Renders the dashboard page (dashboard.html) with charts and driver details.

Templates

- landing_page.html:

Basic HTML structure for the landing page.

- select_country.html:

Contains a form with a dropdown for country selection and a submit button.
Uses CSS for styling and ensuring the button does not cover the full width.

- dashboard.html:

Displays the dashboard with two charts (pie and line) and a detailed section for each driver.
Uses Chart.js for rendering charts.
JavaScript to process and display driver data dynamically.

Static Files

- style.css:
Contains styles for various elements including body, headers, containers, charts, and driver details.
Ensures a clean and responsive design for the application.
API Integration
The project uses the requests library to fetch data from an external API based on the selected country.
Example API Endpoint: https://us-central1-projectexperiment-420611.cloudfunctions.net/assignApi?countryName={countryname}
The data fetched is used to populate charts and driver details on the dashboard page.
