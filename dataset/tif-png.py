from osgeo import gdal
import os

base_path="E:/house/house_1/"
ii = '12-01xtjqk4-20cm'
file_path=os.path.join(base_path,str(ii)+".tif")
print(file_path)
ds=gdal.Open(file_path)
driver=gdal.GetDriverByName('PNG')
savepath = os.path.join(base_path,str(ii)+".png")
dst_ds = driver.CreateCopy(savepath, ds)
dst_ds = None
src_ds = None