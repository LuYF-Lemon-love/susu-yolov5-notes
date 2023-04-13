# susu-yolov5-notes

## 安装

### Windows10

1. 创建虚拟环境:

```shell
py -m venv env
```

2. 激活环境:

```shell
.\env\Scripts\activate
```

3. 确认 Python 解释器位置:

```shell
where python
```

4. Python 版本 (Python 3.8.1):

```shell
python --version
```

5. 安装 Pytorch (cpu):

```shell
pip install torch==1.9.1 torchvision==0.10.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
python -m pip install --upgrade pip
```

6. pycocotools 的安装:

```shell
pip install pycocotools-windows
```

7. 其他包的安装:

```shell
pip install -r requirements.txt
pip install pyqt5
pip install labelme
```

8. 测试一下:

```shell
python detect.py --source data/images/bus.jpg --weights pretrained/yolov5s.pt
```

![](./results/images/01-test.png)

结果保存在 `runs\detect\exp\bus.jpg` :

![](./runs/detect/exp/bus.jpg)

## 数据处理 (Windows10)

1. 安装:

```shell
pip install labelimg -i https://mirror.baidu.com/pypi/simple
```

2. 启动:

```shell
labelimg
```

3. 软件启动后的界面如下:

![](./results/images/02-label.png)

### 数据标注

虽然是yolo的模型训练，但是这里我们还是选择进行voc格式的标注，一是方便在其他的代码中使用数据集，二是我提供了数据格式转化

**标注的过程是：**

**1.打开图片目录**

![image-20210610004158135](./results/images/image-20210610004158135.png)

**2.设置标注文件保存的目录并设置自动保存**

![image-20210610004215206](./results/images/image-20210610004215206.png)

**3.开始标注，画框，标记目标的label，`crtl+s`保存，然后d切换到下一张继续标注，不断重复重复**

![image-20211212201302682](./results/images/image-20211212201302682.png)

labelimg的快捷键如下，学会快捷键可以帮助你提高数据标注的效率。

![image-20210609171855504](./results/images/image-20210609171855504.png)

标注完成之后你会得到一系列的txt文件，这里的txt文件就是目标检测的标注文件，其中txt文件和图片文件的名称是一一对应的，如下图所示：

![image-20211212170509714](./results/images/image-20211212170509714.png)

打开具体的标注文件，你将会看到下面的内容，txt文件中每一行表示一个目标，以空格进行区分，分别表示目标的类别id，归一化处理之后的中心点x坐标、y坐标、目标框的w和h。

![image-20211212170853677](./results/images/image-20211212170853677.png)

**4.修改数据集配置文件**

标记完成的数据请按照下面的格式进行放置，方便程序进行索引。

```bash
YOLO_Mask
└─ score
       ├─ images
       │    ├─ test # 下面放测试集图片
       │    ├─ train # 下面放训练集图片
       │    └─ val # 下面放验证集图片
       └─ labels
              ├─ test # 下面放测试集标签
              ├─ train # 下面放训练集标签
              ├─ val # 下面放验证集标签
```

这里的配置文件是为了方便我们后期训练使用，我们需要在data目录下创建一个`mask_data.yaml`的文件，如下图所示：

![image-20211212174510070](./results/images/image-20211212174510070.png)

到这里，数据集处理部分基本完结撒花了，下面的内容将会是模型训练！