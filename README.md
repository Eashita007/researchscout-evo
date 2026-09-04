# ResearchScout-Evo

**Evolutionary optimization of hybrid information retrieval for academic researcher discovery**

ResearchScout-Evo is a research-oriented web application that combines **natural language processing, large language models, web scraping, semantic retrieval, and evolutionary optimization** to identify researchers whose work best matches a user's interdisciplinary research interests.

The project is designed as both a practical academic discovery system and an experimental framework for studying whether evolutionary optimization can improve hybrid retrieval and ranking over conventional lexical, semantic, and LLM-based approaches.

---

## Research Question

> **Can evolutionary optimization improve hybrid lexical, semantic, and LLM-based ranking for matching researchers to interdisciplinary research interests across heterogeneous academic web data?**

The project compares several retrieval and ranking strategies, including:

* BM25 lexical retrieval
* Transformer-based semantic embeddings
* LLM-based reranking
* Manually weighted hybrid ranking
* Evolutionarily optimized hybrid ranking

The final approaches will be evaluated using standard information-retrieval metrics such as **Precision@K, Recall@K, Mean Reciprocal Rank (MRR), and NDCG@K**.

---

## Motivation

Finding researchers, laboratories, and potential collaborators is often a manual process involving repeated searches across university websites, laboratory pages, publication lists, and research profiles.

This becomes especially challenging for interdisciplinary queries such as:

> *Machine learning for predicting cancer metastasis using genomic and transcriptomic data*

Relevant researchers may describe similar work using very different terminology. A purely keyword-based system may therefore overlook strong matches.

ResearchScout-Evo explores whether combining lexical retrieval, neural semantic representations, LLM-based reasoning, and evolutionary optimization can produce more accurate and explainable researcher recommendations.

---

## Core Features

### Academic Web Data Acquisition

ResearchScout-Evo collects publicly available research information from sources such as:

* Faculty webpages
* University department pages
* Laboratory websites
* Research project pages
* Publication metadata sources

The acquisition pipeline extracts structured information including:

* Researcher name
* Institution
* Department
* Academic title
* Research interests
* Research descriptions
* Laboratory information
* Projects
* Selected publications
* Publication years
* Source URLs

The scraping pipeline is designed to respect applicable website policies, rate limits, and access restrictions.

---

### Natural Language Processing

Academic webpage content is processed through an NLP pipeline for:

* Text extraction and cleaning
* HTML removal
* Text normalization
* Sentence processing
* Duplicate-content detection
* Research-topic identification
* Keyword and concept extraction

The resulting text is transformed into structured researcher profiles suitable for downstream retrieval and ranking.

---

### Lexical Retrieval

ResearchScout-Evo implements **BM25** as a lexical information-retrieval baseline.

BM25 measures overlap between the user's research query and researcher profiles, providing a strong traditional retrieval baseline against which neural and LLM-based methods can be compared.

---

### Semantic Retrieval

Transformer-based sentence embeddings are used to represent research queries and researcher profiles in a shared semantic space.

This enables the system to identify researchers whose work is conceptually related to a user's interests even when their webpages use different terminology.

For example:

**User query**

> Machine learning for cancer metastasis using genomic data

**Researcher description**

> Computational methods for transcriptomic analysis and prediction of metastatic progression

A semantic retrieval model may recognize the strong conceptual relationship even when exact keywords differ.

---

### LLM-Based Reranking

A large language model evaluates a reduced set of candidate researchers returned by the retrieval pipeline.

Rather than allowing the LLM to search freely, ResearchScout-Evo provides structured candidate information including:

* User research interests
* User skills or background
* Researcher profile
* Research projects
* Selected publications
* Retrieval evidence

The LLM returns structured judgments containing information such as:

```json
{
  "relevance_score": 87,
  "research_alignment": [
    "cancer genomics",
    "machine learning",
    "transcriptomic analysis"
  ],
  "skill_alignment": [
    "Python",
    "data science"
  ],
  "potential_gaps": [
    "single-cell analysis"
  ],
  "reasoning": "..."
}
```

This allows the LLM to function as an interpretable reranking component rather than an unconstrained recommendation engine.

---

## Evolutionary Ranking Optimization

One of the primary research components of ResearchScout-Evo is evolutionary optimization of the hybrid ranking strategy.

Instead of manually selecting ranking weights such as:

```python
final_score = (
    0.20 * bm25_score +
    0.30 * semantic_score +
    0.10 * topic_score +
    0.30 * llm_score +
    0.10 * publication_score
)
```

the system evolves ranking configurations automatically.

A candidate chromosome may contain parameters such as:

```text
[
    BM25 weight,
    semantic embedding weight,
    topic weight,
    LLM weight,
    publication weight,
    retrieval top-k,
    semantic similarity threshold
]
```

The evolutionary process follows the general workflow:

```text
Initialize population
        ↓
Evaluate ranking performance
        ↓
Calculate fitness
        ↓
Selection
        ↓
Crossover
        ↓
Mutation
        ↓
New generation
        ↓
Repeat
```

A ranking metric such as **NDCG@10** can be used as the optimization objective.

This allows the system to investigate whether evolutionary algorithms can discover ranking strategies that outperform manually selected configurations.

---

## System Architecture

```text
                         USER
                           │
                           ▼
             ┌────────────────────────┐
             │   ResearchScout Web UI │
             └────────────┬───────────┘
                          │
                          ▼
                 Natural-language query
                          │
          ┌───────────────┴────────────────┐
          │                                │
          ▼                                ▼
   Query NLP Pipeline              User Background Parser
          │                                │
          └───────────────┬────────────────┘
                          ▼
                Candidate Retrieval
                          │
         ┌────────────────┼─────────────────┐
         ▼                ▼                 ▼
       BM25           Embeddings       Topic Matching
         │                │                 │
         └────────────────┼─────────────────┘
                          ▼
                     LLM Reranker
                          │
                          ▼
                Evolutionary Optimizer
                          │
                          ▼
                Final Researcher Ranking
                          │
                          ▼
            Grounded Explanation + Evidence
```

### Data Acquisition Pipeline

```text
University Websites
        +
Faculty Pages
        +
Lab Pages
        +
Publication Metadata
        ↓
Web Scraper / Crawler
        ↓
HTML Extraction
        ↓
NLP Cleaning
        ↓
Structured Researcher Profiles
        ↓
ResearchScout Corpus
```

---

## Experimental Evaluation

The project will evaluate multiple retrieval and ranking methods against a manually labelled benchmark.

Each researcher-query pair will receive a relevance label such as:

```text
0 = Irrelevant
1 = Weakly relevant
2 = Relevant
3 = Highly relevant
```

The following approaches will be compared:

1. BM25
2. Semantic embeddings
3. BM25 + semantic retrieval
4. LLM reranking
5. Manually weighted hybrid retrieval
6. Evolutionarily optimized hybrid retrieval

Evaluation metrics will include:

* Precision@5
* Recall@5
* MRR
* NDCG@5
* NDCG@10

Experimental results will be added once benchmark construction and evaluation are complete.

---

## Scalability

ResearchScout-Evo is designed to move beyond a small demonstration dataset.

Planned scalability experiments will evaluate system performance across increasing corpus sizes, for example:

```text
10 researchers       → development testing
100 researchers      → initial evaluation
1,000 researchers    → scalability testing
5,000+ researchers   → extended experiment
```

Potential measurements include:

* Web acquisition time
* Text preprocessing time
* Embedding generation time
* Retrieval latency
* LLM reranking latency
* Memory consumption

This will allow the project to study not only recommendation quality but also the computational behavior of the system as the academic corpus grows.

---

## Technology Stack

### Core

* Python
* Git / GitHub
* VS Code

### Web Data Acquisition

* Requests
* BeautifulSoup
* lxml
* Playwright or Selenium where dynamic rendering is required

### NLP and Retrieval

* BM25
* Sentence Transformers
* Transformer-based embeddings
* Cosine similarity

### Large Language Models

* LLM-based structured extraction
* Candidate reranking
* Evidence-grounded match explanations

### Evolutionary Computation

* Genetic/evolutionary optimization
* Fitness-based selection
* Crossover
* Mutation
* Parameter optimization

### Web Application

Planned implementation:

* Streamlit for initial development

A more conventional frontend/backend architecture may be introduced later as the project matures.

---

## Planned Repository Structure

```text
researchscout-evo/
│
├── app/
│
├── src/
│   ├── acquisition/
│   ├── preprocessing/
│   ├── retrieval/
│   ├── llm/
│   ├── ranking/
│   ├── evolution/
│   ├── evaluation/
│   └── utils/
│
├── tests/
├── configs/
├── data/
│   ├── raw/
│   ├── processed/
│   └── benchmark/
│
├── experiments/
├── results/
│   ├── figures/
│   └── metrics/
│
├── docs/
│
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
└── README.md
```

---

## Development Roadmap

### Phase 1 — Project Foundation

* Create project architecture
* Configure Python environment
* Establish Git/GitHub workflow
* Define researcher-profile schema
* Add testing and logging structure

### Phase 2 — Academic Data Acquisition

* Build initial university/faculty scraper
* Extract faculty and research information
* Normalize heterogeneous webpage content
* Store structured researcher profiles

### Phase 3 — Retrieval Baselines

* Implement BM25
* Implement semantic embedding retrieval
* Compare lexical and semantic retrieval

### Phase 4 — LLM Reranking

* Add structured LLM evaluation
* Generate grounded relevance explanations
* Test robustness and hallucination behavior

### Phase 5 — Benchmark Construction

* Construct interdisciplinary research queries
* Manually label researcher-query relevance
* Implement information-retrieval metrics

### Phase 6 — Evolutionary Optimization

* Encode hybrid ranking strategies
* Define ranking fitness function
* Implement selection, crossover, and mutation
* Compare optimized and manually weighted rankings

### Phase 7 — Web Application

* Build researcher discovery interface
* Display rankings, evidence, and explanations
* Add filtering and researcher-profile exploration

### Phase 8 — Evaluation and Scalability

* Run full benchmark
* Analyze retrieval performance
* Test increasing corpus sizes
* Produce experimental figures and tables

---

## Current Status

🚧 **Active development**

The project is currently being developed from the ground up. Initial work focuses on the repository architecture, academic data acquisition pipeline, and baseline retrieval methods.

Experimental results and a live demonstration will be added as development progresses.

---

## Future Extensions

Potential extensions include:

* Publication-network analysis
* Research topic trend detection
* Topic evolution over time
* Researcher collaboration graphs
* Research opportunity detection
* Faculty-project matching
* Distributed scraping and embedding generation
* Multi-objective evolutionary optimization
* Personalized researcher recommendations
* Research-field trend forecasting

---

## Project Goals

ResearchScout-Evo is intended to demonstrate the integration of:

**Natural Language Processing · Large Language Models · Web Scraping · Web Development · Information Retrieval · Neural Semantic Representations · Evolutionary Algorithms · Software Engineering · Experimental Evaluation**

The broader goal is to develop a practical scientific system while investigating how evolutionary optimization can improve modern hybrid information-retrieval pipelines.
