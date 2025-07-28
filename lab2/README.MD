## Scenario

You are a data engineer hired by a solid waste management company. It collects and recycles solid waste across major cities in the country of Brazil. They operate hundreds of trucks of different types to collect and transport solid waste. The company would like to create a data warehouse so that it can create reports like:

- Total waste collected per year per city
- Total waste collected per month per city
- Total waste collected per quarter per city
- Total waste collected per year per trucktype
- Total waste collected per trucktype per city
- Total waste collected per trucktype per station per city

You will use your data warehousing skills to design and implement a data warehouse for the company.
Learning objectives

After completing this lab, you will be able to:

- Design a data warehouse.
- Load data into the data warehouse.
- Create a materialized view.

## Steps

### 1. Design a data warehouse

#### MyDimDate
- DateId
- Date
- Day
- Month
- Year
- WeekDay
- Week

### MyDimWaste
- WasteId
- Name

### MyDimZone
- ZoneId
- Name

### MyFactTrips
- TripId
- WasteCollected(tons)
- City
- WasteId (FK)
- ZoneId (FK)
- DateId (FK)
