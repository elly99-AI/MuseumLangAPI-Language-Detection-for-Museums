# MuseumLangAPI – Language Detection for Museums

## Executive Summary
MuseumLangID evolves into **MuseumLangAPI**: a REST service that exposes the model for automatic language detection of museum texts.  
The API receives texts in JSON format, returns the detected language code along with a confidence score, and is designed to scale and integrate seamlessly with the museum’s management systems.

- **Problem:** the model was previously limited to local use; the lack of a standardized interface hindered collaboration and integration.  
- **Objective:** provide the model through a **REST API** (Flask or FastAPI), with JSON input and language code output.  
- **Benefits:**  
  - **Accessibility:** remote service available to all museum departments.  
  - **Integration:** easy embedding into existing software applications.  
  - **Scalability:** support for parallel requests from multiple users.  

---

## What I Did
I designed and implemented **MuseumLangAPI** using Flask:  
- Loaded the model once at startup to optimize performance.  
- Added input validation to ensure reliable requests.  
- Implemented confidence score calculation when available (`predict_proba`).  
- Configured structured logging with INFO/WARNING/ERROR levels.  
- Applied robust error handling with `try/except` and standardized response codes (200, 400, 500).  
- Built the `/identify-language` endpoint ready for integration into external systems.  

---

## Tech Stack
- **Framework:** Flask (Python)  
- **Model:** `language_detection_pipeline.pkl` (scikit-learn pipeline)  
- **Logging:** `api.log` file with INFO/WARNING/ERROR levels  

