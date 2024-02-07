import pandas as pd
from bs4 import BeautifulSoup

# Read the Excel file
df = pd.read_excel('input.xlsx')

# Function to extract article title and text
def extract_article_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find the article title (modify this based on the specific HTML structure)
    article_title = soup.find('h1').text
    
    # Find and concatenate all the paragraphs for the article text
    article_text = '\n'.join([p.text for p in soup.find_all('p')])
    
    return article_title, article_text

# Create a DataFrame to store the extracted data
result_df = pd.DataFrame(columns=['Article Title', 'Article Text'])

# Iterate through each row of the Excel file
for index, row in df.iterrows():
    article_html = row['HTML Content']
    
    # Extract article title and text
    article_title, article_text = extract_article_text(article_html)
    
    # Append the data to the result DataFrame
    result_df = result_df.append({'Article Title': article_title, 'Article Text': article_text}, ignore_index=True)

# Save the result to a new Excel file
result_df.to_excel('output.xlsx', index=False)

print("Extraction complete. The result has been saved to 'output.xlsx'.")