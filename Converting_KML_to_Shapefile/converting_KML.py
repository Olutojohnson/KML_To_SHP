import geopandas as gpd

# Read the KML file
input_kml = r"path/to/your/file.kml"
data = gpd.read_file(input_kml, driver='KML')

# Define the output file path
output_file = r"path/to/your/output/layer.shp"

# Save as a shapefile (layer format)
data.to_file(output_file, driver='ESRI Shapefile')

print(f"KML file has been converted to a layer and saved at {output_file}")
