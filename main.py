import os
import sys
from resume_parse import extract_resume_data
from gemini_client import get_resume_reviews
from utils import save_review

def main():
    if len(sys.argv)<2:
        print("Usage: python main.py <resume_file.pdf/docx>")
        sys.exit(1)
    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        sys.exit(1)
    
    print("Extracting resume data...")
    resume_data = extract_resume_data(file_path)
    print("Parsed Resume Data: ")
    print(resume_data)

    print("\n Sending resume data for review...")
    review=get_resume_reviews(resume_data)
    print("\nGemini Resume Review: \n")
    print(review)

    out_file="review.json" if review.strip().startswith("{") else "review.txt"
    save_review(review, out_file)
    print(f"Review saved to {out_file}")

if __name__ == "__main__":
    main()