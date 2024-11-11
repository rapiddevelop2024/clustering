#DBSCAN 
#author : m.dehghan

'''
DBSCAN (Density-Based Spatial Clustering of Applications with Noise): 
DBSCAN is a density-based algorithm that identifies clusters based on data point density.
 It groups points closely packed together, with a minimum number of points (min_samples) within a certain radius (eps).
 DBSCAN can handle clusters of irregular shapes and detects noise or outliers, making it suitable for complex datasets.
'''

import numpy as np
from sklearn.cluster import DBSCAN

class DBSCANClusterer:
    def __init__(self, data, eps=0.5, min_samples=5):
        """
        Initialize the DBSCAN clusterer with data, eps, and min_samples.
        Initialiser le clusterer DBSCAN avec les données, eps et min_samples.
        مقداردهی اولیه خوشه‌بند DBSCAN با داده‌ها، eps و min_samples.
        تهيئة الكلاستر باستخدام DBSCAN بالبيانات، eps و min_samples.
        """
        self.data = data
        self.eps = eps
        self.min_samples = min_samples
        self.model = None

    def fit(self):
        """
        Apply DBSCAN clustering to the data.
        اعمال خوشه‌بندی DBSCAN به داده‌ها.
        تطبيق DBSCAN على البيانات للتصنيف.
        Appliquer le clustering DBSCAN aux données.
        """
        # Initialize DBSCAN model with specified eps and min_samples.
        # Initialiser le modèle DBSCAN avec les paramètres eps et min_samples.
        # مقداردهی اولیه مدل DBSCAN با پارامترهای eps و min_samples.
        # تهيئة نموذج DBSCAN مع قيم eps و min_samples المحددة.
        self.model = DBSCAN(eps=self.eps, min_samples=self.min_samples)
        
        # Fit the model to the data.
        # برازش مدل به داده‌ها.
        # ملاءمة النموذج على البيانات.
        # Ajuster le modèle aux données.
        self.model.fit(self.data)

    def predict(self):
        """
        Predict cluster labels for each data point.
        Prédire les étiquettes de clusters pour chaque point de données.
        پیش‌بینی برچسب‌های خوشه برای هر نقطه داده.
        التنبؤ بتسميات المجموعات لكل نقطة بيانات.
        """
        if self.model is None:
            raise Exception("Model not fitted. Call the fit() method first.")
        
        # Return the cluster labels for each data point.
        # Retourner les étiquettes de clusters pour chaque point de données.
        # بازگشت برچسب‌های خوشه برای هر نقطه داده.
        # إرجاع تسميات المجموعات لكل نقطة بيانات.
        return self.model.labels_

# Example usage:
# Exemple de données
# داده‌های نمونه
# بيانات عينة
data = np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [4, 0],
                 [10, 10], [10, 12], [10, 8]])
                 
# ایجاد شیء از کلاس خوشه بندی DBSCAN با eps برابر ۲ و min_samples برابر ۲
# إنشاء كائن من فئة الكلاستر DBSCAN مع eps تساوي ٢ و min_samples تساوي ٢
# Création d'un objet de la classe DBSCANClusterer avec eps = 2 et min_samples = 2
dbscan_clusterer = DBSCANClusterer(data, eps=2, min_samples=2)

# Effectuer le clustering
# انجام عملیات خوشه‌بندی
# إجراء عملية التصنيف
dbscan_clusterer.fit()

# Prédire les étiquettes de clusters pour les données
# پیش‌بینی برچسب‌های خوشه‌ها برای داده‌ها
# التنبؤ بتسميات المجموعات للبيانات
labels = dbscan_clusterer.predict()
print("Cluster Labels / برچسب‌های خوشه‌ها / تسميات المجموعات / Étiquettes de clusters:", labels)