import pandas as pd
from sklearn import metrics

# ---------------------------------------------------------------------------------------------------------------------
# Class Algorithm
# ---------------------------------------------------------------------------------------------------------------------

class GraphMetrics():
    """Calculate metrics for simple lists or data frames. Encasulate sklearn metrics methode and add some helpers."""

    def precision(self, y_true, y_pred):
        return metrics.precision_score(y_true, y_pred, zero_division=0)

    def recall(self, y_true, y_pred):
        return metrics.recall_score(y_true, y_pred)

    def f1(self, y_true, y_pred):
        return metrics.f1_score(y_true, y_pred)

    def metrics(self, y_true, y_pred):
        """Return the metrics as list as follows: [precision, recall, f1]."""
        p = self.precision(y_true, y_pred)
        r = self.recall(y_true, y_pred)
        f = self.f1(y_true, y_pred)
        return [p,r,f]

    def labels(self):
        """Return the metric labels, corresponding to the metrics methode."""
        return ["Precision", "Recall", "F1-Score"]

    def print_metrics(self, y_true, y_pred, title="Metrics"):
        print(title)
        print("- Precision =", self.precision(y_true, y_pred))
        print("- Recall    =", self.recall(y_true, y_pred))
        print("- F1-Score  =", self.f1(y_true, y_pred))
        print()

    def metrics_list(self, y_true, y_pred_list):
        """Return metrics from multiple predictions as a list of metrics list: [[precision, recall, f1],[...]]."""
        result = []
        for y_pred in y_pred_list:
            result.append( self.metrics(y_true, y_pred) )
        return result

    def metrics_pandas(self, y_true, y_pred_list, labels, metric_label="Metric"):
        """Assemble metrics into a pandas dataframe"""
        # init result dictionary
        result = {metric_label: self.labels() }
        # calculate metrics
        metrics_list = self.metrics_list(y_true, y_pred_list)
        # add metrics to dict
        for i in range(len(labels)):
            label = labels[i]
            metrics = metrics_list[i]
            result[label] = metrics
        # return result as pandas df
        return pd.DataFrame(result)
