Berner Fachhochschule BFH - MAS Data Science - Graph Machine Learning - Master Thesis FS/2022 Thomas Iten

# Statusberichte

## Juli 2022
Status per 30.07.2022:
- Die geplanten Stunden im Juli wurde übertroffen. Details siehe [Arbeitsrapporte](workreports.md).
- Der Arbeitsfortschritt ist der [Grobplanung](planning.md) voraus.
- Ein Abschluss des Berichts auf Ende August ist realistisch. 
- Ein weiteres [Arbeitspakete](workpackages.md) konnte abgeschlossen werden.
- Mit der Durchführung der Experimente konnte der zweite wichtige Teil der Arbeit abgeschlossen werden.

Erledigte Arbeiten:
- Abschluss [Arbeitspaket 7 Experimente durchführen](workpackages.md)
- Implementation [Data Factory Klassen](../graph/data_factory.py) EdgeLabelFactory und TestTrainDataFactory
- [Experiment 01 Similarity based Scenario A](../experiments/ex01-similarity-scenario-a.ipynb)
- [Experiment 02 Similarity based Scenario B](../experiments/ex02-similarity-scenario-b.ipynb)
- [Experiment 03 Similarity based Scenario C](../experiments/ex03-similarity-scenario-c.ipynb)
- [Experiment 04 Similarity based Scenario D](../experiments/ex04-similarity-scenario-d.ipynb)
- [Experiment 05 Similarity community](../experiments/ex05-similarity-community.ipynb)
- [Experiment 06 Node2Vec Exploration](../experiments/ex06-node2vec-exploration.ipynb)
- [Experiment 07 Node2Vec Parameters](../experiments/ex07-node2vec-params.ipynb)
- [Experiment 08 Node2Vec Employee](../experiments/ex08-node2vec-employee.ipynb)
- ==TODO==
- Bericht Kapitel 6 Experimente und Auswertungen erstellt

Nächste Schritte:
- Bericht Kapitel 7 Fazit und Ausblick erstellen
- Bericht Management Summary erstellen
- Abschluss Bericht per Ende August

## Juni 2022

Status per 27.06.2022:
- Die im Juni geplanten Stunden konnten geleistet werden. Details siehe [Arbeitsrapporte](workreports.md).
- Der Arbeitsfortschritt stimmt mit der [Grobplanung](planning.md) überein.
- Drei weitere [Arbeitspakete](workpackages.md) konnten abgeschlossen werden.
- Mit der Beschreibung der verschiedenen Link Prediction Ansätze konnte ein wichtiger Teil der Arbeit geleistet werden.

Erledigte Arbeiten:
- Abschluss [Arbeitspaket 2 Systematische Recherche](workpackages.md)
- Abschluss [Arbeitspaket 5 Taxonomie Link Prediction](workpackages.md)
- Abschluss [Arbeitspaket 6 Testumgebung bereitstellen](workpackages.md)
- Implementation [Basis Klassen](../graph/) Algorithm und GraphLink
- Implementation [Measure Klassen](../measure/) SystemMeter, CpuSystemMeter, MemorySystemMeter, TimeSystemMeter und StopWatch
- [Notebook 10 Similarity based Graph Link Prediction](../notebooks/nb10-glp-similarity.ipynb)
- [Notebook 11 Embedding based Graph Link Prediction](../notebooks/nb11-glp-embedding.ipynb)
- [Notebook 12 GCN Link Prediction](../notebooks/nb12-glp-gcn.ipynb)
- [Notebook 13 Graph SAGE Link Prediction mit Subject als Node Features](../notebooks/nb13-glp-graph-sage-subject.ipynb)
- [Notebook 14 Graph SAGE Link Prediction mit Identiy Matrix als Node Features](../notebooks/nb14-glp-graph-sage.ipynb)
- [Notebook 15 Performance](../notebooks/nb15-performance.ipynb)
- [Notebook 16 Performance GNN](../notebooks/nb16-performance-gnn.ipynb)
- Bericht Kapitel 5. Graph Machine Learning erstellt
- Start Bericht Kapitel 6.1 Vorbereitung Experimente 

Nächste Schritte:
- Auswahl Link Prediction Algorithmen für Experimente
- Vorbereitung und Durchführung Experimente

## Mai 2022
Status per 28.05.2022:
- Der Verzug gegenüber der ersten Planung konnte zu grossen Teilen aufgeholt werden. Details siehe [Arbeitsrapporte](workreports.md).
- Der Arbeitsfortschritt stimmt mit der [Grobplanung](planning.md) überein.
- Die restlichen [Arbeitspakete](workpackages.md) wurden definiert. Die ersten Arbeitspakete abgeschlossen.
- Das erste Review mit den Experten und dem Betreuer wurde am 20. Mai durchgeführt.
- Die Grundlagen sind erarbeitet und dokumentiert. 
- Die Berichterstellung ist aufwendig und beansprucht mehr Zeit als gedacht.

Erledigte Arbeiten:
- Definition [Arbeitspakete 5-10](workpackages.md)
- Implementation weitere [Basis Klassen](../graph/) graph_embedding, graph_generator
- Implementation [Daten Klassen](../graph/) im Modul data_factory mit Employee, DataCollection, DataFactory, etc.
- [Notebook 05 Graph ML Embedding](../notebooks/nb05-gml-embedding.ipynb)
- [Notebook 06 Graph ML Embedding with GCN](../notebooks/nb06-gml-gcn-unsupervised-embedding.ipynb)
- [Notebook 07 Graph ML Classification with CNN](../notebooks/nb07-gml-cnn-supervised-graph-classification.ipynb)
- [Notebook 08 Graph ML Classification with GCN](../notebooks/nb08-gml-gcn-supervised-graph-classification.ipynb)
- [Notebook 09 Data Factory](../notebooks/nb09-data-factory.ipynb)
- Bericht Kapitel 1. Einleitung, 2. Graphen, 3. Graph Machine Learning, 4. Daten erstellt

Nächste Schritte:
- Grundlagen Link Prediction 
- Bereitstellung Test Umgebung mit Performance Tests 
- Recherche abschliessen
- Start erste Experimente

## April 2022
Status per 30.04.2022:
- Die Arbeiten an der Master Thesis wurden mitte April gestartet. Details siehe [Arbeitsrapporte](workreports.md).
- Bei der ursprüngliche Planung war der Start mitte März geplant. Die [Grobplanung](planning.md) wurde daher angepasst mit dem Ziel, den Verzug bis Ende Mai aufzuholen.
- Die ersten [Arbeitspakete](workpackages.md) wurden definiert und sind in Arbeit.

Erledigte Arbeiten:
- Definition [Arbeitspakete 1-4](workpackages.md)
- Erstellung und Anpassung [Grobplanung](planning.md)
- Erstellung [Installationsanweisung](installation.md) und Definition [Projektstruktur](structure.md)
- Implementation [Basis Klassen](../graph/) graph, graph_viz, graph_builder, graph_utils
- Implementation [Notebook 01 Graph Intro](../notebooks/nb01-graph-intro.ipynb)
- Implementation [Notebook 02 Graph Matrix](../notebooks/nb02-graph-matrix.ipynb)
- Implementation [Notebook 03 Graph Edge List](../notebooks/nb03-graph-edge-list.ipynb)
- Implementation [Notebook 04 Graph Measures](../notebooks/nb04-graph-measures.ipynb)

Nächste Schritte:
- Grundlagen Grahp Machine Learning 
- Bereitstellung Testdaten
- Auswahl Python Libraries für Experimente

---
[Zum Hauptmenu](../README.md)