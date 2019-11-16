#!/usr/bin/env python
# coding: utf-8

# In[17]:


class Grid(object):
    """Represents a two-dimensional grid."""
    
    def __init__(self, rows, columns, fillValue = None):
        """Sets up that data."""
        self.data = []
        for row in range(rows):
            dataInRow = []
            for column in range(columns):
                dataInRow.append(fillValue)
            self.data.append(dataInRow)
    
    
    def getHeight(self):
        """Returns the number of rows."""
        return len(self.data)
    
    
    def getWidth(self):
        """Returns the number of columns"""
        return len(self.data[0])
    
    
    def __str__(self):
        """Returns a string representation of the grid."""
        result = ""
        for row in range(self.getHeight()):
            for col in range(self.getWidth()):
                result += f'{self.data[row][col]} '
            result += '\n'
        return result
    
    
    def __getitem__(self, index):
        """Supports two-dmimensional indexing with [][] (index represents a row number)."""
        return self.data[index]
    
    
    def find(self, value):
        """Returns (row, column) if value is found or None otherwise."""
        for row in range(self.getHeight()):
            for column in range(self.getWidth()):
                if self[row][column] == value:
                    return (row, column)
        return

