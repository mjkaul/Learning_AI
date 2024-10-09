# Build a Knowledge Graph

## Learning Path

There are not a ton of good resources out there on why knowledge graphs are so useful for AI.

But everything I can find I'm collecting here.

A note on terminology: several different terms are used to describe different, sometimes overlapping, areas within this field. "Taxonomy," "ontology," and "knowledge graph" are the three terms that are most useful—and unfortunately these three terms are often defined interchangeably or ambiguously.

## Resources

See the [bibliography](~/bibliography.md) for a complete overview

- Heather Hedden, [*The Accidental Taxonomist*](https://www.hedden-information.com/accidental-taxonomist/)
- Michael Iantosca, Helmut Nagy, and William Sandri, ["Document Object Model Graph RAG: A semantic, content-first, and knowledge-management architecture for neuro-symbolic RAG"](https://medium.com/@nc_mike/document-object-model-graph-rag-af8ae452b0b6) / [pdf version](https://img1.wsimg.com/blobby/go/8d83b4d9-fe3b-41c3-ba74-a645effc4bf2/downloads/The%20DOM%20GraphRAG%20Project.pdf?ver=1726416712048)
- [OWL 2 Primer (W3C)](https://www.w3.org/TR/owl2-primer/#Property_Characteristics)
- Barry Smith, [Ontology for Systems Engineering](https://www.youtube.com/watch?v=bj8mSbHh-qA&t=13s)

## Objectives

1. Build an ontology / knowledge graph manually.
2. Build an ontology / knowledge graph using data you've imported from elsewhere (e.g. DBpedia).
3. Learn how to map not just data but *processes* into your knowledge graph.
4. Train your LLM on your knowledge graph.

## Concepts

- **Knowledge Graph** - An ontology with instances. So, if you create a taxonomy, add relationships to get an ontology, then add particular instances of the classes and relationships within your ontology, you've got a knowledge graph.
- **Ontology** - A taxonomy, plus mapped sets of relationships between the different class/terms that map your domain. Basically, a taxonomy plus *relationships*.
	- Barry Smith, "Ontology is a representation of the types of entities within a given domain and of the relations between them."
- **Taxonomy** - Hierarchical or structured set of terms used within a domain.

## Tools

