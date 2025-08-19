# PCA on 2D noisy path.
# Run: `python pca_path.py`
import numpy as np

def pca(X):
    Xc = X - X.mean(0, keepdims=True)
    C = (Xc.T @ Xc) / (len(X)-1)
    vals, vecs = np.linalg.eigh(C)
    order = np.argsort(vals)[::-1]
    return vals[order], vecs[:,order]

if __name__ == "__main__":
    t = np.linspace(0, 1, 200)
    x = t + 0.05*np.random.randn(len(t))
    y = 0.2*t + 0.05*np.random.randn(len(t))
    X = np.c_[x,y]
    vals, vecs = pca(X)
    print("eigenvalues:", vals)
    print("first principal dir:", vecs[:,0])
