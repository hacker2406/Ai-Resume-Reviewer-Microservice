# AI Resume Reviewer

A Python application that extracts information from PDF and DOCX resumes, analyzes the content, and provides AI-powered feedback.

## Features

- Extracts key details from resumes: name, email, phone, address, summary/objective, skills, experience, education, certifications, projects, and portfolio links.
- Supports both PDF and DOCX formats.
- Uses Gemini AI for resume review and feedback.
- Saves review results to a file.

## Requirements

- Python 3.7+
- Install dependencies:
  ```
  pip install PyMuPDF python-docx
  ```

## Usage

1. Place your resume file (`.pdf` or `.docx`) in a known location.
2. Run the application from the terminal:
   ```
   python main.py <path_to_resume_file>
   ```
   Example:
   ```
   python main.py "C:/Users/YourName/Documents/resume.pdf"
   ```

3. The program will:
   - Extract and display parsed resume data.
   - Send the data for AI review.
   - Print the review and save it to `review.json` or `review.txt`.

## File Structure

- `main.py` — Entry point for the application.
- `resume_parse.py` — Resume parsing logic.
- `gemini_client.py` — Handles AI review requests.
- `utils.py` — Utility functions (e.g., saving review).

## Customization

- Adjust regex patterns in `resume_parse.py` to better match your resume format.
- Extend the parser to extract additional fields as needed.

## License

MIT License

---

**Note:** Ensure you have the correct versions of all dependencies installed. If you encounter issues, uninstall any conflicting packages and reinstall
