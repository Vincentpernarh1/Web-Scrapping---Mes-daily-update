from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
import os

# SharePoint site and credentials
site_url = "https://yourcompany.sharepoint.com/sites/yoursite"
client_id = "your-client-id"
client_secret = "your-client-secret"

# File details
local_file_path = "C:/path/to/your/local/file.xlsx"  # Path to your local file
sharepoint_folder = "Shared Documents"  # Target SharePoint folder

# Authenticate to SharePoint
ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))

# Read file and upload
with open(local_file_path, "rb") as file:
    file_content = file.read()
    target_folder = ctx.web.get_folder_by_server_relative_url(sharepoint_folder)
    file_name = os.path.basename(local_file_path)
    target_file = target_folder.upload_file(file_name, file_content).execute_query()

print(f"File '{file_name}' uploaded successfully to SharePoint.")
