# RAG (Retrieval-Augmented Generation) Application

This Python application demonstrates a RAG implementation using Azure OpenAI and Azure Cognitive Search. It combines document retrieval with AI-powered text generation to provide contextually relevant answers based on indexed documents.

## Overview

The application performs two main functions:
1. **Indexer Management**: Triggers Azure Cognitive Search indexers to process and index documents
2. **RAG Query System**: Processes user questions by retrieving relevant documents and generating AI-powered responses

## Features

- 🔍 Automated document indexing via Azure Cognitive Search
- 💬 Interactive question-answering system
- 🤖 Integration with Azure OpenAI for natural language processing
- 📚 Optional citation display for transparency
- 🔐 Environment-based configuration for security

## Prerequisites

- Python 3.7 or higher
- Azure OpenAI service instance
- Azure Cognitive Search service
- Valid API keys and endpoints for both services

## Required Dependencies

```bash
pip install requests openai python-dotenv
```

## Environment Setup

Create a `.env` file in the same directory as the script with the following variables:

```env
# Azure OpenAI Configuration
AZURE_OAI_ENDPOINT=https://your-openai-service.openai.azure.com/
AZURE_OAI_KEY=your-openai-api-key
AZURE_OAI_DEPLOYMENT=your-deployment-name

# Azure Cognitive Search Configuration
AZURE_SEARCH_ENDPOINT=https://your-search-service.search.windows.net
AZURE_SEARCH_INDEX=your-index-name
AZURE_SEARCH_KEY=your-search-admin-key
```

## Configuration

Before running the application, update the following variables in the script:

```python
# Update these values with your actual service details
search_service_name = "your-search-service-name"
indexer_name = "your-indexer-name"
admin_key = "your-search-admin-key"
```

## Usage

### Running the Application

1. Ensure all environment variables are properly set
2. Update the configuration variables in the script
3. Run the application:

```bash
python RAG.py
```

### Using the RAG System

1. The application will first attempt to trigger the search indexer
2. You'll be prompted to enter a question
3. The system will:
   - Search for relevant documents in your index
   - Generate a response using Azure OpenAI
   - Display the answer to your question

### Enabling Citations

To see the source documents used for generating answers, set the `showCitations` flag to `True`:

```python
showCitations = True
```

## How It Works

### Indexer Triggering
The application sends a POST request to Azure Cognitive Search to trigger document indexing:
- Processes documents in your configured data source
- Updates the search index with new or modified content
- Returns status confirmation

### RAG Process
1. **Question Input**: User provides a natural language question
2. **Document Retrieval**: Azure Cognitive Search finds relevant documents
3. **Context Integration**: Retrieved documents are provided as context to the AI model
4. **Response Generation**: Azure OpenAI generates a response based on the context
5. **Answer Display**: The generated answer is presented to the user

## API Versions

- Azure Cognitive Search: `2023-10-01-Preview`
- Azure OpenAI: `2024-02-01`

## Error Handling

The application includes basic error handling for:
- Indexer triggering failures
- HTTP status code validation
- Environment variable loading

## Security Considerations

- Store all API keys and sensitive information in environment variables
- Never commit `.env` files to version control
- Regularly rotate API keys
- Use managed identities when possible in production environments

## Troubleshooting

### Common Issues

1. **Indexer Trigger Fails**
   - Verify search service name and admin key
   - Check if the indexer exists and is properly configured
   - Ensure API version compatibility

2. **RAG Query Fails**
   - Confirm all Azure OpenAI environment variables are set
   - Verify the deployment name matches your Azure OpenAI model deployment
   - Check Azure Cognitive Search endpoint and index configuration

3. **No Results Returned**
   - Ensure your search index contains documents
   - Verify the indexer has run successfully
   - Check if your question relates to the indexed content

### Status Codes

- `202`: Indexer triggered successfully
- `4xx`: Client errors (check configuration and authentication)
- `5xx`: Server errors (check service availability)

## Sample Run

```bash
python RAG.py

Indexer run triggered successfully.

Enter a question:
What is machine learning?

[AI-generated response based on indexed documents appears here]
```

## File Structure

```
.
├── RAG.py          # Main application file
├── RAG_README.md   # This documentation
└── .env           # Environment variables (create this file)
```

## Code Structure

The `RAG.py` file contains:

1. **Import Section**: Required libraries for HTTP requests, OpenAI client, and environment management
2. **Indexer Configuration**: Service settings for Azure Cognitive Search
3. **Indexer Trigger**: REST API call to start document indexing
4. **RAG Agent Setup**: Azure OpenAI client configuration
5. **Query Processing**: Interactive question-answering with document retrieval

## Next Steps

Consider enhancing the application with:
- Batch question processing
- Custom prompt engineering
- Advanced citation formatting
- Logging and monitoring
- Web interface integration
- Error recovery mechanisms
- Document upload functionality
- Multi-language support

## Support

For issues related to:
- Azure OpenAI: Check the [Azure OpenAI documentation](https://docs.microsoft.com/azure/cognitive-services/openai/)
- Azure Cognitive Search: See the [Azure Cognitive Search documentation](https://docs.microsoft.com/azure/search/)

## License

This project is provided as-is for educational and demonstration purposes.
