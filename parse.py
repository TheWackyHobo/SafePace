def parse_gps_data(filename):
    """Generator to parse GPS data from a file, yielding one latitude and longitude at a time."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(f"Reading line: {line.strip()}")  # Optional: Debugging
                
                # Look for $GPGGA sentences (NMEA GPS data)
                if line.startswith('$GPGGA'):
                    print("Found $GPGGA line.")  # Optional: Debugging
                    parts = line.split(',')
                    
                    # Ensure that there are enough parts (check if it's a valid $GPGGA line)
                    if len(parts) >= 6:
                        lat = parts[2]
                        lat_dir = parts[3]
                        lon = parts[4]
                        lon_dir = parts[5]
                        
                        # Convert to decimal degrees
                        latitude = convert_to_decimal(lat, lat_dir)
                        longitude = convert_to_decimal(lon, lon_dir)
                        
                        # Yield latitude and longitude (use yield for the generator)
                        yield latitude, longitude
                    else:
                        print(f"Invalid $GPGGA line format: {line}")  # Optional: Debugging
                        continue
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    
    # If no valid data found, return None to indicate end of data
    return None, None

def get_next_location(gps_data_generator, filename=None):
    """Fetches the next location (latitude and longitude) from the GPS data generator."""
    try:
        # Get the next latitude and longitude
        lat, lon = next(gps_data_generator)
        return lat, lon, gps_data_generator

    except StopIteration:
        # If the generator is exhausted, return None to signal no more data
        print("No more data available.")
        
        # If filename is provided, restart the generator (reinitialize)
        if filename:
            print("Restarting GPS data generator.")
            gps_data_generator = parse_gps_data(filename)  # Reinitialize the generator
            lat, lon = next(gps_data_generator)  # Get the first location again
            return lat, lon, gps_data_generator
        return None, None, gps_data_generator

# Function to convert coordinates from DDDMM.MMMMM format to decimal degrees
def convert_to_decimal(degree_minute, direction):
    """Converts GPS coordinates from DDDMM.MMMMM format to decimal degrees."""
    try:
        degrees = int(degree_minute[:2])  # Get degrees part
        minutes = float(degree_minute[2:])  # Get minutes part
        decimal = degrees + (minutes / 60)

        if direction in ['S', 'W']:  # Adjust for South and West coordinates
            decimal = -decimal

        return decimal
    except ValueError:
        print(f"Error converting coordinate: {degree_minute} {direction}")
        return None  # Return None if there's an error in conversion

# Example usage
filename = 'gps.txt'  # Path to the GPS file
gps_data_generator = parse_gps_data(filename)  # Initialize the generator

# Get the first location
lat1, lon1, gps_data_generator = get_next_location(gps_data_generator, filename)
if lat1 is not None and lon1 is not None:
    print(f"Latitude: {lat1}, Longitude: {lon1}")

# Get the next location
lat2, lon2, gps_data_generator = get_next_location(gps_data_generator, filename)
if lat2 is not None and lon2 is not None:
    print(f"Latitude: {lat2}, Longitude: {lon2}")

# When all data has been read, it will not try to continue beyond the data available
