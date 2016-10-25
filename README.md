# HubWay_Trends
Visualizing basic trends of the Boston Hubway.
Trying hands-on with pandas and python, I'm working on the Boston HubWay trip history dataset, which stores the data for every Hubway trip from the system launch on July 28th, 2011 till end of November 2013, containing around 1.5 million data entries.

Trips Table Variables: (current as of end of November 2013)
- seq_id: unique record ID
- hubway_id: trip id
- status: trip status; "closed" indicates a trip has terminated
- duration: time of trip in seconds
- start_date: start date of trip with date and time, in EST
- strt_statn: id of start station
- end_date: end date of trip with date and time, in EST
- end_statn: station id of end station
- bike_nr: id of bicycle used
- subsc_type: subscription type - "Registered" is user with membership; "Casual" is user without membership
- zip_code: zipcode of user (only available for registered users) **data includes an apostrophe(') prefix**
- birth_date: birth year of user
- gender: gender of user


Stations Table Variables: (current as of end of November 2013)

Note on variables id versus terminal: Hubway-assigned terminal names (see variable terminalName below) correspond to physical stations. If stations move from one year to the next, the terminal name does not change. This may cause confusion if analysts try to compare station data from different years. Therefore, MAPC added a station id (see variable id below) that corresponds to stations' latitude and longitude. If stations move, they receive a new station id, even if their terminal name does not change. In most cases, station movements are small (across a street, or a block down the same street). 

- id: station id assigned by MAPC; corresponds to start_station and end_station_id in trips table
- terminal: Hubway-assigned station identifier
- station: station name
- municipal: Municipality
- lat: station latitude
- lng: station longitude
- status: Existing station locations and ones that have been removed or relocated

