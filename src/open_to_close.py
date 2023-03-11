import numpy as np

def to_close(self):
    export_ = sum(self.export_a)
    import_ = sum(self.import_b)
    if export_ > import_:
        null_col = np.zeros((self.weight_matrix.shape[0],1), dtype=int)
        self.weight_matrix = np.append(self.weight_matrix, null_col,axis=1)
        self.import_b = np.append(self.import_b, (export_-import_))
    elif export_ < import_:
        null_row = np.zeros(((self.weight_matrix.shape[1]),), dtype=int)
        self.weight_matrix = np.vstack([self.weight_matrix, null_row])
        self.export_a = np.append(self.export_a, (import_-export_))
