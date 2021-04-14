from docutils.writers.latex2e import Writer, Table, LaTeXTranslator


class LatexWriter(Writer):
    def __init__(self):
        super().__init__()
        self.translator_class = DNDTranslator


class DNDTable(Table):
    pass


class DNDTranslator(LaTeXTranslator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.settings.table_style = ["borderless"]
        self.active_table = DNDTable(self, "supertabular")
