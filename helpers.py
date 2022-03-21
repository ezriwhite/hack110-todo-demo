class todo:
    id: int
    title: str
    description: str
    color: str
    visible: bool

    def __init__(self, id: int, title: str, description: str, color: str):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
        self.visible = True
