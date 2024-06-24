import PyPDF2


def merge_pdfs(input_paths, output_path):
    # Create a PdfMerger object
    merger = PyPDF2.PdfMerger()

    # Iterate over each input PDF path
    for path in input_paths:
        # Append the PDF file to the merger
        merger.append(path)

    # Write the merged PDF to the output file
    merger.write(output_path)

    # Close the PdfMerger object
    merger.close()


# Example usage
input_files = ['file1.pdf', 'file2.pdf']  # List of input file paths to merge
output_file = 'merged.pdf'  # Output file name

merge_pdfs(input_files, output_file)
