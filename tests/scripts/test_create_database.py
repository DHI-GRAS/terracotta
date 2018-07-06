from click.testing import CliRunner


def test_create_database(raster_file, tmpdir):
    from terracotta.scripts import cli

    outfile = tmpdir / 'out.sqlite'
    input_pattern = str(raster_file.dirpath('{name}.tif'))

    runner = CliRunner()
    result = runner.invoke(cli.cli, ['create-database', input_pattern, '-o', str(outfile)])
    assert result.exit_code == 0
    assert outfile.check()

    from terracotta import get_driver
    driver = get_driver(str(outfile), provider='sqlite')
    assert driver.available_keys == ('name',)
    assert driver.get_datasets() == {('img',): str(raster_file)}