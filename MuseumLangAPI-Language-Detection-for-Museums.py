! pip install flask

from flask import Flask, request, jsonify
import pickle
import logging
import os

# Inizializzazione dell'app Flask
app = Flask(__name__)

# Configurazione del logging con timestamp
logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Percorso del file modello
filename = "language_detection_pipeline.pkl"

# Verifica del file prima di caricarlo
if not os.path.exists(filename):
    logging.error(f"Errore: Il file '{filename}' non esiste. Assicurati di averlo scaricato.")
    raise FileNotFoundError(f"Il file '{filename}' non esiste.")

# Caricamento del modello di riconoscimento della lingua
try:
    with open(filename, "rb") as file:
        loaded_pipeline = pickle.load(file)
    logging.info("Modello caricato correttamente.")
except Exception as e:
    logging.error(f"Errore nel caricamento del modello: {e}")
    raise RuntimeError("Impossibile caricare il modello.")

@app.route("/identify-language", methods=["POST"])
def identify_language():
    data = request.get_json()

    if not data or "text" not in data or not data["text"].strip():
        logging.warning("Richiesta non valida: testo mancante.")
        return jsonify({"error": "Il campo 'text' è richiesto e non può essere vuoto."}), 400

    text_to_predict = [data["text"]]

    try:
        predicted_language = loaded_pipeline.predict(text_to_predict)

        # Calcolo della confidenza
        confidence =0.95
        if hasattr(loaded_pipeline, "predict_proba"):
            proba = loaded_pipeline.predict_proba(text_to_predict)
            confidence = round(float(max(proba[0])), 2)

        result = {
            "language_code": predicted_language[0].upper(),
            "confidence": confidence
        }

        logging.info(f"Testo analizzato: '{text_to_predict[0]}' -> Lingua: {result['language_code']} | Confidenza={result['confidence']}")
        return jsonify(result), 200

    except Exception as e:
        logging.error(f"Errore durante la previsione: {e}")
        return jsonify({"error": "Errore interno durante la previsione della lingua"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5009)
