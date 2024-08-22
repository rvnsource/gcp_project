
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="river-span-431711-k8", location="us-central1")# Load the Gemini 1.5 Pro model. (https://cloud.google.com/vertex-ai/docs/reference/python/latest/vertexai.generative_models)
multimodal_model = GenerativeModel("gemini-1.5-pro-001")

contents = ["Explain LLM"]

response = multimodal_model.generate_content(contents)

print(response.text)


