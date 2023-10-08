from PIL import Image
import pytesseract

# Load the image containing the graph (replace 'graph.png' with your image file)
image = Image.open('heatmap_capture.png')

# Use pytesseract to perform OCR and extract text from the image
extracted_text = pytesseract.image_to_string(image)

# Split the extracted text into lines
lines = extracted_text.split('\n')

# Initialize empty lists to store extracted data
heat_energy_values = []
emission_factor_values = []

# Parse the extracted lines to extract data points
for line in lines:
    # You may need to customize this part depending on the format of your data
    parts = line.split()  # Split line into words
    if len(parts) == 2:
        try:
            heat_energy = float(parts[0])
            emission_factor = float(parts[1])
            heat_energy_values.append(heat_energy)
            emission_factor_values.append(emission_factor)
        except ValueError:
            pass  # Ignore lines that cannot be converted to floats

# Print the extracted data points
print("Heat Energy Values:", heat_energy_values)
print("Emission Factor Values:", emission_factor_values)
