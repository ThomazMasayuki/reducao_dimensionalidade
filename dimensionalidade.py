import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Carrega a imagem
img = cv2.imread("toni.png", cv2.IMREAD_GRAYSCALE)

# Visualiza a imagem original, apenas em tom cinza
plt.imshow(img, cmap="gray")
plt.title("Imagem original")
plt.axis("off")

# Definição da quantidade de componentes para PCA
n_components = 40  # quanto menor, mais compressão

pca = PCA(n_components=n_components)
img_reduzida = pca.fit_transform(img)
img_reconstruida = pca.inverse_transform(img_reduzida)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(img_reconstruida, cmap="gray")
plt.title(f"PCA com {n_components} componentes")
plt.axis("off")

plt.savefig("toni_pca.png", dpi=300, bbox_inches="tight")
plt.close()
