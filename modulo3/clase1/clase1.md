# CLASE 1: Fundamentos de Seguridad en APIs. Cohorte 7 M3
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

Passlib: Loguear en software, esta en front (passwd)

```bash
pip install argon2-cffi
```