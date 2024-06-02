import click

from iotdevice import create_app


@click.command()
@click.option('--config-name', default='development', help='Configuration name')
@click.option('--host', default='127.0.0.1', help='Listen network address')
@click.option('--port', default=5001, help='Exposed port')
def run(config_name, host, port):
    app = create_app(config_name)
    app.run(host=host, port=port)


if __name__ == '__main__':
    run()
