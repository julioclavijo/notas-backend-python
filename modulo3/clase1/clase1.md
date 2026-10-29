# Conexiones seguras
RFC Protocolos:
JWT Estadar abierto

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip 
pip install -r requirements.txt
```

Para generar el SECRET_KEY
```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

```bash
(.venv) ➜  clase1 git:(main) ✗ python main.py                                                                                                                            git:(main|…1 
Token generado: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c3VhcmlvMTIzIiwiZXhwIjoxNzkzMjM2ODE4fQ.Ztwmpr2H3Y53Mxxi-soNQx8yqVU8XOH24zGfSTIMiMs
```