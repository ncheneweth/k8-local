from invoke import task
from tasks.shared import is_local

FETCH_ISTIO="""
  curl -L https://istio.io/downloadIstio | ISTIO_VERSION={0} sh - && \
  istioctl version --remote=false
"""

@task
def istio(ctx, version):
    """get latest istio release"""
    if is_local():
      # ctx.run('curl -L https://istio.io/downloadIstio | sh -')
      ctx.run(FETCH_ISTIO.format(version))

