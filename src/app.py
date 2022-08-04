import subprocess

from dotenv import load_dotenv

from project import create_app, ext_celery

load_dotenv('.env')

app = create_app()
celery = ext_celery.celery



@app.route("/")
def hello():
    return "Hello, World!"


# Enable celery auto reloading
def run_worker():
    subprocess.call(["celery", "-A", "app.celery", "worker", "--loglevel=info"])


@app.cli.command("celery_worker")
def celery_worker():
    from watchgod import run_process

    run_process("./api", run_worker)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, host="0.0.0.0")