import os
import numpy as np
from tqdm import tqdm

def get_point_cloud_range(points_folder):
    # 초기값 설정: 매우 큰/작은 값으로 설정해 최소/최대값 갱신하도록 함
    min_range = np.array([np.inf, np.inf, np.inf, np.inf])
    max_range = np.array([-np.inf, -np.inf, -np.inf, -np.inf])

    # points 폴더 내 모든 .npy 파일 순회
    for file_name in tqdm(os.listdir(points_folder)):
        if file_name.endswith('.npy'):
            # 각 .npy 파일 로드
            try:
                file_path = os.path.join(points_folder, file_name)
                point_cloud = np.load(file_path)

                # 최소값과 최대값 갱신
                min_range = np.minimum(min_range, point_cloud.min(axis=0))
                max_range = np.maximum(max_range, point_cloud.max(axis=0))
            except:
                pass

    # POINT_CLOUD_RANGE 구하기
    point_cloud_range = max_range - min_range

    return min_range, max_range, point_cloud_range

# 사용 예시
points_folder = '../data/custom_av/points'  # points 폴더 경로 지정
min_range, max_range, point_cloud_range = get_point_cloud_range(points_folder)

print("Minimum range (x, y, z):", min_range)
print("Maximum range (x, y, z):", max_range)
print("Point cloud range (x, y, z):", point_cloud_range)
