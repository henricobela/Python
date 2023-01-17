"""
This class uses my own functions to personalize graphs (graphics bar pattern)

Feel free to use on all your codes :)
"""

class GraphCustomizer:

    def __init__(self):
        pass
    
    def annotate_graph(self):
        """
            This function annotates the quantities according the height and width.
        """
        for patch in self.patches:
            y_value = patch.get_height()
            x_value = patch.get_x() + patch.get_width() / 2
            space = 1
            label = format(y_value)
            self.annotate(label, 
                       (x_value, y_value), 
                        xytext = (0, space), 
                        textcoords = "offset points", 
                        ha = "center", 
                        va = "bottom")
        return self