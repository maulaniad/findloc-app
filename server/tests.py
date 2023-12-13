# import phonenumbers
# import folium
# from phonenumbers import carrier, geocoder
# from opencage.geocoder import OpenCageGeocode

# # taking input the phonenumber along with the country code
# number = input("Enter the PhoneNumber with the country code : ")
# # Parsing the phonenumber string to convert it into phonenumber format
# phoneNumber = phonenumbers.parse(number)

# # Storing the API Key in the Key variable
# Key = "73835ddf8b4442c0825c6c84caee841c"  # Replace with your API key

# # Using the carrier module of phonenumbers to print the service provider name in console
# yourLocation = geocoder.description_for_number(phoneNumber, "en")
# print(f"Location\t\t: {yourLocation}")

# yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
# print(f"Service Provider\t: {yourServiceProvider}")

# # Using opencage to get the latitude and longitude of the location
# geocoder = OpenCageGeocode(Key)
# results = geocoder.geocode(str(yourLocation))

# # Check if results are found
# if len(results) > 0:
#     # Assigning the latitude and longitude values to the lat and lng variables

#     for i, data in enumerate(results):
#         print(f"{i}: {data['confidence']} : {data['formatted']}")
#         lat = results[i]['geometry']['lat']
#         lng = results[i]['geometry']['lng']

#     # Getting the map for the given latitude and longitude
#     myMap = folium.Map(location=[lat, lng], zoom_start=9)

#     # Adding a Marker on the map to show the location name
#     folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

#     # Display the map
#     myMap.save("map.html")  # Save the map to an HTML file
#     print("Map saved as map.html")
# else:
#     print("Location not found for the given phone number.")
