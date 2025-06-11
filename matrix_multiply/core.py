class Matrix:
    def __init__(self, data):
        """Initialize matrix with 2D list of numbers"""
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise ValueError("Matrix data must be a 2D list")
        
        if not data or not data[0]:
            raise ValueError("Matrix cannot be empty")
        
        row_length = len(data[0])
        if not all(len(row) == row_length for row in data):
            raise ValueError("All rows must have the same length")
        
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
