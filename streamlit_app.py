import streamlit as st
import requests

# Langflow API details
LANGFLOW_URL = "https://api.langflow.astra.datastax.com/lf/ab20e4da-070b-4b3f-b234-fb9d194e31a2/api/v1/run/d226b78c-1518-41d2-93fc-278f577359fa?stream=false"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer AstraCS:DNjfxcgsFcfyomsbFBiebmcY:2f8dd9c6a54455875b503f503189a87b41beaa51939a2850f1dd0e6fc1c85af7',
    'Accept': 'application/json'
}

def main():
    st.title("Langflow-Powered Social Media Analytics App")
    st.header("Input Parameters")

    # Multi-select for selecting post types
    selected_post_types = st.multiselect(
        "Select Post Types",
        ["carousel", "reel", "static_image"],  # Add or adjust options as needed
        default=["carousel"]  # Default selected option(s)
    )

    if st.button("Run Workflow"):
        if selected_post_types:
            # Convert selected post types to a comma-separated string
            post_types_str = ",".join(selected_post_types)

            # Create the payload
            payload = {
                "input_value": post_types_str,  # Send as a single string
                "output_type": "chat",
                "input_type": "chat",
                "tweaks": {
                    "TextInput-9iwkN": {},
                    "CustomComponent-guROV": {},
                    "GoogleGenerativeAIModel-9mvzo": {},
                    "Prompt-CFVDN": {},
                    "ChatOutput-2kYu7": {},
                    "ChatInput-1ckrv": {}
                }
            }

            try:
                # Send the request to Langflow API
                response = requests.post(LANGFLOW_URL, headers=headers, json=payload)

                if response.status_code == 200:
                    # Parse and display the output
                    output = response.json()
                    st.header("Output")
                    st.write(output['outputs'][0]["outputs"][0]["results"]["message"]["data"]["text"])
                else:
                    st.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.error("Please select at least one post type.")

if __name__ == "__main__":
    main()

