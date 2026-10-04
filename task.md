# Agentic AI Project --- Intelligent GitHub Issue Refinement & Duplicate Detection System

## 1. Project Overview

Build an **Agentic AI system that assists a user before submitting a new
issue to a large open-source GitHub repository**.

Large GitHub projects such as Kubernetes, VS Code, Apache projects, and
other popular repositories may contain thousands or tens of thousands of
historical issues.

Before a user creates a new issue, the system should automatically:

1.  Validate the issue title and description.
2.  Detect spelling and grammatical errors.
3.  Correct those errors when necessary.
4.  Rewrite/refine the issue into a clear technical issue report.
5.  Search historical GitHub issues for similar or duplicate issues.
6.  Determine whether the proposed issue is likely to be a duplicate.
7.  If a similar issue exists, show the matching issue ID(s) and
    similarity information.
8.  If no sufficiently similar issue exists, indicate that the issue is
    ready to be published.

The project does **not need to actually create an issue on GitHub**. The
final action is a recommendation:

**DUPLICATE / POSSIBLE DUPLICATE / READY TO PUBLISH**

The primary objective is to demonstrate an end-to-end **Agentic AI +
RAG + LLM + tool integration workflow**.

------------------------------------------------------------------------

## 2. Problem Statement

Large software projects receive many duplicate, poorly written,
incomplete, or difficult-to-understand issue reports.

For example, a user may submit:

**Title**

> kube pod is not restrting properly

**Description**

> when pod crash sometime its not coming back i tried restart but same
> problem happening

The system should correct the language, refine the technical report, and
determine whether a similar issue has already been reported.

------------------------------------------------------------------------

## 3. High-Level Architecture

``` text
                         GitHub Repository
                               |
                    GitHub CLI / GitHub API
                               |
                               v
                    GitHub Issue Collector
                               |
                               v
                         issues.json
                               |
                               v
                    Chunk / Normalize Issues
                               |
                               v
                       Embedding Model
                               |
                               v
                     Vector Database / RAG
                    PGVector / Chroma / FAISS
                               |
User Issue                     |
   |                           |
   v                           |
Issue Intake                   |
   |                           |
   v                           |
Spelling / Grammar Agent       |
   |                           |
   v                           |
Issue Refinement Agent         |
   |                           |
   v                           |
Duplicate Search Agent --------+
   |
   v
Similarity Analysis
   |
   +-------------------------------+
   |                               |
Duplicate Found               No Duplicate
   |                               |
   v                               v
Show Existing Issue          READY TO PUBLISH
ID / URL / Similarity
```

------------------------------------------------------------------------

## 4. GitHub Data Collection

The first part of the project is to collect historical issues from a
selected GitHub repository.

The implementation should preferably use the **GitHub CLI (`gh`) or
GitHub API**, rather than HTML/UI scraping.

Example repositories:

``` text
kubernetes/kubernetes
microsoft/vscode
```

The collector should retrieve information such as:

``` json
{
  "id": 12345,
  "number": 12345,
  "title": "Pod fails to restart after node failure",
  "body": "Detailed issue description...",
  "state": "open",
  "labels": ["kind/bug"],
  "created_at": "2026-01-10T10:20:00Z",
  "updated_at": "2026-01-11T11:30:00Z",
  "url": "..."
}
```

The initial implementation may store retrieved issues in:

``` text
data/issues.json
```

This JSON file becomes the **source dataset for the RAG system**.

------------------------------------------------------------------------

## 5. Incremental Synchronization Requirement

The system should not download and re-index every issue every time it
runs.

The synchronization process should identify only new or changed issues.

``` text
GitHub
   |
   v
Check Issue ID / updated_at
   |
   +---- Existing + unchanged ---> Ignore
   |
   +---- New --------------------> Insert
   |
   +---- Updated ----------------> Re-index
```

The system should maintain synchronization metadata such as:

``` text
last_sync_time
issue_id
updated_at
content_hash
```

This prevents unnecessary embedding generation and duplicate vector
insertion.

------------------------------------------------------------------------

## 6. RAG Pipeline

Historical GitHub issues must be converted into searchable knowledge.

``` text
issues.json
     |
     v
Clean / Normalize
     |
     v
Create RAG Documents
     |
     v
Embedding Model
     |
     v
Vector Database
```

A RAG document might contain:

``` text
Issue ID: 12345

Title:
Pod fails to restart after node failure

Description:
After the worker node recovers, some pods remain...

Labels:
kind/bug, sig/node
```

Metadata should be stored separately where supported.

``` json
{
  "issue_number": 12345,
  "repository": "kubernetes/kubernetes",
  "state": "open",
  "labels": ["kind/bug", "sig/node"],
  "url": "...",
  "updated_at": "..."
}
```

------------------------------------------------------------------------

## 7. Agentic Workflow

The workflow should maintain shared state similar to:

``` text
IssueState

original_title
original_description

corrected_title
corrected_description

refined_title
refined_description

spelling_errors

candidate_issues

duplicate_status
duplicate_issue_id
similarity_score

final_decision
```

The implementation may use LangGraph, another agent framework, or a
custom workflow engine.

------------------------------------------------------------------------

## 8. Step 1 --- Issue Intake

The user provides a title and description.

``` text
Title:
pod is not restrting after crash

Description:
pod crash but sometime its not restarting and user need to manually restart it
```

The original input should be preserved for auditing and comparison.

------------------------------------------------------------------------

## 9. Step 2 --- Spelling and Grammar Analysis

The first agent analyzes the title and description and determines
whether spelling or grammatical problems exist.

``` text
            Check Language
                 |
          +------+------+
          |             |
       Errors         No Errors
          |             |
          v             |
       Correct          |
          |             |
          +------+------+
                 |
                 v
             Refinement
```

The system must preserve technical terminology such as:

``` text
kubectl
kubelet
etcd
CrashLoopBackOff
```

------------------------------------------------------------------------

## 10. Step 3 --- Issue Refinement

The Issue Refinement Agent transforms the corrected input into a
professional technical issue report.

Example output:

``` text
Title:

Pod does not automatically restart after an unexpected crash

Description:

In certain situations, a pod that terminates unexpectedly does not
restart automatically.

The pod remains unavailable until it is manually restarted.

Expected Behavior:

The pod should automatically recover according to the configured
restart policy.

Actual Behavior:

The pod occasionally remains unavailable after the crash and requires
manual intervention.
```

The agent must not invent technical facts that the user did not provide.

------------------------------------------------------------------------

## 11. Step 4 --- Duplicate Candidate Retrieval

The refined issue becomes the RAG query.

Generate an embedding for the query and search the vector database.

For example:

``` text
Top K = 10
```

Possible results:

``` text
Issue #9321     0.91
Issue #15102    0.87
Issue #20452    0.79
Issue #41002    0.65
```

**Vector similarity alone should not determine that an issue is a
duplicate.**

It should primarily be used for candidate retrieval.

------------------------------------------------------------------------

## 12. Step 5 --- Duplicate Analysis Agent

The most relevant issues should be passed to an LLM-based Duplicate
Analysis Agent.

The agent should consider:

-   Problem being reported
-   Component/subsystem
-   Symptoms
-   Triggering conditions
-   Expected behavior
-   Actual behavior
-   Relevant technical context

Recommended classifications:

``` text
DUPLICATE
POSSIBLE_DUPLICATE
RELATED
NOT_DUPLICATE
```

------------------------------------------------------------------------

## 13. Step 6 --- Final Decision

### Scenario A --- Duplicate Found

``` text
Status:

DUPLICATE

A highly similar issue already exists.

Existing Issue:
#9321

Title:
Pod remains unavailable after unexpected termination

Similarity:
91%

Recommendation:

Review the existing issue before creating a new GitHub issue.
```

### Scenario B --- Possible Duplicate

``` text
Status:

POSSIBLE DUPLICATE

Potentially related issues were discovered:

#9321
#15102
#20452

Recommendation:

Review these issues before publishing.
```

### Scenario C --- No Duplicate

``` text
Status:

READY TO PUBLISH

No sufficiently similar existing issue was identified.
```

The project does not need to actually publish the issue.

------------------------------------------------------------------------

## 14. Recommended Agent/Node Design

``` text
START
  |
  v
IssueInputNode
  |
  v
LanguageCheckNode
  |
  +---- errors ----> CorrectionNode
  |                       |
  +-----------------------+
  |
  v
IssueRefinementNode
  |
  v
EmbeddingNode
  |
  v
RAGSearchNode
  |
  v
DuplicateAnalysisNode
  |
  v
DecisionNode
  |
  +---- DUPLICATE
  |
  +---- POSSIBLE_DUPLICATE
  |
  +---- READY_TO_PUBLISH
  |
  v
END
```

This architecture is suitable for demonstrating **LangGraph conditional
routing**.

------------------------------------------------------------------------

## 15. Tool Requirements

Students should implement at least the following tools:

### GitHub Issue Collector

Retrieves GitHub issues and stores them in `issues.json`.

### Issue Synchronization Tool

Identifies new and modified GitHub issues.

### Embedding Tool

Converts issue content into embeddings.

### Vector Search Tool

Retrieves semantically similar issues.

### Language Analysis Tool

Identifies spelling and grammar problems while preserving technical
terminology.

### Duplicate Analysis Tool

Compares a proposed issue against retrieved candidates.

------------------------------------------------------------------------

## 16. Recommended Technology Stack

``` text
Python

LangGraph
LangChain

Ollama
  Qwen
  Llama

Embedding Model
  nomic-embed-text
  or another suitable embedding model

Vector Database
  PGVector
  Chroma
  FAISS

GitHub CLI
  gh

GitHub REST / GraphQL API

Optional:
PostgreSQL
FastAPI
Streamlit
```

The architecture should not depend on a specific LLM provider.

------------------------------------------------------------------------

## 17. Important Design Principle

Do not send thousands of GitHub issues directly to the LLM.

Incorrect architecture:

``` text
New Issue
   +
50,000 GitHub Issues
   |
   v
LLM
```

Recommended architecture:

``` text
                   50,000 Issues
                         |
                         v
                   Vector Database

New Issue
   |
Embedding
   |
   v
Vector Search
   |
   v
Top 10 Candidates
   |
   v
LLM Duplicate Analysis
```

RAG provides relevant knowledge.

The LLM performs semantic reasoning.

The agentic workflow coordinates the sequence, conditional routing,
state, and tools.

------------------------------------------------------------------------

## 18. Data Flow

``` text
                 OFFLINE / SYNC PIPELINE

GitHub
  |
  v
GitHub CLI/API
  |
  v
issues.json
  |
  v
Normalization
  |
  v
Embedding
  |
  v
Vector DB


                 ONLINE AGENT WORKFLOW

User Issue
   |
   v
Language Validation
   |
   v
Correction
   |
   v
Issue Refinement
   |
   v
Embedding
   |
   v
Vector Search
   |
   v
Top Candidate Issues
   |
   v
LLM Duplicate Analysis
   |
   v
Decision
   |
   +-----------------------------+
   |              |              |
   v              v              v
DUPLICATE     POSSIBLE       READY TO
              DUPLICATE       PUBLISH
```

------------------------------------------------------------------------

## 19. Functional Requirements

The completed project should be capable of:

1.  Selecting a public GitHub repository.
2.  Retrieving a substantial set of historical issues.
3.  Saving normalized issue information locally.
4.  Incrementally synchronizing new or updated issues.
5.  Creating embeddings for issue content.
6.  Persisting embeddings in a vector database.
7.  Accepting a new issue title and description.
8.  Detecting spelling and grammatical problems.
9.  Correcting those problems.
10. Refining the issue into a professional technical report.
11. Performing semantic retrieval against historical issues.
12. Retrieving the Top-K most relevant candidates.
13. Using an LLM to analyze whether candidates represent the same
    underlying problem.
14. Returning matching issue IDs and URLs when appropriate.
15. Producing one final classification:

``` text
DUPLICATE
POSSIBLE_DUPLICATE
READY_TO_PUBLISH
```

------------------------------------------------------------------------

## 20. Non-Functional Requirements

### Modularity

GitHub ingestion, RAG, agents, embeddings, vector storage, and workflow
orchestration should be separate modules.

### Idempotency

Running synchronization multiple times must not create duplicate issue
records or duplicate embeddings.

### Traceability

The system should expose which candidate issues caused a duplicate
recommendation.

### Structured LLM Output

Where possible, agents should return structured JSON/Pydantic-style
responses.

``` json
{
  "status": "DUPLICATE",
  "issue_number": 9321,
  "confidence": 0.91,
  "reason": "Both issues describe pods remaining unavailable after an unexpected termination."
}
```

### Configurability

The following should be configuration rather than hard-coded values:

``` text
repository
embedding_model
llm_model
top_k
similarity_threshold
vector_database
```

------------------------------------------------------------------------

## 21. Suggested Project Structure

``` text
github-issue-agent/
│
├── README.md
├── requirements.txt
├── .env.example
│
├── config/
│   └── settings.yaml
│
├── data/
│   ├── issues.json
│   └── sync_state.json
│
├── ingestion/
│   ├── github_client.py
│   ├── issue_collector.py
│   └── synchronizer.py
│
├── rag/
│   ├── embeddings.py
│   ├── indexer.py
│   └── retriever.py
│
├── agents/
│   ├── language_agent.py
│   ├── refinement_agent.py
│   └── duplicate_agent.py
│
├── workflow/
│   ├── state.py
│   ├── nodes.py
│   └── graph.py
│
├── models/
│   └── schemas.py
│
├── app/
│   └── main.py
│
└── tests/
    ├── test_ingestion.py
    ├── test_rag.py
    └── test_workflow.py
```

------------------------------------------------------------------------

## 22. Expected Demonstration

First synchronization:

``` text
Repository: kubernetes/kubernetes

Downloading issues...

Issues retrieved: 25,000

New issues: 25,000
Updated issues: 0

Generating embeddings...

Vector index created.
```

Second synchronization:

``` text
Issues checked: 25,010

Existing unchanged: 25,000
New: 8
Updated: 2

Embedding only 10 issues...
```

Example user issue:

``` text
Title:
pod not restrting after crash

Description:
when pod crash some time it not coming again
```

Expected workflow:

``` text
Language Check
      ↓
Spelling Errors Detected
      ↓
Correction
      ↓
Issue Refinement
      ↓
RAG Search
      ↓
10 Candidate Issues
      ↓
Duplicate Analysis
      ↓
DUPLICATE
```

Example final output:

``` text
Result: DUPLICATE

Refined Title:
Pod does not restart automatically after an unexpected crash

Potential Existing Issue:
#9321

Similarity Score:
0.91

Reason:
The existing issue describes substantially the same failure
condition and expected recovery behavior.

Recommendation:
Review issue #9321 before submitting a new issue.
```

------------------------------------------------------------------------

## 23. Learning Objectives

After completing this project, the student should understand the
practical difference between:

### LLM

Provides language understanding and reasoning.

### Embedding Model

Converts issue content into vectors suitable for semantic retrieval.

### Vector Database

Stores and searches historical issue embeddings.

### RAG

Provides relevant historical GitHub issues to the LLM.

### Tools

Interact with external systems such as GitHub and the vector database.

### Agent

Uses reasoning and tools to perform a specific responsibility.

### Agentic Workflow

Coordinates multiple steps, agents, tools, state transitions, and
conditional decisions to accomplish the overall goal.

The project therefore demonstrates:

``` text
LLM
+
Tools
+
RAG
+
Persistent Knowledge
+
State
+
Conditional Routing
+
Agentic Workflow
```

rather than simply building another chatbot.

------------------------------------------------------------------------

## 24. Final Deliverables

The final submission should contain:

``` text
Source Code
README.md
Architecture Diagram
GitHub Issue Collection Script
Sample issues.json
RAG Ingestion Pipeline
Vector Database Integration
Agentic Workflow
Language/Refinement Agent
Duplicate Detection Agent
Configuration
Automated Tests
Sample Input/Output
Instructions to Run Locally
```

The application should be runnable locally and demonstrate the complete
workflow from GitHub issue ingestion through the final:

**DUPLICATE / POSSIBLE_DUPLICATE / READY_TO_PUBLISH**

decision.

------------------------------------------------------------------------

## Key Architectural Principle

**Embedding similarity should retrieve candidate duplicates, not make
the final duplicate decision by itself.**

Two issues can contain very similar terminology while describing
different defects.

A stronger architecture uses vector search to reduce tens of thousands
of historical issues to a small candidate set, such as the top 5--10
results, and then uses the Duplicate Analysis Agent to reason over those
candidates.
