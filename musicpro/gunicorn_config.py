import multiprocessing

bind = "127.0.0.1:8000"  # Dirección IP y puerto en el que Gunicorn escuchará las solicitudes
workers = multiprocessing.cpu_count() * 2 + 1  # Número de procesos de trabajo que Gunicorn utilizará
