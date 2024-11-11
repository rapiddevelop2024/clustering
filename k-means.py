#k-means 
#author : m.dehghan

'''
K-Means is a centroid-based algorithm that divides data into a predefined number of clusters (K) 
based on the Euclidean distance between data points and the centroid of each cluster. 
The algorithm iteratively adjusts the centroids to minimize within-cluster variance. 
K-Means is effective for spherical clusters but may struggle with irregular shapes.

'''

import numpy as np
from sklearn.cluster import KMeans


class Clusterer:
    def __init__(self, data, n_clusters):
        """
        Initialize the Clusterer with data and number of clusters.
        Initialiser le Clusterer avec les données et le nombre de clusters.
        مقداردهی اولیه کلاستر با داده‌ها و تعداد خوشه‌ها.
        تهيئة الكلاستر بالبيانات وعدد المجموعات.
        """
        self.data = data
        self.n_clusters = n_clusters
        self.model = None

    def fit(self):
        """
        Apply KMeans clustering to the data.
        Appliquer le clustering KMeans aux données.
        اعمال خوشه‌بندی KMeans به داده‌ها.
        تطبيق KMeans على البيانات للتصنيف.
        """
        # Initialize KMeans model with the specified number of clusters.
        # مقداردهی اولیه مدل KMeans با تعداد خوشه‌ها.
        # تهيئة نموذج KMeans بعدد المجموعات.
        # Initialiser le modèle KMeans avec le nombre de clusters.
        self.model = KMeans(n_clusters=self.n_clusters)
        
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
        # بازگشت برچسب‌های خوشه برای هر نقطه داده.
        # إرجاع تسميات المجموعات لكل نقطة بيانات.
        # Retourner les étiquettes de clusters pour chaque point de données.
        return self.model.predict(self.data)

    def get_centroids(self):
        """
        Get the centroids of the clusters.
        Obtenir les centroids des clusters.
        دریافت مراکز خوشه‌ها.
        الحصول على مراكز المجموعات.
        """
        if self.model is None:
            raise Exception("Model not fitted. Call the fit() method first.")
        
        # Return the cluster centroids.
        # بازگشت مراکز خوشه‌ها.
        # إرجاع مراكز المجموعات.
        # Retourner les centres des clusters.
        return self.model.cluster_centers_
        
        
        
        
        
# Example usage:
# داده‌های نمونه
# بيانات عينة
# Exemple de données
data = np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [4, 0]])
                 
                 
# ایجاد شیء از کلاس خوشه‌بند با تعداد خوشه ۲
# إنشاء كائن من فئة الكلاستر بعدد مجموعات ٢
# Création d'un objet de la classe Clusterer avec 2 clusters
clusterer = Clusterer(data, 2)

# انجام عملیات خوشه‌بندی
# إجراء عملية التصنيف
# Effectuer le clustering
clusterer.fit()


# پیش‌بینی برچسب‌های خوشه‌ها برای داده‌ها
# التنبؤ بتسميات المجموعات للبيانات
# Prédire les étiquettes de clusters pour les données
labels = clusterer.predict()
print("Cluster Labels / برچسب‌های خوشه‌ها / تسميات المجموعات / Étiquettes de clusters:", labels)

# دریافت مراکز خوشه‌ها
# الحصول على مراكز المجموعات
# Obtenir les centroids des clusters
centroids = clusterer.get_centroids()
print("Cluster Centroids / مراکز خوشه‌ها / مراكز المجموعات / Centroid des clusters:", centroids)