"""This is the project's task runner.
"""
from invoke import task
import os

@task
def docs(ctx, step='build'):
    """Generate documentation.
    """

    image_name = 'docs_debug_lifespline_demo_rst'
    container_name = image_name
    volume_root = os.getcwd()
    volume_path = f'{volume_root}/docs/debug'
    container_host = '0.0.0.0'
    container_port = 8080

    if step == 'debug-setup':
        docker_build = f"docker build . -t {image_name}"
        docker_run = f"""
        docker run \
            --rm -d \
            --mount type=bind,source={volume_path},target=/usr/src/app \
            -p {container_host}:{container_port}:{container_port} \
            --name {container_name} \
            {image_name} {container_port} {container_host}
        """

        cmds = [
            'cd docs/debug',
            docker_build,
            docker_run,

        ]
    elif step == 'debug-clear-setup':
        cmds = [
            f'docker stop {container_name}',
            f'docker rm {container_name}',
            f'docker rmi {image_name}',
        ]
    elif step == 'build':
        cmds = [
            "cd docs",
            "make html",
            "cp -a _build/html/. debug/static/",
            "make clean",
        ]
    
    ctx.run(';'.join(cmds))
