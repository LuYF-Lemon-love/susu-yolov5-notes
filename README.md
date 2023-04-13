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