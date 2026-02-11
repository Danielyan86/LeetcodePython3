"""
K-Means Clustering Implementation (Interview Level)

Features:
- K-means++ initialization for better convergence
- Standard fit/predict API
- Convergence detection with tolerance
- Edge case handling
"""

import numpy as np
from typing import Optional, Tuple


class KMeans:
    def __init__(
        self,
        n_clusters: int = 3,
        max_iters: int = 300,
        tol: float = 1e-4,
        init: str = "kmeans++",
        random_state: Optional[int] = None
    ):
        """
        Args:
            n_clusters: Number of clusters (k)
            max_iters: Maximum iterations
            tol: Convergence tolerance
            init: Initialization method ("kmeans++" or "random")
            random_state: Random seed for reproducibility
        """
        self.n_clusters = n_clusters
        self.max_iters = max_iters
        self.tol = tol
        self.init = init
        self.random_state = random_state

        self.centers_: Optional[np.ndarray] = None
        self.labels_: Optional[np.ndarray] = None
        self.inertia_: float = 0.0  # Sum of squared distances to nearest center
        self.n_iters_: int = 0

    def _init_centers_random(self, X: np.ndarray) -> np.ndarray:
        """Random initialization: pick k random points as centers."""
        indices = np.random.choice(len(X), self.n_clusters, replace=False)
        return X[indices].copy()

    def _init_centers_kmeans_plus_plus(self, X: np.ndarray) -> np.ndarray:
        """
        K-means++ initialization:
        1. Pick first center randomly
        2. Pick next center with probability proportional to distance squared
        3. Repeat until k centers chosen

        This gives better initial centers and faster convergence.
        """
        n_samples = len(X)
        centers = []

        # First center: random
        first_idx = np.random.randint(n_samples)
        centers.append(X[first_idx])

        # Remaining centers
        for _ in range(1, self.n_clusters):
            # Compute squared distances to nearest existing center
            distances = np.min([
                np.sum((X - c) ** 2, axis=1) for c in centers
            ], axis=0)

            # Sample with probability proportional to distance squared
            probs = distances / distances.sum()
            next_idx = np.random.choice(n_samples, p=probs)
            centers.append(X[next_idx])

        return np.array(centers)

    def _compute_distances(self, X: np.ndarray, centers: np.ndarray) -> np.ndarray:
        """Compute squared Euclidean distance from each point to each center."""
        # Shape: (n_samples, n_clusters)
        return np.array([
            np.sum((X - center) ** 2, axis=1)
            for center in centers
        ]).T

    def _assign_clusters(self, X: np.ndarray, centers: np.ndarray) -> np.ndarray:
        """Assign each point to the nearest center."""
        distances = self._compute_distances(X, centers)
        return np.argmin(distances, axis=1)

    def _update_centers(self, X: np.ndarray, labels: np.ndarray) -> np.ndarray:
        """Recompute centers as mean of assigned points."""
        new_centers = np.zeros((self.n_clusters, X.shape[1]))

        for k in range(self.n_clusters):
            mask = labels == k
            if np.any(mask):
                new_centers[k] = X[mask].mean(axis=0)
            else:
                # Empty cluster: reinitialize with random point
                new_centers[k] = X[np.random.randint(len(X))]

        return new_centers

    def _compute_inertia(self, X: np.ndarray, labels: np.ndarray, centers: np.ndarray) -> float:
        """Compute sum of squared distances to nearest center."""
        distances = self._compute_distances(X, centers)
        return np.sum([distances[i, labels[i]] for i in range(len(X))])

    def fit(self, X: np.ndarray) -> "KMeans":
        """
        Fit K-means to the data.

        Args:
            X: Data matrix of shape (n_samples, n_features)

        Returns:
            self
        """
        if self.random_state is not None:
            np.random.seed(self.random_state)

        X = np.asarray(X, dtype=np.float64)

        # Initialize centers
        if self.init == "kmeans++":
            self.centers_ = self._init_centers_kmeans_plus_plus(X)
        else:
            self.centers_ = self._init_centers_random(X)

        # Iterate until convergence
        for i in range(self.max_iters):
            # Assignment step
            self.labels_ = self._assign_clusters(X, self.centers_)

            # Update step
            new_centers = self._update_centers(X, self.labels_)

            # Check convergence
            center_shift = np.sum((new_centers - self.centers_) ** 2)
            self.centers_ = new_centers

            if center_shift < self.tol:
                break

        self.n_iters_ = i + 1
        self.inertia_ = self._compute_inertia(X, self.labels_, self.centers_)

        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict cluster labels for new data."""
        if self.centers_ is None:
            raise ValueError("Model not fitted. Call fit() first.")
        X = np.asarray(X, dtype=np.float64)
        return self._assign_clusters(X, self.centers_)

    def fit_predict(self, X: np.ndarray) -> np.ndarray:
        """Fit and return cluster labels."""
        self.fit(X)
        return self.labels_


# ============== Demo ==============
if __name__ == "__main__":
    # Generate sample data: 3 clusters
    np.random.seed(42)

    cluster1 = np.random.randn(100, 2) + [0, 0]
    cluster2 = np.random.randn(100, 2) + [5, 5]
    cluster3 = np.random.randn(100, 2) + [10, 0]
    X = np.vstack([cluster1, cluster2, cluster3])

    # Fit K-means
    kmeans = KMeans(n_clusters=3, random_state=42)
    labels = kmeans.fit_predict(X)

    print(f"Converged in {kmeans.n_iters_} iterations")
    print(f"Inertia (SSE): {kmeans.inertia_:.2f}")
    print(f"Cluster centers:\n{kmeans.centers_}")
    print(f"Cluster sizes: {[np.sum(labels == i) for i in range(3)]}")
