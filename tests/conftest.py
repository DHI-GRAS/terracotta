import pytest

import numpy as np
import rasterio


@pytest.fixture(scope='session')
def raster_file(tmpdir_factory):
    import affine

    raster_data = np.random.rand(256, 256).astype('float32')
    profile = {
        'driver': 'GTiff',
        'dtype': 'float32',
        'nodata': np.nan,
        'width': raster_data.shape[1],
        'height': raster_data.shape[0],
        'count': 1,
        'crs': {'init': 'epsg:32637'},
        'transform': affine.Affine(
            2.0, 0.0, 694920.0,
            0.0, -2.0, 2055666.0
        )
    }

    outpath = tmpdir_factory.mktemp('raster').join('img.tif')
    with rasterio.open(str(outpath), 'w', **profile) as dst:
        dst.write(raster_data, 1)

    return outpath