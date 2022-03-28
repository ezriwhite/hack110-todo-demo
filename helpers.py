class todo:
    id: int
    title: str
    description: str
    color: str
<<<<<<< Updated upstream
    unchecked: bool
=======
    checked: bool
>>>>>>> Stashed changes

    def __init__(self, id: int, title: str, description: str, color: str):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
<<<<<<< Updated upstream
        self.unchecked = True
=======
        self.checked = False
>>>>>>> Stashed changes
