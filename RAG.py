#imports
import requests
import os
import openai
import dotenv
# upload file to azura blob storage

# Trigger Indexer via REST API (Python requests)
# Config
search_service_name = "your-search-service-name"
indexer_name = "your-indexer-name"
api_version = "2023-10-01-Preview"
admin_key = "your-search-admin-key"

# Endpoint
url = f"https://{search_service_name}.search.windows.net/indexers/{indexer_name}/run?api-version={api_version}"

# Headers
headers = {
    "Content-Type": "application/json",
    "api-key": admin_key
}

# Trigger the indexer
response = requests.post(url, headers=headers)

if response.status_code == 202:
    print("Indexer run triggered successfully.")
else:
    print("Failed to trigger indexer.")
    print(response.status_code, response.text)


# rag agent


## Flag to show citations
showCitations = False

dotenv.load_dotenv()

endpoint = os.environ.get("AZURE_OAI_ENDPOINT")
api_key = os.environ.get("AZURE_OAI_KEY")
deployment = os.environ.get("AZURE_OAI_DEPLOYMENT")

client = openai.AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-02-01",
)

# Configure your data source
text = input('\nEnter a question:\n')

completion = client.chat.completions.create(
    model=deployment,
    messages=[
        {
            "role": "user",
            "content": text,
        },
    ],
    extra_body={
        "data_sources":[
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": os.environ["AZURE_SEARCH_ENDPOINT"],
                    "index_name": os.environ["AZURE_SEARCH_INDEX"],
                    "authentication": {
                        "type": "api_key",
                        "key": os.environ["AZURE_SEARCH_KEY"],
                    }
                }
            }
        ],
    }
)


print(completion.choices[0].message.content)

if showCitations:
    print(f"\n{completion.choices[0].message.context}")
