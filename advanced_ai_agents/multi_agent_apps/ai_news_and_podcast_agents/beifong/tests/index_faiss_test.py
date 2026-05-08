"""FAISS round-trip smoke test, promoted to a real pytest test.

The previous version was a top-level script with prints and no asserts. We now
build a deterministic in-memory index and assert the nearest-neighbour search
returns the planted vector first."""

from __future__ import annotations

import pytest

faiss = pytest.importorskip("faiss")
np = pytest.importorskip("numpy")


@pytest.fixture(scope="module")
def random_vectors():
    rng = np.random.default_rng(seed=42)
    database = rng.random((1_000, 32)).astype("float32")
    query = database[7:8].copy()  # the planted nearest neighbour is row 7
    return database, query


def test_flat_l2_index_finds_planted_vector(random_vectors):
    database, query = random_vectors
    index = faiss.IndexFlatL2(database.shape[1])
    index.add(database)

    assert index.ntotal == database.shape[0]

    distances, indices = index.search(query, k=5)
    assert indices.shape == (1, 5)
    assert indices[0][0] == 7
    assert distances[0][0] == pytest.approx(0.0, abs=1e-5)


def test_search_returns_k_results(random_vectors):
    database, query = random_vectors
    index = faiss.IndexFlatL2(database.shape[1])
    index.add(database)
    _distances, indices = index.search(query, k=10)
    assert indices.shape == (1, 10)
    assert len({int(i) for i in indices[0]}) == 10  # distinct neighbours


def test_search_distances_are_monotonic_nondecreasing(random_vectors):
    database, query = random_vectors
    index = faiss.IndexFlatL2(database.shape[1])
    index.add(database)
    distances, _ = index.search(query, k=10)
    assert all(distances[0][i] <= distances[0][i + 1] for i in range(9))
