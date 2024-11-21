import os
import numpy as np
from tqdm import tqdm

def get_labels_range(labels_folder):
    # 초기값 설정: 매우 큰/작은 값으로 설정해 최소/최대값 갱신하도록 함
    min_range = np.array([np.inf, np.inf, np.inf])
    max_range = np.array([-np.inf, -np.inf, -np.inf])

    # labels 폴더 내 모든 .txt 파일 순회
    for file_name in tqdm(os.listdir(labels_folder)):
        if file_name.endswith('.txt'):
            # 각 .txt 파일 열기
            file_path = os.path.join(labels_folder, file_name)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    # 데이터를 공백으로 구분하여 파싱 (x, y, z는 0, 1, 2번째 인덱스에 위치)
                    data = line.strip().split()
                    x, y, z = float(data[0]), float(data[1]), float(data[2])

                    # 최소값과 최대값 갱신
                    min_range = np.minimum(min_range, [x, y, z])
                    max_range = np.maximum(max_range, [x, y, z])

    # POINT_CLOUD_RANGE 구하기
    point_cloud_range = max_range - min_range

    return min_range, max_range, point_cloud_range

# 사용 예시
labels_folder = '../data/custom_av/labels'  # labels 폴더 경로 지정
min_range, max_range, point_cloud_range = get_labels_range(labels_folder)

print("Minimum range (x, y, z):", min_range)
print("Maximum range (x, y, z):", max_range)
print("Point cloud range (x, y, z):", point_cloud_range)


import os
import numpy as np
import matplotlib.pyplot as plt

# Function to extract x, y, z values from the label files
def extract_xyz_values(labels_folder):
    x_vals, y_vals, z_vals = [], [], []
    
    # Loop through all .txt files in the folder
    for file_name in os.listdir(labels_folder):
        if file_name.endswith('.txt'):
            file_path = os.path.join(labels_folder, file_name)
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    data = line.strip().split()
                    x_vals.append(float(data[0]))  # x
                    y_vals.append(float(data[1]))  # y
                    z_vals.append(float(data[2]))  # z
    
    return np.array(x_vals), np.array(y_vals), np.array(z_vals)

# Plot histograms for x, y, z
def plot_histograms(x, y, z):
    plt.figure(figsize=(15, 5))

    # x histogram
    plt.subplot(1, 3, 1)
    plt.hist(x, bins=50, color='blue', alpha=0.7)
    plt.axvline(x=-75.5, color='red', linestyle='--', linewidth=2)
    plt.axvline(x=75.5, color='red', linestyle='--', linewidth=2)
    plt.title('X values histogram')
    plt.xlabel('X')
    plt.ylabel('Frequency')

    # y histogram
    plt.subplot(1, 3, 2)
    plt.hist(y, bins=50, color='green', alpha=0.7)
    plt.axvline(x=-75.5, color='red', linestyle='--', linewidth=2)
    plt.axvline(x=75.5, color='red', linestyle='--', linewidth=2)
    plt.title('Y values histogram')
    plt.xlabel('Y')
    plt.ylabel('Frequency')

    # z histogram
    plt.subplot(1, 3, 3)
    plt.hist(z, bins=50, color='red', alpha=0.7)
    plt.title('Z values histogram')
    plt.xlabel('Z')
    plt.ylabel('Frequency')

    plt.tight_layout()
    plt.show()

# 사용 예시
labels_folder =  '../data/custom_av/labels'   # labels 폴더 경로 지정
x_vals, y_vals, z_vals = extract_xyz_values(labels_folder)
plot_histograms(x_vals, y_vals, z_vals)
