# The Well — Research Summary

A reference summary of [PolymathicAI/the_well](https://github.com/PolymathicAI/the_well), kept in this
repo for quick orientation. The Well is **not** an LLM app — it is a large-scale physics-simulation
dataset collection plus a PyTorch library for loading and benchmarking on it. This page exists so
contributors here can decide whether it is relevant to a project before reading the upstream docs.

## TL;DR

The Well is a **15 TB collection of 16 numerical-simulation datasets** spanning fluid dynamics,
magnetohydrodynamics (MHD), biological systems, acoustic scattering, and several astrophysical /
reaction-diffusion regimes. It ships with a Python package, `the_well`, that exposes a
`WellDataset` class (a `torch.utils.data.Dataset`), a CLI downloader, and a benchmark harness
built on PyTorch + [Hydra](https://hydra.cc/) with pretrained baseline checkpoints (e.g. FNO)
hosted on the Hugging Face Hub under [polymathic-ai](https://huggingface.co/polymathic-ai).

## Why it exists

The project targets ML research on physical systems — surrogate modeling, neural operators,
PDE benchmarking, and pretraining on physics data. It is the kind of dataset/library a researcher
training a Fourier Neural Operator (FNO) or U-Net on turbulence data would reach for. It does
**not** contain text, instruction data, or anything intended for chat / RAG / agent workflows,
and the rest of this repo's catalog is therefore unrelated to it.

## What's in it

According to the upstream README, The Well bundles **16 datasets** with per-dataset sizes ranging
from **6.9 GB to 5.1 TB**. The project's documentation site (`mkdocs`) additionally hosts
individual pages for further simulations beyond the core 16, so the exact count visible online
may exceed 16 over time. Domains covered include:

| Domain                    | Examples of included simulations                                         |
| ------------------------- | ------------------------------------------------------------------------ |
| Fluid dynamics            | Rayleigh–Bénard convection, Rayleigh–Taylor instability, shear flow, Euler equations, turbulence variants |
| Magnetohydrodynamics      | MHD simulations (multiple resolutions / regimes)                         |
| Astrophysics              | Convective stellar envelopes, neutron-star mergers, supernova explosions |
| Biological / soft matter  | Active matter, viscoelastic instability                                  |
| Acoustics & wave physics  | Acoustic scattering variants, Helmholtz equation                         |
| Reaction–diffusion        | Gray–Scott                                                               |
| Planetary                 | Shallow-water equations on a sphere                                      |

Individual datasets are streamable from Hugging Face, so working with The Well does not require
a 15 TB local download.

## Installation

```
pip install the_well
```

For CUDA 12.1 wheels:

```
pip install . --extra-index-url https://download.pytorch.org/whl/cu121
```

For the benchmark harness (training scripts, configs, baseline models):

```
pip install the_well[benchmark]
```

## Loading data

Local files:

```python
from the_well.data import WellDataset
from torch.utils.data import DataLoader

trainset = WellDataset(
    well_base_path="path/to/base",
    well_dataset_name="name_of_the_dataset",
    well_split_name="train",
)
train_loader = DataLoader(trainset)
```

Streaming directly from the Hugging Face Hub (no full download needed):

```python
trainset = WellDataset(
    well_base_path="hf://datasets/polymathic-ai/",
    well_dataset_name="active_matter",
    well_split_name="train",
)
```

## CLI download

```
the-well-download --base-path path/to/base --dataset active_matter --split train
```

## Benchmarking & pretrained checkpoints

Train a baseline (Fourier Neural Operator on the active-matter dataset, local server config):

```
cd the_well/benchmark
python train.py experiment=fno server=local data=active_matter
```

Load a pretrained checkpoint:

```python
from the_well.benchmark.models import FNO

model = FNO.from_pretrained("polymathic-ai/FNO-active_matter")
```

Configuration is managed with Hydra, so swapping experiments / datasets / servers is done by
changing the right-hand side of those `key=value` pairs.

## Upstream repo layout

```
the_well/
  the_well/            main Python package
    data/              WellDataset, normalization, augmentation, miniwell
    benchmark/         training scripts, models (FNO, ...), Hydra configs
  datasets/            per-dataset documentation pages
  docs/                mkdocs source: tutorials, API, FAQ
  scripts/             utility scripts
  tests/               test suite
  pyproject.toml
  mkdocs.yml
  CITATION
  LICENSE
  README.md
```

## When to reach for it

- Training or benchmarking neural surrogates / neural operators on PDE data.
- Pretraining models on heterogeneous physics simulations.
- Reproducing FNO / U-Net style baselines on fluid, MHD, or astrophysical regimes.

It is **not** the right tool for: chatbots, RAG over documents, agent frameworks, or any
text/code generation task — i.e. the rest of this repository's focus areas.

## Links

- Source: <https://github.com/PolymathicAI/the_well>
- PyPI: <https://pypi.org/project/the-well/>
- Hugging Face org (datasets + pretrained models): <https://huggingface.co/polymathic-ai>
- Project site / docs: <https://polymathic-ai.org/the_well/>
