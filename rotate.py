import PyPDF2


def rotate_pages(input_path, output_path, rotation_angle):
    # Open the input PDF file
    with open(input_path, 'rb') as input_file:
        # Create a PdfReader object
        pdf_reader = PyPDF2.PdfReader(input_file)
        # Create a PdfWriter object
        pdf_writer = PyPDF2.PdfWriter()

        # Iterate through each page in the input PDF
        for page_num in range(len(pdf_reader.pages)):
            # Get the page object
            page = pdf_reader.pages[page_num]
            # Rotate the page by the specified angle
            page.rotate(rotation_angle)
            # Add the rotated page to the PdfWriter object
            pdf_writer.add_page(page)

        # Write the modified pages to the output PDF file
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)


# Example usage
input_file = 'input.pdf'  # Input PDF file
output_file = 'output.pdf'  # Output PDF file
rotation_angle = 90  # Rotation angle in degrees (90 for horizontal rotation)

# Rotate pages in the input PDF and save to the output PDF
rotate_pages(input_file, output_file, rotation_angle)
