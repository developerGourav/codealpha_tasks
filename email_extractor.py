import re

def extract_emails(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, 'r') as file:
            content = file.read()
            
        # Regex pattern for finding email addresses
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # Find all matches in the content
        emails = re.findall(email_pattern, content)
        
        if emails:
            # Write the extracted emails to the output file
            with open(output_file, 'w') as file:
                for email in emails:
                    file.write(email + '\n')
            print(f"Success! Found {len(emails)} emails. Saved to '{output_file}'.")
        else:
            print("No email addresses were found in the file.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found. Please create it first.")
    except Exception as e:
        print(f"An error occurred: {e}")

# --- Instructions ---
# 1. Create a file named 'source.txt' in the same folder as this script.
# 2. Paste your text containing emails into 'source.txt'.
# 3. Run this script.

if __name__ == "__main__":
    extract_emails('source.txt', 'extracted_emails.txt')