class todo:
    id: int
    description: str
    visible: bool

    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description
        self.visible = True
