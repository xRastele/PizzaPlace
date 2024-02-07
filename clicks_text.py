class ClicksText:
    def __init__(self, x, y, text_renderer):
        self.x = x
        self.y = y
        self.text_renderer = text_renderer

    def draw(self, surface, current_clicks, clicks_required):
        progress_text = f"{current_clicks}/{clicks_required}"
        self.text_renderer.render(surface, progress_text, (self.x, self.y))