## Python实现图像比对
## demo1
```python
import cv2
import numpy as np
from PIL import Image
import os
import matplotlib

matplotlib.use('TkAgg')

from matplotlib import pyplot as plt


## 图像处理工具
def extract_features(image_path: str) -> np.ndarray:
    """
    提取图像的ORB特征
    :param image_path: 图像文件路径
    :return: 图像特征
    """
    ## 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    ## 创建ORB特征检测器
    orb = cv2.ORB_create()

    ## 检测关键点和描述符
    kp, des = orb.detectAndCompute(img, None)

    if des is None:
        raise ValueError("无法从图像中提取特征")

    return des


def compare_features(features1: np.ndarray, features2: np.ndarray) -> float:
    """
    比较两组特征的相似度，使用Hamming距离
    :param features1: 图像1的特征
    :param features2: 图像2的特征
    :return: 相似度分数
    """
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(features1, features2)

    ## 返回匹配数目作为相似度评分
    return len(matches)


def search_similar_images(query_image_path: str, image_paths: list) -> list:
    """
    在一组图像中搜索与查询图像最相似的图像
    :param query_image_path: 查询图像路径
    :param image_paths: 目标图像列表
    :return: 返回最相似的图像及其相似度
    """
    ## 提取查询图像的特征
    query_features = extract_features(query_image_path)

    similarity_scores = []

    for image_path in image_paths:
        try:
            ## 提取目标图像的特征
            target_features = extract_features(image_path)

            ## 计算相似度
            similarity = compare_features(query_features, target_features)
            similarity_scores.append((image_path, similarity))
        except ValueError:
            print(f"无法从图像 {image_path} 中提取特征")

    ## 按照相似度排序
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    return similarity_scores


def display_image(image_path: str):
    """显示图像"""
    img = Image.open(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


## 主程序
if __name__ == "__main__":
    ## 查询图像路径
    query_image = "yuan.jpg"

    ## 目标图像目录（这里简单使用3个图像文件）
    image_folder = "./images"

    ## 获取所有图像路径
    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg')]

    ## 进行搜索
    similar_images = search_similar_images(query_image, image_paths)
    most_similar = ''
    print(similar_images)
    print("最相似的图像：")
    max_image_path, max_similarity = max(similar_images, key=lambda x: x[1])
    for image_path, similarity in similar_images:
        print(f"{image_path} 相似度: {similarity}")

    display_image(max_image_path)  ## 显示图像
```



## demo2
```python
import cv2
import numpy as np
import os
from PIL import Image
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


## 图像处理工具
def extract_features(image_path: str, save_path: str = None) -> np.ndarray:
    """
    提取图像的ORB特征
    :param image_path: 图像文件路径
    :param save_path: 特征保存路径 (如果为 None，则不保存)
    :return: 图像特征
    """
    ## 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    ## 创建ORB特征检测器
    orb = cv2.ORB_create()

    ## 检测关键点和描述符
    kp, des = orb.detectAndCompute(img, None)

    if des is None:
        raise ValueError("无法从图像中提取特征")

    ## 如果指定了保存路径，则保存特征
    if save_path:
        np.save(save_path, des)  ## 保存为 .npy 文件

    return des


def compare_features(features1: np.ndarray, features2: np.ndarray) -> float:
    """
    比较两组特征的相似度，使用Hamming距离
    :param features1: 图像1的特征
    :param features2: 图像2的特征
    :return: 相似度分数
    """
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(features1, features2)

    ## 返回匹配数目作为相似度评分
    return len(matches)


def search_similar_images(query_image_path: str, image_paths: list, feature_folder: str) -> list:
    """
    在一组图像中搜索与查询图像最相似的图像
    :param query_image_path: 查询图像路径
    :param image_paths: 目标图像列表
    :param feature_folder: 特征存储的文件夹路径
    :return: 返回最相似的图像及其相似度
    """
    ## 提取查询图像的特征
    query_feature_path = os.path.join(feature_folder, os.path.basename(query_image_path) + '.npy')

    if not os.path.exists(query_feature_path):
        query_features = extract_features(query_image_path, query_feature_path)
    else:
        query_features = np.load(query_feature_path)  ## 加载已保存的特征

    similarity_scores = []

    for image_path in image_paths:
        feature_path = os.path.join(feature_folder, os.path.basename(image_path) + '.npy')

        if not os.path.exists(feature_path):
            try:
                target_features = extract_features(image_path, feature_path)
            except ValueError:
                print(f"无法从图像 {image_path} 中提取特征")
                continue
        else:
            target_features = np.load(feature_path)  ## 加载已保存的特征

        ## 计算相似度
        similarity = compare_features(query_features, target_features)
        similarity_scores.append((image_path, similarity))

    ## 按照相似度排序
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    return similarity_scores


def display_image(image_path: str):
    """显示图像"""
    img = Image.open(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


## 主程序
if __name__ == "__main__":
    ## 查询图像路径
    query_image = "yuan.jpg"

    ## 目标图像目录（这里简单使用3个图像文件）
    image_folder = "./images"

    ## 特征存储目录
    feature_folder = "./features"

    ## 创建特征存储目录（如果不存在）
    if not os.path.exists(feature_folder):
        os.makedirs(feature_folder)

    ## 获取所有图像路径
    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg')]

    ## 进行搜索
    similar_images = search_similar_images(query_image, image_paths, feature_folder)
    most_similar = ''
    print(similar_images)
    print("最相似的图像：")
    max_image_path, max_similarity = max(similar_images, key=lambda x: x[1])
    for image_path, similarity in similar_images:
        print(f"{image_path} 相似度: {similarity}")

    display_image(max_image_path)  ## 显示图像
```



## demo3


```python
import cv2
import numpy as np
import os
import sqlite3
import pickle  ## 用于序列化特征数组
from PIL import Image
import matplotlib

matplotlib.use('TkAgg')
from matplotlib import pyplot as plt


## 图像处理工具
def extract_features(image_path: str) -> np.ndarray:
    """
    提取图像的ORB特征
    :param image_path: 图像文件路径
    :return: 图像特征
    """
    ## 读取图像
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    ## 创建ORB特征检测器
    orb = cv2.ORB_create()

    ## 检测关键点和描述符
    kp, des = orb.detectAndCompute(img, None)

    if des is None:
        raise ValueError(f"无法从图像 {image_path} 中提取特征")

    return des


def save_features_to_db(image_path: str, features: np.ndarray, conn: sqlite3.Connection):
    """
    将图像特征保存到数据库
    :param image_path: 图像路径
    :param features: 图像特征
    :param conn: SQLite数据库连接
    """
    ## 将特征序列化为字节
    feature_blob = pickle.dumps(features)

    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO image_features (image_path, features) 
    VALUES (?, ?)
    """, (image_path, feature_blob))
    conn.commit()


def load_features_from_db(image_path: str, conn: sqlite3.Connection) -> np.ndarray:
    """
    从数据库加载图像特征
    :param image_path: 图像路径
    :param conn: SQLite数据库连接
    :return: 图像特征
    """
    cursor = conn.cursor()
    cursor.execute("""
    SELECT features FROM image_features WHERE image_path = ?
    """, (image_path,))
    result = cursor.fetchone()

    if result is None:
        return None

    ## 反序列化字节为特征数组
    features = pickle.loads(result[0])
    return features


def compare_features(features1: np.ndarray, features2: np.ndarray) -> float:
    """
    比较两组特征的相似度，使用Hamming距离
    :param features1: 图像1的特征
    :param features2: 图像2的特征
    :return: 相似度分数
    """
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(features1, features2)

    ## 返回匹配数目作为相似度评分
    return len(matches)


def search_similar_images(query_image_path: str, image_paths: list, conn: sqlite3.Connection) -> list:
    """
    在一组图像中搜索与查询图像最相似的图像
    :param query_image_path: 查询图像路径
    :param image_paths: 目标图像列表
    :param conn: SQLite数据库连接
    :return: 返回最相似的图像及其相似度
    """
    ## 提取查询图像的特征，如果不存在则提取并保存到数据库
    query_features = load_features_from_db(query_image_path, conn)

    if query_features is None:
        query_features = extract_features(query_image_path)
        save_features_to_db(query_image_path, query_features, conn)

    similarity_scores = []

    for image_path in image_paths:
        ## 加载目标图像特征，如果不存在则提取并保存到数据库
        target_features = load_features_from_db(image_path, conn)

        if target_features is None:
            try:
                target_features = extract_features(image_path)
                save_features_to_db(image_path, target_features, conn)
            except ValueError:
                print(f"无法从图像 {image_path} 中提取特征")
                continue

        ## 计算相似度
        similarity = compare_features(query_features, target_features)
        similarity_scores.append((image_path, similarity))

    ## 按照相似度排序
    similarity_scores.sort(key=lambda x: x[1], reverse=True)

    return similarity_scores


def display_image(image_path: str):
    """显示图像"""
    img = Image.open(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


## 主程序
if __name__ == "__main__":
    ## 查询图像路径
    query_image = "yuan.jpg"

    ## 目标图像目录（这里简单使用3个图像文件）
    image_folder = "./images"

    ## SQLite数据库文件
    db_file = "image_features.db"

    ## 创建数据库连接
    conn = sqlite3.connect(db_file)

    ## 创建表（如果不存在）
    conn.execute("""
    CREATE TABLE IF NOT EXISTS image_features (
        image_path TEXT PRIMARY KEY,
        features BLOB
    )
    """)

    ## 获取所有图像路径
    image_paths = [os.path.join(image_folder, f) for f in os.listdir(image_folder) if f.endswith('.jpg')]

    ## 进行搜索
    similar_images = search_similar_images(query_image, image_paths, conn)

    print("最相似的图像：")
    for image_path, similarity in similar_images:
        print(f"{image_path} 相似度: {similarity}")

    ## 显示最相似的图像
    max_image_path, max_similarity = max(similar_images, key=lambda x: x[1])
    display_image(max_image_path)  ## 显示图像

    ## 关闭数据库连接
    conn.close()
```

