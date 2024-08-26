
# Initialize Vertex AI
import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.generative_models import Part


vertexai.init(project="rtc-ai-20240203", location="us-central1")

# Load the Gemini 1.5 Pro model. (https://cloud.google.com/vertex-ai/generative-ai/docs/reference/python/latest/vertexai.generative_models)
multimodal_model = GenerativeModel("gemini-1.5-pro-001")

# Generate response
contents = [ "Explain LLM" ]
response = multimodal_model.generate_content(contents)

print(response.text)

############################
# Document Summarization
#############################
pdf_file_uri = "https://arxiv.org/pdf/2403.05530.pdf"
pdf_file = Part.from_uri(pdf_file_uri, mime_type = "application/pdf")

print("Done")