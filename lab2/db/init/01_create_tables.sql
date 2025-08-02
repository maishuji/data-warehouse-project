CREATE TABLE DimDate (
    dateid INT PRIMARY KEY,
    date DATE,
    Year INT,
    Quarter INT,
    QuarterName VARCHAR(2),
    Month INT,
    Monthname VARCHAR(20),
    Day INT,
    Weekday INT,
    WeekdayName VARCHAR(10)
);

CREATE TABLE DimStation (
    Stationid INT PRIMARY KEY,
    City VARCHAR(50)
);

CREATE TABLE DimTruck (
    Truckid INT PRIMARY KEY,
    TruckType VARCHAR(20)
);

CREATE TABLE FactTrips (
    Tripid INT PRIMARY KEY,
    Dateid INT,
    Stationid INT,
    Truckid INT,
    Wastecollected DECIMAL(6,2),

    FOREIGN KEY (Dateid) REFERENCES DimDate(dateid),
    FOREIGN KEY (Stationid) REFERENCES DimStation(Stationid),
    FOREIGN KEY (Truckid) REFERENCES DimTruck(Truckid)
);
