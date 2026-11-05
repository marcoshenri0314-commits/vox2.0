import os
import requests
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SUPABASE_URL = os.getenv("SUPABASE_URL", "").strip().rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "").strip()


@app.get("/")
def home():
    return jsonify({
        "app": "VOX 2.0",
        "status": "online",
        "message": "Sua voz, sua rede. 💜"
    })


@app.get("/health")
def health():
    return jsonify({
        "app": "VOX 2.0",
        "flask": "online",
        "supabase_configured": bool(SUPABASE_URL and SUPABASE_KEY)
    })


@app.get("/health/supabase")
def supabase_health():
    if not SUPABASE_URL or not SUPABASE_KEY:
        return jsonify({
            "status": "not_configured",
            "message": "Configure SUPABASE_URL e SUPABASE_KEY no ambiente."
        }), 503

    try:
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/",
            headers={
                "apikey": SUPABASE_KEY,
                "Accept": "application/openapi+json"
            },
            timeout=10
        )

        if response.status_code == 200:
            return jsonify({
                "status": "connected",
                "message": "A API do Supabase respondeu com sucesso."
            })

        return jsonify({
            "status": "response_received",
            "http_status": response.status_code,
            "message": "O Supabase respondeu, mas a conexão precisa ser analisada."
        }), 502

    except requests.RequestException:
        return jsonify({
            "status": "connection_error",
            "message": "Não foi possível alcançar o Supabase. Verifique URL e conexão."
        }), 502


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.getenv("PORT", "5000")),
        debug=False
    )
