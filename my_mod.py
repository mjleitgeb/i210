import csv

# globals
# strings for the columns names in the csv file and for the file name
style = 'style'
year_formed = 'formed'
year_split = 'split'
band_name = 'band_name'
origin_country = 'origin'
file_end_date = 2017
metal_file_name = 'metal_bands_2017_MP2.csv'

def read_data(file_name):
    with open(metal_file_name, 'r', encoding="utf-8-sig") as csvfile:       # open and read the file
        host_reader = csv.DictReader(csvfile)                               # read the data using a DictReader
        data = [row for row in host_reader]
        return data                                                         # return the list for use in other functions
   
      
def get_bands_formed_in_year(year):
    band_data = read_data(metal_file_name)                                  # Get the data from the csv using the read_data() function
    band_list = []
    for row in band_data:                                                   # Look through the data and make a nested list of bands who formed that year and their country of origin
        if row['formed'] == str(year):                                      # If it matches the year used in the argument, add a new element to the list of bands formed that year.
            band_list.append((row['band_name'], row['origin']))             # Each element of the nested list will consist of a tuple, in the form of (band_name, country)
    return band_list

        
def get_bands_with_style(style_keyword):
    band_data = read_data(metal_file_name)                                  # get the data using your read_data() function
    band_list = []
    for row in band_data:
        if style_keyword.lower() in row['style'].lower():                   # iterate through the nested list, looking at the data in the band's 'style' column
            band_list.append((row['band_name'], row['style']))              # if a band's listed style includes the keyword, add the band name and style to to a new nested list (band_name, style)
    return band_list
    

def get_bands_per_country():
    band_data = read_data(metal_file_name)                                  # get the data using your read_data() function
    band_per_country = {}
    for origin in band_data:                                                # Look at the 'origin' column of each row, and count up the number of bands who claim that country as an origin
        if origin['origin'] == '':
            origin['origin'] = 'Unaffiliated'                               # Some bands are too metal for an origin country. Set those to 'Unaffiliated'
        if origin['origin'] not in band_per_country:
            band_per_country[origin['origin']] = 1                          # adds band and origin if it is not yet in the dictionary
        else:
            band_per_country[origin['origin']] += 1                         # adds one to the number of bands in that country

    band_per_country_list = []       
    for key, value in band_per_country.items():
        band_per_country_list.append((value, key))                          # moves value to the front of a list to make sorting easier
        
    band_per_country_list.sort(reverse = True)                              # sorts list and uses reverse = True to make desceding order

    bpc_list = []
    for i in range(len(band_per_country_list)):
        bpc_list.append((band_per_country_list[i][1], band_per_country_list[i][0]))     # adds bands to a seperate list in the descending order
    
    return bpc_list


def get_longest_lived_bands(num_bands):
    band_data = read_data(metal_file_name)                                  # return the data from the file with read_data()

    longest_lived_bands = {}
    for row in band_data:
        if row['formed'] == '-':                                            # If we don't have a 'formed' date, we can't make any assumptions about the band longevity, so we ignore
            continue
        formed = row[year_formed]
        if row[year_split] == '-':                                          # If we don't have an end date, we'll assume the band was still intact as of the date of this data (2017), uses global variable for the end date
            split = file_end_date
        years_together = int(split) - int(formed)
        if years_together == 0:
            years_together = 1                                              # if the band split the same year it formed, we'll say they lasted a year
        longest_lived_bands[row[band_name]] = years_together

    long_list = []
    for key, value in longest_lived_bands.items():
        long_list.append((value,key))                                       # moves value to the front of a list to make sorting easier

        long_list.sort(reverse = True)                                      # sorts list and uses reverse = True to make desceding order

    long_list_final = []
    for i in range(len(long_list)):
        long_list_final.append((long_list[i][1], long_list[i][0]))          # adds bands to a seperate list in the descending order

    return long_list_final[:num_bands]                                      # use slice to determine the number of bands that will be returned
            

   
def print_table(nested_list, col_1_name, col_2_name, width = 40):

   output = "{:<{}} {:<{}}"                                                 # print header row
   print(output.format(col_1_name, width, col_2_name, width))

   print("-" * (width + 1) * 2)                                             # print dashes to match width (2 cols)
   
   for item1, item2 in nested_list:
       print(output.format(item1, width, item2, width))                     # print out data (2 cols)
   print()

   
    
