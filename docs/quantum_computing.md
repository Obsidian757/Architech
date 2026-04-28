# Quantum Computing on GitHub — Landscape Summary

A reference summary of the major repositories listed under
[github.com/topics/quantum-computing](https://github.com/topics/quantum-computing), kept in this
repo for quick orientation. Quantum computing is **not** an LLM/agent topic — none of these
projects belong in the per-app catalog elsewhere in this repo. This page exists so contributors
can decide whether any of them is relevant to a project (e.g. an LLM agent that writes Qiskit
code) before reading the upstream READMEs.

## TL;DR

The topic page is dominated by a handful of Python SDKs from the major cloud / hardware vendors
(IBM, Google, Microsoft, Xanadu) plus a few research and education projects. Three matter most
for day-to-day work:

- **Qiskit** (IBM) — the de-facto general-purpose Python SDK; broadest hardware-vendor reach.
- **Cirq** (Google Quantum AI) — Python framework focused on NISQ-era hardware modeling.
- **PennyLane** (Xanadu) — hybrid quantum/classical with autodiff, integrates with PyTorch /
  TF / JAX. The natural pick if the project also involves ML.

If a project just needs to *call* a quantum backend, start with Qiskit. If it needs to *train*
a model that includes quantum layers, start with PennyLane.

## Topic snapshot

The leaderboard fluctuates, but as of this writing the most-starred entries on
`/topics/quantum-computing` are:

| Repo                          | Stars | Language        | What it is                                                                 |
| ----------------------------- | ----- | --------------- | -------------------------------------------------------------------------- |
| Developer-Y/cs-video-courses  | ~80k  | Markdown        | CS video-course index; quantum computing is one section, not the focus.    |
| Qiskit/qiskit                 | ~7k   | Python (+Rust)  | IBM's open-source SDK for circuits, primitives, transpiler.                |
| quantumlib/Cirq               | ~5k   | Python          | Google Quantum AI's NISQ-focused circuit framework.                        |
| microsoft/QuantumKatas        | ~5k   | Q# / Notebooks  | Tutorials & exercises for Microsoft's Q# language.                         |
| microsoft/Quantum             | ~4k   | Q# / Notebooks  | Microsoft Quantum Development Kit samples.                                 |
| PennyLaneAI/pennylane         | ~3k   | Python          | Hybrid quantum/classical platform with autodiff (PyTorch/TF/JAX).          |
| tensorflow/quantum            | ~2k   | Python          | Hybrid quantum/classical ML, Google + TensorFlow.                          |
| qutip/qutip                   | ~2k   | Python          | Quantum dynamics / open-systems simulation toolbox (not a circuit SDK).    |

Star counts shift; treat the table as an ordering signal, not a precise count.

## The three SDKs you'll actually pick between

### Qiskit (IBM)

- **What:** Open-source SDK "for working with quantum computers at the level of extended
  quantum circuits, operators, and primitives." Includes a transpiler for circuit optimization
  and mapping to hardware constraints, and `Sampler` / `Estimator` primitives.
- **Hardware reach:** Broadest — official provider packages for IBM, IonQ, AQT, AWS Braket,
  Quantinuum, Rigetti, etc.
- **Language:** Python (with Rust internals).
- **Install:** `pip install qiskit`
- **License:** Apache 2.0.
- **Pick when:** you want the path of least resistance to running on real hardware, or you
  need access to the largest ecosystem of provider plugins.

### Cirq (Google Quantum AI)

- **What:** Python framework "for creating, editing, and running NISQ circuits." Strong
  emphasis on modeling the actual hardware (gate set, connectivity, noise) rather than
  treating the device as a black box.
- **Key features:** parameterized circuits, circuit optimization passes, noise models,
  multiple simulators, integration with the `qsim` high-performance simulator.
- **Language:** Python 3.11+.
- **Install:** `pip install cirq`
- **License:** Apache 2.0.
- **Pick when:** you specifically care about NISQ-era device details, or you want the
  Google Quantum AI tooling stack (Cirq + qsim + OpenFermion).

### PennyLane (Xanadu)

- **What:** "Open-source quantum software platform for quantum computing, quantum machine
  learning, and quantum chemistry." The distinguishing feature is **automatic
  differentiation** of quantum circuits — gradients flow into PyTorch, TensorFlow, or JAX,
  which lets you train hybrid quantum/classical models with normal optimizer stacks.
- **Backends:** Plugin architecture; can dispatch to Qiskit and Cirq as backends, in
  addition to its own simulators and connected hardware devices.
- **Language:** Python 3.11+.
- **Install:** `python -m pip install pennylane`
- **License:** Apache 2.0.
- **Pick when:** the project is fundamentally an ML project and quantum circuits are a
  parameterized component you want to train end-to-end.

## Adjacent / specialized projects worth knowing

- **Microsoft Q# / QDK** (`microsoft/QuantumKatas`, `microsoft/Quantum`) — separate
  language (Q#) rather than a Python library, with strong learning materials. Pick if you
  specifically want Microsoft's stack or are using their hardware partners.
- **TensorFlow Quantum** (`tensorflow/quantum`) — Google's hybrid quantum-classical ML
  framework, built on Cirq + TF. Narrower scope than PennyLane and less actively positioned
  than it once was; check recent commit activity before adopting.
- **QuTiP** (`qutip/qutip`) — quantum dynamics and open-quantum-systems simulation.
  **Not** a gate-circuit SDK. Use it when the problem is "simulate the time-evolution of a
  Hamiltonian / master equation," not "compile a circuit and run it on hardware."

## How this would intersect with the rest of this repo

This repo's catalog is LLM apps, agents, and RAG. The realistic intersections with the
quantum-computing topic are:

1. **Code-generation agents.** An LLM agent that writes / reviews Qiskit, Cirq, or
   PennyLane code. This would be a natural fit under `starter_ai_agents/` or
   `advanced_ai_agents/single_agent_apps/` if you ever want to build it.
2. **RAG over quantum-computing docs.** A RAG pipeline indexed against, say, the Qiskit
   textbook or PennyLane's documentation. Would fit under `rag_tutorials/`.
3. **Tool-use / MCP agents.** An agent that, given a problem statement, picks the right
   SDK and dispatches to a quantum simulator. Would fit under `mcp_ai_agents/` once the
   relevant MCP servers exist (none of the major SDKs ship one today, so this is currently
   speculative).

None of those exist in this repo yet, and this doc is not proposing to build them — it
just records the lay of the land so the decision is informed if the question comes up.

## Links

- GitHub topic: <https://github.com/topics/quantum-computing>
- Qiskit: <https://github.com/Qiskit/qiskit> · <https://www.ibm.com/quantum/qiskit>
- Cirq: <https://github.com/quantumlib/Cirq> · <https://quantumai.google/cirq>
- PennyLane: <https://github.com/PennyLaneAI/pennylane> · <https://pennylane.ai>
- Microsoft Q# / QDK: <https://github.com/microsoft/Quantum> · <https://github.com/microsoft/QuantumKatas>
- TensorFlow Quantum: <https://github.com/tensorflow/quantum>
- QuTiP: <https://github.com/qutip/qutip>
