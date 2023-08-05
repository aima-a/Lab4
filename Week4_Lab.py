# File and library setup
import pandas as pd # Import 'pandas' data analysis library
file_path= '/Users/aimaanwar/Downloads/FLIGHT_LOGS.csv' # Specify file path for csv file
file_reader = pd.read_csv(file_path) # Read csv file
data = pd.DataFrame(file_reader) # Create pandas data frame from contents of file
pd.set_option('display.max_columns', None) # Display all columns using print function
print(data) # View data in a readable output

# Remove missing values to create a revised data set
data1 = data.query("departure_airport != '0'" and "arrival_airport != '0'")
    # Note: Entries with missing values for departure or arrival airports are now excluded

# Identify and assign all variables in the data
flight_number = data1['flight_number']
dep_airport = data1['departure_airport']
dep_date = data1['departure_date']
dep_time = data1['departure_time']
arr_airport = data1['arrival_airport']
arr_date = data1['arrival_date']
arr_time = data1['arrival_time']
pass_name = data1['passenger_name']
seat_num = data1['seat_number']
flight_dur = data1['flight_duration']

# Total number of unique airports:
all_airports = pd.concat([dep_airport, arr_airport]).unique() # Concatenate two columns/variables
unique_airports = len(all_airports) # Find length of new column/variable
print(f'The number of airports is {unique_airports}')

# Total number of flights leaving from each airport:
flights_leaving = dep_airport.value_counts()
for airport, count in flights_leaving.items(): # For loop that counts appearance of each airport in departures
    print(f"The number of flights leaving from airport {airport} is {count}")

# Busiest airport:
all_flights = pd.concat([dep_airport, arr_airport]) # Combine departing and arriving flights
busiest_airport = all_flights.value_counts().idxmax() # Identify busiest airport
max_flights_count = all_flights.value_counts().max() # Identify max flight count
print(f"The busiest airport is {busiest_airport} with {max_flights_count} total flights.")

# Number of distinct passengers:
unique_pass = data['passenger_name'].nunique() # Identify number of unique entries
print(f"The number of distinct passengers is: {unique_pass}")

# Longest flight:
long_flight_index = data1['flight_duration'].idxmax() # Identify index of longest flight
long_flight_num = data1.loc[long_flight_index, 'flight_number'] # Identify characteristics of longest flight
long_dep_airport = data1.loc[long_flight_index, 'departure_airport']
long_arr_airport = data1.loc[long_flight_index, 'arrival_airport']
long_dep_time = data1.loc[long_flight_index, 'departure_time']
long_arr_time = data1.loc[long_flight_index, 'arrival_time']
print(f'The longest flight was flight number {long_flight_num} which departed from {long_dep_airport} at {long_dep_time} and arrived at {long_arr_airport} at {long_arr_time}')
