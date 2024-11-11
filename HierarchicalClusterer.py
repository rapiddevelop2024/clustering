#HierarchicalClusterer 
#author : m.dehghan
'''
Hierarchical Clustering:
 Hierarchical Clustering builds a tree-like structure (dendrogram) to represent data grouping hierarchies.
 We used an agglomerative approach, starting with each data point as its own cluster and merging them based on their proximity (defined by the method parameter, such as ward).
 It provides flexibility in determining clusters at various levels by adjusting the threshold parameter.
'''

import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist

class HierarchicalClusterer:
    def __init__(self, data, method='ward', threshold=1.5, criterion='distance'):
        """
        Initialize the HierarchicalClusterer with data, linkage method, threshold, and criterion.
        مقداردهی اولیه خوشه‌بند سلسله‌مراتبی با داده‌ها، روش پیوند، آستانه، و معیار.
        تهيئة الكلاستر الهرمي بالبيانات، طريقة الربط، العتبة، والمعيار.
        Initialiser le clusterer hiérarchique avec les données, méthode de liaison, seuil, et critère.
        """
        self.data = data
        self.method = method
        self.threshold = threshold
        self.criterion = criterion
        self.linkage_matrix = None

    def fit(self):
        """
        Perform hierarchical clustering on the data.
        انجام خوشه‌بندی سلسله‌مراتبی روی داده‌ها.
        إجراء التصنيف الهرمي على البيانات.
        Effectuer le clustering hiérarchique sur les données.
        """
        # Compute the distance matrix and linkage matrix using the specified method.
        # محاسبه ماتریس فاصله و ماتریس پیوند با استفاده از روش مشخص شده.
        # حساب مصفوفة المسافة ومصفوفة الربط باستخدام الطريقة المحددة.
        # Calculer la matrice de distance et la matrice de liaison en utilisant la méthode spécifiée.
        self.linkage_matrix = linkage(self.data, method=self.method)

    def predict(self):
        """
        Predict cluster labels based on the threshold and criterion.
        پیش‌بینی برچسب‌های خوشه براساس آستانه و معیار.
        التنبؤ بتسميات المجموعات بناءً على العتبة والمعيار.
        Prédire les étiquettes de clusters en fonction du seuil et du critère.
        """
        if self.linkage_matrix is None:
            raise Exception("Model not fitted. Call the fit() method first.")
        
        # Assign cluster labels to each data point.
        # اختصاص برچسب‌های خوشه به هر نقطه داده.
        # تخصيص تسميات المجموعات لكل نقطة بيانات.
        # Attribuer des étiquettes de clusters à chaque point de données.
        return fcluster(self.linkage_matrix, t=self.threshold, criterion=self.criterion)
        
# Example usage:
# داده‌های نمونه
# بيانات عينة
# Exemple de données
data = np.array([[1, 2], [1, 4], [1, 0],
                 [4, 2], [4, 4], [4, 0],
                 [10, 10], [10, 12], [10, 8]])
                 
# ایجاد شیء از کلاس خوشه‌بند سلسله‌مراتبی با روش 'ward' و آستانه ۲
# إنشاء كائن من فئة الكلاستر الهرمي مع طريقة 'ward' والعتبة ٢
# Création d'un objet de la classe HierarchicalClusterer avec la méthode 'ward' et un seuil de 2
hierarchical_clusterer = HierarchicalClusterer(data, method='ward', threshold=2)

# انجام عملیات خوشه‌بندی
# إجراء عملية التصنيف
# Effectuer le clustering
hierarchical_clusterer.fit()

# پیش‌بینی برچسب‌های خوشه‌ها برای داده‌ها
# التنبؤ بتسميات المجموعات للبيانات
# Prédire les étiquettes de clusters pour les données
labels = hierarchical_clusterer.predict()
print("Cluster Labels / برچسب‌های خوشه‌ها / تسميات المجموعات / Étiquettes de clusters:", labels)
