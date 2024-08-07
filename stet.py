import sys
import re
from PyPDF2 import PdfReader
import matplotlib.pyplot as plt

def read_pdf(filename):
    # Open the PDF file
    with open(filename, 'rb') as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)
        content = ''
        
        # Extract text from each page
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            content += page.extract_text()
        
    return content

def print_correct_candidate_pairs(content):
    # Find all occurrences of 'Correct Answer' and 'Candidate Answer' followed by 2 characters
    matches = re.findall(r'Correct Answer:\s*(.{3}).*?Candidate Answer:\s*(.{3})', content, re.DOTALL)
    subject = re.findall(r'Subject & Subject Code\s*(.*?)\s*\((\d+)\)', content, re.DOTALL)
    subject = subject[0][0].upper()
    count =0
    subject_wise={}
    q=1
    if matches:
        for correct_answer, candidate_answer in matches:
            if q==1:
                print(subject.upper())
            elif q==101:
                print('CDP')
            elif q==131:
                print('GK+GS')
            elif q==141:
                print('APTI+REASOING')
            print(q)
            print(f"Correct Answer: {correct_answer}")
            print(f"Candidate Answer: {candidate_answer}")
            if correct_answer == candidate_answer:
                print('True')
                count=count+1
            else:
                print('False')
            
            print()
            if q==100:
                subject_wise[subject] =count
            elif q==130:
                    subject_wise['CDP'] =count - subject_wise[subject]
            elif q==140:
                subject_wise['GS+GS'] =count- subject_wise[subject] -subject_wise['CDP'] 
            elif q==150:
                subject_wise['APTI+REASONING'] =count- subject_wise[subject] -subject_wise['CDP'] -subject_wise['GS+GS']
            q=q+1
        print('Total correct:', count)
        print('Total Incorrect:', 150-count)
        print()
        for key, value in subject_wise.items():
            print(f"{key.upper()}: {value}")


        # Extracting keys and values
        labels = list(subject_wise.keys())
        sizes = list(subject_wise.values())

        # Adding the additional data to the legend
        incorrect= 150-count
        total_marks=150
        extra_info = [
            f"Total Correct Marks: {count}",
            f"Total Incorrect Marks: {incorrect}",
            f"Total Marks: {total_marks}"
        ]
        # Creating the pie chart
        plt.figure(figsize=(14, 7.5))
        plt.pie(sizes, labels=labels, autopct=autopct_format(sizes), startangle=140)

        # Adding a legend with additional data
        plt.legend(extra_info, loc='upper right', bbox_to_anchor=(1.1, 1.1), title="Marks Information")
        
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        title_text= 'Distribution of Subjects'
        plt.figtext(0.5, 0.06, title_text, ha='center', va='center', fontsize=14, fontweight='bold')
        plt.show()
        plt.savefig(output_path)

# Custom function to format the labels
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return f'{pct:.1f}% ({val})'
    return my_format

            

# Main program
if __name__ == "__main__":
    # Replace with your PDF filename
    # pdf_filename = 'shashank.pdf'
    # Check if the script received exactly one argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <pdf_file>")
        sys.exit(1)
    
    # The file name is provided as a command-line argument
    pdf_path = sys.argv[1]
    output_path = 'pie_chart.png'

    print(pdf_path)
    # Read PDF content
    pdf_content = read_pdf(pdf_path)
    
    # Print correct and candidate answer pairs
    print_correct_candidate_pairs(pdf_content)
