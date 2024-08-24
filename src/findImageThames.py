import vertexai
from vertexai.preview.generative_models import GenerativeModel, Image


PROJECT_ID = "river-span-431711-k8"
REGION = "us-central1"
vertexai.init(project=PROJECT_ID, location=REGION)

#IMAGE_FILE = "gs://generativeai-downloads/images/scones.jpg"
IMAGE_FILE = "/Users/ravi/gcp_project/data/raw/By_The_River_Thames_at_Vauxhall,_London_-_geograph.org.uk_-_5726285.jpg"
image = Image.load_from_file(IMAGE_FILE)

generative_multimodal_model = GenerativeModel("gemini-1.5-flash-001")
response = generative_multimodal_model.generate_content(["What is shown in this image?", image])

print(response.text)