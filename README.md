# clustering
cluster several excel


English:

In this project, we implemented three clustering algorithms—K-Means, DBSCAN, and Hierarchical Clustering—using Python in an object-oriented approach.

K-Means Clustering: K-Means is a centroid-based algorithm that divides data into a predefined number of clusters (K) based on the Euclidean distance between data points and the centroid of each cluster. The algorithm iteratively adjusts the centroids to minimize within-cluster variance. K-Means is effective for spherical clusters but may struggle with irregular shapes.

DBSCAN (Density-Based Spatial Clustering of Applications with Noise): DBSCAN is a density-based algorithm that identifies clusters based on data point density. It groups points closely packed together, with a minimum number of points (min_samples) within a certain radius (eps). DBSCAN can handle clusters of irregular shapes and detects noise or outliers, making it suitable for complex datasets.

Hierarchical Clustering: Hierarchical Clustering builds a tree-like structure (dendrogram) to represent data grouping hierarchies. We used an agglomerative approach, starting with each data point as its own cluster and merging them based on their proximity (defined by the method parameter, such as ward). It provides flexibility in determining clusters at various levels by adjusting the threshold parameter.

This project highlights the benefits of each algorithm: K-Means is fast and efficient for well-separated clusters, DBSCAN is suitable for noisy and irregular data, and Hierarchical Clustering is effective for visualizing data hierarchies.

فارسی:

در این پروژه، سه الگوریتم خوشه‌بندی K-Means، DBSCAN، و خوشه‌بندی سلسله‌مراتبی را با استفاده از زبان پایتون و رویکرد شیءگرایی پیاده‌سازی کرده‌ایم.

خوشه‌بندی K-Means: K-Means یک الگوریتم مبتنی بر مرکز خوشه است که داده‌ها را به تعداد مشخصی از خوشه‌ها (K) بر اساس فاصله اقلیدسی تقسیم می‌کند. این الگوریتم به صورت تکراری مراکز خوشه‌ها را تنظیم می‌کند تا واریانس درون‌خوشه‌ای را کمینه کند. K-Means برای خوشه‌های کروی مناسب است، اما ممکن است در مواجهه با خوشه‌های نامنظم مشکل داشته باشد.

DBSCAN (خوشه‌بندی مبتنی بر تراکم): DBSCAN یک الگوریتم مبتنی بر تراکم است که خوشه‌ها را براساس تراکم نقاط داده شناسایی می‌کند. این الگوریتم نقاطی را که نزدیک به هم هستند و دارای حداقل تعداد نقاط (min_samples) در شعاع مشخص (eps) می‌باشند، در یک خوشه قرار می‌دهد. DBSCAN توانایی خوشه‌بندی داده‌های پیچیده و شناسایی نویز یا نقاط خارج از محدوده را دارد و برای مجموعه داده‌های نامنظم مناسب است.

خوشه‌بندی سلسله‌مراتبی: خوشه‌بندی سلسله‌مراتبی یک ساختار درخت‌مانند (دندروگرام) ایجاد می‌کند که سلسله‌مراتب گروه‌بندی داده‌ها را نشان می‌دهد. در اینجا، از روش تجمیعی استفاده شده که با قرار دادن هر نقطه داده به عنوان یک خوشه جداگانه شروع کرده و آن‌ها را براساس نزدیکی (تعیین شده توسط پارامتر method مانند ward) ترکیب می‌کند. این روش امکان تنظیم سطح خوشه‌بندی را با استفاده از پارامتر threshold فراهم می‌کند.

این پروژه مزایای هر الگوریتم را به نمایش می‌گذارد: K-Means سریع و کارآمد برای خوشه‌های مجزا، DBSCAN مناسب برای داده‌های نامنظم و نویزدار، و خوشه‌بندی سلسله‌مراتبی موثر برای نمایش سلسله‌مراتب داده‌ها.

عربي:

في هذا المشروع، قمنا بتنفيذ ثلاثة خوارزميات للتصنيف: K-Means، و DBSCAN، والتصنيف الهرمي باستخدام بايثون بطريقة كائنية التوجه.

تصنيف K-Means: خوارزمية K-Means تعتمد على مراكز المجموعات وتقسم البيانات إلى عدد محدد مسبقًا من المجموعات (K) بناءً على المسافة الإقليدية بين النقاط ومركز كل مجموعة. يقوم هذا النظام بتعديل المراكز بشكل متكرر لتقليل تباين داخل المجموعة. يعد K-Means فعالاً للمجموعات الكروية لكنه قد يواجه صعوبة في الأشكال غير المنتظمة.

DBSCAN (التصنيف المكاني الكثيف): خوارزمية DBSCAN تعتمد على الكثافة، حيث تحدد المجموعات بناءً على كثافة النقاط القريبة من بعضها ضمن حد معين (eps) وبوجود عدد أدنى من النقاط (min_samples). يتميز DBSCAN بقدرته على التعامل مع البيانات المعقدة والشوائب، مما يجعله مناسبًا للتعامل مع الأشكال غير المنتظمة.
التصنيف الهرمي: ينشئ التصنيف الهرمي بنية شجرية (شجرة تجمعات) لتمثيل تسلسل المجموعات. استخدمنا هنا طريقة تجميعية، حيث يبدأ كل نقطة كعنصر مستقل ثم يتم دمجهم بناءً على قربهم (يحدد بواسطة method مثل ward). هذا يوفر مرونة في تحديد مستويات مختلفة من المجموعات عن طريق ضبط معلمة threshold.

يعرض هذا المشروع مزايا كل خوارزمية: K-Means سريعة وفعالة للمجموعات المنفصلة، و DBSCAN مناسب للبيانات غير المنتظمة، والتصنيف الهرمي فعال لتصور تسلسل البيانات.

Français:

Dans ce projet, nous avons implémenté trois algorithmes de clustering — K-Means, DBSCAN, et le Clustering Hiérarchique — en utilisant Python avec une approche orientée objet.

Clustering K-Means : K-Means est un algorithme basé sur les centroïdes qui divise les données en un nombre prédéfini de clusters (K) en fonction de la distance euclidienne entre les points de données et le centroïde de chaque cluster. L'algorithme ajuste les centroïdes de manière itérative pour minimiser la variance intra-cluster. K-Means est efficace pour les clusters sphériques, mais peut rencontrer des difficultés avec les formes irrégulières.

DBSCAN (Clustering basé sur la densité) : DBSCAN est un algorithme basé sur la densité qui identifie les clusters en fonction de la densité des points. Il regroupe les points proches, avec un nombre minimal de points (min_samples) dans un rayon donné (eps). DBSCAN peut gérer des clusters de formes irrégulières et détecter le bruit, ce qui le rend adapté aux ensembles de données complexes.

Clustering Hiérarchique : Le Clustering Hiérarchique construit une structure en arbre (dendrogramme) pour représenter les hiérarchies de regroupement de données. Nous avons utilisé une approche agglomérative, en commençant par chaque point de données comme un cluster indépendant, puis en les fusionnant en fonction de leur proximité (définie par le paramètre method, comme ward). Il permet de déterminer les clusters à différents niveaux en ajustant le paramètre threshold.

Ce projet montre les avantages de chaque algorithme : K-Means est rapide et efficace pour des clusters bien séparés, DBSCAN est adapté aux données bruitées et irrégulières, et le Clustering Hiérarchique est utile pour visualiser les hiérarchies de données.
