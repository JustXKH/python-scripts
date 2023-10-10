### coco数据集文件json格式

```python
{
    "info": info,  #介绍信息，对解析数据不重要
    "licenses": [license],  # 对解析数据不重要
    "images": [image],
    "annotations": [annotation],
    "categories": [category]
}

```

1.  images是包含多个image实例的列表，一般包含如下。每个image的实例是一个dict，其都有一个独一无二的id

   ```python
   {
   	"license":3,
   	"file_name":"COCO_val2014_000000391895.jpg",
   	"coco_url":"http://mscoco.org/images/391895",
   	"height":360,"width":640,"date_captured":"2013-11-14 11:18:45",
   	"flickr_url":"http://farm9.staticflickr.com/8186/8119368305_4e622c8349_z.jpg",
   	"id":391895
   }
   ```

2. annotations字段是包含多个annotation实例的一个列表，annotation类型本身又包含了一系列的字段，如这个目标的category id和segmentation mask。segmentation格式取决于这个实例是一个单个的对象（即iscrowd=0，将使用polygons格式）还是一组对象（即iscrowd=1，将使用RLE格式）。如下所示

   ```python
   annotation{
       "id": int, # 对象id，因为每一个图像有不止一个对象，所以要对每一个对象编号（每个对象的id是唯一的）
       "image_id": int,# 对应的图片id（与images中的id对应）
       "category_id": int,# 类别id（与categories中的id对应）
       "segmentation": RLE or [polygon],# 对象的边界点（边界多边形，此时iscrowd=0）。
       #segmentation格式取决于这个实例是一个单个的对象（即iscrowd=0，将使用polygons格式）还是一组对象（即iscrowd=1，将使用RLE格式）
       "area": float, # 区域面积
       "bbox": [top_left_x, top_left_y, width, height], # 定位边框 [x,y,w,h],bbox的左上角坐标和其宽、高值
       "iscrowd": 0 or 1 #见下
   }
   ```

3. categories是一个包含多个category实例的列表，而一个category结构体描述如下：

   ```python
   {
   	"supercategory": str,# 主类别
       "id": int,# 类对应的id （0 默认为背景）
       "name": str # 子类别
   }
   ```

### yolo数据集txt格式

​	每个txt文件包含一行或多行标签数据，每行有5列，第一列为目标类别，后边四个数字为归一化后的目标中心点坐标和宽高值

```python
[x_center, y_center, width_norm, height_norm]
# width, height分别为图像的宽高，则
# width_norm = width / width_bbox, 
# height_norm = height / height_bbox, 
# x_center = width / x_bbox, 
# y_center = height / y_bbox, 
```



