# Invoice Generator

Invoice Generator is a desktop application built with Python that creates invoice documents from a simple graphical interface.

The application allows users to enter customer information, add invoice line items, calculate totals, and generate a `.docx` invoice file using a predefined Word template.

## Features
- Desktop GUI built with `customtkinter`
- Add and remove invoice items interactively
- Automatic subtotal and total calculation
- Invoice export to `.docx`
- Uses a reusable Word template (`invoice_template.docx`)
- Beginner-friendly project structure

## How it works
The application collects:
- Customer name
- Customer surname
- Phone number
- Invoice line items (quantity, description, unit price)

Then it renders the data into a Word template using `docxtpl` and saves the generated invoice as a new `.docx` file.

## Requirements
- Python 3.10 or newer recommended
- A valid `invoice_template.docx` template in the project directory

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Files
- `main.py` — main desktop application
- `invoice_template.docx` — Word template used to generate invoice documents

## Dependencies
This project uses:
- `customtkinter`
- `docxtpl`

## Notes
The current implementation is designed as a local desktop utility and is especially useful as a learning project for:
- GUI development
- Document templating
- File generation workflows
- Basic invoice logic

## Possible improvements
- [ ] Better validation for numeric inputs
- [ ] VAT/tax calculation fixes and configuration
- [ ] File save dialog for selecting output folder
- [ ] Editable invoice number field
- [ ] Company details section
- [ ] PDF export support
- [ ] Improved project structure with separated logic and UI layers

## License
This project is distributed under the MIT License.
