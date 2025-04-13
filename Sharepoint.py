from office365.sharepoint.client_context import ClientContext
from azure.identity import InteractiveBrowserCredential
import pandas as pd
from io import BytesIO
from secret import client_id  # Ensure client_id is available

# SharePoint site and credentials
site_url = "https://shiftup.sharepoint.com/sites/Projetodiariodefuso"
sharepoint_folder = "Shared Documents/Projeto diario de fusão"
file_name = "Diario de fusão.xlsx"

# Authenticate interactively using InteractiveBrowserCredential
credential = InteractiveBrowserCredential()

# Function to dynamically retrieve the access token
def acquire_token():
    token = credential.get_token("https://graph.microsoft.com/.default")
    return token.token  # Return only the token string

# Set up the context using the token function
ctx = ClientContext(site_url).with_access_token(lambda: acquire_token())

# Read file from SharePoint without downloading
file_url = f"/sites/Projetodiariodefuso/{sharepoint_folder}/{file_name}"

# Get the file object from SharePoint
file = ctx.web.get_file_by_server_relative_url(file_url)

# Open the file binary content
file_content = file.open_binary(ctx,file_url).execute_query()

# Load the file content into a BytesIO object
file_data = BytesIO(file_content.content)

# Load Excel file into Pandas
df = pd.read_excel(file_data, engine="openpyxl")
print(df.head())

# Modify Data (Example: Add a new row)
# new_data = pd.DataFrame([{"Column1": "NewValue1", "Column2": "NewValue2"}])  # Adjust column names
# df = pd.concat([df, new_data], ignore_index=True)

# Save modified file back to BytesIO
# output = BytesIO()
# df.to_excel(output, index=False, engine="openpyxl")
# output.seek(0)

# Upload updated file to SharePoint
# ctx.web.get_file_by_server_relative_url(file_url).save_binary(output.getvalue()).execute_query()

# print(f"File '{file_name}' updated successfully in SharePoint.")
