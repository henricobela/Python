class DataAnalysis:

    def __init__(self):
        pass

    def column_count(self):
        for coluna in self.columns:
            count = self[coluna].value_counts()
            print(f"Coluna: {coluna}\n\nContagens:\n{count}\n\n\n\n")

    def fill_na_null(self):
        import statistics
        for coluna in self.columns:
            na_count = self[coluna].isna().value_counts()
            moda = statistics.mode(self[coluna])
            if self[coluna].dtype == "float64":
                if moda == "NaN":
                    if na_count == True:
                        pass
                else: 
                    self[coluna] = self[coluna].fillna(value = moda)   
            if self[coluna].dtype == "int64":
                if moda == "NaN":
                    if na_count == True:
                        pass
                else: 
                    self[coluna] = self[coluna].fillna(value = moda)        
            if self[coluna].dtype == "O":
                if moda == "NaN":
                    if na_count == True:
                        pass
                else: 
                    self[coluna] = self[coluna].fillna(value = moda)