# test_pdf_loader.py
import os
from langchain_community.document_loaders import PyPDFLoader

# Define the path to your PDF file
PDF_PATH = os.path.join("src", "data", "hr_policy.pdf")

def test_pdf_extraction():
    if not os.path.exists(PDF_PATH):
        print(f"Error: The file was not found at {PDF_PATH}")
        return

    print(f"Attempting to load and read text from: {PDF_PATH}")
    loader = PyPDFLoader(PDF_PATH)

    try:
        docs = loader.load()
        if not docs:
            print("\nResult: Failure. The loader returned no documents.")
            print("This likely means the PDF is empty, corrupted, or image-based.")
            return

        print(f"\nResult: Success! Found {len(docs)} page(s) in the document.")

        for i, page in enumerate(docs):
            print(f"\n--- Content of Page {i+1} ---")
            print(page.page_content.strip() if page.page_content else "[No text content found on this page]")
            print("--- End of Page ---")

    except Exception as e:
        print(f"\nAn error occurred while trying to load the PDF: {e}")

if __name__ == "__main__":
    test_pdf_extraction()
    