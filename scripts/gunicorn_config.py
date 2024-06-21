import multiprocessing
import os
import signal
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from gunicorn.arbiter import Arbiter
    from gunicorn.http import Request
    from uvicorn.workers import UvicornWorker


def on_starting(server: 'Arbiter') -> None:  # noqa: ARG001
    pass


def when_ready(server: 'Arbiter') -> None:  # noqa: ARG001
    pass


def pre_fork(server: 'Arbiter', worker: 'UvicornWorker') -> None:  # noqa: ARG001
    pass


def post_fork(server: 'Arbiter', worker: 'UvicornWorker') -> None:  # noqa: ARG001
    pass


def post_worker_init(worker: 'UvicornWorker') -> None:  # noqa: ARG001
    pass


def worker_abort(worker: 'UvicornWorker') -> None:  # noqa: ARG001
    pass


def pre_exec(server: 'Arbiter') -> None:  # noqa: ARG001
    pass


def pre_request(worker: 'UvicornWorker', req: 'Request') -> None:  # noqa: ARG001
    pass


def child_exit(server: 'Arbiter', worker: 'UvicornWorker') -> None:  # noqa: ARG001
    pass


def worker_exit(server: 'Arbiter', worker: 'UvicornWorker') -> None:  # noqa: ARG001
    pass


def nworkers_changed(server: 'Arbiter', new_value: int, old_value: int | None) -> None:  # noqa: ARG001
    pass


def on_exit(server: 'Arbiter') -> None:  # noqa: ARG001
    pass


def worker_int(worker: 'UvicornWorker') -> None:
    # FIXME: Uvicorn workers doesn't reload
    # Ignoring type since it is int and not str
    if reload:
        os.kill(worker.pid, signal.SIGTERM)


def on_reload(server: 'Arbiter') -> None:  # noqa: ARG001
    pass


prod = os.getenv('APP_ENV', 'prod') == 'prod'
workers_per_core_str = os.getenv('GUNICORN_WORKERS_PER_CORE', '1')
proc_name: str = os.getenv('GUNICORN_PROCESS_NAME', 'gunicorn')
timeout = os.getenv('GUNICORN_WORKER_TIMEOUT', '10')
web_concurrecy_str = os.getenv('GUNICORN_WEB_CONCURRENCY')
host = os.getenv('GUNICORN_HOST', '0.0.0.0')  # noqa: S104
port = os.getenv('GUNICORN_PORT', '80')
bind_env = os.getenv('GUNICORN_BIND', None)
use_loglevel = os.getenv('GUNICORN_LOG_LEVEL', 'info')


reload = not prod

use_bind = bind_env if bind_env else f'{host}:{port}'

cores = multiprocessing.cpu_count()
workers_per_core = float(workers_per_core_str)
defualt_web_concurrency = workers_per_core * cores

web_concurrecy = int(web_concurrecy_str) if web_concurrecy_str is not None else max(int(defualt_web_concurrency), 2)

workers = (web_concurrecy if web_concurrecy > 0 else 1) if prod else 2

loglevel = use_loglevel
bind = use_bind
accesslog = '-'
