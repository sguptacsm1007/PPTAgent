ProjectDescription
This project is created using google adk and uses a sequential agent approach to first gather information from web using search agent and then translate the information into ppt for consumption


Deployment to Vertex AI
To deploy this agent to Vertex AI Create a .env file
```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="" #Replace this with your GCP project Id
GOOGLE_CLOUD_LOCATION="" #Replace this with GCP region where you want to deploy this app
MODEL="" #Replace this with gemini or other open source model name
```

Deployment command
```cd searchtopptagent
adk deploy agent_engine searchtoppptagent --display-name "PPTAgent" --region ${GOOGLE_CLOUD_LOCATION} --staging-bucket gs://${GOOGLE_CLOUD_LOCATION}
```


